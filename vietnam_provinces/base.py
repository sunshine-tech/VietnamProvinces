from enum import Enum
from typing import NamedTuple

from .codes import ProvinceCode, WardCode


class VietNamDivisionType(str, Enum):
    # Level 1
    TINH = 'tỉnh'
    THANH_PHO_TRUNG_UONG = 'thành phố trung ương'
    # Level 2
    XA = 'xã'
    PHUONG = 'phường'
    DAC_KHU = 'đặc khu'


class Ward(NamedTuple):
    name: str
    code: int
    division_type: VietNamDivisionType
    codename: str
    province_code: int

    def __eq__(self, other: object):
        if not isinstance(other, Ward):
            return False
        return other.code == self.code

    @staticmethod
    def from_code(code: WardCode) -> 'Ward':
        from .lookup import WARD_MAPPING

        try:
            return WARD_MAPPING[code]
        except KeyError as e:
            msg = f'Ward code {code} is invalid.'
            raise ValueError(msg) from e


class Province(NamedTuple):
    name: str
    code: int
    division_type: VietNamDivisionType
    codename: str
    phone_code: int

    def __eq__(self, other: object):
        if not isinstance(other, Province):
            return False
        return other.code == self.code

    @staticmethod
    def from_code(code: ProvinceCode) -> 'Province':
        from .lookup import PROVINCE_MAPPING

        try:
            return PROVINCE_MAPPING[code]
        except KeyError as e:
            msg = f'Province code {code} is invalid.'
            raise ValueError(msg) from e
