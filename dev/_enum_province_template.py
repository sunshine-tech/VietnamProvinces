from enum import Enum

from ..base import Province, VietNamDivisionType


class ProvinceEnum(Enum):
    """
    Province Enum type, which is convenient for fast looking up Province by its numeric code.

    We cannot use tuple syntax here, because Enum cannot set member attributes from tuple syntax
    if one field is string.
    """

    P_1 = Province('Thành phố Hà Nội', 1, VietNamDivisionType.THANH_PHO_TRUNG_UONG, 'thanh_pho_ha_noi', 24)


class ProvinceDEnum(Enum):
    """
    Province Enum type, whose member name is more descriptive, with province name.

    It helps developer have more idea what Province he is selecting.
    """

    HA_NOI = Province.P_1.value
