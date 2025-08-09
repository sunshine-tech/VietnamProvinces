from collections.abc import Iterator
from dataclasses import dataclass
from enum import Enum

from .codes import ProvinceCode, WardCode


class VietNamDivisionType(str, Enum):
    # Level 1
    TINH = 'tỉnh'
    THANH_PHO_TRUNG_UONG = 'thành phố trung ương'
    # Level 2
    XA = 'xã'
    PHUONG = 'phường'
    DAC_KHU = 'đặc khu'


# We use dataclass instead of NamedTuple to allow this class
# to be mixed in Pydandic dataclass in application side.
@dataclass(frozen=True)
class Province:
    name: str
    code: ProvinceCode
    division_type: VietNamDivisionType
    codename: str
    phone_code: int

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Province):
            return False
        return other.code == self.code

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

    @staticmethod
    def iter_all() -> Iterator['Province']:
        """Get iterator over all provinces."""
        from .lookup import PROVINCE_MAPPING

        values = PROVINCE_MAPPING.values()
        return iter(values)


@dataclass(frozen=True)
class Ward:
    name: str
    code: WardCode
    division_type: VietNamDivisionType
    codename: str
    province_code: ProvinceCode

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ward):
            return False
        return other.code == self.code

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

    @staticmethod
    def iter_all() -> Iterator['Ward']:
        """Get iterator over all wards."""
        from .lookup import WARD_MAPPING

        values = WARD_MAPPING.values()
        return iter(values)

    @staticmethod
    def iter_by_province(code: ProvinceCode) -> Iterator['Ward']:
        """Get iterator over wards belonging to a province."""
        from .lookup import WARD_MAPPING

        values = iter(w for w in WARD_MAPPING.values() if w.province_code == code)
        return values
