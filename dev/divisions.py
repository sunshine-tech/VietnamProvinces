import ast
from pathlib import Path
from collections import deque
from typing import NamedTuple, Optional, List, Tuple, Dict, Sequence

import astor
from logbook import Logger
from pydantic import BaseModel, validator

from vietnam_provinces.base import VietNamDivisionType
from .types import Name, convert_to_codename, convert_to_id_friendly
from .phones import PhoneCodeCSVRecord


logger = Logger(__name__)


def truncate_leading(line: str, prefixes: Sequence[str]) -> str:
    '''
    Remove substring at the beginning.
    If after removing, the remanining string starts with a number, cancel the removal.
    '''
    for p in prefixes:
        if line.startswith(p):
            truncated = line[len(p):]
            if not truncated[0].isdigit():
                return truncated
    return line


def abbreviate_codename(name: str) -> str:
    '''
    ha_noi -> hano
    '''
    words = name.split('_')
    return ''.join((w[0] for w in words))


def abbreviate_doub_codename(name: str) -> str:
    '''
    tan_thanh -> tath
    thu_thua -> thth
    quan_11 -> qu11
    '''
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
    province_codename: Optional[str]
    district_name: Name
    district_code: int
    district_codename: Optional[str]
    ward_name: Name
    ward_code: int
    ward_codename: Optional[str]

    @validator('province_codename', always=True)
    def set_province_codename(cls, v, values):
        return convert_to_codename(values['province_name'])

    @validator('district_codename', always=True)
    def set_district_codename(cls, v, values):
        return convert_to_codename(values['district_name'])

    @validator('ward_codename', always=True)
    def set_ward_codename(cls, v, values):
        return convert_to_codename(values['ward_name'])

    @classmethod
    def from_csv_row(cls, values: List[str]):
        row = WardCSVInputRow.strip_make(values)
        return cls.parse_obj(row._asdict())


class BaseRegion(BaseModel):
    name: str
    code: int
    codename: Optional[str]


class Ward(BaseRegion):
    # Redefine here, or the validator won't run
    division_type: VietNamDivisionType = None
    short_codename: str = None

    @validator('division_type', pre=True, always=True)
    def parse_division_type(cls, v, values):
        if v:
            return v
        name = values['name'].lower()
        possibles = (VietNamDivisionType.THI_TRAN, VietNamDivisionType.XA, VietNamDivisionType.PHUONG)
        return next((t for t in possibles if name.startswith(f'{t.value} ')), None)


class District(BaseRegion):
    # Redefine here, or the validator won't run
    division_type: VietNamDivisionType = None
    short_codename: str = None
    wards: Tuple[Ward, ...] = ()
    # Actual wards are saved here for fast searching
    indexed_wards: Dict[int, Ward] = None

    def __init__(self, **data):
        super().__init__(**data)
        self.indexed_wards = {}

    @validator('division_type', pre=True, always=True)
    def parse_division_type(cls, v, values):
        if v:
            return v
        name = values['name'].lower()
        possibles = (VietNamDivisionType.THANH_PHO, VietNamDivisionType.THI_XA,
                     VietNamDivisionType.QUAN, VietNamDivisionType.HUYEN)
        return next((t for t in possibles if name.startswith(f'{t.value} ')), None)

    @property
    def abbrev(self):
        return abbreviate_doub_codename(self.short_codename)

    def dict(self, exclude={}, **kwargs):
        self.wards = tuple(self.indexed_wards.values())
        out = super().dict(exclude={'indexed_wards'}, **kwargs)
        return out


class Province(BaseRegion):
    # Redefine here, or the validator won't run
    division_type: VietNamDivisionType = None
    phone_code: Optional[str] = None
    districts: Tuple[District, ...] = ()
    # Actual districts are saved here for fast searching
    indexed_districts: Dict[int, District] = None

    def __init__(self, **data):
        super().__init__(**data)
        self.indexed_districts = {}

    @validator('division_type', pre=True, always=True)
    def parse_division_type(cls, v, values):
        if v:
            return v
        name = values['name'].lower()
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

    def dict(self, exclude={}, **kwargs):
        self.districts = tuple(self.indexed_districts.values())
        out = super().dict(exclude={'indexed_districts'}, **kwargs)
        return out


