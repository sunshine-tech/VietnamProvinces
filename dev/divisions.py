import ast
from pathlib import Path
from collections import deque
from typing import NamedTuple, Optional, List, Dict, Sequence, Deque, Iterable, Any, Annotated

from logbook import Logger
from pydantic import BaseModel, ValidationInfo, Field, field_validator, computed_field

from vietnam_provinces.base import VietNamDivisionType
from .types import Name, convert_to_codename, convert_to_id_friendly
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


class WardCSVInputRow(NamedTuple):
    province_name: str
    province_code: int
    district_name: str
    district_code: int
    ward_name: str
    ward_code: int

    @classmethod
    def strip_make(cls, value):
        return cls._make(value[:6])


class WardCSVRecord(BaseModel):
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
    def from_csv_row(cls, values: List[str]) -> 'WardCSVRecord':
        row = WardCSVInputRow.strip_make(values)
        ward = cls.model_validate(row._asdict())
        if not ward.ward_name:
            logger.info('The row {} does not have ward', row)
        return ward


class BaseRegion(BaseModel):
    name: str
    code: int
    codename: str | None


class Ward(BaseRegion):
    # Redefine here, or the validator won't run
    division_type: VietNamDivisionType = VietNamDivisionType.XA
    short_codename: str | None = None

    @field_validator('division_type', mode='before')
    @classmethod
    def parse_division_type(cls, value, info: ValidationInfo):
        if value:
            return value
        name = info.data['name'].lower()
        possibles = (VietNamDivisionType.THI_TRAN, VietNamDivisionType.XA, VietNamDivisionType.PHUONG)
        return next((t for t in possibles if name.startswith(f'{t.value} ')), None)


class District(BaseRegion):
    # Redefine here, or the validator won't run
    division_type: VietNamDivisionType = VietNamDivisionType.HUYEN
    short_codename: str | None = None
    # Actual wards are saved here for fast searching
    indexed_wards: dict[str, Ward] = Field(exclude=True, default_factory=dict)

    @computed_field
    @property
    def wards(self) -> tuple[Ward, ...]:
        return tuple(self.indexed_wards.values())

    @field_validator('division_type', mode='before')
    @classmethod
    def parse_division_type(cls, value, info: ValidationInfo):
        if value:
            return value
        name = info.data['name'].lower()
        possibles = (
            VietNamDivisionType.THANH_PHO,
            VietNamDivisionType.THI_XA,
            VietNamDivisionType.QUAN,
            VietNamDivisionType.HUYEN,
        )
        return next((t for t in possibles if name.startswith(f'{t.value} ')), None)

    @property
    def abbrev(self):
        return abbreviate_doub_codename(self.short_codename)


class Province(BaseRegion):
    # Redefine here, or the validator won't run
    division_type: VietNamDivisionType = VietNamDivisionType.TINH
    phone_code: int | None = None
    # Actual districts are saved here for fast searching
    indexed_districts: dict[str, District] = Field(exclude=True, default_factory=dict)

    @computed_field
    @property
    def districts(self) -> tuple[District, ...]:
        return tuple(self.indexed_districts.values())

    @field_validator('division_type', mode='before')
    @classmethod
    def parse_division_type(cls, value, info: ValidationInfo):
        if value:
            return value
        name = info.data['name'].lower()
        if name.startswith(f'{VietNamDivisionType.THANH_PHO} '):
            return VietNamDivisionType.THANH_PHO_TRUNG_UONG
        if name.startswith(f'{VietNamDivisionType.TINH} '):
            return VietNamDivisionType.TINH

    @property
    def short_codename(self):
        return truncate_leading(self.codename, ('tinh_', 'thanh_pho_'))

    @property
    def abbrev(self):
        return abbreviate_codename(self.short_codename)


