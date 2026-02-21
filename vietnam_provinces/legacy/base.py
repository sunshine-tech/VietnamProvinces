# Data types for pre-2025 administrative divisions.
# These types represent the 3-level hierarchy: Province -> District -> Ward
# that existed before the July 2025 administrative rearrangement.

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from logging import getLogger
from typing import TYPE_CHECKING

from .codes import DistrictCode, ProvinceCode, WardCode


if TYPE_CHECKING:
    from collections.abc import Iterator


log = getLogger(__name__)


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
        """Check equality based on province code.

        :param other: Object to compare with
        :returns: True if other is a :class:`vietnam_provinces.legacy.Province` with the same code, False otherwise
        """
        if not isinstance(other, Province):
            return False
        return other.code == self.code

    def __str__(self) -> str:
        """Return the province name.

        :returns: The province name
        """
        return self.name

    @classmethod
    def from_code(cls, code: ProvinceCode) -> Province:
        """Look up a Province from code.

        :param code: The province code
        :returns: The corresponding :class:`vietnam_provinces.legacy.Province` object
        :raises ValueError: If the province code is invalid
        """
        from ._lookup import PROVINCE_MAPPING

        try:
            return PROVINCE_MAPPING[code]
        except KeyError as e:
            msg = f'Province code {code} is invalid.'
            raise ValueError(msg) from e

    @classmethod
    def iter_all(cls) -> Iterator[Province]:
        """Get iterator over all provinces.

        :returns: Iterator over all :class:`vietnam_provinces.legacy.Province` objects
        """
        from ._lookup import PROVINCE_MAPPING

        values = PROVINCE_MAPPING.values()
        return iter(values)

    @classmethod
    def search(cls, name: str = '') -> tuple[Province, ...]:
        """Search for provinces by name.

        This method searches for provinces matching the given name with priority:
        1. Exact match (case-sensitive, with diacritics)
        2. Exact match (case-insensitive, with diacritics)
        3. Exact match (normalized, no diacritics)
        4. Partial match (earlier position is better)

        If the input contains multiple words, all words must match as whole words.

        :param name: Part of a province name to search for
        :returns: Tuple of matching :class:`vietnam_provinces.legacy.Province` objects
        """
        if not name:
            log.debug('Empty search query provided')
            return ()

        from ..helpers import calculate_simple_match_score, normalize_search_name

        # Split input into words, normalize, and filter out division type prefixes
        # Only filter if they appear at the beginning (e.g., "Tỉnh Hà Giang" -> "Hà Giang")
        division_types = {'tinh', 'thanh', 'pho'}
        words = [normalize_search_name(word) for word in name.split()]
        # Only skip division type words at the beginning
        normalized_words = []
        skipped_prefix = True
        for word in words:
            if skipped_prefix and word in division_types:
                continue
            skipped_prefix = False
            normalized_words.append(word)
        query = normalize_search_name(name)
        results: list[tuple[Province, int]] = []  # (province, match_score)

        for province in cls.iter_all():
            normalized_name = normalize_search_name(province.name)
            # Split normalized name into words for whole-word matching
            name_words = set(normalized_name.split())

            # All query words must be present as whole words in the name
            if not all(word in name_words for word in normalized_words):
                continue

            # Calculate match score (lower is better)
            match_score = calculate_simple_match_score(name, query, province.name)
            results.append((province, match_score))

        # Sort by match score (lower is better)
        results.sort(key=lambda x: x[1])
        return tuple(province for province, _ in results)


