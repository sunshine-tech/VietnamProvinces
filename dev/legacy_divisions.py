"""Parse pre-2025 CSV data and generate Python code for legacy administrative divisions."""

from __future__ import annotations

import ast
import csv
from collections.abc import Iterable, Sequence
from enum import StrEnum
from pathlib import Path
from typing import Any, NamedTuple, Self

from logbook import Logger
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    ValidationInfo,
    computed_field,
    field_validator,
)

from .phones import PhoneCodeCSVRecord
from .types import Name, convert_to_codename


logger = Logger(__name__)


# Division types for pre-2025 (level 2 and 3 have more options)
class VietNamDivisionType(StrEnum):
    """Division types for pre-2025 administrative units."""

    # Level 1: Provinces
    TINH = 'tỉnh'
    THANH_PHO_TRUNG_UONG = 'thành phố trung ương'
    # Level 2: Districts
    HUYEN = 'huyện'
    QUAN = 'quận'
    THANH_PHO = 'thành phố'
    THI_XA = 'thị xã'
    # Level 3: Wards
    XA = 'xã'
    THI_TRAN = 'thị trấn'
    PHUONG = 'phường'


def truncate_leading(line: str, prefixes: Sequence[str]) -> str:
    """Remove substring at the beginning."""
    for p in prefixes:
        if line.startswith(p):
            truncated = line[len(p) :]
            if not truncated or not truncated[0].isdigit():
                return truncated
    return line


def abbreviate_codename(name: str) -> str:
    """ha_noi -> hano"""
    words = name.split('_')
    return ''.join(w[0] for w in words)


def abbreviate_doub_codename(name: str) -> str:
    """tan_thanh -> tath, thu_thua -> thth, quan_11 -> qu11"""
    words = name.split('_')
    return ''.join(w[:2] for w in words)


class Pre2025WardCSVInputRow(NamedTuple):
    """Input row structure for pre-2025 ward CSV."""

    province_name: str
    province_code: int
    district_name: str
    district_code: int
    ward_name: str
    ward_code: int

    @classmethod
    def strip_make(cls, values: Sequence[str]) -> Self:
        return cls._make(values[:6])


class Pre2025WardCSVRecord(BaseModel):
    """Parsed record from pre-2025 ward CSV."""

    province_name: Name
    province_code: int
    district_name: Name
    district_code: int
    # Some districts don't have ward
    ward_name: Name | None
    ward_code: int | None

    @computed_field
    @property
    def province_codename(self) -> str:
        return convert_to_codename(self.province_name)

    @computed_field
    @property
    def district_codename(self) -> str:
        return convert_to_codename(self.district_name)

    @computed_field
    @property
    def ward_codename(self) -> str | None:
        return convert_to_codename(self.ward_name) if self.ward_name else None

    @field_validator('ward_code', mode='before')
    @classmethod
    def set_ward_code(cls, value: Any) -> int | None:
        if not value:
            return None
        return int(value)

    @classmethod
    def from_csv_row(cls, values: Sequence[str]) -> Self:
        row = Pre2025WardCSVInputRow.strip_make(values)
        ward = cls.model_validate(row._asdict())
        if not ward.ward_name:
            logger.info('The row {} does not have ward', row)
        return ward


class BaseRegion(BaseModel):
    """Base model for administrative regions."""

    name: str
    code: int
    codename: str = ''


class Ward(BaseRegion):
    """Ward model for pre-2025 data."""

    division_type: VietNamDivisionType = VietNamDivisionType.XA
    short_codename: str | None = None
    model_config = ConfigDict(validate_default=True)

    @field_validator('division_type', mode='after')
    @classmethod
    def parse_division_type(cls, value: VietNamDivisionType, info: ValidationInfo) -> VietNamDivisionType:
        name = info.data['name'].lower()
        possibles = (
            VietNamDivisionType.THI_TRAN,
            VietNamDivisionType.XA,
            VietNamDivisionType.PHUONG,
        )
        return next((t for t in possibles if name.startswith(f'{t.value} ')), VietNamDivisionType.XA)