def generate_district_short_codenames(province: Province):
    """
    In list of districts of a province, there can be duplicate if stripping prefix, like
    "huyen_ky_anh" and "thi_xa_ky_anh". It is because "Huyện Kỳ Anh" was promoted to "Thị xã" but its old record
    still remains. In that case, we will strip prefix of "thi_xa_ky_anh" but keep original name of "huyen_ky_anh".
    """
    prefixes = ('huyen_', 'thi_xa_', 'quan_', 'thanh_pho_')
    # First, just generate short_codename as normal
    for d in province.indexed_districts.values():
        if d.codename:
            d.short_codename = truncate_leading(d.codename, prefixes)
    # Second, find ones whose short_codename is the same as other
    # Nummeric codes of districts whose shortname is duplicate
    duplicates: Deque[str] = deque()
    trial_short_names = tuple(d.short_codename for d in province.indexed_districts.values())
    for i, d in province.indexed_districts.items():
        name = d.short_codename
        if trial_short_names.count(name) > 1:
            duplicates.append(i)
    if duplicates:
        logger.debug('Districts with duplicate short codename: {}', duplicates)
    # OK, now fix short codename for those duplicated districts
    for i in duplicates:
        d = province.indexed_districts[i]
        if d.codename:
            d.short_codename = truncate_leading(d.codename, ('thi_xa_', 'quan_', 'thanh_pho_'))


def generate_ward_short_codenames(district: District):
    """
    In list of wards of a district, there can be duplicate if stripping prefix, like
    "xa_yen_vien" and "thi_tran_yen_vien". It is because "Xã Yên Viên" was promoted to "Thị trấn" but its old record
    still remains. In that case, we will strip prefix of "thi_tran_yen_vien" but keep original name of "xa_yen_vien".
    """
    prefixes = ('xa_', 'phuong_', 'thi_tran_')
    # First, just generate short_codename as normal
    for w in district.indexed_wards.values():
        if w.codename:
            w.short_codename = truncate_leading(w.codename, prefixes)
    # Second, find ones whose short_codename is the same as other
    # Nummeric codes of wards whose shortname is duplicate
    duplicates: Deque[str] = deque()
    trial_short_names = tuple(w.short_codename for w in district.indexed_wards.values())
    for i, w in district.indexed_wards.items():
        name = w.short_codename
        if trial_short_names.count(name) > 1:
            duplicates.append(i)
    if duplicates:
        logger.debug('Wards with duplicate short codename: {}', duplicates)
    # OK, now fix short codename for those duplicated wards
    for i in duplicates:
        w = district.indexed_wards[i]
        w.short_codename = truncate_leading(w.codename, ('phuong_', 'thi_tran_')) if w.codename else None
    # There are still duplicate:
    # - "Phường Sa Pa" and "Phường Sa Pả", both belong to "Thị xã Sa Pa" (Lào Cai)
    # "Xã Đông Thạnh" and "Xã Đông Thành", both belong to "Huyện Bình Minh" (Vĩnh Long)


def generate_unique_ward_ids(district: District, province: Province):
    prefixes = ('xã_', 'phường_', 'thị_trấn_')
    # First, just generate short_codename as normal
    for w in district.indexed_wards.values():
        idf_name = convert_to_id_friendly(w.name)
        w.short_codename = truncate_leading(idf_name, prefixes)
    pass


def add_to_existing_province(w: WardCSVRecord, province: Province) -> Ward | None:
    if not w.ward_name or not w.ward_code:
        return None
    ward = Ward(name=w.ward_name, code=w.ward_code, codename=w.ward_codename)
    try:
        district = province.indexed_districts[str(w.district_code)]
        district.indexed_wards[str(w.ward_code)] = ward
    except KeyError:
        district = District(name=w.district_name, code=w.district_code, codename=w.district_codename)
        province.indexed_districts[str(w.district_code)] = district
        if ward:
            district.indexed_wards = {str(w.ward_code): ward}
    return ward


def convert_to_nested(
    records: Sequence[WardCSVRecord], phone_codes: Iterable[PhoneCodeCSVRecord]
) -> Dict[int, Province]:
    table: Dict[int,Province] = {}
    for w in records:
        # This district doesn't have ward
        province_code = w.province_code
        try:
            province = table[province_code]
            add_to_existing_province(w, province)
        except KeyError:
            province = Province(name=w.province_name, code=province_code, codename=w.province_codename)
            # Find phone_code
            # c.province_codename will be 'ba_ria_vung_tau'
            # province.codename will be 'tinh_ba_ria_vung_tau'
            matched_phone_code = next((ph for ph in phone_codes if w.province_codename.endswith(ph.province_codename)), None)
            if matched_phone_code is None:
                logger.error('Could not find phone code for {}', province.name)
            else:
                province.phone_code = matched_phone_code.code
            district = District(name=w.district_name, code=w.district_code, codename=w.district_codename)
            province.indexed_districts[str(w.district_code)] = district
            if w.ward_code and w.ward_name:
                ward = Ward(name=w.ward_name, code=w.ward_code, codename=w.ward_codename)
                district.indexed_wards[str(w.ward_code)] = ward
            table[province_code] = province
    for p in table.values():
        generate_district_short_codenames(p)
        for d in p.indexed_districts.values():
            generate_ward_short_codenames(d)
    return table


