# Define main data types for the library.
#
# In the code of this file, sometimes we import other modules inside a function, instead of at the
# top of the file, to avoid loading large datasets when not needed.

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from enum import StrEnum
from logging import getLogger
from typing import TYPE_CHECKING

from .codes import ProvinceCode, WardCode


if TYPE_CHECKING:
    from .legacy.base import Province as LegacyProvince
    from .legacy.base import Ward as LegacyWard


log = getLogger(__name__)


class VietNamDivisionType(StrEnum):
    """Vietnamese administrative division types."""

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
    """Province data type for post-2025 administrative divisions."""

    name: str
    code: ProvinceCode
    division_type: VietNamDivisionType
    codename: str
    phone_code: int

    def __eq__(self, other: object) -> bool:
        """Check equality based on province code.

        :param other: Object to compare with
        :returns: True if other is a :class:`vietnam_provinces.Province` with the same code, False otherwise
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
        :returns: The corresponding :class:`vietnam_provinces.Province` object
        :raises ValueError: If the province code is invalid
        """
        # Cannot use `Self` in return type because this method returns values from
        # a pre-built mapping (PROVINCE_MAPPING), and the type checker cannot infer Self.
        from ._lookup import PROVINCE_MAPPING

        try:
            return PROVINCE_MAPPING[code]
        except KeyError as e:
            msg = f'Province code {code} is invalid.'
            raise ValueError(msg) from e

    @classmethod
    def iter_all(cls) -> Iterator[Province]:
        """Get iterator over all provinces.

        :returns: Iterator over all :class:`vietnam_provinces.Province` objects
        """
        # Cannot use `Self` in return type because this method returns values from
        # a pre-built mapping (PROVINCE_MAPPING), and the type checker cannot infer Self.
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

        If the input contains multiple words, all words must match.

        :param name: Part of a province name to search for
        :returns: Tuple of matching :class:`vietnam_provinces.Province` objects
        """
        if not name:
            log.debug('Empty search query provided')
            return ()

        from .helpers import calculate_simple_match_score, normalize_search_name

        # Split input into words, normalize, and filter out division type prefixes
        division_types = {'tinh', 'thanh', 'pho', 'xa', 'phuong', 'thi', 'tran'}
        words = [normalize_search_name(word) for word in name.split()]
        normalized_words = [word for word in words if word not in division_types]
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

    @classmethod
    def search_from_legacy(cls, name: str = '', code: int = 0) -> tuple[Province, ...]:
        """Given a legacy province code or part of a legacy province name, return all matching provinces.

        This method searches for current (post-2025) provinces that were formed from
        legacy (pre-2025) provinces matching the given criteria.

        :param name: Part of a legacy province name to search for
        :param code: The legacy province code
        :returns: Tuple of matching :class:`vietnam_provinces.Province` objects

        Example:
            >>> # Search by legacy province code
            >>> Province.search_from_legacy(code=77)  # Tỉnh Bà Rịa - Vũng Tàu (old)
            (Province(name='Thành phố Hồ Chí Minh', ...),)
        """
        # Cannot use `Self` in return type because this method uses generator expressions
        # with cls.from_code(), and the type checker cannot infer Self in this context.
        from ._province_conversion_2025 import OLD_TO_NEW
        from .legacy import Province as LegacyProvince
        from .legacy.codes import ProvinceCode as LegacyProvinceCode

        if code > 0:
            if (entry := OLD_TO_NEW.get(code)) is None:
                log.debug('No conversion entry found for legacy province code %s', code)
                return ()
            return tuple(cls.from_code(ProvinceCode(np.code)) for np in entry.new_provinces)

        if not name:
            log.debug('Empty search query provided')
            return ()

        # Search by name - normalize and match (ignoring division type prefix)
        from .helpers import calculate_province_match_score, normalize_province_search_name

        # Split input into words, normalize, and filter out division type prefixes
        division_types = {'tinh', 'thanh', 'pho', 'xa', 'phuong', 'thi', 'tran'}
        words = [normalize_province_search_name(word) for word in name.split()]
        normalized_words = [word for word in words if word not in division_types]
        query = normalize_province_search_name(name)
        results: list[tuple[Province, str, int]] = []  # (province, old_name, match_score)
        seen_codes: set[int] = set()

        for old_code, entry in OLD_TO_NEW.items():
            try:
                legacy_province = LegacyProvince.from_code(LegacyProvinceCode(old_code))
                old_name = legacy_province.name
                division_type = legacy_province.division_type.value
            except (ValueError, KeyError):
                log.debug('Legacy province code %s not found in lookup', old_code)
                continue

            normalized_old_name = normalize_province_search_name(old_name)
            # Split normalized name into words for whole-word matching
            name_words = set(normalized_old_name.split())

            # All query words must be present as whole words in the name
            if not all(word in name_words for word in normalized_words):
                continue

            # Calculate match score with division type priority (thành phố > tỉnh)
            match_score = calculate_province_match_score(name, query, old_name, division_type)

            for np in entry.new_provinces:
                if np.code in seen_codes:
                    continue

                try:
                    province = cls.from_code(ProvinceCode(np.code))
                    results.append((province, old_name, match_score))
                    seen_codes.add(np.code)
                except ValueError:
                    log.debug('New province code %s not found in lookup', np.code)
                    continue

        # Sort by match score (lower is better)
        results.sort(key=lambda x: x[2])
        return tuple(province for province, _, _ in results)

    def get_legacy_sources(self) -> tuple[LegacyProvince, ...]:
        """Get the legacy (pre-2025) province sources that were merged to form this province.

        This method returns the legacy provinces that were merged or reorganized to form
        the current (post-2025) province.

        :returns: Tuple of legacy :class:`vietnam_provinces.legacy.Province` objects

        Example:
            >>> province = Province.from_code(79)  # Thành phố Hồ Chí Minh
            >>> province.get_legacy_sources()
            (Province(name='Tỉnh Bình Dương', ...), Province(name='Tỉnh Bà Rịa - Vũng Tàu', ...),
             Province(name='Thành phố Hồ Chí Minh', ...))
        """
        from ._province_conversion_2025 import NEW_TO_OLD
        from .legacy import Province as LegacyProvince
        from .legacy.codes import ProvinceCode as LegacyProvinceCode

        if (entry := NEW_TO_OLD.get(self.code.value)) is None:
            log.debug('No legacy source found for province code %s', self.code.value)
            return ()

        legacy_provinces: list[LegacyProvince] = []
        for old_ref in entry.old_provinces:
            try:
                province = LegacyProvince.from_code(LegacyProvinceCode(old_ref.code))
                legacy_provinces.append(province)
            except (ValueError, KeyError):
                log.debug('Legacy province code %s not found in lookup', old_ref.code)
                continue

        return tuple(legacy_provinces)


@dataclass(frozen=True)
class Ward:
    """Ward data type for post-2025 administrative divisions."""

    name: str
    code: WardCode
    division_type: VietNamDivisionType
    codename: str
    province_code: ProvinceCode

    def __eq__(self, other: object) -> bool:
        """Check equality based on ward code.

        :param other: Object to compare with
        :returns: True if other is a :class:`vietnam_provinces.Ward` with the same code, False otherwise
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
        :returns: The corresponding :class:`vietnam_provinces.Ward` object
        :raises ValueError: If the ward code is invalid
        """
        # Cannot use `Self` in return type because this method returns values from
        # a pre-built mapping (WARD_MAPPING), and the type checker cannot infer Self.
        from ._lookup import WARD_MAPPING

        try:
            return WARD_MAPPING[code]
        except KeyError as e:
            msg = f'Ward code {code} is invalid.'
            raise ValueError(msg) from e

    @classmethod
    def iter_all(cls) -> Iterator[Ward]:
        """Get iterator over all wards.

        :returns: Iterator over all :class:`vietnam_provinces.Ward` objects
        """
        # Cannot use `Self` in return type because this method returns values from
        # a pre-built mapping (WARD_MAPPING), and the type checker cannot infer Self.
        from ._lookup import WARD_MAPPING

        values = WARD_MAPPING.values()
        return iter(values)

    @classmethod
    def iter_by_province(cls, code: ProvinceCode) -> Iterator[Ward]:
        """Get iterator over wards belonging to a province.

        :param code: The province code
        :returns: Iterator over :class:`vietnam_provinces.Ward` objects belonging to the specified province
        """
        # Cannot use `Self` in return type because this method returns values from
        # a pre-built mapping (WARD_MAPPING), and the type checker cannot infer Self.
        from ._lookup import WARD_MAPPING

        values = iter(w for w in WARD_MAPPING.values() if w.province_code == code)
        return values

    @classmethod
    def search(cls, name: str = '') -> tuple[Ward, ...]:
        """Search for wards by name.

        This method searches for wards matching the given name with priority:
        1. Exact match (case-sensitive, with diacritics)
        2. Exact match (case-insensitive, with diacritics)
        3. Exact match (normalized, no diacritics)
        4. Partial match (earlier position is better)

        If the input contains multiple words, all words must match.

        :param name: Part of a ward name to search for
        :returns: Tuple of matching :class:`vietnam_provinces.Ward` objects
        """
        if not name:
            log.debug('Empty search query provided')
            return ()

        from .helpers import calculate_simple_match_score, normalize_search_name

        # Split input into words, normalize, and filter out division type prefixes
        division_types = {'tinh', 'thanh', 'pho', 'xa', 'phuong', 'thi', 'tran'}
        words = [normalize_search_name(word) for word in name.split()]
        normalized_words = [word for word in words if word not in division_types]
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

    @classmethod
    def search_from_legacy(cls, name: str = '', code: int = 0) -> tuple[Ward, ...]:
        """Given a legacy ward code or part of a legacy ward name, return all matching wards.

        This method searches for current (post-2025) wards that were formed from
        legacy (pre-2025) wards matching the given criteria.

        :param name: Part of a legacy ward name to search for
        :param code: The legacy ward code
        :returns: Tuple of matching :class:`vietnam_provinces.Ward` objects

        Example:
            >>> # Search by legacy ward name
            >>> Ward.search_from_legacy(name='phu my')
            (Ward(name='Phường Phú Mỹ', ...), Ward(name='Xã Phú Mỹ', ...), ...)

            >>> # Search by legacy ward code
            >>> Ward.search_from_legacy(code=22855)  # Xã Tân Hải
            (Ward(name='Xã Tân Hải', ...),)
        """
        # Cannot use `Self` in return type because this method uses generator expressions
        # with cls.from_code(), and the type checker cannot infer Self in this context.
        from ._ward_conversion_2025 import OLD_TO_NEW
        from .legacy import Ward as LegacyWard
        from .legacy.codes import WardCode as LegacyWardCode

        if code > 0:
            if (entry := OLD_TO_NEW.get(code)) is None:
                log.debug('No conversion entry found for legacy ward code %s', code)
                return ()
            return tuple(cls.from_code(WardCode(nw.code)) for nw in entry.new_wards)

        if not name:
            log.debug('Empty search query provided')
            return ()

        from ._bridges import calculate_match_score
        from .helpers import normalize_search_name

        # Split input into words, normalize, and filter out division type prefixes
        division_types = {'tinh', 'thanh', 'pho', 'xa', 'phuong', 'thi', 'tran'}
        words = [normalize_search_name(word) for word in name.split()]
        normalized_words = [word for word in words if word not in division_types]
        query = normalize_search_name(name)
        results: list[tuple[Ward, str, int]] = []  # (ward, old_name, match_score)
        seen_codes: set[int] = set()

        for old_code, entry in OLD_TO_NEW.items():
            # Look up the old ward name from legacy dataclass
            try:
                legacy_ward = LegacyWard.from_code(LegacyWardCode(old_code))
                old_name = legacy_ward.name
            except (ValueError, KeyError):
                log.debug('Legacy ward code %s not found in lookup', old_code)
                continue

            normalized_old_name = normalize_search_name(old_name)
            # Split normalized name into words for whole-word matching
            name_words = set(normalized_old_name.split())

            # All query words must be present as whole words in the name
            if not all(word in name_words for word in normalized_words):
                continue

            # Calculate match score (lower is better)
            match_score = calculate_match_score(name, query, old_name, legacy_ward.division_type)

            for nw in entry.new_wards:
                if nw.code in seen_codes:
                    continue

                try:
                    ward = cls.from_code(WardCode(nw.code))
                    results.append((ward, old_name, match_score))
                    seen_codes.add(nw.code)
                except ValueError:
                    log.debug('New ward code %s not found in lookup', nw.code)
                    continue

        # Sort by match score (lower is better)
        results.sort(key=lambda x: x[2])
        return tuple(ward for ward, _, _ in results)

    @classmethod
    def search_from_legacy_district(cls, name: str = '', code: int = 0) -> tuple[Ward, ...]:
        """Given a legacy district code or part of a legacy district name, return all new wards.

        This method searches for current (post-2025) wards that were formed from
        legacy (pre-2025) districts matching the given criteria.
        Since districts were dissolved in the 2025 administrative rearrangement,
        this helps find which new wards now cover the area of an old district.

        :param name: Part of a legacy district name to search for
        :param code: The legacy district code
        :returns: Tuple of matching :class:`vietnam_provinces.Ward` objects

        Example:
            >>> # Search by legacy district code
            >>> Ward.search_from_legacy_district(code=748)  # Thành phố Bà Rịa (old)
            (Ward(name='Phường Bà Rịa', ...), Ward(name='Phường Long Hương', ...), ...)

            >>> # Search by legacy district name
            >>> Ward.search_from_legacy_district(name='Bà Rịa')
            (Ward(name='Phường Bà Rịa', ...), Ward(name='Phường Long Hương', ...), ...)
        """
        from ._ward_conversion_2025 import OLD_TO_NEW
        from .legacy import District as LegacyDistrict

        if code > 0:
            # Find all legacy wards in this district, then get their new wards
            district_code = code
        elif name:
            # Search for districts by name
            districts = LegacyDistrict.search(name)
            if not districts:
                log.debug('No legacy district found matching name %r', name)
                return ()
            # Use the first matching district
            district_code = districts[0].code.value
        else:
            log.debug('Empty search query provided')
            return ()

        # Collect all new ward codes from wards in this district
        new_ward_codes: set[int] = set()

        for old_code, entry in OLD_TO_NEW.items():
            if entry.old_ward.district_code == district_code:
                for nw in entry.new_wards:
                    new_ward_codes.add(nw.code)

        if not new_ward_codes:
            log.debug('No new wards found for legacy district code %s', district_code)
            return ()

        # Convert to Ward objects
        wards: list[Ward] = []
        for nw_code in sorted(new_ward_codes):
            try:
                ward = cls.from_code(WardCode(nw_code))
                wards.append(ward)
            except ValueError:
                log.debug('New ward code %s not found in lookup', nw_code)
                continue

        return tuple(wards)

    def get_legacy_sources(self) -> tuple[LegacyWard, ...]:
        """Get the legacy (pre-2025) ward sources that were merged to form this ward.

        This method returns the legacy wards that were merged or reorganized to form
        the current (post-2025) ward.

        :returns: Tuple of legacy :class:`vietnam_provinces.legacy.Ward` objects

        Example:
            >>> ward = Ward.from_code(4)  # Phường Ba Đình
            >>> ward.get_legacy_sources()
            (Ward(name='Phường Trúc Bạch', ...), Ward(name='Phường Quán Thánh', ...), ...)

            >>> ward = Ward.from_code(22861)  # Xã Tân Hải
            >>> ward.get_legacy_sources()
            (Ward(name='Xã Tân Hải', ...),)
        """
        from ._ward_conversion_2025 import NEW_TO_OLD
        from .legacy import Ward as LegacyWard
        from .legacy.codes import WardCode as LegacyWardCode

        if (entry := NEW_TO_OLD.get(self.code.value)) is None:
            log.debug('No legacy source found for ward code %s', self.code.value)
            return ()

        legacy_wards: list[LegacyWard] = []
        for old_ref in entry.old_wards:
            try:
                ward = LegacyWard.from_code(LegacyWardCode(old_ref.code))
                legacy_wards.append(ward)
            except (ValueError, KeyError):
                log.debug('Legacy ward code %s not found in lookup', old_ref.code)
                continue

        return tuple(legacy_wards)
