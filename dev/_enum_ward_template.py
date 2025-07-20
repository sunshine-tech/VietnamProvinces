from fast_enum import FastEnum

from ..base import VietNamDivisionType, Ward


class WardEnum(metaclass=FastEnum):
    """
    Ward Enum type, which is convenient for fast looking up Ward by its numeric code.
    """

    W_478 = Ward('Xã Uy Nỗ', 478, VietNamDivisionType.XA, 'xa_uy_no', 17)


class WardDEnum(metaclass=FastEnum):
    """
    Ward Enum type, whose member name is more descriptive, with ward name, abbreviated province name.

    It helps developer have more idea what Ward he is selecting.
    """

    DA_UY_NO = WardEnum.W_478