class District(BaseRegion):
    """District model for pre-2025 data."""

    division_type: VietNamDivisionType = VietNamDivisionType.HUYEN
    short_codename: str | None = None
    # Actual wards are saved here for fast searching
    indexed_wards: dict[str, Ward] = Field(exclude=True, default_factory=dict)
    model_config = ConfigDict(validate_default=True)

    @computed_field
    @property
    def wards(self) -> tuple[Ward, ...]:
        return tuple(self.indexed_wards.values())

    @field_validator('division_type', mode='after')
    @classmethod
    def parse_division_type(cls, value: VietNamDivisionType, info: ValidationInfo) -> VietNamDivisionType:
        name = info.data['name'].lower()
        possibles = (
            VietNamDivisionType.THANH_PHO,
            VietNamDivisionType.THI_XA,
            VietNamDivisionType.QUAN,
            VietNamDivisionType.HUYEN,
        )
        return next((t for t in possibles if name.startswith(f'{t.value} ')), VietNamDivisionType.HUYEN)

    @property
    def abbrev(self) -> str:
        return abbreviate_doub_codename(self.short_codename) if self.short_codename else ''


class Province(BaseRegion):
    """Province model for pre-2025 data."""

    division_type: VietNamDivisionType = VietNamDivisionType.TINH
    phone_code: int = 0
    # Actual districts are saved here for fast searching
    indexed_districts: dict[str, District] = Field(exclude=True, default_factory=dict)
    model_config = ConfigDict(validate_default=True)

    @computed_field
    @property
    def districts(self) -> tuple[District, ...]:
        return tuple(self.indexed_districts.values())

    @field_validator('division_type', mode='after')
    @classmethod
    def parse_division_type(cls, value: VietNamDivisionType, info: ValidationInfo) -> VietNamDivisionType:
        name = info.data['name'].lower()
        if name.startswith('thành phố '):
            return VietNamDivisionType.THANH_PHO_TRUNG_UONG
        return value

    @property
    def short_codename(self) -> str:
        return truncate_leading(self.codename, ('tinh_', 'thanh_pho_')) if self.codename else ''

    @property
    def abbrev(self) -> str:
        return abbreviate_codename(self.short_codename) if self.short_codename else ''


def generate_district_short_codenames(province: Province) -> None:
    """Generate short codenames for districts, handling duplicates."""
    prefixes = ('huyen_', 'thi_xa_', 'quan_', 'thanh_pho_')
    # First, just generate short_codename as normal
    for d in province.indexed_districts.values():
        if d.codename:
            d.short_codename = truncate_leading(d.codename, prefixes)
    # Second, find ones whose short_codename is the same as other
    from collections import deque

    duplicates: deque[str] = deque()
    trial_short_names = tuple(d.short_codename for d in province.indexed_districts.values())
    for i, d in province.indexed_districts.items():
        if d.short_codename and trial_short_names.count(d.short_codename) > 1:
            duplicates.append(i)
    # For duplicates, keep the original codename
    while duplicates:
        dup_code = duplicates.popleft()
        district = province.indexed_districts[dup_code]
        district.short_codename = district.codename


def generate_ward_short_codenames(district: District) -> None:
    """Generate short codenames for wards, handling duplicates."""
    prefixes = ('xa_', 'thi_tran_', 'phuong_')
    # First, just generate short_codename as normal
    for w in district.indexed_wards.values():
        if w.codename:
            w.short_codename = truncate_leading(w.codename, prefixes)
    # Second, find ones whose short_codename is the same as other
    from collections import deque

    duplicates: deque[str] = deque()
    trial_short_names = tuple(w.short_codename for w in district.indexed_wards.values())
    for i, w in district.indexed_wards.items():
        if w.short_codename and trial_short_names.count(w.short_codename) > 1:
            duplicates.append(i)
    # For duplicates, keep the original codename
    while duplicates:
        dup_code = duplicates.popleft()
        ward = district.indexed_wards[dup_code]
        ward.short_codename = ward.codename


