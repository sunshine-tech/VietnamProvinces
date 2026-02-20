# Data types for pre-2025 administrative divisions.
# These types represent the 3-level hierarchy: Province -> District -> Ward
# that existed before the July 2025 administrative rearrangement.

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import TYPE_CHECKING

from .codes import DistrictCode, ProvinceCode, WardCode


if TYPE_CHECKING:
    from collections.abc import Iterator


class VietNamDivisionType(StrEnum):
    """Division types for pre-2025 administrative units."""

    # Level 1: Provinces
    TINH = 'tỉnh'
    THANH_PHO_TRUNG_UONG = 'thành phố trung ương'
    # Level 2: Districts
    HUYEN = 'huyện'
    QUAN = 'quận'
    THANH_PHO = 'thành phố'
    THI_XA = 'thị xã'
    # Level 3: Wards
    XA = 'xã'
    THI_TRAN = 'thị trấn'
    PHUONG = 'phường'


@dataclass(frozen=True)
class Province:
    """Province data type for pre-2025 administrative divisions."""

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
    def from_code(code: ProvinceCode) -> Province:
        """Look up a Province from code."""
        from .lookup import PROVINCE_MAPPING

        try:
            return PROVINCE_MAPPING[code]
        except KeyError as e:
            msg = f'Province code {code} is invalid.'
            raise ValueError(msg) from e

    @staticmethod
    def iter_all() -> Iterator[Province]:
        """Get iterator over all provinces."""
        from .lookup import PROVINCE_MAPPING

        values = PROVINCE_MAPPING.values()
        return iter(values)


@dataclass(frozen=True)
class District:
    """District data type for pre-2025 administrative divisions."""

    name: str
    code: DistrictCode
    division_type: VietNamDivisionType
    codename: str
    province_code: ProvinceCode

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, District):
            return False
        return other.code == self.code

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def from_code(code: DistrictCode) -> District:
        """Look up a District from code."""
        from .lookup import DISTRICT_MAPPING

        try:
            return DISTRICT_MAPPING[code]
        except KeyError as e:
            msg = f'District code {code} is invalid.'
            raise ValueError(msg) from e

    @staticmethod
    def iter_all() -> Iterator[District]:
        """Get iterator over all districts."""
        from .lookup import DISTRICT_MAPPING

        values = DISTRICT_MAPPING.values()
        return iter(values)

    @staticmethod
    def iter_by_province(code: ProvinceCode) -> Iterator[District]:
        """Get iterator over districts belonging to a province."""
        from .lookup import DISTRICT_MAPPING

        values = (d for d in DISTRICT_MAPPING.values() if d.province_code == code)
        return values


@dataclass(frozen=True)
class Ward:
    """Ward data type for pre-2025 administrative divisions."""

    name: str
    code: WardCode
    division_type: VietNamDivisionType
    codename: str
    district_code: DistrictCode

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ward):
            return False
        return other.code == self.code

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def from_code(code: WardCode) -> Ward:
        """Look up a Ward from code."""
        from .lookup import WARD_MAPPING

        try:
            return WARD_MAPPING[code]
        except KeyError as e:
            msg = f'Ward code {code} is invalid.'
            raise ValueError(msg) from e

    @staticmethod
    def iter_all() -> Iterator[Ward]:
        """Get iterator over all wards."""
        from .lookup import WARD_MAPPING

        values = WARD_MAPPING.values()
        return iter(values)

    @staticmethod
    def iter_by_district(code: DistrictCode) -> Iterator[Ward]:
        """Get iterator over wards belonging to a district."""
        from .lookup import WARD_MAPPING

        values = (w for w in WARD_MAPPING.values() if w.district_code == code)
        return values

    @staticmethod
    def iter_by_province(code: ProvinceCode) -> Iterator[Ward]:
        """Get iterator over wards belonging to a province."""
        from .lookup import WARD_MAPPING

        values = (w for w in WARD_MAPPING.values() if w.province_code == code)
        return iter(values)

    @property
    def province_code(self) -> ProvinceCode:
        """Get the province code for this ward (via district)."""
        from .lookup import DISTRICT_MAPPING

        district = DISTRICT_MAPPING[self.district_code]
        return district.province_code
