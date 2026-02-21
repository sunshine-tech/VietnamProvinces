# Utilities for coverting new and old administrative divisions
"""
Bridge functions for converting between legacy (pre-2025) and new (post-2025) data.

This module provides helper functions for searching and converting between
old and new administrative divisions.
"""

from __future__ import annotations

import re
import unicodedata


def normalize_search_name(name: str) -> str:
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
