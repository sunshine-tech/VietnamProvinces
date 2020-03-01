# Please be careful, this file takes a lot of time to load

from fast_enum import FastEnum

from ..base import Ward, VietNamDivisionType


class WardEnum(metaclass=FastEnum):
    DA_UY_NO_478 = Ward(name="Xã Uy Nỗ", code=478, division_type=VietNamDivisionType.XA,
                        codename="xa_uy_no", district_code=17)
