from enum import Enum
from ..base import Province, VietNamDivisionType


class ProvinceEnum(Enum):
    """
    Province Enum type, which is convenient for fast looking up Province by its numeric code.

    We cannot use tuple syntax here, because Enum cannot set member attributes from tuple syntax
    if one field is string.
    """

    P_1 = Province('Thành phố Hà Nội', 1, VietNamDivisionType.TINH, 'ha_noi', 24)
    P_4 = Province('Cao Bằng', 4, VietNamDivisionType.TINH, 'cao_bang', 206)
    P_8 = Province('Tuyên Quang', 8, VietNamDivisionType.TINH, 'tuyen_quang', 207)
    P_11 = Province('Điện Biên', 11, VietNamDivisionType.TINH, 'dien_bien', 215)
    P_12 = Province('Lai Châu', 12, VietNamDivisionType.TINH, 'lai_chau', 213)
    P_14 = Province('Sơn La', 14, VietNamDivisionType.TINH, 'son_la', 212)
    P_15 = Province('Lào Cai', 15, VietNamDivisionType.TINH, 'lao_cai', 214)
    P_19 = Province('Thái Nguyên', 19, VietNamDivisionType.TINH, 'thai_nguyen', 208)
    P_20 = Province('Lạng Sơn', 20, VietNamDivisionType.TINH, 'lang_son', 205)
    P_22 = Province('Quảng Ninh', 22, VietNamDivisionType.TINH, 'quang_ninh', 203)
    P_24 = Province('Bắc Ninh', 24, VietNamDivisionType.TINH, 'bac_ninh', 222)
    P_25 = Province('Phú Thọ', 25, VietNamDivisionType.TINH, 'phu_tho', 210)
    P_31 = Province('Thành phố Hải Phòng', 31, VietNamDivisionType.TINH, 'hai_phong', 225)
    P_33 = Province('Hưng Yên', 33, VietNamDivisionType.TINH, 'hung_yen', 221)
    P_37 = Province('Ninh Bình', 37, VietNamDivisionType.TINH, 'ninh_binh', 229)
    P_38 = Province('Thanh Hóa', 38, VietNamDivisionType.TINH, 'thanh_hoa', 237)
    P_40 = Province('Nghệ An', 40, VietNamDivisionType.TINH, 'nghe_an', 238)
    P_42 = Province('Hà Tĩnh', 42, VietNamDivisionType.TINH, 'ha_tinh', 239)
    P_44 = Province('Quảng Trị', 44, VietNamDivisionType.TINH, 'quang_tri', 233)
    P_46 = Province('Thành phố Huế', 46, VietNamDivisionType.TINH, 'hue', 234)
    P_48 = Province('Thành phố Đà Nẵng', 48, VietNamDivisionType.TINH, 'da_nang', 236)
    P_51 = Province('Quảng Ngãi', 51, VietNamDivisionType.TINH, 'quang_ngai', 255)
    P_52 = Province('Gia Lai', 52, VietNamDivisionType.TINH, 'gia_lai', 269)
    P_56 = Province('Khánh Hòa', 56, VietNamDivisionType.TINH, 'khanh_hoa', 258)
    P_66 = Province('Đắk Lắk', 66, VietNamDivisionType.TINH, 'dak_lak', 262)
    P_68 = Province('Lâm Đồng', 68, VietNamDivisionType.TINH, 'lam_dong', 263)
    P_75 = Province('Đồng Nai', 75, VietNamDivisionType.TINH, 'dong_nai', 251)
    P_79 = Province('Thành phố Hồ Chí Minh', 79, VietNamDivisionType.TINH, 'ho_chi_minh', 28)
    P_80 = Province('Tây Ninh', 80, VietNamDivisionType.TINH, 'tay_ninh', 276)
    P_82 = Province('Đồng Tháp', 82, VietNamDivisionType.TINH, 'dong_thap', 277)
    P_86 = Province('Vĩnh Long', 86, VietNamDivisionType.TINH, 'vinh_long', 270)
    P_91 = Province('An Giang', 91, VietNamDivisionType.TINH, 'an_giang', 296)
    P_92 = Province('Thành phố Cần Thơ', 92, VietNamDivisionType.TINH, 'can_tho', 292)
    P_96 = Province('Cà Mau', 96, VietNamDivisionType.TINH, 'ca_mau', 290)


class ProvinceDEnum(Enum):
    """
    Province Enum type, whose member name is more descriptive, with province name.

    It helps developer have more idea what Province he is selecting.
    """

    HA_NOI = ProvinceEnum.P_1.value
    CAO_BANG = ProvinceEnum.P_4.value
    TUYEN_QUANG = ProvinceEnum.P_8.value
    DIEN_BIEN = ProvinceEnum.P_11.value
    LAI_CHAU = ProvinceEnum.P_12.value
    SON_LA = ProvinceEnum.P_14.value
    LAO_CAI = ProvinceEnum.P_15.value
    THAI_NGUYEN = ProvinceEnum.P_19.value
    LANG_SON = ProvinceEnum.P_20.value
    QUANG_NINH = ProvinceEnum.P_22.value
    BAC_NINH = ProvinceEnum.P_24.value
    PHU_THO = ProvinceEnum.P_25.value
    HAI_PHONG = ProvinceEnum.P_31.value
    HUNG_YEN = ProvinceEnum.P_33.value
    NINH_BINH = ProvinceEnum.P_37.value
    THANH_HOA = ProvinceEnum.P_38.value
    NGHE_AN = ProvinceEnum.P_40.value
    HA_TINH = ProvinceEnum.P_42.value
    QUANG_TRI = ProvinceEnum.P_44.value
    HUE = ProvinceEnum.P_46.value
    DA_NANG = ProvinceEnum.P_48.value
    QUANG_NGAI = ProvinceEnum.P_51.value
    GIA_LAI = ProvinceEnum.P_52.value
    KHANH_HOA = ProvinceEnum.P_56.value
    DAK_LAK = ProvinceEnum.P_66.value
    LAM_DONG = ProvinceEnum.P_68.value
    DONG_NAI = ProvinceEnum.P_75.value
    HO_CHI_MINH = ProvinceEnum.P_79.value
    TAY_NINH = ProvinceEnum.P_80.value
    DONG_THAP = ProvinceEnum.P_82.value
    VINH_LONG = ProvinceEnum.P_86.value
    AN_GIANG = ProvinceEnum.P_91.value
    CAN_THO = ProvinceEnum.P_92.value
    CA_MAU = ProvinceEnum.P_96.value
