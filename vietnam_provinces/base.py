# Define main data types for the library.
#
# In the code of this file, sometimes we import other modules inside a function, instead of at the
# top of the file, to avoid loading large datasets when not needed.

from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterator
from dataclasses import dataclass
from enum import StrEnum
from logging import getLogger
from typing import TYPE_CHECKING

from .codes import ProvinceCode, WardCode


if TYPE_CHECKING:
    from ._ward_conversion_2025 import OldWardRef
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

    @staticmethod
    def from_code(code: ProvinceCode) -> Province:
        """Look up a Province from code.

        :param code: The province code
        :returns: The corresponding :class:`vietnam_provinces.Province` object
        :raises ValueError: If the province code is invalid
        """
        from ._lookup import PROVINCE_MAPPING

        try:
            return PROVINCE_MAPPING[code]
        except KeyError as e:
            msg = f'Province code {code} is invalid.'
            raise ValueError(msg) from e

    @staticmethod
    def iter_all() -> Iterator[Province]:
        """Get iterator over all provinces.

        :returns: Iterator over all :class:`vietnam_provinces.Province` objects
        """
        from ._lookup import PROVINCE_MAPPING

        values = PROVINCE_MAPPING.values()
        return iter(values)


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

    @staticmethod
    def from_code(code: WardCode) -> Ward:
        """Look up a Ward from code.

        :param code: The ward code
        :returns: The corresponding :class:`vietnam_provinces.Ward` object
        :raises ValueError: If the ward code is invalid
        """
        from ._lookup import WARD_MAPPING

        try:
            return WARD_MAPPING[code]
        except KeyError as e:
            msg = f'Ward code {code} is invalid.'
            raise ValueError(msg) from e

    @staticmethod
    def iter_all() -> Iterator[Ward]:
        """Get iterator over all wards.

        :returns: Iterator over all :class:`vietnam_provinces.Ward` objects
        """
        from ._lookup import WARD_MAPPING

        values = WARD_MAPPING.values()
        return iter(values)

    @staticmethod
    def iter_by_province(code: ProvinceCode) -> Iterator[Ward]:
        """Get iterator over wards belonging to a province.

        :param code: The province code
        :returns: Iterator over :class:`vietnam_provinces.Ward` objects belonging to the specified province
        """
        from ._lookup import WARD_MAPPING

        values = iter(w for w in WARD_MAPPING.values() if w.province_code == code)
        return values

    @classmethod
    def search_from_legacy(cls, name: str = '', code: int = 0) -> tuple[Ward, ...]:
        """Given a legacy ward code or part of a legacy ward name, return all matching wards.

        :param name: Part of a legacy ward name to search for
        :param code: The legacy ward code
        :returns: Tuple of matching :class:`vietnam_provinces.Ward` objects
        """
        from ._ward_conversion_2025 import OLD_TO_NEW

        if code > 0:
            if (entry := OLD_TO_NEW.get(code)) is None:
                log.debug('No conversion entry found for legacy ward code %s', code)
                return ()
            return tuple(cls.from_code(WardCode(nw.code)) for nw in entry.new_wards)

        if not name:
            log.debug('Empty search query provided')
            return ()

        query = _normalize_search_name(name)
        results: list[tuple[Ward, str, int]] = []  # (ward, old_name, match_score)
        seen_codes: set[int] = set()

        for entry in OLD_TO_NEW.values():
            old_name = entry.old_ward.name
            normalized_old_name = _normalize_search_name(old_name)

            if query not in normalized_old_name:
                continue

            # Calculate match score (lower is better)
            match_score = _calculate_match_score(name, query, entry.old_ward)

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

    def get_legacy_sources(self) -> tuple[LegacyWard, ...]:
        """Get the legacy (pre-2025) ward sources that were merged to form this ward.

        :returns: Tuple of legacy :class:`vietnam_provinces.legacy.Ward` objects
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


def _normalize_search_name(name: str) -> str:
    """Normalize Vietnamese name for fuzzy searching.

    :param name: The name to normalize
    :returns: Normalized name string
    """
    name = name.lower()
    # Remove common prefixes
    name = re.sub(r'^(xã|phường|thị trấn)\s+', '', name)
    # Remove diacritics
    name = unicodedata.normalize('NFD', name)
    name = ''.join(c for c in name if unicodedata.category(c) != 'Mn')
    name = name.replace('đ', 'd')
    return unicodedata.normalize('NFC', name)


def _calculate_match_score(
    query: str,
    normalized_query: str,
    old_ward: OldWardRef,
) -> int:
    """Calculate match score for sorting search results (lower score = better match).

    Priority:
    1. Exact match (case-sensitive, with diacritics)
    2. Exact match (case-insensitive, with diacritics)
    3. Exact match (normalized, no diacritics)
    4. Partial match scores based on position and length

    Within each priority level, prefer "Thị trấn" > "Phường" > "Xã"

    :param query: Original query string
    :param normalized_query: Normalized query (lowercase, no diacritics)
    :param old_ward: The old ward reference with name and division_type
    :returns: Match score (lower is better)
    """
    from vietnam_provinces.legacy import base as legacy

    candidate = old_ward.name
    normalized_candidate = _normalize_search_name(candidate)

    # Remove common prefixes from candidates for comparison
    candidate_clean = re.sub(r'^(xã|phường|thị trấn)\s+', '', candidate, flags=re.IGNORECASE)
    candidate_lower = candidate.lower()
    candidate_lower_clean = re.sub(r'^(xã|phường|thị trấn)\s+', '', candidate_lower)

    # Determine prefix bonus (thị trấn is preferred) using the stored division_type
    prefix_bonus = 0
    if old_ward.division_type == legacy.VietNamDivisionType.THI_TRAN:
        prefix_bonus = 0
    elif old_ward.division_type == legacy.VietNamDivisionType.PHUONG:
        prefix_bonus = 3
    elif old_ward.division_type == legacy.VietNamDivisionType.XA:
        prefix_bonus = 6

    # Check if query includes prefix - if so, match full name with prefix
    query_lower = query.lower()
    if query_lower.startswith('xã ') or query_lower.startswith('phường ') or query_lower.startswith('thị trấn '):
        # Query includes prefix, do full match including prefix
        if query == candidate:
            return 0
        if query_lower == candidate_lower:
            return 1
        # Continue to normalized match below
    else:
        # Query doesn't include prefix, match without prefix
        # Exact match with diacritics and case
        if query == candidate_clean:
            return 0 + prefix_bonus

        # Exact match with diacritics, case-insensitive
        if query.lower() == candidate_lower_clean:
            return 1 + prefix_bonus

    # Exact match normalized (no diacritics)
    normalized_candidate_clean = re.sub(r'^(xa|phuong|thi tran)\s+', '', normalized_candidate)
    if normalized_query == normalized_candidate_clean:
        return 2 + prefix_bonus

    # Partial match: earlier position is better
    pos = normalized_candidate.find(normalized_query)
    if pos == 0:
        # Match at start (after prefix removal)
        return 10 + prefix_bonus
    elif pos > 0:
        # Match in middle/end: score increases with position
        return 100 + pos + prefix_bonus

    # Should not reach here since we filter by containment before calling this
    return 1000
