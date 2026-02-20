"""Lookup mappings for pre-2025 administrative divisions."""

# Import dataclasses and division types from the local legacy package
from .base import (
    District,
    Province,
    VietNamDivisionType,
    Ward,
)

# Import enums from the local codes module
from .codes import (
    DistrictCode,
    ProvinceCode,
    WardCode,
)


PROVINCE_MAPPING: dict[int, Province] = {
    1: Province(
        'Thành phố Hà Nội',
        ProvinceCode.P_01,
        VietNamDivisionType.THANH_PHO_TRUNG_UONG,
        'thanh_pho_ha_noi',
        24,
    ),
}

DISTRICT_MAPPING: dict[int, District] = {
    1: District(
        'Quận Ba Đình',
        DistrictCode.D_001,
        VietNamDivisionType.QUAN,
        'quan_ba_dinh',
        ProvinceCode.P_01,
    ),
}

WARD_MAPPING: dict[int, Ward] = {
    1: Ward(
        'Phường Phúc Xá',
        WardCode.W_00001,
        VietNamDivisionType.PHUONG,
        'phuong_phuc_xa',
        DistrictCode.D_001,
    ),
}
