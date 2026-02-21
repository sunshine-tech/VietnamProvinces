# Helper utilities for the vietnam_provinces library.
"""
Helper functions for the vietnam_provinces library.

This module provides utility functions used across the library,
including text normalization for searching.
"""

from __future__ import annotations

import re
import unicodedata


def normalize_search_name(name: str) -> str:
    """Normalize Vietnamese name for fuzzy searching.

    This function normalizes Vietnamese text by:
    1. Converting to lowercase
    2. Removing common prefixes (xã, phường, thị trấn)
    3. Removing diacritics
    4. Replacing 'đ' with 'd'

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


def calculate_simple_match_score(query: str, normalized_query: str, candidate_name: str) -> int:
    """Calculate match score for sorting search results (lower score = better match).

    Priority:
    1. Exact match (case-sensitive, with diacritics)
    2. Exact match (case-insensitive, with diacritics)
    3. Exact match (normalized, no diacritics)
    4. Partial match scores based on position

    :param query: Original query string
    :param normalized_query: Normalized query (lowercase, no diacritics)
    :param candidate_name: The candidate name to match against
    :returns: Match score (lower is better)
    """
    normalized_candidate = normalize_search_name(candidate_name)

    # Remove common prefixes from candidates for comparison
    candidate_clean = re.sub(r'^(xã|phường|thị trấn)\s+', '', candidate_name, flags=re.IGNORECASE)
    candidate_lower = candidate_name.lower()
    candidate_lower_clean = re.sub(r'^(xã|phường|thị trấn)\s+', '', candidate_lower)

    # Check if query includes prefix - if so, match full name with prefix
    query_lower = query.lower()
    if query_lower.startswith('xã ') or query_lower.startswith('phường ') or query_lower.startswith('thị trấn '):
        # Query includes prefix, do full match including prefix
        if query == candidate_name:
            return 0
        if query_lower == candidate_lower:
            return 1
        # Continue to normalized match below
    else:
        # Query doesn't include prefix, match without prefix
        # Exact match with diacritics and case
        if query == candidate_clean:
            return 0

        # Exact match with diacritics, case-insensitive
        if query.lower() == candidate_lower_clean:
            return 1

    # Exact match normalized (no diacritics)
    normalized_candidate_clean = re.sub(r'^(xa|phuong|thi tran)\s+', '', normalized_candidate)
    if normalized_query == normalized_candidate_clean:
        return 2

    # Partial match: earlier position is better
    pos = normalized_candidate.find(normalized_query)
    if pos == 0:
        # Match at start (after prefix removal)
        return 10
    elif pos > 0:
        # Match in middle/end: score increases with position
        return 100 + pos

    # Should not reach here since we filter by containment before calling this
    return 1000


def normalize_province_search_name(name: str) -> str:
    """Normalize Vietnamese province name for fuzzy searching.

    This function normalizes Vietnamese province text by:
    1. Converting to lowercase
    2. Removing division type prefixes (tỉnh, thành phố)
    3. Removing diacritics
    4. Replacing 'đ' with 'd'

    :param name: The province name to normalize
    :returns: Normalized name string (without division type prefix)
    """
    name = name.lower()
    # Remove division type prefixes
    name = re.sub(r'^(tỉnh|thành phố)\s+', '', name)
    # Remove diacritics
    name = unicodedata.normalize('NFD', name)
    name = ''.join(c for c in name if unicodedata.category(c) != 'Mn')
    name = name.replace('đ', 'd')
    return unicodedata.normalize('NFC', name)


def calculate_province_match_score(query: str, normalized_query: str, candidate_name: str, division_type: str) -> int:
    """Calculate match score for province search results (lower score = better match).

    The division type prefix (tỉnh, thành phố) is ignored in name matching but
    used for priority scoring: thành phố > tỉnh.

    Priority:
    1. Exact match (case-sensitive, with diacritics, without prefix)
    2. Exact match (case-insensitive, with diacritics, without prefix)
    3. Exact match (normalized, no diacritics, without prefix)
    4. Partial match scores based on position

    Within each priority level, prefer "thành phố" > "tỉnh".

    :param query: Original query string
    :param normalized_query: Normalized query (lowercase, no diacritics, without prefix)
    :param candidate_name: The candidate province name to match against
    :param division_type: The division type ('thành phố trung ương' or 'tỉnh')
    :returns: Match score (lower is better)
    """
    normalized_candidate = normalize_province_search_name(candidate_name)

    # Remove division type prefixes from candidate for comparison
    candidate_clean = re.sub(r'^(tỉnh|thành phố)\s+', '', candidate_name, flags=re.IGNORECASE)
    candidate_lower = candidate_name.lower()
    candidate_lower_clean = re.sub(r'^(tỉnh|thành phố)\s+', '', candidate_lower)

    # Determine division type bonus (thành phố is preferred)
    # division_type values are: 'thành phố trung ương' or 'tỉnh'
    prefix_bonus = 0
    if 'thành phố' in division_type:
        prefix_bonus = 0
    elif 'tỉnh' in division_type:
        prefix_bonus = 3

    # Check if query includes prefix - if so, match full name with prefix
    query_lower = query.lower()
    if query_lower.startswith('tỉnh ') or query_lower.startswith('thành phố '):
        # Query includes prefix, do full match including prefix
        if query == candidate_name:
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
    normalized_candidate_clean = re.sub(r'^(tinh|thanh pho)\s+', '', normalized_candidate)
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
