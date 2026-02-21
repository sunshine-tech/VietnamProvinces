"""
Generate ward conversion table for 2025 administrative changes.

This module parses the conversion CSV and generates Python code
with the conversion table embedded as module-level constants.
"""

import ast
import csv
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Annotated

from pydantic import AfterValidator, BaseModel, Field, StringConstraints

from vietnam_provinces.legacy.base import VietNamDivisionType

from .divisions import normalize_vietnamese


# Type alias for normalized strings using the existing normalize_vietnamese function
NormalizedStr = Annotated[str, StringConstraints(strip_whitespace=True), AfterValidator(normalize_vietnamese)]


@dataclass
class ConversionCSVRecord:
    """Raw record from parsing the conversion CSV."""

    new_ward_code: int
    new_ward_name: str
    new_province_code: int
    old_ward_code: int
    old_ward_name: str
    old_district_code: int
    old_province_code: int
    is_partly_merged: bool


class OldWardRef(BaseModel):
    """Reference to an old ward (pre-2025)."""

    code: int
    district_code: int
    province_code: int
    is_partly_merged: bool


class NewWardRef(BaseModel):
    """Reference to a new ward (post-2025)."""

    code: int
    province_code: int


class OldToNewEntry(BaseModel):
    """Mapping from old ward to new ward(s)."""

    old_ward: OldWardRef
    new_wards: list[NewWardRef]


class NewToOldEntry(BaseModel):
    """Mapping from new ward to old ward(s)."""

    new_ward: NewWardRef
    old_wards: list[OldWardRef]


@dataclass
class ConversionStats:
    """Statistics for the conversion table."""

    old_wards_count: int
    new_wards_count: int
    partly_merged_count: int


@dataclass
class ConversionMetadata:
    """Metadata for the conversion table."""

    description: str
    effective_date: str
    source: str
    stats: ConversionStats


class ConversionTable(BaseModel):
    """Complete conversion table for 2025 ward changes."""

    metadata: dict = Field(default_factory=dict)
    old_to_new: dict[str, OldToNewEntry]
    new_to_old: dict[str, NewToOldEntry]


def is_partly_merged_from_note(ghi_chu: str) -> bool:
    """Parse the 'Ghi chú' column to determine if merge is partial."""
    ghi_chu_lower = ghi_chu.lower().strip()
    return 'toàn bộ' not in ghi_chu_lower


def extract_division_type_from_name(name: str) -> VietNamDivisionType:
    """Extract division type from ward name.

    Maps the prefix of the ward name to the legacy VietNamDivisionType.
    """
    name_lower = name.lower().strip()

    if name_lower.startswith('thị trấn '):
        return VietNamDivisionType.THI_TRAN
    elif name_lower.startswith('phường '):
        return VietNamDivisionType.PHUONG
    elif name_lower.startswith('xã '):
        return VietNamDivisionType.XA
    else:
        # Default to XA if no recognized prefix
        return VietNamDivisionType.XA


def extract_code_from_parentheses(text: str) -> int:
    """Extract numeric code from text like 'Thành phố Hà Nội (01)' or '00004'."""
    text = text.strip()
    match = re.search(r'\((\d+)\)', text)
    if match:
        return int(match.group(1))
    match = re.search(r'(\d+)', text)
    if match:
        return int(match.group(1))
    raise ValueError(f'Cannot extract code from: {text}')


def parse_conversion_csv(filepath: Path) -> list[ConversionCSVRecord]:
    """Parse the conversion CSV file and return raw records."""
    records: list[ConversionCSVRecord] = []

    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        next(reader)

        for row in reader:
            if len(row) < 8:
                continue

            province_new_full = row[0].strip()
            new_ward_name = row[1].strip()
            new_ward_code_str = row[2].strip()
            old_ward_name = row[3].strip()
            old_ward_code_str = row[4].strip()
            ghi_chu = row[5].strip()
            old_district_full = row[6].strip()
            old_province_full = row[7].strip()

            if not new_ward_code_str or not old_ward_code_str:
                continue
            if not new_ward_name or not old_ward_name:
                continue

            try:
                new_ward_code = int(new_ward_code_str)
                old_ward_code = int(old_ward_code_str)
                new_province_code = extract_code_from_parentheses(province_new_full)
                old_province_code = extract_code_from_parentheses(old_province_full)
                old_district_code = extract_code_from_parentheses(old_district_full)
            except (ValueError, IndexError):
                continue

            records.append(
                ConversionCSVRecord(
                    new_ward_code=new_ward_code,
                    new_ward_name=new_ward_name,
                    new_province_code=new_province_code,
                    old_ward_code=old_ward_code,
                    old_ward_name=old_ward_name,
                    old_district_code=old_district_code,
                    old_province_code=old_province_code,
                    is_partly_merged=is_partly_merged_from_note(ghi_chu),
                )
            )

    return records


