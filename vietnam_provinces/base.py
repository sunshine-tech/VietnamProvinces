from enum import Enum
from typing import NamedTuple
from dataclasses import dataclass


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


# I make Ward as a type from dataclass, to:
# - Work-around problem with fast-enum
# - Using fast-enum to work-around problem of slow loading standard Enum type in Python.
# In the future, when Python fix the issue with slow Enum, I will base Ward on NamedTuple,
# as other types in this module.
@dataclass(frozen=True)
class Ward:
    name: str
    code: int
    division_type: VietNamDivisionType
    codename: str
    district_code: int


class District(NamedTuple):
    name: str
    code: int
    division_type: VietNamDivisionType
    codename: str
    province_code: int


class Province(NamedTuple):
    name: str
    code: int
    division_type: VietNamDivisionType
    codename: str
    phone_code: int