def convert_to_nested(
    records: Sequence[Pre2025WardCSVRecord],
    phone_codes: Iterable[PhoneCodeCSVRecord],
) -> dict[int, Province]:
    """Convert flat CSV records to nested province -> district -> ward structure."""
    table: dict[int, Province] = {}
    for w in records:
        province_code = w.province_code
        try:
            province = table[province_code]
            add_to_existing_province(w, province)
        except KeyError:
            province = Province(name=w.province_name, code=province_code, codename=w.province_codename)
            # Find phone_code
            matched_phone_code = next(
                (ph for ph in phone_codes if w.province_codename.endswith(ph.province_codename)), None
            )
            if matched_phone_code is None:
                logger.error('Could not find phone code for {}', province.name)
            else:
                province.phone_code = matched_phone_code.code
            district = District(name=w.district_name, code=w.district_code, codename=w.district_codename)
            province.indexed_districts[str(w.district_code)] = district
            if w.ward_code and w.ward_name and w.ward_codename:
                ward = Ward(name=w.ward_name, code=w.ward_code, codename=w.ward_codename)
                district.indexed_wards[str(w.ward_code)] = ward
            table[province_code] = province
    for p in table.values():
        generate_district_short_codenames(p)
        for d in p.indexed_districts.values():
            generate_ward_short_codenames(d)
    return table


def add_to_existing_province(record: Pre2025WardCSVRecord, province: Province) -> None:
    """Add ward/district to an existing province structure."""
    district_code = record.district_code
    try:
        district = province.indexed_districts[str(district_code)]
    except KeyError:
        district = District(name=record.district_name, code=district_code, codename=record.district_codename)
        province.indexed_districts[str(district_code)] = district
    if record.ward_code and record.ward_name and record.ward_codename:
        try:
            district.indexed_wards[str(record.ward_code)]
        except KeyError:
            ward = Ward(name=record.ward_name, code=record.ward_code, codename=record.ward_codename)
            district.indexed_wards[str(record.ward_code)] = ward


# Python code generation functions


def province_code_enum_member(province: Province) -> tuple[ast.Assign, ast.Expr]:
    """Generate AST tree for province code enum member."""
    province_id = f'P_{province.code:02}'
    node = ast.Assign(
        targets=[ast.Name(id=province_id)],
        value=ast.Constant(value=province.code),
    )
    docstring = ast.Expr(value=ast.Constant(value=province.name))
    return (node, docstring)


def district_code_enum_member(district: District) -> tuple[ast.Assign, ast.Expr]:
    """Generate AST tree for district code enum member."""
    district_id = f'D_{district.code:03}'
    node = ast.Assign(
        targets=[ast.Name(id=district_id)],
        value=ast.Constant(value=district.code),
    )
    docstring = ast.Expr(value=ast.Constant(value=district.name))
    return (node, docstring)


def ward_code_enum_member(ward: Ward) -> tuple[ast.Assign, ast.Expr]:
    """Generate AST tree for ward code enum member."""
    ward_id = f'W_{ward.code:05}'
    node = ast.Assign(
        targets=[ast.Name(id=ward_id)],
        value=ast.Constant(value=ward.code),
    )
    docstring = ast.Expr(value=ast.Constant(value=ward.name))
    return (node, docstring)


def gen_python_code_enums(provinces: Iterable[Province]) -> str:
    """Generate Python code for province, district, ward code enums."""
    template_file = Path(__file__).parent / '_legacy_enum_template.py'
    module = ast.parse(template_file.read_text())
    class_defs = tuple(n for n in module.body if isinstance(n, ast.ClassDef))

    # ProvinceCode enum
    province_enum_def = next(n for n in class_defs if n.name == 'ProvinceCode')
    first_member = next(iter(province_enum_def.body))
    province_enum_def.body = [first_member] if isinstance(first_member, ast.Expr) else []

    # DistrictCode enum
    district_enum_def = next(n for n in class_defs if n.name == 'DistrictCode')
    first_member = next(iter(district_enum_def.body))
    district_enum_def.body = [first_member] if isinstance(first_member, ast.Expr) else []

    # WardCode enum
    ward_enum_def = next(n for n in class_defs if n.name == 'WardCode')
    first_member = next(iter(ward_enum_def.body))
    ward_enum_def.body = [first_member] if isinstance(first_member, ast.Expr) else []

    for p in provinces:
        node = province_code_enum_member(p)
        province_enum_def.body.extend(node)
        for d in p.indexed_districts.values():
            node_d = district_code_enum_member(d)
            district_enum_def.body.extend(node_d)
            for w in d.indexed_wards.values():
                node_w = ward_code_enum_member(w)
                ward_enum_def.body.extend(node_w)

    return ast.unparse(ast.fix_missing_locations(module))