def generate_district_short_codenames(province: Province):
    '''
    In list of districts of a province, there can be duplicate if stripping prefix, like
    "huyen_ky_anh" and "thi_xa_ky_anh". It is because "Huyện Kỳ Anh" was promoted to "Thị xã" but its old record
    still remains. In that case, we will strip prefix of "thi_xa_ky_anh" but keep original name of "huyen_ky_anh".
    '''
    prefixes = ('huyen_', 'thi_xa_', 'quan_', 'thanh_pho_')
    # First, just generate short_codename as normal
    for d in province.indexed_districts.values():
        d.short_codename = truncate_leading(d.codename, prefixes)
    # Second, find ones whose short_codename is the same as other
    # Nummeric codes of districts whose shortname is duplicate
    duplicates = deque()
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
        d.short_codename = truncate_leading(d.codename, ('thi_xa_', 'quan_', 'thanh_pho_'))


def generate_ward_short_codenames(district: District):
    '''
    In list of wards of a district, there can be duplicate if stripping prefix, like
    "xa_yen_vien" and "thi_tran_yen_vien". It is because "Xã Yên Viên" was promoted to "Thị trấn" but its old record
    still remains. In that case, we will strip prefix of "thi_tran_yen_vien" but keep original name of "xa_yen_vien".
    '''
    prefixes = ('xa_', 'phuong_', 'thi_tran_')
    # First, just generate short_codename as normal
    for w in district.indexed_wards.values():
        w.short_codename = truncate_leading(w.codename, prefixes)
    # Second, find ones whose short_codename is the same as other
    # Nummeric codes of wards whose shortname is duplicate
    duplicates = deque()
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
        w.short_codename = truncate_leading(w.codename, ('phuong_', 'thi_tran_'))
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


def add_to_existing_province(w: WardCSVRecord, province: Province) -> Ward:
    ward = Ward(name=w.ward_name, code=w.ward_code, codename=w.ward_codename)
    try:
        district = province.indexed_districts[w.district_code]
        district.indexed_wards[w.ward_code] = ward
    except KeyError:
        district = District(name=w.district_name, code=w.district_code, codename=w.district_codename)
        province.indexed_districts[w.district_code] = district
        district.indexed_wards = {w.ward_code: ward}
    return ward


def convert_to_nested(records: Sequence[WardCSVRecord],
                      phone_codes: Sequence[PhoneCodeCSVRecord]) -> Dict[int, Province]:
    table = {}    # type: Dict[int, Province]
    for w in records:
        province_code = w.province_code
        try:
            province = table[province_code]
            add_to_existing_province(w, province)
        except KeyError:
            province = Province(name=w.province_name, code=province_code, codename=w.province_codename)
            # Find phone_code
            # c.province_codename will be 'ba_ria_vung_tau'
            # province.codename will be 'tinh_ba_ria_vung_tau'
            matched_phone_code = next((c for c in phone_codes if province.codename.endswith(c.province_codename)), None)
            if matched_phone_code is None:
                logger.error('Could not find phone code for {}', province.name)
            else:
                province.phone_code = matched_phone_code.code
            district = District(name=w.district_name, code=w.district_code, codename=w.district_codename)
            province.indexed_districts[w.district_code] = district
            ward = Ward(name=w.ward_name, code=w.ward_code, codename=w.ward_codename)
            district.indexed_wards[w.ward_code] = ward
            table[province_code] = province
    for p in table.values():
        generate_district_short_codenames(p)
        for d in p.indexed_districts.values():
            generate_ward_short_codenames(d)
    return table


def province_enum_member(province: Province):
    '''
    Generate AST tree for line of code equivalent to:
    HA_NOI = Province('Thành phố Hà Nội', 1, VietNamDivisionType.THANH_PHO_TRUNG_UONG, 'thanh_pho_ha_noi', 24)
    '''
    province_id = province.short_codename.upper()
    enum_def_args = [
        ast.Str(s=province.name),
        ast.Num(n=province.code),
        ast.Attribute(value=ast.Name(id='VietNamDivisionType'), attr=province.division_type.name),
        ast.Str(s=province.codename),
        ast.Num(province.phone_code)
    ]
    node = ast.Assign(targets=[ast.Name(id=province_id)],
                      value=ast.Call(func=ast.Name(id='Province'),
                                     args=enum_def_args,
                                     keywords=[]))
    return node


