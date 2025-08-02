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

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Ward):
            return other.code == self.code
        if isinstance(other, tuple):
            return other == tuple(self)
        return False

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def from_code(code: WardCode) -> 'Ward':
        """Look up a Ward from code."""
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

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Province):
            return other.code == self.code
        if isinstance(other, tuple):
            return other == tuple(self)
        return False

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def from_code(code: ProvinceCode) -> 'Province':
        """Look up a Province from code."""
        from .lookup import PROVINCE_MAPPING

        try:
            return PROVINCE_MAPPING[code]
        except KeyError as e:
            msg = f'Province code {code} is invalid.'
            raise ValueError(msg) from e
