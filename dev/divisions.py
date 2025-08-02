import ast
import itertools
from pathlib import Path
from collections.abc import Iterable, Sequence
from typing import Self, NamedTuple, Any, Annotated

from logbook import Logger
from pydantic import BaseModel, ValidationInfo, Field, StringConstraints, ConfigDict, field_validator, computed_field

from vietnam_provinces.base import VietNamDivisionType
from .types import Name, convert_to_codename, make_province_codename, make_ward_short_codename
from .phones import PhoneCodeCSVRecord


logger = Logger(__name__)


def truncate_leading(line: str, prefixes: Sequence[str]) -> str:
    """
    Remove substring at the beginning.
    If after removing, the remanining string starts with a number, cancel the removal.
    """
    for p in prefixes:
        if line.startswith(p):
            truncated = line[len(p) :]
            if not truncated[0].isdigit():
                return truncated
    return line


def abbreviate_codename(name: str) -> str:
    """
    ha_noi -> hano
    """
    words = name.split('_')
    return ''.join((w[0] for w in words))


def abbreviate_doub_codename(name: str) -> str:
    """
    tan_thanh -> tath
    thu_thua -> thth
    quan_11 -> qu11
    """
    words = name.split('_')
    return ''.join((w[:2] for w in words))


class Pre2025WardCSVInputRow(NamedTuple):
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
    province_name: Name
    province_code: int
    district_name: Name
    district_code: int
    # Some districts don't have ward, like Huyện Bạch Long Vĩ (2021)
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
    def set_ward_code(cls, value: Any):
        if not value:
            return None
        return value

    @classmethod
    def from_csv_row(cls, values: Sequence[str]) -> Self:
        row = Pre2025WardCSVInputRow.strip_make(values)
        ward = cls.model_validate(row._asdict())
        if not ward.ward_name:
            logger.info('The row {} does not have ward', row)
        return ward


class WardCSVInputRow(NamedTuple):
    code: str
    name: str
    province_name: str


class ProvinceCSVInputRow(NamedTuple):
    code: str
    name: str


class WardCSVRecord(BaseModel):
    code: int
    name: Annotated[str, StringConstraints(strip_whitespace=True)]
    province_name: str

    @computed_field
    @property
    def codename(self) -> str:
        return convert_to_codename(self.name)

    @computed_field
    @property
    def province_codename(self) -> str:
        return make_province_codename(self.province_name)


class ProvinceCSVRecord(BaseModel):
    code: int
    name: str

    @computed_field
    @property
    def codename(self) -> str:
        return make_province_codename(self.name)

    @classmethod
    def from_csv_row(cls, values: Iterable[str]) -> Self:
        row = ProvinceCSVInputRow._make(values)
        return cls.model_validate(row._asdict())


class BaseRegion(BaseModel):
    name: str
    code: int
    codename: str = ''


class Ward(BaseRegion):
    # Redefine here, or the validator won't run
    division_type: VietNamDivisionType = VietNamDivisionType.XA
    short_codename: str | None = None
    model_config = ConfigDict(validate_default=True)

    @field_validator('division_type', mode='after')
    @classmethod
    def parse_division_type(cls, value: VietNamDivisionType, info: ValidationInfo) -> VietNamDivisionType:
        name = info.data['name'].lower()
        possibles = (VietNamDivisionType.DAC_KHU, VietNamDivisionType.XA, VietNamDivisionType.PHUONG)
        return next((t for t in possibles if name.startswith(f'{t.value} ')), VietNamDivisionType.XA)


class Province(BaseRegion):
    division_type: VietNamDivisionType = VietNamDivisionType.TINH
    phone_code: int = 0
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
        if name.startswith('thành phố '):
            return VietNamDivisionType.THANH_PHO_TRUNG_UONG
        return value

    @property
    def short_codename(self) -> str:
        return truncate_leading(self.codename, ('tinh_', 'thanh_pho_')) if self.codename else ''

    @property
    def abbrev(self) -> str:
        return abbreviate_codename(self.short_codename) if self.short_codename else ''


def convert_to_nested(
    csv_provinces: Sequence[ProvinceCSVRecord],
    csv_wards: Sequence[WardCSVRecord],
    phone_codes: Iterable[PhoneCodeCSVRecord],
) -> dict[str, Province]:
    # Map from codename to Province. The codename is used for key because the Wards CSV refers to province by name.
    province_dict: dict[str, Province] = {}
    # Collect provinces from CSV
    for p in csv_provinces:
        try:
            province_dict[p.codename]
        except KeyError:
            province = Province.model_validate(dict(name=p.name, code=p.code, codename=p.codename))
            # Find phone_code
            matched_phone_code = next(
                (ph for ph in phone_codes if province.codename.endswith(ph.province_codename)), None
            )
            if matched_phone_code is not None:
                province.phone_code = matched_phone_code.code
            else:
                logger.error('Could not find phone code for {}', province.name)
            province_dict[province.codename] = province
    # Collect wards from CSV
    for w in csv_wards:
        try:
            short_codename = make_ward_short_codename(w.codename)
            province_dict[w.province_codename].indexed_wards[str(w.code)] = Ward(
                name=w.name, code=w.code, codename=w.codename, short_codename=short_codename
            )
        except KeyError:
            logger.error('Could not find {} province for ward {}', w.province_codename, w.name)
    return province_dict