@dataclass(frozen=True)
class District:
    """District data type for pre-2025 administrative divisions."""

    name: str
    code: DistrictCode
    division_type: VietNamDivisionType
    codename: str
    province_code: ProvinceCode

    def __eq__(self, other: object) -> bool:
        """Check equality based on district code.

        :param other: Object to compare with
        :returns: True if other is a :class:`vietnam_provinces.legacy.District` with the same code, False otherwise
        """
        if not isinstance(other, District):
            return False
        return other.code == self.code

    def __str__(self) -> str:
        """Return the district name.

        :returns: The district name
        """
        return self.name

    @classmethod
    def from_code(cls, code: DistrictCode) -> District:
        """Look up a District from code.

        :param code: The district code
        :returns: The corresponding :class:`vietnam_provinces.legacy.District` object
        :raises ValueError: If the district code is invalid
        """
        from ._lookup import DISTRICT_MAPPING

        try:
            return DISTRICT_MAPPING[code]
        except KeyError as e:
            msg = f'District code {code} is invalid.'
            raise ValueError(msg) from e

    @classmethod
    def iter_all(cls) -> Iterator[District]:
        """Get iterator over all districts.

        :returns: Iterator over all :class:`vietnam_provinces.legacy.District` objects
        """
        from ._lookup import DISTRICT_MAPPING

        values = DISTRICT_MAPPING.values()
        return iter(values)

    @classmethod
    def iter_by_province(cls, code: ProvinceCode) -> Iterator[District]:
        """Get iterator over districts belonging to a province.

        :param code: The province code (:class:`vietnam_provinces.legacy.ProvinceCode`)
        :returns: Iterator over :class:`vietnam_provinces.legacy.District` objects belonging to the specified province
        """
        from ._lookup import DISTRICT_MAPPING

        values = (d for d in DISTRICT_MAPPING.values() if d.province_code == code)
        return values

    @classmethod
    def search(cls, name: str = '') -> tuple[District, ...]:
        """Search for districts by name.

        This method searches for districts matching the given name with priority:
        1. Exact match (case-sensitive, with diacritics)
        2. Exact match (case-insensitive, with diacritics)
        3. Exact match (normalized, no diacritics)
        4. Partial match (earlier position is better)

        If the input contains multiple words, all words must match as whole words.

        :param name: Part of a district name to search for
        :returns: Tuple of matching :class:`vietnam_provinces.legacy.District` objects
        """
        if not name:
            log.debug('Empty search query provided')
            return ()

        from ..helpers import calculate_simple_match_score, normalize_search_name

        # Split input into words, normalize, and filter out division type prefixes
        # Only filter if they appear at the beginning (e.g., "Xã Tân Hòa" -> "Tân Hòa")
        division_types = {'tinh', 'thanh', 'pho', 'quan', 'huyen', 'thi', 'xa', 'phuong', 'thi', 'tran'}
        words = [normalize_search_name(word) for word in name.split()]
        # Only skip division type words at the beginning
        normalized_words = []
        skipped_prefix = True
        for word in words:
            if skipped_prefix and word in division_types:
                continue
            skipped_prefix = False
            normalized_words.append(word)
        query = normalize_search_name(name)
        results: list[tuple[District, int]] = []  # (district, match_score)

        for district in cls.iter_all():
            normalized_name = normalize_search_name(district.name)
            # Split normalized name into words for whole-word matching
            name_words = set(normalized_name.split())

            # All query words must be present as whole words in the name
            if not all(word in name_words for word in normalized_words):
                continue

            # Calculate match score (lower is better)
            match_score = calculate_simple_match_score(name, query, district.name)
            results.append((district, match_score))

        # Sort by match score (lower is better)
        results.sort(key=lambda x: x[1])
        return tuple(district for district, _ in results)


