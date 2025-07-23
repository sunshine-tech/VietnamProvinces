from enum import Enum

from ..base import VietNamDivisionType, Ward


class WardEnum(Enum):
    """
    Ward Enum type, which is convenient for fast looking up Ward by its numeric code.
    """

    W_478 = Ward('Xã Uy Nỗ', 478, VietNamDivisionType.XA, 'xa_uy_no', 17)


class WardDEnum(Enum):
    """
    Ward Enum type, whose member name is more descriptive, with ward name, abbreviated province name.

    It helps developer have more idea what Ward he is selecting.
    """

    HN_UY_NO_78 = WardEnum.W_478