def province_code_enum_member(province: Province) -> tuple[ast.Assign, ast.Expr]:
    """
    Generate AST tree for line of code equivalent to:
    P_01 = 1
    """
    province_id = f'P_{province.code:02}'
    node = ast.Assign(
        targets=[ast.Name(id=province_id)],
        value=ast.Constant(value=province.code),
    )
    docstring = ast.Expr(value=ast.Constant(value=province.name))
    return (node, docstring)


def ward_code_enum_member(ward: Ward) -> tuple[ast.Assign, ast.Expr]:
    """
    Generate AST tree for line of code equivalent to:
    W_00001 = 1
    """
    ward_id = f'W_{ward.code:05}'
    node = ast.Assign(
        targets=[ast.Name(id=ward_id)],
        value=ast.Constant(value=ward.code),
    )
    docstring = ast.Expr(value=ast.Constant(value=ward.name))
    return (node, docstring)


def gen_python_code_enums(provinces: Iterable[Province]) -> str:
    template_file = Path(__file__).parent / '_enum_code_template.py'
    module = ast.parse(template_file.read_text())
    class_defs = tuple(n for n in module.body if isinstance(n, ast.ClassDef))
    # Will generate members for ProvinceCode
    province_enum_def = next(n for n in class_defs if n.name == 'ProvinceCode')
    # Remove example members, except for the first docstring.
    first_member = next(iter(province_enum_def.body))
    province_enum_def.body = [first_member] if isinstance(first_member, ast.Expr) else []
    # Will generate members for WardCode
    ward_enum_def = next(n for n in class_defs if n.name == 'WardCode')
    # Remove example members, except for the first docstring.
    first_member = next(iter(ward_enum_def.body))
    ward_enum_def.body = [first_member] if isinstance(first_member, ast.Expr) else []
    for p in provinces:
        node = province_code_enum_member(p)
        province_enum_def.body.extend(node)
        for w in p.indexed_wards.values():
            node_w = ward_code_enum_member(w)
            ward_enum_def.body.extend(node_w)
    return ast.unparse(ast.fix_missing_locations(module))


def gen_province_object_creation(province: Province) -> ast.Call:
    def_args = [
        ast.Constant(value=province.name),
        ast.Constant(value=province.code),
        ast.Attribute(value=ast.Name(id='VietNamDivisionType'), attr=province.division_type.name),
        ast.Constant(value=province.codename),
        ast.Constant(value=province.phone_code),
    ]
    return ast.Call(func=ast.Name(id='Province'), args=def_args, keywords=[])


def gen_ward_object_creation(ward: Ward, province: Province) -> ast.Call:
    def_args = [
        ast.Constant(value=ward.name),
        ast.Constant(value=ward.code),
        ast.Attribute(value=ast.Name(id='VietNamDivisionType'), attr=ward.division_type.name),
        ast.Constant(value=ward.codename),
        ast.Constant(value=province.code),
    ]
    return ast.Call(func=ast.Name(id='Ward'), args=def_args, keywords=[])


def gen_python_province_lookup(provinces: Iterable[Province]) -> str:
    template_file = Path(__file__).parent / '_lookup_template.py'
    module = ast.parse(template_file.read_text())
    ward_map_node = next(
        n for n in module.body if isinstance(n, ast.Assign) and ast.unparse(n.targets[0]) == 'WARD_MAPPING'
    )
    province_map_node = next(
        n for n in module.body if isinstance(n, ast.Assign) and ast.unparse(n.targets[0]) == 'PROVINCE_MAPPING'
    )
    p_keys: list[ast.expr | None] = [ast.Constant(value=p.code) for p in provinces]
    p_values: list[ast.expr] = [gen_province_object_creation(p) for p in provinces]
    province_map_node.value = ast.Dict(keys=p_keys, values=p_values)
    wards = itertools.chain.from_iterable(p.indexed_wards.values() for p in provinces)
    w_keys: list[ast.expr | None] = [ast.Constant(value=w.code) for w in wards]
    w_values: list[ast.expr] = []
    for p in provinces:
        for w in p.indexed_wards.values():
            w_values.append(gen_ward_object_creation(w, p))
    ward_map_node.value = ast.Dict(keys=w_keys, values=w_values)
    return ast.unparse(ast.fix_missing_locations(module))