@dataclass(frozen=True)
class Ward:
    """Ward data type for pre-2025 administrative divisions."""

    name: str
    code: WardCode
    division_type: VietNamDivisionType
    codename: str
    district_code: DistrictCode

    def __eq__(self, other: object) -> bool:
        """Check equality based on ward code.

        :param other: Object to compare with
        :returns: True if other is a :class:`vietnam_provinces.legacy.Ward` with the same code, False otherwise
        """
        if not isinstance(other, Ward):
            return False
        return other.code == self.code

    def __str__(self) -> str:
        """Return the ward name.

        :returns: The ward name
        """
        return self.name

    @classmethod
    def from_code(cls, code: WardCode) -> Ward:
        """Look up a Ward from code.

        :param code: The ward code
        :returns: The corresponding :class:`vietnam_provinces.legacy.Ward` object
        :raises ValueError: If the ward code is invalid
        """
        from ._lookup import WARD_MAPPING

        try:
            return WARD_MAPPING[code]
        except KeyError as e:
            msg = f'Ward code {code} is invalid.'
            raise ValueError(msg) from e

    @classmethod
    def iter_all(cls) -> Iterator[Ward]:
        """Get iterator over all wards.

        :returns: Iterator over all :class:`vietnam_provinces.legacy.Ward` objects
        """
        from ._lookup import WARD_MAPPING

        values = WARD_MAPPING.values()
        return iter(values)

    @classmethod
    def iter_by_district(cls, code: DistrictCode) -> Iterator[Ward]:
        """Get iterator over wards belonging to a district.

        :param code: The district code (:class:`vietnam_provinces.legacy.DistrictCode`)
        :returns: Iterator over :class:`vietnam_provinces.legacy.Ward` objects belonging to the specified district
        """
        from ._lookup import WARD_MAPPING

        values = (w for w in WARD_MAPPING.values() if w.district_code == code)
        return values

    @classmethod
    def iter_by_province(cls, code: ProvinceCode) -> Iterator[Ward]:
        """Get iterator over wards belonging to a province.

        :param code: The province code (:class:`vietnam_provinces.legacy.ProvinceCode`)
        :returns: Iterator over :class:`vietnam_provinces.legacy.Ward` objects belonging to the specified province
        """
        from ._lookup import WARD_MAPPING

        values = (w for w in WARD_MAPPING.values() if w.province_code == code)
        return iter(values)

    @property
    def province_code(self) -> ProvinceCode:
        """Get the province code for this ward (via district).

        :returns: The province code (:class:`vietnam_provinces.legacy.ProvinceCode`)
        """
        from ._lookup import DISTRICT_MAPPING

        district = DISTRICT_MAPPING[self.district_code]
        return district.province_code

    @classmethod
    def search(cls, name: str = '') -> tuple[Ward, ...]:
        """Search for wards by name.

        This method searches for wards matching the given name with priority:
        1. Exact match (case-sensitive, with diacritics)
        2. Exact match (case-insensitive, with diacritics)
        3. Exact match (normalized, no diacritics)
        4. Partial match (earlier position is better)

        If the input contains multiple words, all words must match as whole words.

        :param name: Part of a ward name to search for
        :returns: Tuple of matching :class:`vietnam_provinces.legacy.Ward` objects
        """
        if not name:
            log.debug('Empty search query provided')
            return ()

        from ..helpers import calculate_simple_match_score, normalize_search_name

        # Split input into words, normalize, and filter out division type prefixes
        # Only filter if they appear at the beginning (e.g., "Xã Tân Hòa" -> "Tân Hòa")
        division_types = {'tinh', 'thanh', 'pho', 'quan', 'huyen', 'thi', 'xa', 'phuong', 'thi', 'tran'}
        words = [normalize_search_name(word) for word in name.split()]
        # Only skip division type words at the beginning
        normalized_words = []
        skipped_prefix = True
        for word in words:
            if skipped_prefix and word in division_types:
                continue
            skipped_prefix = False
            normalized_words.append(word)
        query = normalize_search_name(name)
        results: list[tuple[Ward, int]] = []  # (ward, match_score)

        for ward in cls.iter_all():
            normalized_name = normalize_search_name(ward.name)
            # Split normalized name into words for whole-word matching
            name_words = set(normalized_name.split())

            # All query words must be present as whole words in the name
            if not all(word in name_words for word in normalized_words):
                continue

            # Calculate match score (lower is better)
            match_score = calculate_simple_match_score(name, query, ward.name)
            results.append((ward, match_score))

        # Sort by match score (lower is better)
        results.sort(key=lambda x: x[1])
        return tuple(ward for ward, _ in results)
