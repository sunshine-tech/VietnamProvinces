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

from .codes import ProvinceCode, WardCode


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
            entry = OLD_TO_NEW.get(code)
            return tuple(cls.from_code(WardCode(nw.code)) for nw in entry.new_wards) if entry else ()

        if not name:
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
            match_score = _calculate_match_score(name, old_name, query, normalized_old_name)

            for nw in entry.new_wards:
                if nw.code in seen_codes:
                    continue

                try:
                    ward = cls.from_code(WardCode(nw.code))
                    results.append((ward, old_name, match_score))
                    seen_codes.add(nw.code)
                except ValueError:
                    continue

        # Sort by match score (lower is better)
        results.sort(key=lambda x: x[2])
        return tuple(ward for ward, _, _ in results)


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


def _calculate_match_score(query: str, candidate: str, normalized_query: str, normalized_candidate: str) -> int:
    """Calculate match score for sorting search results (lower score = better match).

    Priority:
    1. Exact match (case-sensitive, with diacritics)
    2. Exact match (case-insensitive, with diacritics)
    3. Exact match (normalized, no diacritics)
    4. Partial match scores based on position and length

    Within each priority level, prefer "Thị trấn" > "Phường" > "Xã"

    :param query: Original query string
    :param candidate: Original candidate string
    :param normalized_query: Normalized query (lowercase, no diacritics)
    :param normalized_candidate: Normalized candidate (lowercase, no diacritics)
    :returns: Match score (lower is better)
    """
    from vietnam_provinces.legacy.base import VietNamDivisionType as LegacyDivisionType

    # Remove common prefixes from candidates for comparison
    candidate_clean = re.sub(r'^(xã|phường|thị trấn)\s+', '', candidate, flags=re.IGNORECASE)
    candidate_lower = candidate.lower()
    candidate_lower_clean = re.sub(r'^(xã|phường|thị trấn)\s+', '', candidate_lower)

    # Determine prefix bonus (thị trấn is preferred)
    prefix_bonus = 0
    if candidate.lower().startswith(f'{LegacyDivisionType.THI_TRAN} '):
        prefix_bonus = 0
    elif candidate.lower().startswith(f'{LegacyDivisionType.PHUONG} '):
        prefix_bonus = 0.3
    elif candidate.lower().startswith(f'{LegacyDivisionType.XA} '):
        prefix_bonus = 0.6

    # Check if query includes prefix - if so, match full name with prefix
    query_lower = query.lower()
    if (
        query_lower.startswith(f'{LegacyDivisionType.XA} ')
        or query_lower.startswith(f'{LegacyDivisionType.PHUONG} ')
        or query_lower.startswith(f'{LegacyDivisionType.THI_TRAN} ')
    ):
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