def district_enum_member(district: District, province: Province):
    '''
    Generate AST tree for line of code equivalent to:
    VINH_LOI_BL = District('Huyện Vĩnh Lợi', 958, VietNamDivisionType.HUYEN, 'huyen_vinh_loi', 95)
    '''
    province_abbr = province.abbrev
    # For example, Huyện Châu Thành of Tỉnh Tiền Giang will have ID "CHAU_THANH_TG"
    district_id = f'{district.short_codename}_{province_abbr}'.upper()
    enum_def_args = [
        ast.Str(s=district.name),
        ast.Num(n=district.code),
        ast.Attribute(value=ast.Name(id='VietNamDivisionType'), attr=district.division_type.name),
        ast.Str(s=district.codename),
        ast.Num(province.code)
    ]
    node = ast.Assign(targets=[ast.Name(id=district_id)],
                      value=ast.Call(func=ast.Name(id='District'),
                                     args=enum_def_args,
                                     keywords=[]))
    return node


def ward_enum_member(ward: Ward, district: District, province: Province):
    '''
    Generate AST tree for line of code equivalent to:
    TAN_BINH_DH = District('Xã Tân Bình', 6904, VietNamDivisionType.XA, 'xa_tan_binh', 200)
    '''
    # For example, Xã Tân Bình of Huyện Đầm Hà (Tỉnh Quảng Ninh) will have ID "TAN_BINH_DH_QN"
    # The reason we have to include province abbreviation name because, includung district only is not enough
    # to create unique ID for ward. For example, I found:
    # "Xã Thanh Bình" of "Huyện Chương Mỹ" -> thanh_binh_cm
    # "Xã Thanh Bình" of "Huyện Chợ Mới" -> thanh_binh_cm
    # are duplicate.
    ward_id = f'{province.abbrev}_{ward.short_codename}_{ward.code}'.upper()
    enum_def_args = [
        ast.Str(s=ward.name),
        ast.Num(n=ward.code),
        ast.Attribute(value=ast.Name(id='VietNamDivisionType'), attr=ward.division_type.name),
        ast.Str(s=ward.codename),
        ast.Num(district.code)
    ]
    node = ast.Assign(targets=[ast.Name(id=ward_id)],
                      value=ast.Call(func=ast.Name(id='Ward'),
                                     args=enum_def_args,
                                     keywords=[]))
    return node


def gen_python_code(provinces: Sequence[Province]):
    template_file = Path(__file__).parent / '_enums_template.py'
    module = astor.parse_file(template_file)
    class_defs = tuple(n for n in module.body if isinstance(n, ast.ClassDef))
    # Will generate definition for ProvinceEnum
    province_enum_def = next(n for n in class_defs if n.name == 'ProvinceEnum')
    province_enum_def.body = []
    # Will generate members for DistrictEnum
    district_enum_def = next(n for n in class_defs if n.name == 'DistrictEnum')
    district_enum_def.body = []
    # Will generate members for WardEnum
    ward_enum_def = next(n for n in class_defs if n.name == 'WardEnum')
    ward_enum_def.body = []
    for p in provinces:
        node = province_enum_member(p)
        province_enum_def.body.append(node)
        for d in p.indexed_districts.values():
            node_d = district_enum_member(d, p)
            district_enum_def.body.append(node_d)
            for w in d.indexed_wards.values():
                node_w = ward_enum_member(w, d, p)
                ward_enum_def.body.append(node_w)
    return astor.to_source(module)


def gen_python_district_enums(provinces: Sequence[Province]) -> str:
    template_file = Path(__file__).parent / '_enums_district_template.py'
    module = astor.parse_file(template_file)
    class_defs = tuple(n for n in module.body if isinstance(n, ast.ClassDef))
    # Will generate definition for ProvinceEnum
    province_enum_def = next(n for n in class_defs if n.name == 'ProvinceEnum')
    province_enum_def.body = []
    # Will generate members for DistrictEnum
    district_enum_def = next(n for n in class_defs if n.name == 'DistrictEnum')
    district_enum_def.body = []
    for p in provinces:
        node = province_enum_member(p)
        province_enum_def.body.append(node)
        for d in p.indexed_districts.values():
            node_d = district_enum_member(d, p)
            district_enum_def.body.append(node_d)
    return astor.to_source(module)


def gen_python_ward_enums(provinces: Sequence[Province]):
    template_file = Path(__file__).parent / '_enums_ward_template.py'
    module = astor.parse_file(template_file)
    class_defs = tuple(n for n in module.body if isinstance(n, ast.ClassDef))
    # Will generate members for WardEnum
    ward_enum_def = next(n for n in class_defs if n.name == 'WardEnum')
    ward_enum_def.body = []
    for p in provinces:
        for d in p.indexed_districts.values():
            for w in d.indexed_wards.values():
                node_w = ward_enum_member(w, d, p)
                ward_enum_def.body.append(node_w)
    return astor.to_source(module)
