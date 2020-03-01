# Please be careful, this file takes a lot of time to load

from fast_enum import FastEnum

from ..base import Ward, VietNamDivisionType


class WardEnum(metaclass=FastEnum):
    '''
    Ward Enum type, which is convenient for fast looking up Ward by its numeric code.
    '''
    W_478 = Ward(name="Xã Uy Nỗ", code=478, division_type=VietNamDivisionType.XA,
                 codename="xa_uy_no", district_code=17)


class WardDEnum(metaclass=FastEnum):
    '''
    Ward Enum type, whose member name is more descriptive, with ward name, abbreviated province name.

    It helps developer have more idea what Ward he is selecting.
    '''
    DA_UY_NO_478 = WardEnum.W_478.value
