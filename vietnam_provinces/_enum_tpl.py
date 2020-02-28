from enum import Enum

from . import Ward, District, Province, VietNamDivisionType


class WardEnum(Ward, Enum):
    pass


class DistrictEnum(District, Enum):
    pass


class ProvinceEnum(Province, Enum):
    HA_NOI = Province('Thành phố Hà Nội', 1, VietNamDivisionType.THANH_PHO_TRUNG_UONG, 'thanh_pho_ha_noi', 24)
