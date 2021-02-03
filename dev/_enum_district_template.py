from enum import Enum

from ..base import District, Province, VietNamDivisionType


class ProvinceEnum(Enum):
    '''
    Province Enum type, which is convenient for fast looking up Province by its numeric code.

    We cannot use tuple syntax here, because Enum cannot set member attributes from tuple syntax
    if one field is string.
    '''
    P_1 = Province(name='Thành phố Hà Nội', code=1,
                   division_type=VietNamDivisionType.THANH_PHO_TRUNG_UONG,
                   codename='thanh_pho_ha_noi', phone_code=24)


class ProvinceDEnum(Enum):
    '''
    Province Enum type, whose member name is more descriptive, with province name.

    It helps developer have more idea what Province he is selecting.
    '''
    HA_NOI = Province.P_1.value


class DistrictEnum(Enum):
    '''
    District Enum type, which is convenient for fast looking up District by its numeric code.
    '''
    D_656 = District(name="Huyện Lắk", code=656, division_type=VietNamDivisionType.HUYEN,
                     codename="huyen_lak", province_code=66)


class DistrictDEnum(Enum):
    '''
    District Enum type, whose member name is more descriptive, with district name.

    It helps developer have more idea what District he is selecting.
    '''
    LAK_DL = DistrictEnum.D_656
