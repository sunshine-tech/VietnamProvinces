from enum import IntEnum

from .compat import document_enum


@document_enum
class ProvinceCode(IntEnum):
    P_01 = 1
    """Hà Nội"""


@document_enum
class WardCode(IntEnum):
    W_00004 = 4
    """Phường"""