def gen_province_object_creation(province: Province) -> ast.Call:
    """Generate AST for Province object creation."""
    def_args = [
        ast.Constant(value=province.name),
        ast.Attribute(value=ast.Name(id='ProvinceCode'), attr=f'P_{province.code:02}'),
        ast.Attribute(value=ast.Name(id='VietNamDivisionType'), attr=province.division_type.name),
        ast.Constant(value=province.codename),
        ast.Constant(value=province.phone_code),
    ]
    return ast.Call(func=ast.Name(id='Province'), args=def_args, keywords=[])


def gen_district_object_creation(district: District, province: Province) -> ast.Call:
    """Generate AST for District object creation."""
    def_args = [
        ast.Constant(value=district.name),
        ast.Attribute(value=ast.Name(id='DistrictCode'), attr=f'D_{district.code:03}'),
        ast.Attribute(value=ast.Name(id='VietNamDivisionType'), attr=district.division_type.name),
        ast.Constant(value=district.codename),
        ast.Attribute(value=ast.Name(id='ProvinceCode'), attr=f'P_{province.code:02}'),
    ]
    return ast.Call(func=ast.Name(id='District'), args=def_args, keywords=[])


def gen_ward_object_creation(ward: Ward, district: District, province: Province) -> ast.Call:
    """Generate AST for Ward object creation."""
    def_args = [
        ast.Constant(value=ward.name),
        ast.Attribute(value=ast.Name(id='WardCode'), attr=f'W_{ward.code:05}'),
        ast.Attribute(value=ast.Name(id='VietNamDivisionType'), attr=ward.division_type.name),
        ast.Constant(value=ward.codename),
        ast.Attribute(value=ast.Name(id='DistrictCode'), attr=f'D_{district.code:03}'),
    ]
    return ast.Call(func=ast.Name(id='Ward'), args=def_args, keywords=[])


def gen_python_lookup(provinces: Iterable[Province]) -> str:
    """Generate Python code for lookup mappings."""
    template_file = Path(__file__).parent / '_legacy_lookup_template.py'
    header = '# This file is named with "_" prefix to prevent being imported by accident.\n\n'
    module = ast.parse(template_file.read_text())

    province_map_node = next(
        n
        for n in module.body
        if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name) and n.target.id == 'PROVINCE_MAPPING'
    )
    district_map_node = next(
        n
        for n in module.body
        if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name) and n.target.id == 'DISTRICT_MAPPING'
    )
    ward_map_node = next(
        n
        for n in module.body
        if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name) and n.target.id == 'WARD_MAPPING'
    )

    # Province mapping
    p_keys: list[ast.expr | None] = [ast.Constant(value=p.code) for p in provinces]
    p_values: list[ast.expr] = [gen_province_object_creation(p) for p in provinces]
    province_map_node.value = ast.Dict(keys=p_keys, values=p_values)

    # District mapping
    d_keys: list[ast.expr | None] = []
    d_values: list[ast.expr] = []
    for p in provinces:
        for d in p.indexed_districts.values():
            d_keys.append(ast.Constant(value=d.code))
            d_values.append(gen_district_object_creation(d, p))
    district_map_node.value = ast.Dict(keys=d_keys, values=d_values)

    # Ward mapping
    w_keys: list[ast.expr | None] = []
    w_values: list[ast.expr] = []
    for p in provinces:
        for d in p.indexed_districts.values():
            for w in d.indexed_wards.values():
                w_keys.append(ast.Constant(value=w.code))
                w_values.append(gen_ward_object_creation(w, d, p))
    ward_map_node.value = ast.Dict(keys=w_keys, values=w_values)

    return header + ast.unparse(ast.fix_missing_locations(module))


def parse_pre2025_csv(csv_path: Path) -> list[Pre2025WardCSVRecord]:
    """Parse pre-2025 ward CSV file."""
    records: list[Pre2025WardCSVRecord] = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        # Skip header row
        _header = next(reader)
        for row in reader:
            try:
                record = Pre2025WardCSVRecord.from_csv_row(row)
                records.append(record)
            except ValidationError as e:
                logger.warning('Failed to parse row {}: {}', row, e)
    return records