def province_enum_member(province: Province):
    """
    Generate AST tree for line of code equivalent to:
    P_1 = Province('Thành phố Hà Nội', 1, VietNamDivisionType.THANH_PHO_TRUNG_UONG, 'thanh_pho_ha_noi', 24)
    """
    province_id = f'P_{province.code}'
    enum_def_args = [
        ast.Constant(value=province.name),
        ast.Constant(value=province.code),
        ast.Attribute(value=ast.Name(id='VietNamDivisionType'), attr=province.division_type.name),
        ast.Constant(value=province.codename),
        ast.Constant(value=province.phone_code),
    ]
    node = ast.Assign(
        targets=[ast.Name(id=province_id)],
        value=ast.Call(func=ast.Name(id='Province'), args=enum_def_args, keywords=[]),
    )
    return node


def province_descriptive_enum_member(province: Province):
    """
    Generate AST tree for line of code equivalent to:
    HA_NOI = ProvinceEnum.P_1.value
    """
    province_id = province.short_codename.upper()
    right_hand_side = ast.Attribute(
        value=ast.Attribute(value=ast.Name(id='ProvinceEnum'), attr=f'P_{province.code}'), attr='value'
    )
    node = ast.Assign(targets=[ast.Name(id=province_id)], value=right_hand_side)
    return node


def district_enum_member(district: District, province: Province):
    """
    Generate AST tree for line of code equivalent to:
    D_958 = District('Huyện Vĩnh Lợi', 958, VietNamDivisionType.HUYEN, 'huyen_vinh_loi', 95)
    """
    # For example, Huyện Châu Thành of Tỉnh Tiền Giang will have ID "CHAU_THANH_TG"
    enum_def_args = [
        ast.Constant(value=district.name),
        ast.Constant(value=district.code),
        ast.Attribute(value=ast.Name(id='VietNamDivisionType'), attr=district.division_type.name),
        ast.Constant(value=district.codename),
        ast.Constant(value=province.code),
    ]
    node = ast.Assign(
        targets=[ast.Name(id=f'D_{district.code}')],
        value=ast.Call(func=ast.Name(id='District'), args=enum_def_args, keywords=[]),
    )
    return node


def district_descriptive_enum_member(district: District, province: Province):
    """
    Generate AST tree for line of code equivalent to:
    VINH_LOI_BL = DistrictDEnum.D_958.value
    """
    province_abbr = province.abbrev
    # For example, Huyện Châu Thành of Tỉnh Tiền Giang will have ID "CHAU_THANH_TG"
    district_id = f'{district.short_codename}_{province_abbr}'.upper()
    right_hand_side = ast.Attribute(
        value=ast.Attribute(value=ast.Name(id='DistrictEnum'), attr=f'D_{district.code}'), attr='value'
    )
    node = ast.Assign(targets=[ast.Name(id=district_id)], value=right_hand_side)
    return node


def gen_ast_ward_tuple(ward: Ward, district: District, province: Province):
    enum_def_args = [
        ast.Constant(value=ward.name),
        ast.Constant(value=ward.code),
        ast.Attribute(value=ast.Name(id='VietNamDivisionType'), attr=ward.division_type.name),
        ast.Constant(value=ward.codename),
        ast.Constant(value=district.code),
    ]
    return ast.Call(func=ast.Name(id='Ward'), args=enum_def_args, keywords=[])


