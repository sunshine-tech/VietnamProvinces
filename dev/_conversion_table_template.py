"""
Ward conversion table for 2025 administrative changes.

This module provides bidirectional lookup for converting between
old wards (pre-2025) and new wards (post-2025).

Auto-generated from BangChuyendoiĐVHCmoi_cu_khong_merge.csv
"""

from typing import NamedTuple


class OldWardRef(NamedTuple):
    """Reference to an old ward (pre-2025)."""

    code: int
    district_code: int
    province_code: int
    is_partly_merged: bool


class NewWardRef(NamedTuple):
    """Reference to a new ward (post-2025)."""

    code: int
    province_code: int


class OldToNewEntry(NamedTuple):
    """Mapping from old ward to new ward(s)."""

    old_ward: OldWardRef
    new_wards: tuple[NewWardRef, ...]


class NewToOldEntry(NamedTuple):
    """Mapping from new ward to old ward(s)."""

    new_ward: NewWardRef
    old_wards: tuple[OldWardRef, ...]


# Metadata
EFFECTIVE_DATE = '2025-07-01'
SOURCE = 'BangChuyendoiĐVHCmoi_cu_khong_merge.csv'

# Old ward code -> New ward(s) mapping
OLD_TO_NEW: dict[int, OldToNewEntry] = {}

# New ward code -> Old ward(s) mapping
NEW_TO_OLD: dict[int, NewToOldEntry] = {}


def find_new_wards(old_ward_code: int) -> OldToNewEntry | None:
    """Find new ward(s) that an old ward was merged into."""
    return OLD_TO_NEW.get(old_ward_code)


def find_old_wards(new_ward_code: int) -> NewToOldEntry | None:
    """Find old ward(s) that were merged to form a new ward."""
    return NEW_TO_OLD.get(new_ward_code)


def is_partly_merged(old_ward_code: int) -> bool | None:
    """Check if an old ward was partly merged (split across multiple new wards)."""
    entry = OLD_TO_NEW.get(old_ward_code)
    if entry is None:
        return None
    return entry.old_ward.is_partly_merged
