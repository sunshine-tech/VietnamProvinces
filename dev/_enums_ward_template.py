# Please be careful, this file takes a lot of time to load

from enum import Enum

from ..base import Ward, VietNamDivisionType


class WardEnum(Ward, Enum):
    UY_NO_DA = Ward("Xã Uy Nỗ", 478, VietNamDivisionType.XA, "xa_uy_no", 17)