def ward_enum_member(ward: Ward, district: District, province: Province):
    """
    Generate AST tree for line of code equivalent to:
    QN_TAN_BINH_6904 = Ward('Xã Tân Bình', 6904, VietNamDivisionType.XA, 'xa_tan_binh', 200)
    where:
    - QN means "Tỉnh Quảng Ninh"
    - 6904 is the numeric code of "Xã Tân Bình"
    - 200 is the numberic code of "Huyện Đầm Hà"

    I choose that naming scheme for Ward ID,
    because there are a lot of wards with the same pure-Latin name (after stripping Vietnamese marks),
    stopping us from building unique ID based on Latin letters only.
    For example, we have "Xã Sa Pa" and "Xã Sa Pả", in the same district and province, "Xã Đông Thành"
    and "Xã Đông Thạnh". If only rely on Latin letters, they produce "XA_SA_PA", "XA_SA_PA",
    "XA_DONG_THANNH", "XA_DONG_THANH", indistinguishable.
    """
    ward_id = f'W_{ward.code}'.upper()
    node = ast.Assign(targets=[ast.Name(id=ward_id)], value=gen_ast_ward_tuple(ward, district, province))
    return node


def ward_descriptive_enum_member(ward: Ward, district: District, province: Province):
    """
    Generate AST tree for line of code equivalent to:
    QN_TAN_BINH_6904 = WardEnum.W_6904
    where:
    - QN means "Tỉnh Quảng Ninh"
    - 6904 is the numeric code of "Xã Tân Bình"
    """
    ward_id = f'{province.abbrev}_{ward.short_codename}_{ward.code}'.upper()
    right_hand_side = ast.Attribute(value=ast.Name(id='WardEnum'), attr=f'W_{ward.code}')
    node = ast.Assign(targets=[ast.Name(id=ward_id)], value=right_hand_side)
    return node


def gen_python_district_enums(provinces: Iterable[Province]) -> str:
    template_file = Path(__file__).parent / '_enum_district_template.py'
    module = ast.parse(template_file.read_text())
    class_defs = tuple(n for n in module.body if isinstance(n, ast.ClassDef))
    # Will generate definition for ProvinceEnum, ProvinceDEnum
    province_enum_def = next(n for n in class_defs if n.name == 'ProvinceEnum')
    province_enum_desc_def = next(n for n in class_defs if n.name == 'ProvinceDEnum')
    # Remove example members, except for the docstring.
    old_body = province_enum_def.body
    province_enum_def.body = [m for m in old_body if isinstance(m, ast.Expr)]
    old_body = province_enum_desc_def.body
    province_enum_desc_def.body = [m for m in old_body if isinstance(m, ast.Expr)]
    # Will generate members for DistrictEnum, DistrictDEnum
    district_enum_def = next(n for n in class_defs if n.name == 'DistrictEnum')
    district_enum_desc_def = next(n for n in class_defs if n.name == 'DistrictDEnum')
    # Remove example members, except for the docstring.
    old_body = district_enum_def.body
    district_enum_def.body = [m for m in old_body if isinstance(m, ast.Expr)]
    old_body = district_enum_desc_def.body
    district_enum_desc_def.body = [m for m in old_body if isinstance(m, ast.Expr)]
    for p in provinces:
        node = province_enum_member(p)
        province_enum_def.body.append(node)
        desc_node = province_descriptive_enum_member(p)
        province_enum_desc_def.body.append(desc_node)
        for d in p.indexed_districts.values():
            node_d = district_enum_member(d, p)
            district_enum_def.body.append(node_d)
            desc_node_d = district_descriptive_enum_member(d, p)
            district_enum_desc_def.body.append(desc_node_d)
    return ast.unparse(ast.fix_missing_locations(module))


def gen_python_ward_enums(provinces: Iterable[Province]) -> str:
    template_file = Path(__file__).parent / '_enum_ward_template.py'
    module = ast.parse(template_file.read_text())
    class_defs = tuple(n for n in module.body if isinstance(n, ast.ClassDef))
    # Will generate members for WardEnum and WardDEnum
    ward_enum_def = next(n for n in class_defs if n.name == 'WardEnum')
    ward_desc_enum_def = next(n for n in class_defs if n.name == 'WardDEnum')
    # Remove example members, except for the docstring.
    old_body = ward_enum_def.body
    ward_enum_def.body = [m for m in old_body if isinstance(m, ast.Expr)]
    old_body = ward_desc_enum_def.body
    ward_desc_enum_def.body = [m for m in old_body if isinstance(m, ast.Expr)]
    for p in provinces:
        for d in p.indexed_districts.values():
            for w in d.indexed_wards.values():
                node_w = ward_enum_member(w, d, p)
                ward_enum_def.body.append(node_w)
                node_dw = ward_descriptive_enum_member(w, d, p)
                ward_desc_enum_def.body.append(node_dw)
    return ast.unparse(ast.fix_missing_locations(module))