def build_conversion_table(records: list[ConversionCSVRecord]) -> ConversionTable:
    """Build the conversion table from parsed records."""

    old_ward_groups: dict[int, list[ConversionCSVRecord]] = defaultdict(list)
    for r in records:
        old_ward_groups[r.old_ward_code].append(r)

    old_to_new: dict[str, OldToNewEntry] = {}
    for old_code, group in old_ward_groups.items():
        is_partly_merged = len(group) > 1 or any(r.is_partly_merged for r in group)

        old_ref = OldWardRef(
            code=group[0].old_ward_code,
            district_code=group[0].old_district_code,
            province_code=group[0].old_province_code,
            is_partly_merged=is_partly_merged,
        )

        new_refs = [NewWardRef(code=r.new_ward_code, province_code=r.new_province_code) for r in group]

        old_to_new[str(old_code)] = OldToNewEntry(old_ward=old_ref, new_wards=new_refs)

    new_ward_groups: dict[int, list[ConversionCSVRecord]] = defaultdict(list)
    for r in records:
        new_ward_groups[r.new_ward_code].append(r)

    new_to_old: dict[str, NewToOldEntry] = {}
    for new_code, group in new_ward_groups.items():
        new_ref = NewWardRef(code=group[0].new_ward_code, province_code=group[0].new_province_code)

        old_refs = [
            OldWardRef(
                code=r.old_ward_code,
                district_code=r.old_district_code,
                province_code=r.old_province_code,
                is_partly_merged=r.is_partly_merged,
            )
            for r in group
        ]

        new_to_old[str(new_code)] = NewToOldEntry(new_ward=new_ref, old_wards=old_refs)

    metadata = {
        'description': 'Ward conversion table for administrative changes effective 01/07/2025',
        'effective_date': '2025-07-01',
        'source': 'BangChuyendoiĐVHCmoi_cu_khong_merge.csv',
        'stats': {
            'old_wards_count': len(old_to_new),
            'new_wards_count': len(new_to_old),
            'partly_merged_count': sum(1 for e in old_to_new.values() if e.old_ward.is_partly_merged),
        },
    }

    return ConversionTable(metadata=metadata, old_to_new=old_to_new, new_to_old=new_to_old)


# Python code generation functions - using positional args for compactness
def gen_old_ward_ref(old_ref: OldWardRef) -> ast.Call:
    """Generate AST for OldWardRef creation using positional args."""
    return ast.Call(
        func=ast.Name(id='OldWardRef'),
        args=[
            ast.Constant(value=old_ref.code),
            ast.Constant(value=old_ref.district_code),
            ast.Constant(value=old_ref.province_code),
            ast.Constant(value=old_ref.is_partly_merged),
        ],
        keywords=[],
    )


def gen_new_ward_ref(new_ref: NewWardRef) -> ast.Call:
    """Generate AST for NewWardRef creation using positional args."""
    return ast.Call(
        func=ast.Name(id='NewWardRef'),
        args=[
            ast.Constant(value=new_ref.code),
            ast.Constant(value=new_ref.province_code),
        ],
        keywords=[],
    )


def gen_old_to_new_entry(old_code: str, entry: OldToNewEntry) -> tuple[ast.expr, ast.expr]:
    """Generate AST key-value pair for OLD_TO_NEW dict entry."""
    key = ast.Constant(value=int(old_code))

    new_wards_tuple = ast.Tuple(elts=[gen_new_ward_ref(nw) for nw in entry.new_wards], ctx=ast.Load())

    value = ast.Call(
        func=ast.Name(id='OldToNewEntry'), args=[gen_old_ward_ref(entry.old_ward), new_wards_tuple], keywords=[]
    )
    return (key, value)


def gen_new_to_old_entry(new_code: str, entry: NewToOldEntry) -> tuple[ast.expr, ast.expr]:
    """Generate AST key-value pair for NEW_TO_OLD dict entry."""
    key = ast.Constant(value=int(new_code))

    old_wards_tuple = ast.Tuple(elts=[gen_old_ward_ref(ow) for ow in entry.old_wards], ctx=ast.Load())

    value = ast.Call(
        func=ast.Name(id='NewToOldEntry'), args=[gen_new_ward_ref(entry.new_ward), old_wards_tuple], keywords=[]
    )
    return (key, value)


