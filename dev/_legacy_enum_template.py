"""Enum definitions for pre-2025 administrative divisions."""

from enum import IntEnum


# Note: This module only defines the enums.
# The Province, District, Ward dataclasses are defined in legacy/base.py


class ProvinceCode(IntEnum):
    """Enum for province codes (pre-2025)."""

    P_01 = 1
    """Thành phố Hà Nội"""


class DistrictCode(IntEnum):
    """Enum for district codes (pre-2025)."""

    D_001 = 1
    """Quận Ba Đình"""


class WardCode(IntEnum):
    """Enum for ward codes (pre-2025)."""

    W_00001 = 1
    """Phường Phúc Xá"""
