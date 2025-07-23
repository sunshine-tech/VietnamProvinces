from enum import Enum
from dataclasses import dataclass


class VietNamDivisionType(str, Enum):
    # Level 1
    TINH = 'tỉnh'
    THANH_PHO_TRUNG_UONG = 'thành phố trung ương'
    # Level 2
    XA = 'xã'
    PHUONG = 'phường'
    DAC_KHU = 'đặc khu'


@dataclass(frozen=True)
class Ward:
    __slots__ = ('name', 'code', 'division_type', 'codename', 'province_code')
    name: str
    code: int
    division_type: VietNamDivisionType
    codename: str
    province_code: int

    def __eq__(self, other: object):
        if not isinstance(other, Ward):
            return False
        return other.code == self.code


@dataclass
class Province:
    name: str
    code: int
    division_type: VietNamDivisionType
    codename: str
    phone_code: int

    def __eq__(self, other: object):
        if not isinstance(other, Province):
            return False
        return other.code == self.code