def generate_ward_conversion_table(csv_path: Path, output_path: Path) -> ConversionMetadata:
    """Generate the ward conversion table as Python code."""
    records = parse_conversion_csv(csv_path)
    table = build_conversion_table(records)

    template_file = Path(__file__).parent / '_conversion_table_template.py'
    module = ast.parse(template_file.read_text())

    old_to_new_node = next(
        n
        for n in module.body
        if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name) and n.target.id == 'OLD_TO_NEW'
    )
    new_to_old_node = next(
        n
        for n in module.body
        if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name) and n.target.id == 'NEW_TO_OLD'
    )

    old_to_new_keys: list[ast.expr | None] = []
    old_to_new_values: list[ast.expr] = []
    for old_code, entry in table.old_to_new.items():
        key, value = gen_old_to_new_entry(old_code, entry)
        old_to_new_keys.append(key)
        old_to_new_values.append(value)

    old_to_new_node.value = ast.Dict(keys=old_to_new_keys, values=old_to_new_values)

    new_to_old_keys: list[ast.expr | None] = []
    new_to_old_values: list[ast.expr] = []
    for new_code, entry in table.new_to_old.items():
        key, value = gen_new_to_old_entry(new_code, entry)
        new_to_old_keys.append(key)
        new_to_old_values.append(value)

    new_to_old_node.value = ast.Dict(keys=new_to_old_keys, values=new_to_old_values)

    code = ast.unparse(ast.fix_missing_locations(module))
    output_path.write_text(code)

    stats = ConversionStats(
        old_wards_count=len(table.old_to_new),
        new_wards_count=len(table.new_to_old),
        partly_merged_count=sum(1 for e in table.old_to_new.values() if e.old_ward.is_partly_merged),
    )
    return ConversionMetadata(
        description=table.metadata['description'],
        effective_date=table.metadata['effective_date'],
        source=table.metadata['source'],
        stats=stats,
    )


# Province conversion table classes and functions
class OldProvinceRef(BaseModel):
    """Reference to an old province (pre-2025)."""

    code: int


class NewProvinceRef(BaseModel):
    """Reference to a new province (post-2025)."""

    code: int


class ProvinceOldToNewEntry(BaseModel):
    """Mapping from old province to new province(s)."""

    old_province: OldProvinceRef
    new_provinces: list[NewProvinceRef]


class ProvinceNewToOldEntry(BaseModel):
    """Mapping from new province to old province(s)."""

    new_province: NewProvinceRef
    old_provinces: list[OldProvinceRef]


@dataclass
class ProvinceConversionStats:
    """Statistics for the province conversion table."""

    old_provinces_count: int
    new_provinces_count: int


@dataclass
class ProvinceConversionMetadata:
    """Metadata for the province conversion table."""

    description: str
    effective_date: str
    source: str
    stats: ProvinceConversionStats


class ProvinceConversionTable(BaseModel):
    """Complete conversion table for 2025 province changes."""

    metadata: dict = Field(default_factory=dict)
    old_to_new: dict[str, ProvinceOldToNewEntry]
    new_to_old: dict[str, ProvinceNewToOldEntry]


def build_province_conversion_table(records: list[ConversionCSVRecord]) -> ProvinceConversionTable:
    """Build the province conversion table from ward conversion records."""
    from collections import defaultdict

    # Build province mappings from ward records
    old_to_new_provinces: dict[int, set[int]] = defaultdict(set)
    new_to_old_provinces: dict[int, set[int]] = defaultdict(set)

    for r in records:
        old_to_new_provinces[r.old_province_code].add(r.new_province_code)
        new_to_old_provinces[r.new_province_code].add(r.old_province_code)

    # Build old_to_new entries
    old_to_new: dict[str, ProvinceOldToNewEntry] = {}
    for old_code in sorted(old_to_new_provinces.keys()):
        new_codes = sorted(old_to_new_provinces[old_code])
        old_ref = OldProvinceRef(code=old_code)
        new_refs = [NewProvinceRef(code=c) for c in new_codes]
        old_to_new[str(old_code)] = ProvinceOldToNewEntry(old_province=old_ref, new_provinces=new_refs)

    # Build new_to_old entries
    new_to_old: dict[str, ProvinceNewToOldEntry] = {}
    for new_code in sorted(new_to_old_provinces.keys()):
        old_codes = sorted(new_to_old_provinces[new_code])
        new_ref = NewProvinceRef(code=new_code)
        old_refs = [OldProvinceRef(code=c) for c in old_codes]
        new_to_old[str(new_code)] = ProvinceNewToOldEntry(new_province=new_ref, old_provinces=old_refs)

    metadata = {
        'description': 'Province conversion table for administrative changes effective 01/07/2025',
        'effective_date': '2025-07-01',
        'source': 'BangChuyendoiĐVHCmoi_cu_khong_merge.csv',
    }

    return ProvinceConversionTable(metadata=metadata, old_to_new=old_to_new, new_to_old=new_to_old)


