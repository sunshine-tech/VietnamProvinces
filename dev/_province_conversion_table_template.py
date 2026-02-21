"""
Province conversion table for 2025 administrative changes.

This module provides bidirectional lookup for converting between
old provinces (pre-2025) and new provinces (post-2025).

Auto-generated from ward conversion data.
"""

from typing import NamedTuple


class OldProvinceRef(NamedTuple):
    """Reference to an old province (pre-2025)."""

    code: int


class NewProvinceRef(NamedTuple):
    """Reference to a new province (post-2025)."""

    code: int


class OldToNewEntry(NamedTuple):
    """Mapping from old province to new province(s)."""

    old_province: OldProvinceRef
    new_provinces: tuple[NewProvinceRef, ...]


class NewToOldEntry(NamedTuple):
    """Mapping from new province to old province(s)."""

    new_province: NewProvinceRef
    old_provinces: tuple[OldProvinceRef, ...]


EFFECTIVE_DATE = '2025-07-01'

# Mapping from old province code to new province(s)
OLD_TO_NEW: dict[int, OldToNewEntry] = {}

# Mapping from new province code to old province(s)
NEW_TO_OLD: dict[int, NewToOldEntry] = {}


def find_new_provinces(old_province_code: int) -> OldToNewEntry | None:
    """Find new province(s) that an old province was merged into."""
    return OLD_TO_NEW.get(old_province_code)


def find_old_provinces(new_province_code: int) -> NewToOldEntry | None:
    """Find old province(s) that were merged to form a new province."""
    return NEW_TO_OLD.get(new_province_code)
