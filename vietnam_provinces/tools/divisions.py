import ast
from enum import Enum
from pathlib import Path
from typing import NamedTuple, Optional, List, Tuple, Dict, Sequence

import astor
from logbook import Logger
from pydantic import BaseModel, validator

from .types import Name, convert_to_codename
from .phones import PhoneCodeCSVRecord


logger = Logger(__name__)


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


class VietNamDivisionType(str, Enum):
    # Level 1
    TINH = 'tỉnh'
    THANH_PHO_TRUNG_UONG = 'thành phố trung ương'
    # Level 2
    HUYEN = 'huyện'
    QUAN = 'quận'
    THANH_PHO = 'thành phố'
    THI_XA = 'thị xã'
    # Level 3
    XA = 'xã'
    THI_TRAN = 'thị trấn'
    PHUONG = 'phường'


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

    def dict(self, exclude={}, **kwargs):
        self.districts = tuple(self.indexed_districts.values())
        out = super().dict(exclude={'indexed_districts'}, **kwargs)
        return out


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
    return table


def province_enum_member(province: Province):
    '''
    Generate AST tree for line of code equivalent to:
    HA_NOI = Province('Thành phố Hà Nội', 1, VietNamDivisionType.THANH_PHO_TRUNG_UONG, 'thanh_pho_ha_noi', 24)
    '''
    province_id = province.codename.upper()
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


def gen_python_code(provinces: Sequence[Province]):
    template_file = Path(__file__).parent.parent / '_enum_tpl.py'
    module = astor.parse_file(template_file)
    class_defs = tuple(n for n in module.body if isinstance(n, ast.ClassDef))
    province_enum_def = next(n for n in class_defs if n.name == 'ProvinceEnum')
    province_enum_def.body = []
    for p in provinces:
        node = province_enum_member(p)
        province_enum_def.body.append(node)
    return astor.to_source(module)
