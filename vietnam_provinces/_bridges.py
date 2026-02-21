# Utilities for coverting new and old administrative divisions
"""
Bridge functions for converting between legacy (pre-2025) and new (post-2025) data.

This module provides helper functions for searching and converting between
old and new administrative divisions.
"""

from __future__ import annotations

import re
from logging import getLogger

from .base import Province, ProvinceCode, ProvinceWithLegacy, Ward, WardCode, WardWithLegacy
from .helpers import calculate_province_match_score, normalize_province_search_name, normalize_search_name


log = getLogger(__name__)


def calculate_match_score(
    query: str,
    normalized_query: str,
    old_ward_name: str,
    old_ward_division_type: object,
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
    :param old_ward_name: The name of the old ward
    :param old_ward_division_type: The division type enum of the old ward (e.g., VietNamDivisionType.THI_TRAN)
    :returns: Match score (lower is better)
    """
    from vietnam_provinces.legacy import base as legacy

    candidate = old_ward_name
    normalized_candidate = normalize_search_name(candidate)

    # Remove common prefixes from candidates for comparison
    candidate_clean = re.sub(r'^(xã|phường|thị trấn)\s+', '', candidate, flags=re.IGNORECASE)
    candidate_lower = candidate.lower()
    candidate_lower_clean = re.sub(r'^(xã|phường|thị trấn)\s+', '', candidate_lower)

    # Determine prefix bonus (thị trấn is preferred) using the division_type enum
    prefix_bonus = 0
    if old_ward_division_type == legacy.VietNamDivisionType.THI_TRAN:
        prefix_bonus = 0
    elif old_ward_division_type == legacy.VietNamDivisionType.PHUONG:
        prefix_bonus = 3
    elif old_ward_division_type == legacy.VietNamDivisionType.XA:
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


def search_provinces_from_legacy(
    name: str = '',
    code: int = 0,
) -> tuple[ProvinceWithLegacy, ...]:
    """Search current provinces from legacy province criteria."""
    from ._province_conversion_2025 import OLD_TO_NEW
    from .legacy import Province as LegacyProvince
    from .legacy.codes import ProvinceCode as LegacyProvinceCode

    if code > 0:
        if (entry := OLD_TO_NEW.get(code)) is None:
            log.debug('No conversion entry found for legacy province code %s', code)
            return ()
        return tuple(
            ProvinceWithLegacy(source_code=code, province=Province.from_code(ProvinceCode(np.code)))
            for np in entry.new_provinces
        )

    if not name:
        log.debug('Empty search query provided')
        return ()

    query = normalize_province_search_name(name)
    normalized_words = query.split()
    results: list[tuple[ProvinceWithLegacy, int]] = []
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
        name_words = set(normalized_old_name.split())
        if not all(word in name_words for word in normalized_words):
            log.debug(
                'Legacy province %r (normalized: %r) does not match query %r (normalized words: %r) - missing words',
                old_name,
                normalized_old_name,
                name,
                normalized_words,
            )
            continue
        log.debug(
            'Legacy province %r (normalized: %r) matches query %r (normalized words: %r) - all words found',
            old_name,
            normalized_old_name,
            name,
            normalized_words,
        )

        match_score = calculate_province_match_score(name, query, old_name, division_type)

        for np in entry.new_provinces:
            if np.code in seen_codes:
                continue

            try:
                province = Province.from_code(ProvinceCode(np.code))
                results.append((ProvinceWithLegacy(source_code=old_code, province=province), match_score))
                seen_codes.add(np.code)
            except ValueError:
                log.debug('New province code %s not found in lookup', np.code)
                continue

    results.sort(key=lambda x: x[1])
    return tuple(result for result, _ in results)


def search_wards_from_legacy(name: str = '', code: int = 0) -> tuple[WardWithLegacy, ...]:
    """Search current wards from legacy ward criteria."""
    from ._ward_conversion_2025 import OLD_TO_NEW
    from .legacy import Ward as LegacyWard
    from .legacy.codes import WardCode as LegacyWardCode

    if code > 0:
        if (entry := OLD_TO_NEW.get(code)) is None:
            log.debug('No conversion entry found for legacy ward code %s', code)
            return ()
        return tuple(WardWithLegacy(source_code=code, ward=Ward.from_code(WardCode(nw.code))) for nw in entry.new_wards)

    if not name:
        log.debug('Empty search query provided')
        return ()

    # Split input into words, normalize, and filter out division type prefixes
    # Only filter if they appear at the beginning (e.g., "Xã Tân Hòa" -> "Tân Hòa")
    division_types = {'tinh', 'thanh', 'pho', 'xa', 'phuong', 'thi', 'tran'}
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
    results: list[tuple[WardWithLegacy, int]] = []
    seen_codes: set[int] = set()

    for old_code, entry in OLD_TO_NEW.items():
        try:
            legacy_ward = LegacyWard.from_code(LegacyWardCode(old_code))
            old_name = legacy_ward.name
        except (ValueError, KeyError):
            log.debug('Legacy ward code %s not found in lookup', old_code)
            continue

        normalized_old_name = normalize_search_name(old_name)
        name_words = set(normalized_old_name.split())

        if not all(word in name_words for word in normalized_words):
            log.debug(
                'Legacy ward %r (normalized: %r) does not match query %r (normalized words: %r) - missing words',
                old_name,
                normalized_old_name,
                name,
                normalized_words,
            )
            continue
        log.debug(
            'Legacy ward %r (normalized: %r) matches query %r (normalized words: %r) - all words found',
            old_name,
            normalized_old_name,
            name,
            normalized_words,
        )

        match_score = calculate_match_score(name, query, old_name, legacy_ward.division_type)

        for nw in entry.new_wards:
            if nw.code in seen_codes:
                continue

            try:
                ward = Ward.from_code(WardCode(nw.code))
                results.append((WardWithLegacy(source_code=old_code, ward=ward), match_score))
                seen_codes.add(nw.code)
            except ValueError:
                log.debug('New ward code %s not found in lookup', nw.code)
                continue

    results.sort(key=lambda x: x[1])
    return tuple(result for result, _ in results)


def search_wards_from_legacy_district(name: str = '', code: int = 0) -> tuple[WardWithLegacy, ...]:
    """Search current wards from legacy district criteria."""
    from ._ward_conversion_2025 import OLD_TO_NEW
    from .legacy import base as legacy

    if code > 0:
        # Find all legacy wards in this district, then get their new wards
        district_code = code
    elif name:
        # Search for districts by name
        districts = legacy.District.search(name)
        if not districts:
            log.debug('No legacy district found matching name %r', name)
            return ()
        # Use the first matching district
        district_code = districts[0].code.value
    else:
        log.debug('Empty search query provided')
        return ()

    # Collect new ward codes from wards in this district, along with one legacy source code
    new_ward_to_old_code: dict[int, int] = {}

    for old_code, entry in OLD_TO_NEW.items():
        if entry.old_ward.district_code == district_code:
            for nw in entry.new_wards:
                if nw.code not in new_ward_to_old_code:
                    new_ward_to_old_code[nw.code] = old_code

    if not new_ward_to_old_code:
        log.debug('No new wards found for legacy district code %s', district_code)
        return ()

    # Convert to WardWithLegacy objects
    results: list[WardWithLegacy] = []
    for nw_code in sorted(new_ward_to_old_code):
        try:
            ward = Ward.from_code(WardCode(nw_code))
            results.append(WardWithLegacy(source_code=new_ward_to_old_code[nw_code], ward=ward))
        except ValueError:
            log.debug('New ward code %s not found in lookup', nw_code)
            continue

    return tuple(results)