def gen_old_province_ref(old_ref: OldProvinceRef) -> ast.Call:
    """Generate AST for OldProvinceRef creation using positional args."""
    return ast.Call(
        func=ast.Name(id='OldProvinceRef'),
        args=[ast.Constant(value=old_ref.code)],
        keywords=[],
    )


def gen_new_province_ref(new_ref: NewProvinceRef) -> ast.Call:
    """Generate AST for NewProvinceRef creation using positional args."""
    return ast.Call(
        func=ast.Name(id='NewProvinceRef'),
        args=[ast.Constant(value=new_ref.code)],
        keywords=[],
    )


def gen_province_old_to_new_entry(old_code: str, entry: ProvinceOldToNewEntry) -> tuple[ast.expr, ast.expr]:
    """Generate AST key-value pair for OLD_TO_NEW dict entry."""
    key = ast.Constant(value=int(old_code))

    new_provinces_tuple = ast.Tuple(elts=[gen_new_province_ref(np) for np in entry.new_provinces], ctx=ast.Load())

    value = ast.Call(
        func=ast.Name(id='OldToNewEntry'),
        args=[gen_old_province_ref(entry.old_province), new_provinces_tuple],
        keywords=[],
    )
    return (key, value)


def gen_province_new_to_old_entry(new_code: str, entry: ProvinceNewToOldEntry) -> tuple[ast.expr, ast.expr]:
    """Generate AST key-value pair for NEW_TO_OLD dict entry."""
    key = ast.Constant(value=int(new_code))

    old_provinces_tuple = ast.Tuple(elts=[gen_old_province_ref(op) for op in entry.old_provinces], ctx=ast.Load())

    value = ast.Call(
        func=ast.Name(id='NewToOldEntry'),
        args=[gen_new_province_ref(entry.new_province), old_provinces_tuple],
        keywords=[],
    )
    return (key, value)


def generate_province_conversion_table(csv_path: Path, output_path: Path) -> ProvinceConversionMetadata:
    """Generate the province conversion table as Python code."""
    records = parse_conversion_csv(csv_path)
    table = build_province_conversion_table(records)

    template_file = Path(__file__).parent / '_province_conversion_table_template.py'
    module = ast.parse(template_file.read_text())

    old_to_new_node = next(
        n
        for n in module.body
        if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name) and n.target.id == 'OLD_TO_NEW'
    )
    new_to_old_node = next(
        n
        for n in module.body
        if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name) and n.target.id == 'NEW_TO_OLD'
    )

    old_to_new_keys: list[ast.expr | None] = []
    old_to_new_values: list[ast.expr] = []
    for old_code, entry in table.old_to_new.items():
        key, value = gen_province_old_to_new_entry(old_code, entry)
        old_to_new_keys.append(key)
        old_to_new_values.append(value)

    old_to_new_node.value = ast.Dict(keys=old_to_new_keys, values=old_to_new_values)

    new_to_old_keys: list[ast.expr | None] = []
    new_to_old_values: list[ast.expr] = []
    for new_code, entry in table.new_to_old.items():
        key, value = gen_province_new_to_old_entry(new_code, entry)
        new_to_old_keys.append(key)
        new_to_old_values.append(value)

    new_to_old_node.value = ast.Dict(keys=new_to_old_keys, values=new_to_old_values)

    code = ast.unparse(ast.fix_missing_locations(module))
    output_path.write_text(code)

    stats = ProvinceConversionStats(
        old_provinces_count=len(table.old_to_new),
        new_provinces_count=len(table.new_to_old),
    )
    return ProvinceConversionMetadata(
        description=table.metadata['description'],
        effective_date=table.metadata['effective_date'],
        source=table.metadata['source'],
        stats=stats,
    )
