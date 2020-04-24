from enum import Enum
from ..base import District, Province, VietNamDivisionType


class ProvinceEnum(Enum):
    """
    Province Enum type, which is convenient for fast looking up Province by its numeric code.
    """

    P_1 = Province(
        name="Thành phố Hà Nội",
        code=1,
        division_type=VietNamDivisionType.THANH_PHO_TRUNG_UONG,
        codename="thanh_pho_ha_noi",
        phone_code=24,
    )
    P_2 = Province(
        name="Tỉnh Hà Giang", code=2, division_type=VietNamDivisionType.TINH, codename="tinh_ha_giang", phone_code=219
    )
    P_4 = Province(
        name="Tỉnh Cao Bằng", code=4, division_type=VietNamDivisionType.TINH, codename="tinh_cao_bang", phone_code=206
    )
    P_6 = Province(
        name="Tỉnh Bắc Kạn", code=6, division_type=VietNamDivisionType.TINH, codename="tinh_bac_kan", phone_code=209
    )
    P_8 = Province(
        name="Tỉnh Tuyên Quang",
        code=8,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_tuyen_quang",
        phone_code=207,
    )
    P_10 = Province(
        name="Tỉnh Lào Cai", code=10, division_type=VietNamDivisionType.TINH, codename="tinh_lao_cai", phone_code=214
    )
    P_11 = Province(
        name="Tỉnh Điện Biên",
        code=11,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_dien_bien",
        phone_code=215,
    )
    P_12 = Province(
        name="Tỉnh Lai Châu", code=12, division_type=VietNamDivisionType.TINH, codename="tinh_lai_chau", phone_code=213
    )
    P_14 = Province(
        name="Tỉnh Sơn La", code=14, division_type=VietNamDivisionType.TINH, codename="tinh_son_la", phone_code=212
    )
    P_15 = Province(
        name="Tỉnh Yên Bái", code=15, division_type=VietNamDivisionType.TINH, codename="tinh_yen_bai", phone_code=216
    )
    P_17 = Province(
        name="Tỉnh Hoà Bình", code=17, division_type=VietNamDivisionType.TINH, codename="tinh_hoa_binh", phone_code=218
    )
    P_19 = Province(
        name="Tỉnh Thái Nguyên",
        code=19,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_thai_nguyen",
        phone_code=208,
    )
    P_20 = Province(
        name="Tỉnh Lạng Sơn", code=20, division_type=VietNamDivisionType.TINH, codename="tinh_lang_son", phone_code=205
    )
    P_22 = Province(
        name="Tỉnh Quảng Ninh",
        code=22,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_quang_ninh",
        phone_code=203,
    )
    P_24 = Province(
        name="Tỉnh Bắc Giang",
        code=24,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_bac_giang",
        phone_code=204,
    )
    P_25 = Province(
        name="Tỉnh Phú Thọ", code=25, division_type=VietNamDivisionType.TINH, codename="tinh_phu_tho", phone_code=210
    )
    P_26 = Province(
        name="Tỉnh Vĩnh Phúc",
        code=26,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_vinh_phuc",
        phone_code=211,
    )
    P_27 = Province(
        name="Tỉnh Bắc Ninh", code=27, division_type=VietNamDivisionType.TINH, codename="tinh_bac_ninh", phone_code=222
    )
    P_30 = Province(
        name="Tỉnh Hải Dương",
        code=30,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_hai_duong",
        phone_code=220,
    )
    P_31 = Province(
        name="Thành phố Hải Phòng",
        code=31,
        division_type=VietNamDivisionType.THANH_PHO_TRUNG_UONG,
        codename="thanh_pho_hai_phong",
        phone_code=225,
    )
    P_33 = Province(
        name="Tỉnh Hưng Yên", code=33, division_type=VietNamDivisionType.TINH, codename="tinh_hung_yen", phone_code=221
    )
    P_34 = Province(
        name="Tỉnh Thái Bình",
        code=34,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_thai_binh",
        phone_code=227,
    )
    P_35 = Province(
        name="Tỉnh Hà Nam", code=35, division_type=VietNamDivisionType.TINH, codename="tinh_ha_nam", phone_code=226
    )
    P_36 = Province(
        name="Tỉnh Nam Định", code=36, division_type=VietNamDivisionType.TINH, codename="tinh_nam_dinh", phone_code=228
    )
    P_37 = Province(
        name="Tỉnh Ninh Bình",
        code=37,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_ninh_binh",
        phone_code=229,
    )
    P_38 = Province(
        name="Tỉnh Thanh Hóa",
        code=38,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_thanh_hoa",
        phone_code=237,
    )
    P_40 = Province(
        name="Tỉnh Nghệ An", code=40, division_type=VietNamDivisionType.TINH, codename="tinh_nghe_an", phone_code=238
    )
    P_42 = Province(
        name="Tỉnh Hà Tĩnh", code=42, division_type=VietNamDivisionType.TINH, codename="tinh_ha_tinh", phone_code=239
    )
    P_44 = Province(
        name="Tỉnh Quảng Bình",
        code=44,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_quang_binh",
        phone_code=232,
    )
    P_45 = Province(
        name="Tỉnh Quảng Trị",
        code=45,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_quang_tri",
        phone_code=233,
    )
    P_46 = Province(
        name="Tỉnh Thừa Thiên Huế",
        code=46,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_thua_thien_hue",
        phone_code=234,
    )
    P_48 = Province(
        name="Thành phố Đà Nẵng",
        code=48,
        division_type=VietNamDivisionType.THANH_PHO_TRUNG_UONG,
        codename="thanh_pho_da_nang",
        phone_code=236,
    )
    P_49 = Province(
        name="Tỉnh Quảng Nam",
        code=49,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_quang_nam",
        phone_code=235,
    )
    P_51 = Province(
        name="Tỉnh Quảng Ngãi",
        code=51,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_quang_ngai",
        phone_code=255,
    )
    P_52 = Province(
        name="Tỉnh Bình Định",
        code=52,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_binh_dinh",
        phone_code=256,
    )
    P_54 = Province(
        name="Tỉnh Phú Yên", code=54, division_type=VietNamDivisionType.TINH, codename="tinh_phu_yen", phone_code=257
    )
    P_56 = Province(
        name="Tỉnh Khánh Hòa",
        code=56,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_khanh_hoa",
        phone_code=258,
    )
    P_58 = Province(
        name="Tỉnh Ninh Thuận",
        code=58,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_ninh_thuan",
        phone_code=259,
    )
    P_60 = Province(
        name="Tỉnh Bình Thuận",
        code=60,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_binh_thuan",
        phone_code=252,
    )
    P_62 = Province(
        name="Tỉnh Kon Tum", code=62, division_type=VietNamDivisionType.TINH, codename="tinh_kon_tum", phone_code=260
    )
    P_64 = Province(
        name="Tỉnh Gia Lai", code=64, division_type=VietNamDivisionType.TINH, codename="tinh_gia_lai", phone_code=269
    )
    P_66 = Province(
        name="Tỉnh Đắk Lắk", code=66, division_type=VietNamDivisionType.TINH, codename="tinh_dak_lak", phone_code=262
    )
    P_67 = Province(
        name="Tỉnh Đắk Nông", code=67, division_type=VietNamDivisionType.TINH, codename="tinh_dak_nong", phone_code=261
    )
    P_68 = Province(
        name="Tỉnh Lâm Đồng", code=68, division_type=VietNamDivisionType.TINH, codename="tinh_lam_dong", phone_code=263
    )
    P_70 = Province(
        name="Tỉnh Bình Phước",
        code=70,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_binh_phuoc",
        phone_code=271,
    )
    P_72 = Province(
        name="Tỉnh Tây Ninh", code=72, division_type=VietNamDivisionType.TINH, codename="tinh_tay_ninh", phone_code=276
    )
    P_74 = Province(
        name="Tỉnh Bình Dương",
        code=74,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_binh_duong",
        phone_code=274,
    )
    P_75 = Province(
        name="Tỉnh Đồng Nai", code=75, division_type=VietNamDivisionType.TINH, codename="tinh_dong_nai", phone_code=251
    )
    P_77 = Province(
        name="Tỉnh Bà Rịa - Vũng Tàu",
        code=77,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_ba_ria_vung_tau",
        phone_code=254,
    )
    P_79 = Province(
        name="Thành phố Hồ Chí Minh",
        code=79,
        division_type=VietNamDivisionType.THANH_PHO_TRUNG_UONG,
        codename="thanh_pho_ho_chi_minh",
        phone_code=28,
    )
    P_80 = Province(
        name="Tỉnh Long An", code=80, division_type=VietNamDivisionType.TINH, codename="tinh_long_an", phone_code=272
    )
    P_82 = Province(
        name="Tỉnh Tiền Giang",
        code=82,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_tien_giang",
        phone_code=273,
    )
    P_83 = Province(
        name="Tỉnh Bến Tre", code=83, division_type=VietNamDivisionType.TINH, codename="tinh_ben_tre", phone_code=275
    )
    P_84 = Province(
        name="Tỉnh Trà Vinh", code=84, division_type=VietNamDivisionType.TINH, codename="tinh_tra_vinh", phone_code=294
    )
    P_86 = Province(
        name="Tỉnh Vĩnh Long",
        code=86,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_vinh_long",
        phone_code=270,
    )
    P_87 = Province(
        name="Tỉnh Đồng Tháp",
        code=87,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_dong_thap",
        phone_code=277,
    )
    P_89 = Province(
        name="Tỉnh An Giang", code=89, division_type=VietNamDivisionType.TINH, codename="tinh_an_giang", phone_code=296
    )
    P_91 = Province(
        name="Tỉnh Kiên Giang",
        code=91,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_kien_giang",
        phone_code=297,
    )
    P_92 = Province(
        name="Thành phố Cần Thơ",
        code=92,
        division_type=VietNamDivisionType.THANH_PHO_TRUNG_UONG,
        codename="thanh_pho_can_tho",
        phone_code=292,
    )
    P_93 = Province(
        name="Tỉnh Hậu Giang",
        code=93,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_hau_giang",
        phone_code=293,
    )
    P_94 = Province(
        name="Tỉnh Sóc Trăng",
        code=94,
        division_type=VietNamDivisionType.TINH,
        codename="tinh_soc_trang",
        phone_code=299,
    )
    P_95 = Province(
        name="Tỉnh Bạc Liêu", code=95, division_type=VietNamDivisionType.TINH, codename="tinh_bac_lieu", phone_code=291
    )
    P_96 = Province(
        name="Tỉnh Cà Mau", code=96, division_type=VietNamDivisionType.TINH, codename="tinh_ca_mau", phone_code=290
    )


class ProvinceDEnum(Enum):
    """
    Province Enum type, whose member name is more descriptive, with province name.

    It helps developer have more idea what Province he is selecting.
    """

    HA_NOI = ProvinceEnum.P_1.value
    HA_GIANG = ProvinceEnum.P_2.value
    CAO_BANG = ProvinceEnum.P_4.value
    BAC_KAN = ProvinceEnum.P_6.value
    TUYEN_QUANG = ProvinceEnum.P_8.value
    LAO_CAI = ProvinceEnum.P_10.value
    DIEN_BIEN = ProvinceEnum.P_11.value
    LAI_CHAU = ProvinceEnum.P_12.value
    SON_LA = ProvinceEnum.P_14.value
    YEN_BAI = ProvinceEnum.P_15.value
    HOA_BINH = ProvinceEnum.P_17.value
    THAI_NGUYEN = ProvinceEnum.P_19.value
    LANG_SON = ProvinceEnum.P_20.value
    QUANG_NINH = ProvinceEnum.P_22.value
    BAC_GIANG = ProvinceEnum.P_24.value
    PHU_THO = ProvinceEnum.P_25.value
    VINH_PHUC = ProvinceEnum.P_26.value
    BAC_NINH = ProvinceEnum.P_27.value
    HAI_DUONG = ProvinceEnum.P_30.value
    HAI_PHONG = ProvinceEnum.P_31.value
    HUNG_YEN = ProvinceEnum.P_33.value
    THAI_BINH = ProvinceEnum.P_34.value
    HA_NAM = ProvinceEnum.P_35.value
    NAM_DINH = ProvinceEnum.P_36.value
    NINH_BINH = ProvinceEnum.P_37.value
    THANH_HOA = ProvinceEnum.P_38.value
    NGHE_AN = ProvinceEnum.P_40.value
    HA_TINH = ProvinceEnum.P_42.value
    QUANG_BINH = ProvinceEnum.P_44.value
    QUANG_TRI = ProvinceEnum.P_45.value
    THUA_THIEN_HUE = ProvinceEnum.P_46.value
    DA_NANG = ProvinceEnum.P_48.value
    QUANG_NAM = ProvinceEnum.P_49.value
    QUANG_NGAI = ProvinceEnum.P_51.value
    BINH_DINH = ProvinceEnum.P_52.value
    PHU_YEN = ProvinceEnum.P_54.value
    KHANH_HOA = ProvinceEnum.P_56.value
    NINH_THUAN = ProvinceEnum.P_58.value
    BINH_THUAN = ProvinceEnum.P_60.value
    KON_TUM = ProvinceEnum.P_62.value
    GIA_LAI = ProvinceEnum.P_64.value
    DAK_LAK = ProvinceEnum.P_66.value
    DAK_NONG = ProvinceEnum.P_67.value
    LAM_DONG = ProvinceEnum.P_68.value
    BINH_PHUOC = ProvinceEnum.P_70.value
    TAY_NINH = ProvinceEnum.P_72.value
    BINH_DUONG = ProvinceEnum.P_74.value
    DONG_NAI = ProvinceEnum.P_75.value
    BA_RIA_VUNG_TAU = ProvinceEnum.P_77.value
    HO_CHI_MINH = ProvinceEnum.P_79.value
    LONG_AN = ProvinceEnum.P_80.value
    TIEN_GIANG = ProvinceEnum.P_82.value
    BEN_TRE = ProvinceEnum.P_83.value
    TRA_VINH = ProvinceEnum.P_84.value
    VINH_LONG = ProvinceEnum.P_86.value
    DONG_THAP = ProvinceEnum.P_87.value
    AN_GIANG = ProvinceEnum.P_89.value
    KIEN_GIANG = ProvinceEnum.P_91.value
    CAN_THO = ProvinceEnum.P_92.value
    HAU_GIANG = ProvinceEnum.P_93.value
    SOC_TRANG = ProvinceEnum.P_94.value
    BAC_LIEU = ProvinceEnum.P_95.value
    CA_MAU = ProvinceEnum.P_96.value


class DistrictEnum(Enum):
    """
    District Enum type, which is convenient for fast looking up District by its numeric code.
    """

    D_1 = District(
        name="Quận Ba Đình", code=1, division_type=VietNamDivisionType.QUAN, codename="quan_ba_dinh", province_code=1
    )
    D_2 = District(
        name="Quận Hoàn Kiếm",
        code=2,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_hoan_kiem",
        province_code=1,
    )
    D_3 = District(
        name="Quận Tây Hồ", code=3, division_type=VietNamDivisionType.QUAN, codename="quan_tay_ho", province_code=1
    )
    D_4 = District(
        name="Quận Long Biên",
        code=4,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_long_bien",
        province_code=1,
    )
    D_5 = District(
        name="Quận Cầu Giấy", code=5, division_type=VietNamDivisionType.QUAN, codename="quan_cau_giay", province_code=1
    )
    D_6 = District(
        name="Quận Đống Đa", code=6, division_type=VietNamDivisionType.QUAN, codename="quan_dong_da", province_code=1
    )
    D_7 = District(
        name="Quận Hai Bà Trưng",
        code=7,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_hai_ba_trung",
        province_code=1,
    )
    D_8 = District(
        name="Quận Hoàng Mai",
        code=8,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_hoang_mai",
        province_code=1,
    )
    D_9 = District(
        name="Quận Thanh Xuân",
        code=9,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_thanh_xuan",
        province_code=1,
    )
    D_16 = District(
        name="Huyện Sóc Sơn",
        code=16,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_soc_son",
        province_code=1,
    )
    D_17 = District(
        name="Huyện Đông Anh",
        code=17,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dong_anh",
        province_code=1,
    )
    D_18 = District(
        name="Huyện Gia Lâm",
        code=18,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_gia_lam",
        province_code=1,
    )
    D_19 = District(
        name="Quận Nam Từ Liêm",
        code=19,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_nam_tu_liem",
        province_code=1,
    )
    D_20 = District(
        name="Huyện Thanh Trì",
        code=20,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thanh_tri",
        province_code=1,
    )
    D_21 = District(
        name="Quận Bắc Từ Liêm",
        code=21,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_bac_tu_liem",
        province_code=1,
    )
    D_250 = District(
        name="Huyện Mê Linh",
        code=250,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_me_linh",
        province_code=1,
    )
    D_268 = District(
        name="Quận Hà Đông", code=268, division_type=VietNamDivisionType.QUAN, codename="quan_ha_dong", province_code=1
    )
    D_269 = District(
        name="Thị xã Sơn Tây",
        code=269,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_son_tay",
        province_code=1,
    )
    D_271 = District(
        name="Huyện Ba Vì", code=271, division_type=VietNamDivisionType.HUYEN, codename="huyen_ba_vi", province_code=1
    )
    D_272 = District(
        name="Huyện Phúc Thọ",
        code=272,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phuc_tho",
        province_code=1,
    )
    D_273 = District(
        name="Huyện Đan Phượng",
        code=273,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dan_phuong",
        province_code=1,
    )
    D_274 = District(
        name="Huyện Hoài Đức",
        code=274,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hoai_duc",
        province_code=1,
    )
    D_275 = District(
        name="Huyện Quốc Oai",
        code=275,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quoc_oai",
        province_code=1,
    )
    D_276 = District(
        name="Huyện Thạch Thất",
        code=276,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thach_that",
        province_code=1,
    )
    D_277 = District(
        name="Huyện Chương Mỹ",
        code=277,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chuong_my",
        province_code=1,
    )
    D_278 = District(
        name="Huyện Thanh Oai",
        code=278,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thanh_oai",
        province_code=1,
    )
    D_279 = District(
        name="Huyện Thường Tín",
        code=279,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thuong_tin",
        province_code=1,
    )
    D_280 = District(
        name="Huyện Phú Xuyên",
        code=280,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_xuyen",
        province_code=1,
    )
    D_281 = District(
        name="Huyện Ứng Hòa",
        code=281,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ung_hoa",
        province_code=1,
    )
    D_282 = District(
        name="Huyện Mỹ Đức", code=282, division_type=VietNamDivisionType.HUYEN, codename="huyen_my_duc", province_code=1
    )
    D_24 = District(
        name="Thành phố Hà Giang",
        code=24,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_ha_giang",
        province_code=2,
    )
    D_26 = District(
        name="Huyện Đồng Văn",
        code=26,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dong_van",
        province_code=2,
    )
    D_27 = District(
        name="Huyện Mèo Vạc",
        code=27,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_meo_vac",
        province_code=2,
    )
    D_28 = District(
        name="Huyện Yên Minh",
        code=28,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_minh",
        province_code=2,
    )
    D_29 = District(
        name="Huyện Quản Bạ",
        code=29,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quan_ba",
        province_code=2,
    )
    D_30 = District(
        name="Huyện Vị Xuyên",
        code=30,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vi_xuyen",
        province_code=2,
    )
    D_31 = District(
        name="Huyện Bắc Mê", code=31, division_type=VietNamDivisionType.HUYEN, codename="huyen_bac_me", province_code=2
    )
    D_32 = District(
        name="Huyện Hoàng Su Phì",
        code=32,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hoang_su_phi",
        province_code=2,
    )
    D_33 = District(
        name="Huyện Xín Mần",
        code=33,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_xin_man",
        province_code=2,
    )
    D_34 = District(
        name="Huyện Bắc Quang",
        code=34,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bac_quang",
        province_code=2,
    )
    D_35 = District(
        name="Huyện Quang Bình",
        code=35,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quang_binh",
        province_code=2,
    )
    D_40 = District(
        name="Thành phố Cao Bằng",
        code=40,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_cao_bang",
        province_code=4,
    )
    D_42 = District(
        name="Huyện Bảo Lâm",
        code=42,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bao_lam",
        province_code=4,
    )
    D_43 = District(
        name="Huyện Bảo Lạc",
        code=43,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bao_lac",
        province_code=4,
    )
    D_44 = District(
        name="Huyện Thông Nông",
        code=44,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thong_nong",
        province_code=4,
    )
    D_45 = District(
        name="Huyện Hà Quảng",
        code=45,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ha_quang",
        province_code=4,
    )
    D_46 = District(
        name="Huyện Trà Lĩnh",
        code=46,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tra_linh",
        province_code=4,
    )
    D_47 = District(
        name="Huyện Trùng Khánh",
        code=47,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_trung_khanh",
        province_code=4,
    )
    D_48 = District(
        name="Huyện Hạ Lang",
        code=48,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ha_lang",
        province_code=4,
    )
    D_49 = District(
        name="Huyện Quảng Uyên",
        code=49,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quang_uyen",
        province_code=4,
    )
    D_50 = District(
        name="Huyện Phục Hoà",
        code=50,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phuc_hoa",
        province_code=4,
    )
    D_51 = District(
        name="Huyện Hoà An", code=51, division_type=VietNamDivisionType.HUYEN, codename="huyen_hoa_an", province_code=4
    )
    D_52 = District(
        name="Huyện Nguyên Bình",
        code=52,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nguyen_binh",
        province_code=4,
    )
    D_53 = District(
        name="Huyện Thạch An",
        code=53,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thach_an",
        province_code=4,
    )
    D_58 = District(
        name="Thành Phố Bắc Kạn",
        code=58,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_bac_kan",
        province_code=6,
    )
    D_60 = District(
        name="Huyện Pác Nặm",
        code=60,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_pac_nam",
        province_code=6,
    )
    D_61 = District(
        name="Huyện Ba Bể", code=61, division_type=VietNamDivisionType.HUYEN, codename="huyen_ba_be", province_code=6
    )
    D_62 = District(
        name="Huyện Ngân Sơn",
        code=62,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ngan_son",
        province_code=6,
    )
    D_63 = District(
        name="Huyện Bạch Thông",
        code=63,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bach_thong",
        province_code=6,
    )
    D_64 = District(
        name="Huyện Chợ Đồn",
        code=64,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cho_don",
        province_code=6,
    )
    D_65 = District(
        name="Huyện Chợ Mới",
        code=65,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cho_moi",
        province_code=6,
    )
    D_66 = District(
        name="Huyện Na Rì", code=66, division_type=VietNamDivisionType.HUYEN, codename="huyen_na_ri", province_code=6
    )
    D_70 = District(
        name="Thành phố Tuyên Quang",
        code=70,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_tuyen_quang",
        province_code=8,
    )
    D_71 = District(
        name="Huyện Lâm Bình",
        code=71,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_lam_binh",
        province_code=8,
    )
    D_72 = District(
        name="Huyện Na Hang",
        code=72,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_na_hang",
        province_code=8,
    )
    D_73 = District(
        name="Huyện Chiêm Hóa",
        code=73,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chiem_hoa",
        province_code=8,
    )
    D_74 = District(
        name="Huyện Hàm Yên",
        code=74,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ham_yen",
        province_code=8,
    )
    D_75 = District(
        name="Huyện Yên Sơn",
        code=75,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_son",
        province_code=8,
    )
    D_76 = District(
        name="Huyện Sơn Dương",
        code=76,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_son_duong",
        province_code=8,
    )
    D_80 = District(
        name="Thành phố Lào Cai",
        code=80,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_lao_cai",
        province_code=10,
    )
    D_82 = District(
        name="Huyện Bát Xát",
        code=82,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bat_xat",
        province_code=10,
    )
    D_83 = District(
        name="Huyện Mường Khương",
        code=83,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_muong_khuong",
        province_code=10,
    )
    D_84 = District(
        name="Huyện Si Ma Cai",
        code=84,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_si_ma_cai",
        province_code=10,
    )
    D_85 = District(
        name="Huyện Bắc Hà", code=85, division_type=VietNamDivisionType.HUYEN, codename="huyen_bac_ha", province_code=10
    )
    D_86 = District(
        name="Huyện Bảo Thắng",
        code=86,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bao_thang",
        province_code=10,
    )
    D_87 = District(
        name="Huyện Bảo Yên",
        code=87,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bao_yen",
        province_code=10,
    )
    D_88 = District(
        name="Thị xã Sa Pa",
        code=88,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_sa_pa",
        province_code=10,
    )
    D_89 = District(
        name="Huyện Văn Bàn",
        code=89,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_van_ban",
        province_code=10,
    )
    D_94 = District(
        name="Thành phố Điện Biên Phủ",
        code=94,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_dien_bien_phu",
        province_code=11,
    )
    D_95 = District(
        name="Thị Xã Mường Lay",
        code=95,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_muong_lay",
        province_code=11,
    )
    D_96 = District(
        name="Huyện Mường Nhé",
        code=96,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_muong_nhe",
        province_code=11,
    )
    D_97 = District(
        name="Huyện Mường Chà",
        code=97,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_muong_cha",
        province_code=11,
    )
    D_98 = District(
        name="Huyện Tủa Chùa",
        code=98,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tua_chua",
        province_code=11,
    )
    D_99 = District(
        name="Huyện Tuần Giáo",
        code=99,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tuan_giao",
        province_code=11,
    )
    D_100 = District(
        name="Huyện Điện Biên",
        code=100,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dien_bien",
        province_code=11,
    )
    D_101 = District(
        name="Huyện Điện Biên Đông",
        code=101,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dien_bien_dong",
        province_code=11,
    )
    D_102 = District(
        name="Huyện Mường Ảng",
        code=102,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_muong_ang",
        province_code=11,
    )
    D_103 = District(
        name="Huyện Nậm Pồ",
        code=103,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nam_po",
        province_code=11,
    )
    D_105 = District(
        name="Thành phố Lai Châu",
        code=105,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_lai_chau",
        province_code=12,
    )
    D_106 = District(
        name="Huyện Tam Đường",
        code=106,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tam_duong",
        province_code=12,
    )
    D_107 = District(
        name="Huyện Mường Tè",
        code=107,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_muong_te",
        province_code=12,
    )
    D_108 = District(
        name="Huyện Sìn Hồ",
        code=108,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_sin_ho",
        province_code=12,
    )
    D_109 = District(
        name="Huyện Phong Thổ",
        code=109,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phong_tho",
        province_code=12,
    )
    D_110 = District(
        name="Huyện Than Uyên",
        code=110,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_than_uyen",
        province_code=12,
    )
    D_111 = District(
        name="Huyện Tân Uyên",
        code=111,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_uyen",
        province_code=12,
    )
    D_112 = District(
        name="Huyện Nậm Nhùn",
        code=112,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nam_nhun",
        province_code=12,
    )
    D_116 = District(
        name="Thành phố Sơn La",
        code=116,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_son_la",
        province_code=14,
    )
    D_118 = District(
        name="Huyện Quỳnh Nhai",
        code=118,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quynh_nhai",
        province_code=14,
    )
    D_119 = District(
        name="Huyện Thuận Châu",
        code=119,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thuan_chau",
        province_code=14,
    )
    D_120 = District(
        name="Huyện Mường La",
        code=120,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_muong_la",
        province_code=14,
    )
    D_121 = District(
        name="Huyện Bắc Yên",
        code=121,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bac_yen",
        province_code=14,
    )
    D_122 = District(
        name="Huyện Phù Yên",
        code=122,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_yen",
        province_code=14,
    )
    D_123 = District(
        name="Huyện Mộc Châu",
        code=123,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_moc_chau",
        province_code=14,
    )
    D_124 = District(
        name="Huyện Yên Châu",
        code=124,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_chau",
        province_code=14,
    )
    D_125 = District(
        name="Huyện Mai Sơn",
        code=125,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_mai_son",
        province_code=14,
    )
    D_126 = District(
        name="Huyện Sông Mã",
        code=126,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_song_ma",
        province_code=14,
    )
    D_127 = District(
        name="Huyện Sốp Cộp",
        code=127,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_sop_cop",
        province_code=14,
    )
    D_128 = District(
        name="Huyện Vân Hồ",
        code=128,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_van_ho",
        province_code=14,
    )
    D_132 = District(
        name="Thành phố Yên Bái",
        code=132,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_yen_bai",
        province_code=15,
    )
    D_133 = District(
        name="Thị xã Nghĩa Lộ",
        code=133,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_nghia_lo",
        province_code=15,
    )
    D_135 = District(
        name="Huyện Lục Yên",
        code=135,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_luc_yen",
        province_code=15,
    )
    D_136 = District(
        name="Huyện Văn Yên",
        code=136,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_van_yen",
        province_code=15,
    )
    D_137 = District(
        name="Huyện Mù Căng Chải",
        code=137,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_mu_cang_chai",
        province_code=15,
    )
    D_138 = District(
        name="Huyện Trấn Yên",
        code=138,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tran_yen",
        province_code=15,
    )
    D_139 = District(
        name="Huyện Trạm Tấu",
        code=139,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tram_tau",
        province_code=15,
    )
    D_140 = District(
        name="Huyện Văn Chấn",
        code=140,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_van_chan",
        province_code=15,
    )
    D_141 = District(
        name="Huyện Yên Bình",
        code=141,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_binh",
        province_code=15,
    )
    D_148 = District(
        name="Thành phố Hòa Bình",
        code=148,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_hoa_binh",
        province_code=17,
    )
    D_150 = District(
        name="Huyện Đà Bắc",
        code=150,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_da_bac",
        province_code=17,
    )
    D_152 = District(
        name="Huyện Lương Sơn",
        code=152,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_luong_son",
        province_code=17,
    )
    D_153 = District(
        name="Huyện Kim Bôi",
        code=153,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_kim_boi",
        province_code=17,
    )
    D_154 = District(
        name="Huyện Cao Phong",
        code=154,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cao_phong",
        province_code=17,
    )
    D_155 = District(
        name="Huyện Tân Lạc",
        code=155,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_lac",
        province_code=17,
    )
    D_156 = District(
        name="Huyện Mai Châu",
        code=156,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_mai_chau",
        province_code=17,
    )
    D_157 = District(
        name="Huyện Lạc Sơn",
        code=157,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_lac_son",
        province_code=17,
    )
    D_158 = District(
        name="Huyện Yên Thủy",
        code=158,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_thuy",
        province_code=17,
    )
    D_159 = District(
        name="Huyện Lạc Thủy",
        code=159,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_lac_thuy",
        province_code=17,
    )
    D_164 = District(
        name="Thành phố Thái Nguyên",
        code=164,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_thai_nguyen",
        province_code=19,
    )
    D_165 = District(
        name="Thành phố Sông Công",
        code=165,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_song_cong",
        province_code=19,
    )
    D_167 = District(
        name="Huyện Định Hóa",
        code=167,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dinh_hoa",
        province_code=19,
    )
    D_168 = District(
        name="Huyện Phú Lương",
        code=168,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_luong",
        province_code=19,
    )
    D_169 = District(
        name="Huyện Đồng Hỷ",
        code=169,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dong_hy",
        province_code=19,
    )
    D_170 = District(
        name="Huyện Võ Nhai",
        code=170,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vo_nhai",
        province_code=19,
    )
    D_171 = District(
        name="Huyện Đại Từ",
        code=171,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dai_tu",
        province_code=19,
    )
    D_172 = District(
        name="Thị xã Phổ Yên",
        code=172,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_pho_yen",
        province_code=19,
    )
    D_173 = District(
        name="Huyện Phú Bình",
        code=173,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_binh",
        province_code=19,
    )
    D_178 = District(
        name="Thành phố Lạng Sơn",
        code=178,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_lang_son",
        province_code=20,
    )
    D_180 = District(
        name="Huyện Tràng Định",
        code=180,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_trang_dinh",
        province_code=20,
    )
    D_181 = District(
        name="Huyện Bình Gia",
        code=181,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_binh_gia",
        province_code=20,
    )
    D_182 = District(
        name="Huyện Văn Lãng",
        code=182,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_van_lang",
        province_code=20,
    )
    D_183 = District(
        name="Huyện Cao Lộc",
        code=183,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cao_loc",
        province_code=20,
    )
    D_184 = District(
        name="Huyện Văn Quan",
        code=184,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_van_quan",
        province_code=20,
    )
    D_185 = District(
        name="Huyện Bắc Sơn",
        code=185,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bac_son",
        province_code=20,
    )
    D_186 = District(
        name="Huyện Hữu Lũng",
        code=186,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_huu_lung",
        province_code=20,
    )
    D_187 = District(
        name="Huyện Chi Lăng",
        code=187,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chi_lang",
        province_code=20,
    )
    D_188 = District(
        name="Huyện Lộc Bình",
        code=188,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_loc_binh",
        province_code=20,
    )
    D_189 = District(
        name="Huyện Đình Lập",
        code=189,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dinh_lap",
        province_code=20,
    )
    D_193 = District(
        name="Thành phố Hạ Long",
        code=193,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_ha_long",
        province_code=22,
    )
    D_194 = District(
        name="Thành phố Móng Cái",
        code=194,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_mong_cai",
        province_code=22,
    )
    D_195 = District(
        name="Thành phố Cẩm Phả",
        code=195,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_cam_pha",
        province_code=22,
    )
    D_196 = District(
        name="Thành phố Uông Bí",
        code=196,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_uong_bi",
        province_code=22,
    )
    D_198 = District(
        name="Huyện Bình Liêu",
        code=198,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_binh_lieu",
        province_code=22,
    )
    D_199 = District(
        name="Huyện Tiên Yên",
        code=199,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tien_yen",
        province_code=22,
    )
    D_200 = District(
        name="Huyện Đầm Hà",
        code=200,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dam_ha",
        province_code=22,
    )
    D_201 = District(
        name="Huyện Hải Hà",
        code=201,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hai_ha",
        province_code=22,
    )
    D_202 = District(
        name="Huyện Ba Chẽ",
        code=202,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ba_che",
        province_code=22,
    )
    D_203 = District(
        name="Huyện Vân Đồn",
        code=203,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_van_don",
        province_code=22,
    )
    D_205 = District(
        name="Thị xã Đông Triều",
        code=205,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_dong_trieu",
        province_code=22,
    )
    D_206 = District(
        name="Thị xã Quảng Yên",
        code=206,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_quang_yen",
        province_code=22,
    )
    D_207 = District(
        name="Huyện Cô Tô", code=207, division_type=VietNamDivisionType.HUYEN, codename="huyen_co_to", province_code=22
    )
    D_213 = District(
        name="Thành phố Bắc Giang",
        code=213,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_bac_giang",
        province_code=24,
    )
    D_215 = District(
        name="Huyện Yên Thế",
        code=215,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_the",
        province_code=24,
    )
    D_216 = District(
        name="Huyện Tân Yên",
        code=216,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_yen",
        province_code=24,
    )
    D_217 = District(
        name="Huyện Lạng Giang",
        code=217,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_lang_giang",
        province_code=24,
    )
    D_218 = District(
        name="Huyện Lục Nam",
        code=218,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_luc_nam",
        province_code=24,
    )
    D_219 = District(
        name="Huyện Lục Ngạn",
        code=219,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_luc_ngan",
        province_code=24,
    )
    D_220 = District(
        name="Huyện Sơn Động",
        code=220,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_son_dong",
        province_code=24,
    )
    D_221 = District(
        name="Huyện Yên Dũng",
        code=221,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_dung",
        province_code=24,
    )
    D_222 = District(
        name="Huyện Việt Yên",
        code=222,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_viet_yen",
        province_code=24,
    )
    D_223 = District(
        name="Huyện Hiệp Hòa",
        code=223,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hiep_hoa",
        province_code=24,
    )
    D_227 = District(
        name="Thành phố Việt Trì",
        code=227,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_viet_tri",
        province_code=25,
    )
    D_228 = District(
        name="Thị xã Phú Thọ",
        code=228,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_phu_tho",
        province_code=25,
    )
    D_230 = District(
        name="Huyện Đoan Hùng",
        code=230,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_doan_hung",
        province_code=25,
    )
    D_231 = District(
        name="Huyện Hạ Hoà",
        code=231,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ha_hoa",
        province_code=25,
    )
    D_232 = District(
        name="Huyện Thanh Ba",
        code=232,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thanh_ba",
        province_code=25,
    )
    D_233 = District(
        name="Huyện Phù Ninh",
        code=233,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_ninh",
        province_code=25,
    )
    D_234 = District(
        name="Huyện Yên Lập",
        code=234,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_lap",
        province_code=25,
    )
    D_235 = District(
        name="Huyện Cẩm Khê",
        code=235,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cam_khe",
        province_code=25,
    )
    D_236 = District(
        name="Huyện Tam Nông",
        code=236,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tam_nong",
        province_code=25,
    )
    D_237 = District(
        name="Huyện Lâm Thao",
        code=237,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_lam_thao",
        province_code=25,
    )
    D_238 = District(
        name="Huyện Thanh Sơn",
        code=238,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thanh_son",
        province_code=25,
    )
    D_239 = District(
        name="Huyện Thanh Thuỷ",
        code=239,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thanh_thuy",
        province_code=25,
    )
    D_240 = District(
        name="Huyện Tân Sơn",
        code=240,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_son",
        province_code=25,
    )
    D_243 = District(
        name="Thành phố Vĩnh Yên",
        code=243,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_vinh_yen",
        province_code=26,
    )
    D_244 = District(
        name="Thành phố Phúc Yên",
        code=244,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_phuc_yen",
        province_code=26,
    )
    D_246 = District(
        name="Huyện Lập Thạch",
        code=246,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_lap_thach",
        province_code=26,
    )
    D_247 = District(
        name="Huyện Tam Dương",
        code=247,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tam_duong",
        province_code=26,
    )
    D_248 = District(
        name="Huyện Tam Đảo",
        code=248,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tam_dao",
        province_code=26,
    )
    D_249 = District(
        name="Huyện Bình Xuyên",
        code=249,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_binh_xuyen",
        province_code=26,
    )
    D_251 = District(
        name="Huyện Yên Lạc",
        code=251,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_lac",
        province_code=26,
    )
    D_252 = District(
        name="Huyện Vĩnh Tường",
        code=252,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vinh_tuong",
        province_code=26,
    )
    D_253 = District(
        name="Huyện Sông Lô",
        code=253,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_song_lo",
        province_code=26,
    )
    D_256 = District(
        name="Thành phố Bắc Ninh",
        code=256,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_bac_ninh",
        province_code=27,
    )
    D_258 = District(
        name="Huyện Yên Phong",
        code=258,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_phong",
        province_code=27,
    )
    D_259 = District(
        name="Huyện Quế Võ",
        code=259,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_que_vo",
        province_code=27,
    )
    D_260 = District(
        name="Huyện Tiên Du",
        code=260,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tien_du",
        province_code=27,
    )
    D_261 = District(
        name="Thị xã Từ Sơn",
        code=261,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_tu_son",
        province_code=27,
    )
    D_262 = District(
        name="Huyện Thuận Thành",
        code=262,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thuan_thanh",
        province_code=27,
    )
    D_263 = District(
        name="Huyện Gia Bình",
        code=263,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_gia_binh",
        province_code=27,
    )
    D_264 = District(
        name="Huyện Lương Tài",
        code=264,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_luong_tai",
        province_code=27,
    )
    D_288 = District(
        name="Thành phố Hải Dương",
        code=288,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_hai_duong",
        province_code=30,
    )
    D_290 = District(
        name="Thành phố Chí Linh",
        code=290,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_chi_linh",
        province_code=30,
    )
    D_291 = District(
        name="Huyện Nam Sách",
        code=291,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nam_sach",
        province_code=30,
    )
    D_292 = District(
        name="Thị xã Kinh Môn",
        code=292,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_kinh_mon",
        province_code=30,
    )
    D_293 = District(
        name="Huyện Kim Thành",
        code=293,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_kim_thanh",
        province_code=30,
    )
    D_294 = District(
        name="Huyện Thanh Hà",
        code=294,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thanh_ha",
        province_code=30,
    )
    D_295 = District(
        name="Huyện Cẩm Giàng",
        code=295,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cam_giang",
        province_code=30,
    )
    D_296 = District(
        name="Huyện Bình Giang",
        code=296,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_binh_giang",
        province_code=30,
    )
    D_297 = District(
        name="Huyện Gia Lộc",
        code=297,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_gia_loc",
        province_code=30,
    )
    D_298 = District(
        name="Huyện Tứ Kỳ", code=298, division_type=VietNamDivisionType.HUYEN, codename="huyen_tu_ky", province_code=30
    )
    D_299 = District(
        name="Huyện Ninh Giang",
        code=299,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ninh_giang",
        province_code=30,
    )
    D_300 = District(
        name="Huyện Thanh Miện",
        code=300,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thanh_mien",
        province_code=30,
    )
    D_303 = District(
        name="Quận Hồng Bàng",
        code=303,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_hong_bang",
        province_code=31,
    )
    D_304 = District(
        name="Quận Ngô Quyền",
        code=304,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_ngo_quyen",
        province_code=31,
    )
    D_305 = District(
        name="Quận Lê Chân", code=305, division_type=VietNamDivisionType.QUAN, codename="quan_le_chan", province_code=31
    )
    D_306 = District(
        name="Quận Hải An", code=306, division_type=VietNamDivisionType.QUAN, codename="quan_hai_an", province_code=31
    )
    D_307 = District(
        name="Quận Kiến An", code=307, division_type=VietNamDivisionType.QUAN, codename="quan_kien_an", province_code=31
    )
    D_308 = District(
        name="Quận Đồ Sơn", code=308, division_type=VietNamDivisionType.QUAN, codename="quan_do_son", province_code=31
    )
    D_309 = District(
        name="Quận Dương Kinh",
        code=309,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_duong_kinh",
        province_code=31,
    )
    D_311 = District(
        name="Huyện Thuỷ Nguyên",
        code=311,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thuy_nguyen",
        province_code=31,
    )
    D_312 = District(
        name="Huyện An Dương",
        code=312,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_an_duong",
        province_code=31,
    )
    D_313 = District(
        name="Huyện An Lão",
        code=313,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_an_lao",
        province_code=31,
    )
    D_314 = District(
        name="Huyện Kiến Thuỵ",
        code=314,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_kien_thuy",
        province_code=31,
    )
    D_315 = District(
        name="Huyện Tiên Lãng",
        code=315,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tien_lang",
        province_code=31,
    )
    D_316 = District(
        name="Huyện Vĩnh Bảo",
        code=316,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vinh_bao",
        province_code=31,
    )
    D_317 = District(
        name="Huyện Cát Hải",
        code=317,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cat_hai",
        province_code=31,
    )
    D_323 = District(
        name="Thành phố Hưng Yên",
        code=323,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_hung_yen",
        province_code=33,
    )
    D_325 = District(
        name="Huyện Văn Lâm",
        code=325,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_van_lam",
        province_code=33,
    )
    D_326 = District(
        name="Huyện Văn Giang",
        code=326,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_van_giang",
        province_code=33,
    )
    D_327 = District(
        name="Huyện Yên Mỹ",
        code=327,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_my",
        province_code=33,
    )
    D_328 = District(
        name="Thị xã Mỹ Hào",
        code=328,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_my_hao",
        province_code=33,
    )
    D_329 = District(
        name="Huyện Ân Thi",
        code=329,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_an_thi",
        province_code=33,
    )
    D_330 = District(
        name="Huyện Khoái Châu",
        code=330,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_khoai_chau",
        province_code=33,
    )
    D_331 = District(
        name="Huyện Kim Động",
        code=331,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_kim_dong",
        province_code=33,
    )
    D_332 = District(
        name="Huyện Tiên Lữ",
        code=332,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tien_lu",
        province_code=33,
    )
    D_333 = District(
        name="Huyện Phù Cừ",
        code=333,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_cu",
        province_code=33,
    )
    D_336 = District(
        name="Thành phố Thái Bình",
        code=336,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_thai_binh",
        province_code=34,
    )
    D_338 = District(
        name="Huyện Quỳnh Phụ",
        code=338,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quynh_phu",
        province_code=34,
    )
    D_339 = District(
        name="Huyện Hưng Hà",
        code=339,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hung_ha",
        province_code=34,
    )
    D_340 = District(
        name="Huyện Đông Hưng",
        code=340,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dong_hung",
        province_code=34,
    )
    D_341 = District(
        name="Huyện Thái Thụy",
        code=341,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thai_thuy",
        province_code=34,
    )
    D_342 = District(
        name="Huyện Tiền Hải",
        code=342,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tien_hai",
        province_code=34,
    )
    D_343 = District(
        name="Huyện Kiến Xương",
        code=343,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_kien_xuong",
        province_code=34,
    )
    D_344 = District(
        name="Huyện Vũ Thư",
        code=344,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vu_thu",
        province_code=34,
    )
    D_347 = District(
        name="Thành phố Phủ Lý",
        code=347,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_phu_ly",
        province_code=35,
    )
    D_349 = District(
        name="Thị xã Duy Tiên",
        code=349,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_duy_tien",
        province_code=35,
    )
    D_350 = District(
        name="Huyện Kim Bảng",
        code=350,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_kim_bang",
        province_code=35,
    )
    D_351 = District(
        name="Huyện Thanh Liêm",
        code=351,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thanh_liem",
        province_code=35,
    )
    D_352 = District(
        name="Huyện Bình Lục",
        code=352,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_binh_luc",
        province_code=35,
    )
    D_353 = District(
        name="Huyện Lý Nhân",
        code=353,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ly_nhan",
        province_code=35,
    )
    D_356 = District(
        name="Thành phố Nam Định",
        code=356,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_nam_dinh",
        province_code=36,
    )
    D_358 = District(
        name="Huyện Mỹ Lộc",
        code=358,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_my_loc",
        province_code=36,
    )
    D_359 = District(
        name="Huyện Vụ Bản",
        code=359,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vu_ban",
        province_code=36,
    )
    D_360 = District(
        name="Huyện Ý Yên", code=360, division_type=VietNamDivisionType.HUYEN, codename="huyen_y_yen", province_code=36
    )
    D_361 = District(
        name="Huyện Nghĩa Hưng",
        code=361,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nghia_hung",
        province_code=36,
    )
    D_362 = District(
        name="Huyện Nam Trực",
        code=362,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nam_truc",
        province_code=36,
    )
    D_363 = District(
        name="Huyện Trực Ninh",
        code=363,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_truc_ninh",
        province_code=36,
    )
    D_364 = District(
        name="Huyện Xuân Trường",
        code=364,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_xuan_truong",
        province_code=36,
    )
    D_365 = District(
        name="Huyện Giao Thủy",
        code=365,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_giao_thuy",
        province_code=36,
    )
    D_366 = District(
        name="Huyện Hải Hậu",
        code=366,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hai_hau",
        province_code=36,
    )
    D_369 = District(
        name="Thành phố Ninh Bình",
        code=369,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_ninh_binh",
        province_code=37,
    )
    D_370 = District(
        name="Thành phố Tam Điệp",
        code=370,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_tam_diep",
        province_code=37,
    )
    D_372 = District(
        name="Huyện Nho Quan",
        code=372,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nho_quan",
        province_code=37,
    )
    D_373 = District(
        name="Huyện Gia Viễn",
        code=373,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_gia_vien",
        province_code=37,
    )
    D_374 = District(
        name="Huyện Hoa Lư",
        code=374,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hoa_lu",
        province_code=37,
    )
    D_375 = District(
        name="Huyện Yên Khánh",
        code=375,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_khanh",
        province_code=37,
    )
    D_376 = District(
        name="Huyện Kim Sơn",
        code=376,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_kim_son",
        province_code=37,
    )
    D_377 = District(
        name="Huyện Yên Mô",
        code=377,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_mo",
        province_code=37,
    )
    D_380 = District(
        name="Thành phố Thanh Hóa",
        code=380,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_thanh_hoa",
        province_code=38,
    )
    D_381 = District(
        name="Thị xã Bỉm Sơn",
        code=381,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_bim_son",
        province_code=38,
    )
    D_382 = District(
        name="Thành phố Sầm Sơn",
        code=382,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_sam_son",
        province_code=38,
    )
    D_384 = District(
        name="Huyện Mường Lát",
        code=384,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_muong_lat",
        province_code=38,
    )
    D_385 = District(
        name="Huyện Quan Hóa",
        code=385,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quan_hoa",
        province_code=38,
    )
    D_386 = District(
        name="Huyện Bá Thước",
        code=386,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ba_thuoc",
        province_code=38,
    )
    D_387 = District(
        name="Huyện Quan Sơn",
        code=387,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quan_son",
        province_code=38,
    )
    D_388 = District(
        name="Huyện Lang Chánh",
        code=388,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_lang_chanh",
        province_code=38,
    )
    D_389 = District(
        name="Huyện Ngọc Lặc",
        code=389,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ngoc_lac",
        province_code=38,
    )
    D_390 = District(
        name="Huyện Cẩm Thủy",
        code=390,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cam_thuy",
        province_code=38,
    )
    D_391 = District(
        name="Huyện Thạch Thành",
        code=391,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thach_thanh",
        province_code=38,
    )
    D_392 = District(
        name="Huyện Hà Trung",
        code=392,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ha_trung",
        province_code=38,
    )
    D_393 = District(
        name="Huyện Vĩnh Lộc",
        code=393,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vinh_loc",
        province_code=38,
    )
    D_394 = District(
        name="Huyện Yên Định",
        code=394,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_dinh",
        province_code=38,
    )
    D_395 = District(
        name="Huyện Thọ Xuân",
        code=395,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tho_xuan",
        province_code=38,
    )
    D_396 = District(
        name="Huyện Thường Xuân",
        code=396,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thuong_xuan",
        province_code=38,
    )
    D_397 = District(
        name="Huyện Triệu Sơn",
        code=397,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_trieu_son",
        province_code=38,
    )
    D_398 = District(
        name="Huyện Thiệu Hóa",
        code=398,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thieu_hoa",
        province_code=38,
    )
    D_399 = District(
        name="Huyện Hoằng Hóa",
        code=399,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hoang_hoa",
        province_code=38,
    )
    D_400 = District(
        name="Huyện Hậu Lộc",
        code=400,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hau_loc",
        province_code=38,
    )
    D_401 = District(
        name="Huyện Nga Sơn",
        code=401,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nga_son",
        province_code=38,
    )
    D_402 = District(
        name="Huyện Như Xuân",
        code=402,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nhu_xuan",
        province_code=38,
    )
    D_403 = District(
        name="Huyện Như Thanh",
        code=403,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nhu_thanh",
        province_code=38,
    )
    D_404 = District(
        name="Huyện Nông Cống",
        code=404,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nong_cong",
        province_code=38,
    )
    D_405 = District(
        name="Huyện Đông Sơn",
        code=405,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dong_son",
        province_code=38,
    )
    D_406 = District(
        name="Huyện Quảng Xương",
        code=406,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quang_xuong",
        province_code=38,
    )
    D_407 = District(
        name="Huyện Tĩnh Gia",
        code=407,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tinh_gia",
        province_code=38,
    )
    D_412 = District(
        name="Thành phố Vinh",
        code=412,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_vinh",
        province_code=40,
    )
    D_413 = District(
        name="Thị xã Cửa Lò",
        code=413,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_cua_lo",
        province_code=40,
    )
    D_414 = District(
        name="Thị xã Thái Hoà",
        code=414,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_thai_hoa",
        province_code=40,
    )
    D_415 = District(
        name="Huyện Quế Phong",
        code=415,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_que_phong",
        province_code=40,
    )
    D_416 = District(
        name="Huyện Quỳ Châu",
        code=416,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quy_chau",
        province_code=40,
    )
    D_417 = District(
        name="Huyện Kỳ Sơn",
        code=417,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ky_son",
        province_code=40,
    )
    D_418 = District(
        name="Huyện Tương Dương",
        code=418,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tuong_duong",
        province_code=40,
    )
    D_419 = District(
        name="Huyện Nghĩa Đàn",
        code=419,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nghia_dan",
        province_code=40,
    )
    D_420 = District(
        name="Huyện Quỳ Hợp",
        code=420,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quy_hop",
        province_code=40,
    )
    D_421 = District(
        name="Huyện Quỳnh Lưu",
        code=421,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quynh_luu",
        province_code=40,
    )
    D_422 = District(
        name="Huyện Con Cuông",
        code=422,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_con_cuong",
        province_code=40,
    )
    D_423 = District(
        name="Huyện Tân Kỳ",
        code=423,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_ky",
        province_code=40,
    )
    D_424 = District(
        name="Huyện Anh Sơn",
        code=424,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_anh_son",
        province_code=40,
    )
    D_425 = District(
        name="Huyện Diễn Châu",
        code=425,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dien_chau",
        province_code=40,
    )
    D_426 = District(
        name="Huyện Yên Thành",
        code=426,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_yen_thanh",
        province_code=40,
    )
    D_427 = District(
        name="Huyện Đô Lương",
        code=427,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_do_luong",
        province_code=40,
    )
    D_428 = District(
        name="Huyện Thanh Chương",
        code=428,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thanh_chuong",
        province_code=40,
    )
    D_429 = District(
        name="Huyện Nghi Lộc",
        code=429,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nghi_loc",
        province_code=40,
    )
    D_430 = District(
        name="Huyện Nam Đàn",
        code=430,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nam_dan",
        province_code=40,
    )
    D_431 = District(
        name="Huyện Hưng Nguyên",
        code=431,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hung_nguyen",
        province_code=40,
    )
    D_432 = District(
        name="Thị xã Hoàng Mai",
        code=432,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_hoang_mai",
        province_code=40,
    )
    D_436 = District(
        name="Thành phố Hà Tĩnh",
        code=436,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_ha_tinh",
        province_code=42,
    )
    D_437 = District(
        name="Thị xã Hồng Lĩnh",
        code=437,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_hong_linh",
        province_code=42,
    )
    D_439 = District(
        name="Huyện Hương Sơn",
        code=439,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_huong_son",
        province_code=42,
    )
    D_440 = District(
        name="Huyện Đức Thọ",
        code=440,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_duc_tho",
        province_code=42,
    )
    D_441 = District(
        name="Huyện Vũ Quang",
        code=441,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vu_quang",
        province_code=42,
    )
    D_442 = District(
        name="Huyện Nghi Xuân",
        code=442,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nghi_xuan",
        province_code=42,
    )
    D_443 = District(
        name="Huyện Can Lộc",
        code=443,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_can_loc",
        province_code=42,
    )
    D_444 = District(
        name="Huyện Hương Khê",
        code=444,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_huong_khe",
        province_code=42,
    )
    D_445 = District(
        name="Huyện Thạch Hà",
        code=445,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thach_ha",
        province_code=42,
    )
    D_446 = District(
        name="Huyện Cẩm Xuyên",
        code=446,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cam_xuyen",
        province_code=42,
    )
    D_447 = District(
        name="Huyện Kỳ Anh",
        code=447,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ky_anh",
        province_code=42,
    )
    D_448 = District(
        name="Huyện Lộc Hà",
        code=448,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_loc_ha",
        province_code=42,
    )
    D_449 = District(
        name="Thị xã Kỳ Anh",
        code=449,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_ky_anh",
        province_code=42,
    )
    D_450 = District(
        name="Thành Phố Đồng Hới",
        code=450,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_dong_hoi",
        province_code=44,
    )
    D_452 = District(
        name="Huyện Minh Hóa",
        code=452,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_minh_hoa",
        province_code=44,
    )
    D_453 = District(
        name="Huyện Tuyên Hóa",
        code=453,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tuyen_hoa",
        province_code=44,
    )
    D_454 = District(
        name="Huyện Quảng Trạch",
        code=454,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quang_trach",
        province_code=44,
    )
    D_455 = District(
        name="Huyện Bố Trạch",
        code=455,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bo_trach",
        province_code=44,
    )
    D_456 = District(
        name="Huyện Quảng Ninh",
        code=456,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quang_ninh",
        province_code=44,
    )
    D_457 = District(
        name="Huyện Lệ Thủy",
        code=457,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_le_thuy",
        province_code=44,
    )
    D_458 = District(
        name="Thị xã Ba Đồn",
        code=458,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_ba_don",
        province_code=44,
    )
    D_461 = District(
        name="Thành phố Đông Hà",
        code=461,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_dong_ha",
        province_code=45,
    )
    D_462 = District(
        name="Thị xã Quảng Trị",
        code=462,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_quang_tri",
        province_code=45,
    )
    D_464 = District(
        name="Huyện Vĩnh Linh",
        code=464,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vinh_linh",
        province_code=45,
    )
    D_465 = District(
        name="Huyện Hướng Hóa",
        code=465,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_huong_hoa",
        province_code=45,
    )
    D_466 = District(
        name="Huyện Gio Linh",
        code=466,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_gio_linh",
        province_code=45,
    )
    D_467 = District(
        name="Huyện Đa Krông",
        code=467,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_da_krong",
        province_code=45,
    )
    D_468 = District(
        name="Huyện Cam Lộ",
        code=468,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cam_lo",
        province_code=45,
    )
    D_469 = District(
        name="Huyện Triệu Phong",
        code=469,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_trieu_phong",
        province_code=45,
    )
    D_470 = District(
        name="Huyện Hải Lăng",
        code=470,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hai_lang",
        province_code=45,
    )
    D_474 = District(
        name="Thành phố Huế",
        code=474,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_hue",
        province_code=46,
    )
    D_476 = District(
        name="Huyện Phong Điền",
        code=476,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phong_dien",
        province_code=46,
    )
    D_477 = District(
        name="Huyện Quảng Điền",
        code=477,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_quang_dien",
        province_code=46,
    )
    D_478 = District(
        name="Huyện Phú Vang",
        code=478,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_vang",
        province_code=46,
    )
    D_479 = District(
        name="Thị xã Hương Thủy",
        code=479,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_huong_thuy",
        province_code=46,
    )
    D_480 = District(
        name="Thị xã Hương Trà",
        code=480,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_huong_tra",
        province_code=46,
    )
    D_481 = District(
        name="Huyện A Lưới",
        code=481,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_a_luoi",
        province_code=46,
    )
    D_482 = District(
        name="Huyện Phú Lộc",
        code=482,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_loc",
        province_code=46,
    )
    D_483 = District(
        name="Huyện Nam Đông",
        code=483,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nam_dong",
        province_code=46,
    )
    D_490 = District(
        name="Quận Liên Chiểu",
        code=490,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_lien_chieu",
        province_code=48,
    )
    D_491 = District(
        name="Quận Thanh Khê",
        code=491,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_thanh_khe",
        province_code=48,
    )
    D_492 = District(
        name="Quận Hải Châu",
        code=492,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_hai_chau",
        province_code=48,
    )
    D_493 = District(
        name="Quận Sơn Trà", code=493, division_type=VietNamDivisionType.QUAN, codename="quan_son_tra", province_code=48
    )
    D_494 = District(
        name="Quận Ngũ Hành Sơn",
        code=494,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_ngu_hanh_son",
        province_code=48,
    )
    D_495 = District(
        name="Quận Cẩm Lệ", code=495, division_type=VietNamDivisionType.QUAN, codename="quan_cam_le", province_code=48
    )
    D_497 = District(
        name="Huyện Hòa Vang",
        code=497,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hoa_vang",
        province_code=48,
    )
    D_502 = District(
        name="Thành phố Tam Kỳ",
        code=502,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_tam_ky",
        province_code=49,
    )
    D_503 = District(
        name="Thành phố Hội An",
        code=503,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_hoi_an",
        province_code=49,
    )
    D_504 = District(
        name="Huyện Tây Giang",
        code=504,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tay_giang",
        province_code=49,
    )
    D_505 = District(
        name="Huyện Đông Giang",
        code=505,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dong_giang",
        province_code=49,
    )
    D_506 = District(
        name="Huyện Đại Lộc",
        code=506,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dai_loc",
        province_code=49,
    )
    D_507 = District(
        name="Thị xã Điện Bàn",
        code=507,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_dien_ban",
        province_code=49,
    )
    D_508 = District(
        name="Huyện Duy Xuyên",
        code=508,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_duy_xuyen",
        province_code=49,
    )
    D_509 = District(
        name="Huyện Quế Sơn",
        code=509,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_que_son",
        province_code=49,
    )
    D_510 = District(
        name="Huyện Nam Giang",
        code=510,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nam_giang",
        province_code=49,
    )
    D_511 = District(
        name="Huyện Phước Sơn",
        code=511,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phuoc_son",
        province_code=49,
    )
    D_512 = District(
        name="Huyện Hiệp Đức",
        code=512,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hiep_duc",
        province_code=49,
    )
    D_513 = District(
        name="Huyện Thăng Bình",
        code=513,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thang_binh",
        province_code=49,
    )
    D_514 = District(
        name="Huyện Tiên Phước",
        code=514,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tien_phuoc",
        province_code=49,
    )
    D_515 = District(
        name="Huyện Bắc Trà My",
        code=515,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bac_tra_my",
        province_code=49,
    )
    D_516 = District(
        name="Huyện Nam Trà My",
        code=516,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nam_tra_my",
        province_code=49,
    )
    D_517 = District(
        name="Huyện Núi Thành",
        code=517,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nui_thanh",
        province_code=49,
    )
    D_518 = District(
        name="Huyện Phú Ninh",
        code=518,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_ninh",
        province_code=49,
    )
    D_519 = District(
        name="Huyện Nông Sơn",
        code=519,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nong_son",
        province_code=49,
    )
    D_522 = District(
        name="Thành phố Quảng Ngãi",
        code=522,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_quang_ngai",
        province_code=51,
    )
    D_524 = District(
        name="Huyện Bình Sơn",
        code=524,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_binh_son",
        province_code=51,
    )
    D_525 = District(
        name="Huyện Trà Bồng",
        code=525,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tra_bong",
        province_code=51,
    )
    D_526 = District(
        name="Huyện Tây Trà",
        code=526,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tay_tra",
        province_code=51,
    )
    D_527 = District(
        name="Huyện Sơn Tịnh",
        code=527,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_son_tinh",
        province_code=51,
    )
    D_528 = District(
        name="Huyện Tư Nghĩa",
        code=528,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tu_nghia",
        province_code=51,
    )
    D_529 = District(
        name="Huyện Sơn Hà",
        code=529,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_son_ha",
        province_code=51,
    )
    D_530 = District(
        name="Huyện Sơn Tây",
        code=530,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_son_tay",
        province_code=51,
    )
    D_531 = District(
        name="Huyện Minh Long",
        code=531,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_minh_long",
        province_code=51,
    )
    D_532 = District(
        name="Huyện Nghĩa Hành",
        code=532,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nghia_hanh",
        province_code=51,
    )
    D_533 = District(
        name="Huyện Mộ Đức",
        code=533,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_mo_duc",
        province_code=51,
    )
    D_534 = District(
        name="Huyện Đức Phổ",
        code=534,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_duc_pho",
        province_code=51,
    )
    D_535 = District(
        name="Huyện Ba Tơ", code=535, division_type=VietNamDivisionType.HUYEN, codename="huyen_ba_to", province_code=51
    )
    D_536 = District(
        name="Huyện Lý Sơn",
        code=536,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ly_son",
        province_code=51,
    )
    D_540 = District(
        name="Thành phố Qui Nhơn",
        code=540,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_qui_nhon",
        province_code=52,
    )
    D_542 = District(
        name="Huyện An Lão",
        code=542,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_an_lao",
        province_code=52,
    )
    D_543 = District(
        name="Huyện Hoài Nhơn",
        code=543,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hoai_nhon",
        province_code=52,
    )
    D_544 = District(
        name="Huyện Hoài Ân",
        code=544,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hoai_an",
        province_code=52,
    )
    D_545 = District(
        name="Huyện Phù Mỹ",
        code=545,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_my",
        province_code=52,
    )
    D_546 = District(
        name="Huyện Vĩnh Thạnh",
        code=546,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vinh_thanh",
        province_code=52,
    )
    D_547 = District(
        name="Huyện Tây Sơn",
        code=547,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tay_son",
        province_code=52,
    )
    D_548 = District(
        name="Huyện Phù Cát",
        code=548,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_cat",
        province_code=52,
    )
    D_549 = District(
        name="Thị xã An Nhơn",
        code=549,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_an_nhon",
        province_code=52,
    )
    D_550 = District(
        name="Huyện Tuy Phước",
        code=550,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tuy_phuoc",
        province_code=52,
    )
    D_551 = District(
        name="Huyện Vân Canh",
        code=551,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_van_canh",
        province_code=52,
    )
    D_555 = District(
        name="Thành phố Tuy Hoà",
        code=555,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_tuy_hoa",
        province_code=54,
    )
    D_557 = District(
        name="Thị xã Sông Cầu",
        code=557,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_song_cau",
        province_code=54,
    )
    D_558 = District(
        name="Huyện Đồng Xuân",
        code=558,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dong_xuan",
        province_code=54,
    )
    D_559 = District(
        name="Huyện Tuy An",
        code=559,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tuy_an",
        province_code=54,
    )
    D_560 = District(
        name="Huyện Sơn Hòa",
        code=560,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_son_hoa",
        province_code=54,
    )
    D_561 = District(
        name="Huyện Sông Hinh",
        code=561,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_song_hinh",
        province_code=54,
    )
    D_562 = District(
        name="Huyện Tây Hoà",
        code=562,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tay_hoa",
        province_code=54,
    )
    D_563 = District(
        name="Huyện Phú Hoà",
        code=563,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_hoa",
        province_code=54,
    )
    D_564 = District(
        name="Huyện Đông Hòa",
        code=564,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dong_hoa",
        province_code=54,
    )
    D_568 = District(
        name="Thành phố Nha Trang",
        code=568,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_nha_trang",
        province_code=56,
    )
    D_569 = District(
        name="Thành phố Cam Ranh",
        code=569,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_cam_ranh",
        province_code=56,
    )
    D_570 = District(
        name="Huyện Cam Lâm",
        code=570,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cam_lam",
        province_code=56,
    )
    D_571 = District(
        name="Huyện Vạn Ninh",
        code=571,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_van_ninh",
        province_code=56,
    )
    D_572 = District(
        name="Thị xã Ninh Hòa",
        code=572,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_ninh_hoa",
        province_code=56,
    )
    D_573 = District(
        name="Huyện Khánh Vĩnh",
        code=573,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_khanh_vinh",
        province_code=56,
    )
    D_574 = District(
        name="Huyện Diên Khánh",
        code=574,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dien_khanh",
        province_code=56,
    )
    D_575 = District(
        name="Huyện Khánh Sơn",
        code=575,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_khanh_son",
        province_code=56,
    )
    D_576 = District(
        name="Huyện Trường Sa",
        code=576,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_truong_sa",
        province_code=56,
    )
    D_582 = District(
        name="Thành phố Phan Rang-Tháp Chàm",
        code=582,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_phan_rang_thap_cham",
        province_code=58,
    )
    D_584 = District(
        name="Huyện Bác Ái",
        code=584,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bac_ai",
        province_code=58,
    )
    D_585 = District(
        name="Huyện Ninh Sơn",
        code=585,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ninh_son",
        province_code=58,
    )
    D_586 = District(
        name="Huyện Ninh Hải",
        code=586,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ninh_hai",
        province_code=58,
    )
    D_587 = District(
        name="Huyện Ninh Phước",
        code=587,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ninh_phuoc",
        province_code=58,
    )
    D_588 = District(
        name="Huyện Thuận Bắc",
        code=588,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thuan_bac",
        province_code=58,
    )
    D_589 = District(
        name="Huyện Thuận Nam",
        code=589,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thuan_nam",
        province_code=58,
    )
    D_593 = District(
        name="Thành phố Phan Thiết",
        code=593,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_phan_thiet",
        province_code=60,
    )
    D_594 = District(
        name="Thị xã La Gi",
        code=594,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_la_gi",
        province_code=60,
    )
    D_595 = District(
        name="Huyện Tuy Phong",
        code=595,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tuy_phong",
        province_code=60,
    )
    D_596 = District(
        name="Huyện Bắc Bình",
        code=596,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bac_binh",
        province_code=60,
    )
    D_597 = District(
        name="Huyện Hàm Thuận Bắc",
        code=597,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ham_thuan_bac",
        province_code=60,
    )
    D_598 = District(
        name="Huyện Hàm Thuận Nam",
        code=598,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ham_thuan_nam",
        province_code=60,
    )
    D_599 = District(
        name="Huyện Tánh Linh",
        code=599,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tanh_linh",
        province_code=60,
    )
    D_600 = District(
        name="Huyện Đức Linh",
        code=600,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_duc_linh",
        province_code=60,
    )
    D_601 = District(
        name="Huyện Hàm Tân",
        code=601,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ham_tan",
        province_code=60,
    )
    D_602 = District(
        name="Huyện Phú Quí",
        code=602,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_qui",
        province_code=60,
    )
    D_608 = District(
        name="Thành phố Kon Tum",
        code=608,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_kon_tum",
        province_code=62,
    )
    D_610 = District(
        name="Huyện Đắk Glei",
        code=610,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dak_glei",
        province_code=62,
    )
    D_611 = District(
        name="Huyện Ngọc Hồi",
        code=611,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ngoc_hoi",
        province_code=62,
    )
    D_612 = District(
        name="Huyện Đắk Tô",
        code=612,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dak_to",
        province_code=62,
    )
    D_613 = District(
        name="Huyện Kon Plông",
        code=613,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_kon_plong",
        province_code=62,
    )
    D_614 = District(
        name="Huyện Kon Rẫy",
        code=614,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_kon_ray",
        province_code=62,
    )
    D_615 = District(
        name="Huyện Đắk Hà",
        code=615,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dak_ha",
        province_code=62,
    )
    D_616 = District(
        name="Huyện Sa Thầy",
        code=616,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_sa_thay",
        province_code=62,
    )
    D_617 = District(
        name="Huyện Tu Mơ Rông",
        code=617,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tu_mo_rong",
        province_code=62,
    )
    D_618 = District(
        name="Huyện Ia H' Drai",
        code=618,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ia_h_drai",
        province_code=62,
    )
    D_622 = District(
        name="Thành phố Pleiku",
        code=622,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_pleiku",
        province_code=64,
    )
    D_623 = District(
        name="Thị xã An Khê",
        code=623,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_an_khe",
        province_code=64,
    )
    D_624 = District(
        name="Thị xã Ayun Pa",
        code=624,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_ayun_pa",
        province_code=64,
    )
    D_625 = District(
        name="Huyện KBang", code=625, division_type=VietNamDivisionType.HUYEN, codename="huyen_kbang", province_code=64
    )
    D_626 = District(
        name="Huyện Đăk Đoa",
        code=626,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dak_doa",
        province_code=64,
    )
    D_627 = District(
        name="Huyện Chư Păh",
        code=627,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chu_pah",
        province_code=64,
    )
    D_628 = District(
        name="Huyện Ia Grai",
        code=628,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ia_grai",
        province_code=64,
    )
    D_629 = District(
        name="Huyện Mang Yang",
        code=629,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_mang_yang",
        province_code=64,
    )
    D_630 = District(
        name="Huyện Kông Chro",
        code=630,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_kong_chro",
        province_code=64,
    )
    D_631 = District(
        name="Huyện Đức Cơ",
        code=631,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_duc_co",
        province_code=64,
    )
    D_632 = District(
        name="Huyện Chư Prông",
        code=632,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chu_prong",
        province_code=64,
    )
    D_633 = District(
        name="Huyện Chư Sê",
        code=633,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chu_se",
        province_code=64,
    )
    D_634 = District(
        name="Huyện Đăk Pơ",
        code=634,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dak_po",
        province_code=64,
    )
    D_635 = District(
        name="Huyện Ia Pa", code=635, division_type=VietNamDivisionType.HUYEN, codename="huyen_ia_pa", province_code=64
    )
    D_637 = District(
        name="Huyện Krông Pa",
        code=637,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_krong_pa",
        province_code=64,
    )
    D_638 = District(
        name="Huyện Phú Thiện",
        code=638,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_thien",
        province_code=64,
    )
    D_639 = District(
        name="Huyện Chư Pưh",
        code=639,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chu_puh",
        province_code=64,
    )
    D_643 = District(
        name="Thành phố Buôn Ma Thuột",
        code=643,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_buon_ma_thuot",
        province_code=66,
    )
    D_644 = District(
        name="Thị Xã Buôn Hồ",
        code=644,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_buon_ho",
        province_code=66,
    )
    D_645 = District(
        name="Huyện Ea H'leo",
        code=645,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ea_hleo",
        province_code=66,
    )
    D_646 = District(
        name="Huyện Ea Súp",
        code=646,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ea_sup",
        province_code=66,
    )
    D_647 = District(
        name="Huyện Buôn Đôn",
        code=647,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_buon_don",
        province_code=66,
    )
    D_648 = District(
        name="Huyện Cư M'gar",
        code=648,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cu_mgar",
        province_code=66,
    )
    D_649 = District(
        name="Huyện Krông Búk",
        code=649,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_krong_buk",
        province_code=66,
    )
    D_650 = District(
        name="Huyện Krông Năng",
        code=650,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_krong_nang",
        province_code=66,
    )
    D_651 = District(
        name="Huyện Ea Kar",
        code=651,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ea_kar",
        province_code=66,
    )
    D_652 = District(
        name="Huyện M'Đrắk", code=652, division_type=VietNamDivisionType.HUYEN, codename="huyen_mdrak", province_code=66
    )
    D_653 = District(
        name="Huyện Krông Bông",
        code=653,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_krong_bong",
        province_code=66,
    )
    D_654 = District(
        name="Huyện Krông Pắc",
        code=654,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_krong_pac",
        province_code=66,
    )
    D_655 = District(
        name="Huyện Krông A Na",
        code=655,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_krong_a_na",
        province_code=66,
    )
    D_656 = District(
        name="Huyện Lắk", code=656, division_type=VietNamDivisionType.HUYEN, codename="huyen_lak", province_code=66
    )
    D_657 = District(
        name="Huyện Cư Kuin",
        code=657,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cu_kuin",
        province_code=66,
    )
    D_660 = District(
        name="Thành phố Gia Nghĩa",
        code=660,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_gia_nghia",
        province_code=67,
    )
    D_661 = District(
        name="Huyện Đăk Glong",
        code=661,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dak_glong",
        province_code=67,
    )
    D_662 = District(
        name="Huyện Cư Jút",
        code=662,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cu_jut",
        province_code=67,
    )
    D_663 = District(
        name="Huyện Đắk Mil",
        code=663,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dak_mil",
        province_code=67,
    )
    D_664 = District(
        name="Huyện Krông Nô",
        code=664,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_krong_no",
        province_code=67,
    )
    D_665 = District(
        name="Huyện Đắk Song",
        code=665,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dak_song",
        province_code=67,
    )
    D_666 = District(
        name="Huyện Đắk R'Lấp",
        code=666,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dak_rlap",
        province_code=67,
    )
    D_667 = District(
        name="Huyện Tuy Đức",
        code=667,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tuy_duc",
        province_code=67,
    )
    D_672 = District(
        name="Thành phố Đà Lạt",
        code=672,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_da_lat",
        province_code=68,
    )
    D_673 = District(
        name="Thành phố Bảo Lộc",
        code=673,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_bao_loc",
        province_code=68,
    )
    D_674 = District(
        name="Huyện Đam Rông",
        code=674,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dam_rong",
        province_code=68,
    )
    D_675 = District(
        name="Huyện Lạc Dương",
        code=675,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_lac_duong",
        province_code=68,
    )
    D_676 = District(
        name="Huyện Lâm Hà",
        code=676,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_lam_ha",
        province_code=68,
    )
    D_677 = District(
        name="Huyện Đơn Dương",
        code=677,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_don_duong",
        province_code=68,
    )
    D_678 = District(
        name="Huyện Đức Trọng",
        code=678,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_duc_trong",
        province_code=68,
    )
    D_679 = District(
        name="Huyện Di Linh",
        code=679,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_di_linh",
        province_code=68,
    )
    D_680 = District(
        name="Huyện Bảo Lâm",
        code=680,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bao_lam",
        province_code=68,
    )
    D_681 = District(
        name="Huyện Đạ Huoai",
        code=681,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_da_huoai",
        province_code=68,
    )
    D_682 = District(
        name="Huyện Đạ Tẻh",
        code=682,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_da_teh",
        province_code=68,
    )
    D_683 = District(
        name="Huyện Cát Tiên",
        code=683,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cat_tien",
        province_code=68,
    )
    D_688 = District(
        name="Thị xã Phước Long",
        code=688,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_phuoc_long",
        province_code=70,
    )
    D_689 = District(
        name="Thành phố Đồng Xoài",
        code=689,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_dong_xoai",
        province_code=70,
    )
    D_690 = District(
        name="Thị xã Bình Long",
        code=690,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_binh_long",
        province_code=70,
    )
    D_691 = District(
        name="Huyện Bù Gia Mập",
        code=691,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bu_gia_map",
        province_code=70,
    )
    D_692 = District(
        name="Huyện Lộc Ninh",
        code=692,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_loc_ninh",
        province_code=70,
    )
    D_693 = District(
        name="Huyện Bù Đốp",
        code=693,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bu_dop",
        province_code=70,
    )
    D_694 = District(
        name="Huyện Hớn Quản",
        code=694,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hon_quan",
        province_code=70,
    )
    D_695 = District(
        name="Huyện Đồng Phú",
        code=695,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dong_phu",
        province_code=70,
    )
    D_696 = District(
        name="Huyện Bù Đăng",
        code=696,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bu_dang",
        province_code=70,
    )
    D_697 = District(
        name="Huyện Chơn Thành",
        code=697,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chon_thanh",
        province_code=70,
    )
    D_698 = District(
        name="Huyện Phú Riềng",
        code=698,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_rieng",
        province_code=70,
    )
    D_703 = District(
        name="Thành phố Tây Ninh",
        code=703,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_tay_ninh",
        province_code=72,
    )
    D_705 = District(
        name="Huyện Tân Biên",
        code=705,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_bien",
        province_code=72,
    )
    D_706 = District(
        name="Huyện Tân Châu",
        code=706,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_chau",
        province_code=72,
    )
    D_707 = District(
        name="Huyện Dương Minh Châu",
        code=707,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_duong_minh_chau",
        province_code=72,
    )
    D_708 = District(
        name="Huyện Châu Thành",
        code=708,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chau_thanh",
        province_code=72,
    )
    D_709 = District(
        name="Huyện Hòa Thành",
        code=709,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hoa_thanh",
        province_code=72,
    )
    D_710 = District(
        name="Huyện Gò Dầu",
        code=710,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_go_dau",
        province_code=72,
    )
    D_711 = District(
        name="Huyện Bến Cầu",
        code=711,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ben_cau",
        province_code=72,
    )
    D_712 = District(
        name="Huyện Trảng Bàng",
        code=712,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_trang_bang",
        province_code=72,
    )
    D_718 = District(
        name="Thành phố Thủ Dầu Một",
        code=718,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_thu_dau_mot",
        province_code=74,
    )
    D_719 = District(
        name="Huyện Bàu Bàng",
        code=719,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bau_bang",
        province_code=74,
    )
    D_720 = District(
        name="Huyện Dầu Tiếng",
        code=720,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dau_tieng",
        province_code=74,
    )
    D_721 = District(
        name="Thị xã Bến Cát",
        code=721,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_ben_cat",
        province_code=74,
    )
    D_722 = District(
        name="Huyện Phú Giáo",
        code=722,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_giao",
        province_code=74,
    )
    D_723 = District(
        name="Thị xã Tân Uyên",
        code=723,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_tan_uyen",
        province_code=74,
    )
    D_724 = District(
        name="Thị xã Dĩ An",
        code=724,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_di_an",
        province_code=74,
    )
    D_725 = District(
        name="Thị xã Thuận An",
        code=725,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_thuan_an",
        province_code=74,
    )
    D_726 = District(
        name="Huyện Bắc Tân Uyên",
        code=726,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_bac_tan_uyen",
        province_code=74,
    )
    D_731 = District(
        name="Thành phố Biên Hòa",
        code=731,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_bien_hoa",
        province_code=75,
    )
    D_732 = District(
        name="Thành phố Long Khánh",
        code=732,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_long_khanh",
        province_code=75,
    )
    D_734 = District(
        name="Huyện Tân Phú",
        code=734,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_phu",
        province_code=75,
    )
    D_735 = District(
        name="Huyện Vĩnh Cửu",
        code=735,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vinh_cuu",
        province_code=75,
    )
    D_736 = District(
        name="Huyện Định Quán",
        code=736,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dinh_quan",
        province_code=75,
    )
    D_737 = District(
        name="Huyện Trảng Bom",
        code=737,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_trang_bom",
        province_code=75,
    )
    D_738 = District(
        name="Huyện Thống Nhất",
        code=738,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thong_nhat",
        province_code=75,
    )
    D_739 = District(
        name="Huyện Cẩm Mỹ",
        code=739,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cam_my",
        province_code=75,
    )
    D_740 = District(
        name="Huyện Long Thành",
        code=740,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_long_thanh",
        province_code=75,
    )
    D_741 = District(
        name="Huyện Xuân Lộc",
        code=741,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_xuan_loc",
        province_code=75,
    )
    D_742 = District(
        name="Huyện Nhơn Trạch",
        code=742,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nhon_trach",
        province_code=75,
    )
    D_747 = District(
        name="Thành phố Vũng Tàu",
        code=747,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_vung_tau",
        province_code=77,
    )
    D_748 = District(
        name="Thành phố Bà Rịa",
        code=748,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_ba_ria",
        province_code=77,
    )
    D_750 = District(
        name="Huyện Châu Đức",
        code=750,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chau_duc",
        province_code=77,
    )
    D_751 = District(
        name="Huyện Xuyên Mộc",
        code=751,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_xuyen_moc",
        province_code=77,
    )
    D_752 = District(
        name="Huyện Long Điền",
        code=752,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_long_dien",
        province_code=77,
    )
    D_753 = District(
        name="Huyện Đất Đỏ",
        code=753,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dat_do",
        province_code=77,
    )
    D_754 = District(
        name="Thị xã Phú Mỹ",
        code=754,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_phu_my",
        province_code=77,
    )
    D_760 = District(
        name="Quận 1", code=760, division_type=VietNamDivisionType.QUAN, codename="quan_1", province_code=79
    )
    D_761 = District(
        name="Quận 12", code=761, division_type=VietNamDivisionType.QUAN, codename="quan_12", province_code=79
    )
    D_762 = District(
        name="Quận Thủ Đức", code=762, division_type=VietNamDivisionType.QUAN, codename="quan_thu_duc", province_code=79
    )
    D_763 = District(
        name="Quận 9", code=763, division_type=VietNamDivisionType.QUAN, codename="quan_9", province_code=79
    )
    D_764 = District(
        name="Quận Gò Vấp", code=764, division_type=VietNamDivisionType.QUAN, codename="quan_go_vap", province_code=79
    )
    D_765 = District(
        name="Quận Bình Thạnh",
        code=765,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_binh_thanh",
        province_code=79,
    )
    D_766 = District(
        name="Quận Tân Bình",
        code=766,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_tan_binh",
        province_code=79,
    )
    D_767 = District(
        name="Quận Tân Phú", code=767, division_type=VietNamDivisionType.QUAN, codename="quan_tan_phu", province_code=79
    )
    D_768 = District(
        name="Quận Phú Nhuận",
        code=768,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_phu_nhuan",
        province_code=79,
    )
    D_769 = District(
        name="Quận 2", code=769, division_type=VietNamDivisionType.QUAN, codename="quan_2", province_code=79
    )
    D_770 = District(
        name="Quận 3", code=770, division_type=VietNamDivisionType.QUAN, codename="quan_3", province_code=79
    )
    D_771 = District(
        name="Quận 10", code=771, division_type=VietNamDivisionType.QUAN, codename="quan_10", province_code=79
    )
    D_772 = District(
        name="Quận 11", code=772, division_type=VietNamDivisionType.QUAN, codename="quan_11", province_code=79
    )
    D_773 = District(
        name="Quận 4", code=773, division_type=VietNamDivisionType.QUAN, codename="quan_4", province_code=79
    )
    D_774 = District(
        name="Quận 5", code=774, division_type=VietNamDivisionType.QUAN, codename="quan_5", province_code=79
    )
    D_775 = District(
        name="Quận 6", code=775, division_type=VietNamDivisionType.QUAN, codename="quan_6", province_code=79
    )
    D_776 = District(
        name="Quận 8", code=776, division_type=VietNamDivisionType.QUAN, codename="quan_8", province_code=79
    )
    D_777 = District(
        name="Quận Bình Tân",
        code=777,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_binh_tan",
        province_code=79,
    )
    D_778 = District(
        name="Quận 7", code=778, division_type=VietNamDivisionType.QUAN, codename="quan_7", province_code=79
    )
    D_783 = District(
        name="Huyện Củ Chi",
        code=783,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cu_chi",
        province_code=79,
    )
    D_784 = District(
        name="Huyện Hóc Môn",
        code=784,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hoc_mon",
        province_code=79,
    )
    D_785 = District(
        name="Huyện Bình Chánh",
        code=785,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_binh_chanh",
        province_code=79,
    )
    D_786 = District(
        name="Huyện Nhà Bè",
        code=786,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nha_be",
        province_code=79,
    )
    D_787 = District(
        name="Huyện Cần Giờ",
        code=787,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_can_gio",
        province_code=79,
    )
    D_794 = District(
        name="Thành phố Tân An",
        code=794,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_tan_an",
        province_code=80,
    )
    D_795 = District(
        name="Thị xã Kiến Tường",
        code=795,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_kien_tuong",
        province_code=80,
    )
    D_796 = District(
        name="Huyện Tân Hưng",
        code=796,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_hung",
        province_code=80,
    )
    D_797 = District(
        name="Huyện Vĩnh Hưng",
        code=797,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vinh_hung",
        province_code=80,
    )
    D_798 = District(
        name="Huyện Mộc Hóa",
        code=798,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_moc_hoa",
        province_code=80,
    )
    D_799 = District(
        name="Huyện Tân Thạnh",
        code=799,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_thanh",
        province_code=80,
    )
    D_800 = District(
        name="Huyện Thạnh Hóa",
        code=800,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thanh_hoa",
        province_code=80,
    )
    D_801 = District(
        name="Huyện Đức Huệ",
        code=801,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_duc_hue",
        province_code=80,
    )
    D_802 = District(
        name="Huyện Đức Hòa",
        code=802,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_duc_hoa",
        province_code=80,
    )
    D_803 = District(
        name="Huyện Bến Lức",
        code=803,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ben_luc",
        province_code=80,
    )
    D_804 = District(
        name="Huyện Thủ Thừa",
        code=804,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thu_thua",
        province_code=80,
    )
    D_805 = District(
        name="Huyện Tân Trụ",
        code=805,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_tru",
        province_code=80,
    )
    D_806 = District(
        name="Huyện Cần Đước",
        code=806,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_can_duoc",
        province_code=80,
    )
    D_807 = District(
        name="Huyện Cần Giuộc",
        code=807,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_can_giuoc",
        province_code=80,
    )
    D_808 = District(
        name="Huyện Châu Thành",
        code=808,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chau_thanh",
        province_code=80,
    )
    D_815 = District(
        name="Thành phố Mỹ Tho",
        code=815,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_my_tho",
        province_code=82,
    )
    D_816 = District(
        name="Thị xã Gò Công",
        code=816,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_go_cong",
        province_code=82,
    )
    D_817 = District(
        name="Thị xã Cai Lậy",
        code=817,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_cai_lay",
        province_code=82,
    )
    D_818 = District(
        name="Huyện Tân Phước",
        code=818,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_phuoc",
        province_code=82,
    )
    D_819 = District(
        name="Huyện Cái Bè",
        code=819,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cai_be",
        province_code=82,
    )
    D_820 = District(
        name="Huyện Cai Lậy",
        code=820,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cai_lay",
        province_code=82,
    )
    D_821 = District(
        name="Huyện Châu Thành",
        code=821,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chau_thanh",
        province_code=82,
    )
    D_822 = District(
        name="Huyện Chợ Gạo",
        code=822,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cho_gao",
        province_code=82,
    )
    D_823 = District(
        name="Huyện Gò Công Tây",
        code=823,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_go_cong_tay",
        province_code=82,
    )
    D_824 = District(
        name="Huyện Gò Công Đông",
        code=824,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_go_cong_dong",
        province_code=82,
    )
    D_825 = District(
        name="Huyện Tân Phú Đông",
        code=825,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_phu_dong",
        province_code=82,
    )
    D_829 = District(
        name="Thành phố Bến Tre",
        code=829,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_ben_tre",
        province_code=83,
    )
    D_831 = District(
        name="Huyện Châu Thành",
        code=831,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chau_thanh",
        province_code=83,
    )
    D_832 = District(
        name="Huyện Chợ Lách",
        code=832,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cho_lach",
        province_code=83,
    )
    D_833 = District(
        name="Huyện Mỏ Cày Nam",
        code=833,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_mo_cay_nam",
        province_code=83,
    )
    D_834 = District(
        name="Huyện Giồng Trôm",
        code=834,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_giong_trom",
        province_code=83,
    )
    D_835 = District(
        name="Huyện Bình Đại",
        code=835,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_binh_dai",
        province_code=83,
    )
    D_836 = District(
        name="Huyện Ba Tri",
        code=836,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ba_tri",
        province_code=83,
    )
    D_837 = District(
        name="Huyện Thạnh Phú",
        code=837,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thanh_phu",
        province_code=83,
    )
    D_838 = District(
        name="Huyện Mỏ Cày Bắc",
        code=838,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_mo_cay_bac",
        province_code=83,
    )
    D_842 = District(
        name="Thành phố Trà Vinh",
        code=842,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_tra_vinh",
        province_code=84,
    )
    D_844 = District(
        name="Huyện Càng Long",
        code=844,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cang_long",
        province_code=84,
    )
    D_845 = District(
        name="Huyện Cầu Kè",
        code=845,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cau_ke",
        province_code=84,
    )
    D_846 = District(
        name="Huyện Tiểu Cần",
        code=846,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tieu_can",
        province_code=84,
    )
    D_847 = District(
        name="Huyện Châu Thành",
        code=847,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chau_thanh",
        province_code=84,
    )
    D_848 = District(
        name="Huyện Cầu Ngang",
        code=848,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cau_ngang",
        province_code=84,
    )
    D_849 = District(
        name="Huyện Trà Cú",
        code=849,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tra_cu",
        province_code=84,
    )
    D_850 = District(
        name="Huyện Duyên Hải",
        code=850,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_duyen_hai",
        province_code=84,
    )
    D_851 = District(
        name="Thị xã Duyên Hải",
        code=851,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_duyen_hai",
        province_code=84,
    )
    D_855 = District(
        name="Thành phố Vĩnh Long",
        code=855,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_vinh_long",
        province_code=86,
    )
    D_857 = District(
        name="Huyện Long Hồ",
        code=857,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_long_ho",
        province_code=86,
    )
    D_858 = District(
        name="Huyện Mang Thít",
        code=858,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_mang_thit",
        province_code=86,
    )
    D_859 = District(
        name="Huyện Vũng Liêm",
        code=859,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vung_liem",
        province_code=86,
    )
    D_860 = District(
        name="Huyện Tam Bình",
        code=860,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tam_binh",
        province_code=86,
    )
    D_861 = District(
        name="Thị xã Bình Minh",
        code=861,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_binh_minh",
        province_code=86,
    )
    D_862 = District(
        name="Huyện Trà Ôn",
        code=862,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tra_on",
        province_code=86,
    )
    D_863 = District(
        name="Huyện Bình Tân",
        code=863,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_binh_tan",
        province_code=86,
    )
    D_866 = District(
        name="Thành phố Cao Lãnh",
        code=866,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_cao_lanh",
        province_code=87,
    )
    D_867 = District(
        name="Thành phố Sa Đéc",
        code=867,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_sa_dec",
        province_code=87,
    )
    D_868 = District(
        name="Thị xã Hồng Ngự",
        code=868,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_hong_ngu",
        province_code=87,
    )
    D_869 = District(
        name="Huyện Tân Hồng",
        code=869,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_hong",
        province_code=87,
    )
    D_870 = District(
        name="Huyện Hồng Ngự",
        code=870,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hong_ngu",
        province_code=87,
    )
    D_871 = District(
        name="Huyện Tam Nông",
        code=871,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tam_nong",
        province_code=87,
    )
    D_872 = District(
        name="Huyện Tháp Mười",
        code=872,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thap_muoi",
        province_code=87,
    )
    D_873 = District(
        name="Huyện Cao Lãnh",
        code=873,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cao_lanh",
        province_code=87,
    )
    D_874 = District(
        name="Huyện Thanh Bình",
        code=874,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thanh_binh",
        province_code=87,
    )
    D_875 = District(
        name="Huyện Lấp Vò",
        code=875,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_lap_vo",
        province_code=87,
    )
    D_876 = District(
        name="Huyện Lai Vung",
        code=876,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_lai_vung",
        province_code=87,
    )
    D_877 = District(
        name="Huyện Châu Thành",
        code=877,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chau_thanh",
        province_code=87,
    )
    D_883 = District(
        name="Thành phố Long Xuyên",
        code=883,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_long_xuyen",
        province_code=89,
    )
    D_884 = District(
        name="Thành phố Châu Đốc",
        code=884,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_chau_doc",
        province_code=89,
    )
    D_886 = District(
        name="Huyện An Phú",
        code=886,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_an_phu",
        province_code=89,
    )
    D_887 = District(
        name="Thị xã Tân Châu",
        code=887,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_tan_chau",
        province_code=89,
    )
    D_888 = District(
        name="Huyện Phú Tân",
        code=888,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_tan",
        province_code=89,
    )
    D_889 = District(
        name="Huyện Châu Phú",
        code=889,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chau_phu",
        province_code=89,
    )
    D_890 = District(
        name="Huyện Tịnh Biên",
        code=890,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tinh_bien",
        province_code=89,
    )
    D_891 = District(
        name="Huyện Tri Tôn",
        code=891,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tri_ton",
        province_code=89,
    )
    D_892 = District(
        name="Huyện Châu Thành",
        code=892,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chau_thanh",
        province_code=89,
    )
    D_893 = District(
        name="Huyện Chợ Mới",
        code=893,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cho_moi",
        province_code=89,
    )
    D_894 = District(
        name="Huyện Thoại Sơn",
        code=894,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thoai_son",
        province_code=89,
    )
    D_899 = District(
        name="Thành phố Rạch Giá",
        code=899,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_rach_gia",
        province_code=91,
    )
    D_900 = District(
        name="Thành phố Hà Tiên",
        code=900,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_ha_tien",
        province_code=91,
    )
    D_902 = District(
        name="Huyện Kiên Lương",
        code=902,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_kien_luong",
        province_code=91,
    )
    D_903 = District(
        name="Huyện Hòn Đất",
        code=903,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hon_dat",
        province_code=91,
    )
    D_904 = District(
        name="Huyện Tân Hiệp",
        code=904,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tan_hiep",
        province_code=91,
    )
    D_905 = District(
        name="Huyện Châu Thành",
        code=905,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chau_thanh",
        province_code=91,
    )
    D_906 = District(
        name="Huyện Giồng Riềng",
        code=906,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_giong_rieng",
        province_code=91,
    )
    D_907 = District(
        name="Huyện Gò Quao",
        code=907,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_go_quao",
        province_code=91,
    )
    D_908 = District(
        name="Huyện An Biên",
        code=908,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_an_bien",
        province_code=91,
    )
    D_909 = District(
        name="Huyện An Minh",
        code=909,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_an_minh",
        province_code=91,
    )
    D_910 = District(
        name="Huyện Vĩnh Thuận",
        code=910,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vinh_thuan",
        province_code=91,
    )
    D_911 = District(
        name="Huyện Phú Quốc",
        code=911,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_quoc",
        province_code=91,
    )
    D_912 = District(
        name="Huyện Kiên Hải",
        code=912,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_kien_hai",
        province_code=91,
    )
    D_913 = District(
        name="Huyện U Minh Thượng",
        code=913,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_u_minh_thuong",
        province_code=91,
    )
    D_914 = District(
        name="Huyện Giang Thành",
        code=914,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_giang_thanh",
        province_code=91,
    )
    D_916 = District(
        name="Quận Ninh Kiều",
        code=916,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_ninh_kieu",
        province_code=92,
    )
    D_917 = District(
        name="Quận Ô Môn", code=917, division_type=VietNamDivisionType.QUAN, codename="quan_o_mon", province_code=92
    )
    D_918 = District(
        name="Quận Bình Thuỷ",
        code=918,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_binh_thuy",
        province_code=92,
    )
    D_919 = District(
        name="Quận Cái Răng",
        code=919,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_cai_rang",
        province_code=92,
    )
    D_923 = District(
        name="Quận Thốt Nốt",
        code=923,
        division_type=VietNamDivisionType.QUAN,
        codename="quan_thot_not",
        province_code=92,
    )
    D_924 = District(
        name="Huyện Vĩnh Thạnh",
        code=924,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vinh_thanh",
        province_code=92,
    )
    D_925 = District(
        name="Huyện Cờ Đỏ", code=925, division_type=VietNamDivisionType.HUYEN, codename="huyen_co_do", province_code=92
    )
    D_926 = District(
        name="Huyện Phong Điền",
        code=926,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phong_dien",
        province_code=92,
    )
    D_927 = District(
        name="Huyện Thới Lai",
        code=927,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thoi_lai",
        province_code=92,
    )
    D_930 = District(
        name="Thành phố Vị Thanh",
        code=930,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_vi_thanh",
        province_code=93,
    )
    D_931 = District(
        name="Thị xã Ngã Bảy",
        code=931,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_nga_bay",
        province_code=93,
    )
    D_932 = District(
        name="Huyện Châu Thành A",
        code=932,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chau_thanh_a",
        province_code=93,
    )
    D_933 = District(
        name="Huyện Châu Thành",
        code=933,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chau_thanh",
        province_code=93,
    )
    D_934 = District(
        name="Huyện Phụng Hiệp",
        code=934,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phung_hiep",
        province_code=93,
    )
    D_935 = District(
        name="Huyện Vị Thuỷ",
        code=935,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vi_thuy",
        province_code=93,
    )
    D_936 = District(
        name="Huyện Long Mỹ",
        code=936,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_long_my",
        province_code=93,
    )
    D_937 = District(
        name="Thị xã Long Mỹ",
        code=937,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_long_my",
        province_code=93,
    )
    D_941 = District(
        name="Thành phố Sóc Trăng",
        code=941,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_soc_trang",
        province_code=94,
    )
    D_942 = District(
        name="Huyện Châu Thành",
        code=942,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_chau_thanh",
        province_code=94,
    )
    D_943 = District(
        name="Huyện Kế Sách",
        code=943,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ke_sach",
        province_code=94,
    )
    D_944 = District(
        name="Huyện Mỹ Tú", code=944, division_type=VietNamDivisionType.HUYEN, codename="huyen_my_tu", province_code=94
    )
    D_945 = District(
        name="Huyện Cù Lao Dung",
        code=945,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cu_lao_dung",
        province_code=94,
    )
    D_946 = District(
        name="Huyện Long Phú",
        code=946,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_long_phu",
        province_code=94,
    )
    D_947 = District(
        name="Huyện Mỹ Xuyên",
        code=947,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_my_xuyen",
        province_code=94,
    )
    D_948 = District(
        name="Thị xã Ngã Năm",
        code=948,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_nga_nam",
        province_code=94,
    )
    D_949 = District(
        name="Huyện Thạnh Trị",
        code=949,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thanh_tri",
        province_code=94,
    )
    D_950 = District(
        name="Thị xã Vĩnh Châu",
        code=950,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_vinh_chau",
        province_code=94,
    )
    D_951 = District(
        name="Huyện Trần Đề",
        code=951,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tran_de",
        province_code=94,
    )
    D_954 = District(
        name="Thành phố Bạc Liêu",
        code=954,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_bac_lieu",
        province_code=95,
    )
    D_956 = District(
        name="Huyện Hồng Dân",
        code=956,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hong_dan",
        province_code=95,
    )
    D_957 = District(
        name="Huyện Phước Long",
        code=957,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phuoc_long",
        province_code=95,
    )
    D_958 = District(
        name="Huyện Vĩnh Lợi",
        code=958,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_vinh_loi",
        province_code=95,
    )
    D_959 = District(
        name="Thị xã Giá Rai",
        code=959,
        division_type=VietNamDivisionType.THI_XA,
        codename="thi_xa_gia_rai",
        province_code=95,
    )
    D_960 = District(
        name="Huyện Đông Hải",
        code=960,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dong_hai",
        province_code=95,
    )
    D_961 = District(
        name="Huyện Hoà Bình",
        code=961,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_hoa_binh",
        province_code=95,
    )
    D_964 = District(
        name="Thành phố Cà Mau",
        code=964,
        division_type=VietNamDivisionType.THANH_PHO,
        codename="thanh_pho_ca_mau",
        province_code=96,
    )
    D_966 = District(
        name="Huyện U Minh",
        code=966,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_u_minh",
        province_code=96,
    )
    D_967 = District(
        name="Huyện Thới Bình",
        code=967,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_thoi_binh",
        province_code=96,
    )
    D_968 = District(
        name="Huyện Trần Văn Thời",
        code=968,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_tran_van_thoi",
        province_code=96,
    )
    D_969 = District(
        name="Huyện Cái Nước",
        code=969,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_cai_nuoc",
        province_code=96,
    )
    D_970 = District(
        name="Huyện Đầm Dơi",
        code=970,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_dam_doi",
        province_code=96,
    )
    D_971 = District(
        name="Huyện Năm Căn",
        code=971,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_nam_can",
        province_code=96,
    )
    D_972 = District(
        name="Huyện Phú Tân",
        code=972,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_phu_tan",
        province_code=96,
    )
    D_973 = District(
        name="Huyện Ngọc Hiển",
        code=973,
        division_type=VietNamDivisionType.HUYEN,
        codename="huyen_ngoc_hien",
        province_code=96,
    )


class DistrictDEnum(Enum):
    """
    District Enum type, whose member name is more descriptive, with district name.

    It helps developer have more idea what District he is selecting.
    """

    BA_DINH_HN = DistrictEnum.D_1.value
    HOAN_KIEM_HN = DistrictEnum.D_2.value
    TAY_HO_HN = DistrictEnum.D_3.value
    LONG_BIEN_HN = DistrictEnum.D_4.value
    CAU_GIAY_HN = DistrictEnum.D_5.value
    DONG_DA_HN = DistrictEnum.D_6.value
    HAI_BA_TRUNG_HN = DistrictEnum.D_7.value
    HOANG_MAI_HN = DistrictEnum.D_8.value
    THANH_XUAN_HN = DistrictEnum.D_9.value
    SOC_SON_HN = DistrictEnum.D_16.value
    DONG_ANH_HN = DistrictEnum.D_17.value
    GIA_LAM_HN = DistrictEnum.D_18.value
    NAM_TU_LIEM_HN = DistrictEnum.D_19.value
    THANH_TRI_HN = DistrictEnum.D_20.value
    BAC_TU_LIEM_HN = DistrictEnum.D_21.value
    ME_LINH_HN = DistrictEnum.D_250.value
    HA_DONG_HN = DistrictEnum.D_268.value
    SON_TAY_HN = DistrictEnum.D_269.value
    BA_VI_HN = DistrictEnum.D_271.value
    PHUC_THO_HN = DistrictEnum.D_272.value
    DAN_PHUONG_HN = DistrictEnum.D_273.value
    HOAI_DUC_HN = DistrictEnum.D_274.value
    QUOC_OAI_HN = DistrictEnum.D_275.value
    THACH_THAT_HN = DistrictEnum.D_276.value
    CHUONG_MY_HN = DistrictEnum.D_277.value
    THANH_OAI_HN = DistrictEnum.D_278.value
    THUONG_TIN_HN = DistrictEnum.D_279.value
    PHU_XUYEN_HN = DistrictEnum.D_280.value
    UNG_HOA_HN = DistrictEnum.D_281.value
    MY_DUC_HN = DistrictEnum.D_282.value
    HA_GIANG_HG = DistrictEnum.D_24.value
    DONG_VAN_HG = DistrictEnum.D_26.value
    MEO_VAC_HG = DistrictEnum.D_27.value
    YEN_MINH_HG = DistrictEnum.D_28.value
    QUAN_BA_HG = DistrictEnum.D_29.value
    VI_XUYEN_HG = DistrictEnum.D_30.value
    BAC_ME_HG = DistrictEnum.D_31.value
    HOANG_SU_PHI_HG = DistrictEnum.D_32.value
    XIN_MAN_HG = DistrictEnum.D_33.value
    BAC_QUANG_HG = DistrictEnum.D_34.value
    QUANG_BINH_HG = DistrictEnum.D_35.value
    CAO_BANG_CB = DistrictEnum.D_40.value
    BAO_LAM_CB = DistrictEnum.D_42.value
    BAO_LAC_CB = DistrictEnum.D_43.value
    THONG_NONG_CB = DistrictEnum.D_44.value
    HA_QUANG_CB = DistrictEnum.D_45.value
    TRA_LINH_CB = DistrictEnum.D_46.value
    TRUNG_KHANH_CB = DistrictEnum.D_47.value
    HA_LANG_CB = DistrictEnum.D_48.value
    QUANG_UYEN_CB = DistrictEnum.D_49.value
    PHUC_HOA_CB = DistrictEnum.D_50.value
    HOA_AN_CB = DistrictEnum.D_51.value
    NGUYEN_BINH_CB = DistrictEnum.D_52.value
    THACH_AN_CB = DistrictEnum.D_53.value
    BAC_KAN_BK = DistrictEnum.D_58.value
    PAC_NAM_BK = DistrictEnum.D_60.value
    BA_BE_BK = DistrictEnum.D_61.value
    NGAN_SON_BK = DistrictEnum.D_62.value
    BACH_THONG_BK = DistrictEnum.D_63.value
    CHO_DON_BK = DistrictEnum.D_64.value
    CHO_MOI_BK = DistrictEnum.D_65.value
    NA_RI_BK = DistrictEnum.D_66.value
    TUYEN_QUANG_TQ = DistrictEnum.D_70.value
    LAM_BINH_TQ = DistrictEnum.D_71.value
    NA_HANG_TQ = DistrictEnum.D_72.value
    CHIEM_HOA_TQ = DistrictEnum.D_73.value
    HAM_YEN_TQ = DistrictEnum.D_74.value
    YEN_SON_TQ = DistrictEnum.D_75.value
    SON_DUONG_TQ = DistrictEnum.D_76.value
    LAO_CAI_LC = DistrictEnum.D_80.value
    BAT_XAT_LC = DistrictEnum.D_82.value
    MUONG_KHUONG_LC = DistrictEnum.D_83.value
    SI_MA_CAI_LC = DistrictEnum.D_84.value
    BAC_HA_LC = DistrictEnum.D_85.value
    BAO_THANG_LC = DistrictEnum.D_86.value
    BAO_YEN_LC = DistrictEnum.D_87.value
    SA_PA_LC = DistrictEnum.D_88.value
    VAN_BAN_LC = DistrictEnum.D_89.value
    DIEN_BIEN_PHU_DB = DistrictEnum.D_94.value
    MUONG_LAY_DB = DistrictEnum.D_95.value
    MUONG_NHE_DB = DistrictEnum.D_96.value
    MUONG_CHA_DB = DistrictEnum.D_97.value
    TUA_CHUA_DB = DistrictEnum.D_98.value
    TUAN_GIAO_DB = DistrictEnum.D_99.value
    DIEN_BIEN_DB = DistrictEnum.D_100.value
    DIEN_BIEN_DONG_DB = DistrictEnum.D_101.value
    MUONG_ANG_DB = DistrictEnum.D_102.value
    NAM_PO_DB = DistrictEnum.D_103.value
    LAI_CHAU_LC = DistrictEnum.D_105.value
    TAM_DUONG_LC = DistrictEnum.D_106.value
    MUONG_TE_LC = DistrictEnum.D_107.value
    SIN_HO_LC = DistrictEnum.D_108.value
    PHONG_THO_LC = DistrictEnum.D_109.value
    THAN_UYEN_LC = DistrictEnum.D_110.value
    TAN_UYEN_LC = DistrictEnum.D_111.value
    NAM_NHUN_LC = DistrictEnum.D_112.value
    SON_LA_SL = DistrictEnum.D_116.value
    QUYNH_NHAI_SL = DistrictEnum.D_118.value
    THUAN_CHAU_SL = DistrictEnum.D_119.value
    MUONG_LA_SL = DistrictEnum.D_120.value
    BAC_YEN_SL = DistrictEnum.D_121.value
    PHU_YEN_SL = DistrictEnum.D_122.value
    MOC_CHAU_SL = DistrictEnum.D_123.value
    YEN_CHAU_SL = DistrictEnum.D_124.value
    MAI_SON_SL = DistrictEnum.D_125.value
    SONG_MA_SL = DistrictEnum.D_126.value
    SOP_COP_SL = DistrictEnum.D_127.value
    VAN_HO_SL = DistrictEnum.D_128.value
    YEN_BAI_YB = DistrictEnum.D_132.value
    NGHIA_LO_YB = DistrictEnum.D_133.value
    LUC_YEN_YB = DistrictEnum.D_135.value
    VAN_YEN_YB = DistrictEnum.D_136.value
    MU_CANG_CHAI_YB = DistrictEnum.D_137.value
    TRAN_YEN_YB = DistrictEnum.D_138.value
    TRAM_TAU_YB = DistrictEnum.D_139.value
    VAN_CHAN_YB = DistrictEnum.D_140.value
    YEN_BINH_YB = DistrictEnum.D_141.value
    HOA_BINH_HB = DistrictEnum.D_148.value
    DA_BAC_HB = DistrictEnum.D_150.value
    LUONG_SON_HB = DistrictEnum.D_152.value
    KIM_BOI_HB = DistrictEnum.D_153.value
    CAO_PHONG_HB = DistrictEnum.D_154.value
    TAN_LAC_HB = DistrictEnum.D_155.value
    MAI_CHAU_HB = DistrictEnum.D_156.value
    LAC_SON_HB = DistrictEnum.D_157.value
    YEN_THUY_HB = DistrictEnum.D_158.value
    LAC_THUY_HB = DistrictEnum.D_159.value
    THAI_NGUYEN_TN = DistrictEnum.D_164.value
    SONG_CONG_TN = DistrictEnum.D_165.value
    DINH_HOA_TN = DistrictEnum.D_167.value
    PHU_LUONG_TN = DistrictEnum.D_168.value
    DONG_HY_TN = DistrictEnum.D_169.value
    VO_NHAI_TN = DistrictEnum.D_170.value
    DAI_TU_TN = DistrictEnum.D_171.value
    PHO_YEN_TN = DistrictEnum.D_172.value
    PHU_BINH_TN = DistrictEnum.D_173.value
    LANG_SON_LS = DistrictEnum.D_178.value
    TRANG_DINH_LS = DistrictEnum.D_180.value
    BINH_GIA_LS = DistrictEnum.D_181.value
    VAN_LANG_LS = DistrictEnum.D_182.value
    CAO_LOC_LS = DistrictEnum.D_183.value
    VAN_QUAN_LS = DistrictEnum.D_184.value
    BAC_SON_LS = DistrictEnum.D_185.value
    HUU_LUNG_LS = DistrictEnum.D_186.value
    CHI_LANG_LS = DistrictEnum.D_187.value
    LOC_BINH_LS = DistrictEnum.D_188.value
    DINH_LAP_LS = DistrictEnum.D_189.value
    HA_LONG_QN = DistrictEnum.D_193.value
    MONG_CAI_QN = DistrictEnum.D_194.value
    CAM_PHA_QN = DistrictEnum.D_195.value
    UONG_BI_QN = DistrictEnum.D_196.value
    BINH_LIEU_QN = DistrictEnum.D_198.value
    TIEN_YEN_QN = DistrictEnum.D_199.value
    DAM_HA_QN = DistrictEnum.D_200.value
    HAI_HA_QN = DistrictEnum.D_201.value
    BA_CHE_QN = DistrictEnum.D_202.value
    VAN_DON_QN = DistrictEnum.D_203.value
    DONG_TRIEU_QN = DistrictEnum.D_205.value
    QUANG_YEN_QN = DistrictEnum.D_206.value
    CO_TO_QN = DistrictEnum.D_207.value
    BAC_GIANG_BG = DistrictEnum.D_213.value
    YEN_THE_BG = DistrictEnum.D_215.value
    TAN_YEN_BG = DistrictEnum.D_216.value
    LANG_GIANG_BG = DistrictEnum.D_217.value
    LUC_NAM_BG = DistrictEnum.D_218.value
    LUC_NGAN_BG = DistrictEnum.D_219.value
    SON_DONG_BG = DistrictEnum.D_220.value
    YEN_DUNG_BG = DistrictEnum.D_221.value
    VIET_YEN_BG = DistrictEnum.D_222.value
    HIEP_HOA_BG = DistrictEnum.D_223.value
    VIET_TRI_PT = DistrictEnum.D_227.value
    PHU_THO_PT = DistrictEnum.D_228.value
    DOAN_HUNG_PT = DistrictEnum.D_230.value
    HA_HOA_PT = DistrictEnum.D_231.value
    THANH_BA_PT = DistrictEnum.D_232.value
    PHU_NINH_PT = DistrictEnum.D_233.value
    YEN_LAP_PT = DistrictEnum.D_234.value
    CAM_KHE_PT = DistrictEnum.D_235.value
    TAM_NONG_PT = DistrictEnum.D_236.value
    LAM_THAO_PT = DistrictEnum.D_237.value
    THANH_SON_PT = DistrictEnum.D_238.value
    THANH_THUY_PT = DistrictEnum.D_239.value
    TAN_SON_PT = DistrictEnum.D_240.value
    VINH_YEN_VP = DistrictEnum.D_243.value
    PHUC_YEN_VP = DistrictEnum.D_244.value
    LAP_THACH_VP = DistrictEnum.D_246.value
    TAM_DUONG_VP = DistrictEnum.D_247.value
    TAM_DAO_VP = DistrictEnum.D_248.value
    BINH_XUYEN_VP = DistrictEnum.D_249.value
    YEN_LAC_VP = DistrictEnum.D_251.value
    VINH_TUONG_VP = DistrictEnum.D_252.value
    SONG_LO_VP = DistrictEnum.D_253.value
    BAC_NINH_BN = DistrictEnum.D_256.value
    YEN_PHONG_BN = DistrictEnum.D_258.value
    QUE_VO_BN = DistrictEnum.D_259.value
    TIEN_DU_BN = DistrictEnum.D_260.value
    TU_SON_BN = DistrictEnum.D_261.value
    THUAN_THANH_BN = DistrictEnum.D_262.value
    GIA_BINH_BN = DistrictEnum.D_263.value
    LUONG_TAI_BN = DistrictEnum.D_264.value
    HAI_DUONG_HD = DistrictEnum.D_288.value
    CHI_LINH_HD = DistrictEnum.D_290.value
    NAM_SACH_HD = DistrictEnum.D_291.value
    KINH_MON_HD = DistrictEnum.D_292.value
    KIM_THANH_HD = DistrictEnum.D_293.value
    THANH_HA_HD = DistrictEnum.D_294.value
    CAM_GIANG_HD = DistrictEnum.D_295.value
    BINH_GIANG_HD = DistrictEnum.D_296.value
    GIA_LOC_HD = DistrictEnum.D_297.value
    TU_KY_HD = DistrictEnum.D_298.value
    NINH_GIANG_HD = DistrictEnum.D_299.value
    THANH_MIEN_HD = DistrictEnum.D_300.value
    HONG_BANG_HP = DistrictEnum.D_303.value
    NGO_QUYEN_HP = DistrictEnum.D_304.value
    LE_CHAN_HP = DistrictEnum.D_305.value
    HAI_AN_HP = DistrictEnum.D_306.value
    KIEN_AN_HP = DistrictEnum.D_307.value
    DO_SON_HP = DistrictEnum.D_308.value
    DUONG_KINH_HP = DistrictEnum.D_309.value
    THUY_NGUYEN_HP = DistrictEnum.D_311.value
    AN_DUONG_HP = DistrictEnum.D_312.value
    AN_LAO_HP = DistrictEnum.D_313.value
    KIEN_THUY_HP = DistrictEnum.D_314.value
    TIEN_LANG_HP = DistrictEnum.D_315.value
    VINH_BAO_HP = DistrictEnum.D_316.value
    CAT_HAI_HP = DistrictEnum.D_317.value
    HUNG_YEN_HY = DistrictEnum.D_323.value
    VAN_LAM_HY = DistrictEnum.D_325.value
    VAN_GIANG_HY = DistrictEnum.D_326.value
    YEN_MY_HY = DistrictEnum.D_327.value
    MY_HAO_HY = DistrictEnum.D_328.value
    AN_THI_HY = DistrictEnum.D_329.value
    KHOAI_CHAU_HY = DistrictEnum.D_330.value
    KIM_DONG_HY = DistrictEnum.D_331.value
    TIEN_LU_HY = DistrictEnum.D_332.value
    PHU_CU_HY = DistrictEnum.D_333.value
    THAI_BINH_TB = DistrictEnum.D_336.value
    QUYNH_PHU_TB = DistrictEnum.D_338.value
    HUNG_HA_TB = DistrictEnum.D_339.value
    DONG_HUNG_TB = DistrictEnum.D_340.value
    THAI_THUY_TB = DistrictEnum.D_341.value
    TIEN_HAI_TB = DistrictEnum.D_342.value
    KIEN_XUONG_TB = DistrictEnum.D_343.value
    VU_THU_TB = DistrictEnum.D_344.value
    PHU_LY_HN = DistrictEnum.D_347.value
    DUY_TIEN_HN = DistrictEnum.D_349.value
    KIM_BANG_HN = DistrictEnum.D_350.value
    THANH_LIEM_HN = DistrictEnum.D_351.value
    BINH_LUC_HN = DistrictEnum.D_352.value
    LY_NHAN_HN = DistrictEnum.D_353.value
    NAM_DINH_ND = DistrictEnum.D_356.value
    MY_LOC_ND = DistrictEnum.D_358.value
    VU_BAN_ND = DistrictEnum.D_359.value
    Y_YEN_ND = DistrictEnum.D_360.value
    NGHIA_HUNG_ND = DistrictEnum.D_361.value
    NAM_TRUC_ND = DistrictEnum.D_362.value
    TRUC_NINH_ND = DistrictEnum.D_363.value
    XUAN_TRUONG_ND = DistrictEnum.D_364.value
    GIAO_THUY_ND = DistrictEnum.D_365.value
    HAI_HAU_ND = DistrictEnum.D_366.value
    NINH_BINH_NB = DistrictEnum.D_369.value
    TAM_DIEP_NB = DistrictEnum.D_370.value
    NHO_QUAN_NB = DistrictEnum.D_372.value
    GIA_VIEN_NB = DistrictEnum.D_373.value
    HOA_LU_NB = DistrictEnum.D_374.value
    YEN_KHANH_NB = DistrictEnum.D_375.value
    KIM_SON_NB = DistrictEnum.D_376.value
    YEN_MO_NB = DistrictEnum.D_377.value
    THANH_HOA_TH = DistrictEnum.D_380.value
    BIM_SON_TH = DistrictEnum.D_381.value
    SAM_SON_TH = DistrictEnum.D_382.value
    MUONG_LAT_TH = DistrictEnum.D_384.value
    QUAN_HOA_TH = DistrictEnum.D_385.value
    BA_THUOC_TH = DistrictEnum.D_386.value
    QUAN_SON_TH = DistrictEnum.D_387.value
    LANG_CHANH_TH = DistrictEnum.D_388.value
    NGOC_LAC_TH = DistrictEnum.D_389.value
    CAM_THUY_TH = DistrictEnum.D_390.value
    THACH_THANH_TH = DistrictEnum.D_391.value
    HA_TRUNG_TH = DistrictEnum.D_392.value
    VINH_LOC_TH = DistrictEnum.D_393.value
    YEN_DINH_TH = DistrictEnum.D_394.value
    THO_XUAN_TH = DistrictEnum.D_395.value
    THUONG_XUAN_TH = DistrictEnum.D_396.value
    TRIEU_SON_TH = DistrictEnum.D_397.value
    THIEU_HOA_TH = DistrictEnum.D_398.value
    HOANG_HOA_TH = DistrictEnum.D_399.value
    HAU_LOC_TH = DistrictEnum.D_400.value
    NGA_SON_TH = DistrictEnum.D_401.value
    NHU_XUAN_TH = DistrictEnum.D_402.value
    NHU_THANH_TH = DistrictEnum.D_403.value
    NONG_CONG_TH = DistrictEnum.D_404.value
    DONG_SON_TH = DistrictEnum.D_405.value
    QUANG_XUONG_TH = DistrictEnum.D_406.value
    TINH_GIA_TH = DistrictEnum.D_407.value
    VINH_NA = DistrictEnum.D_412.value
    CUA_LO_NA = DistrictEnum.D_413.value
    THAI_HOA_NA = DistrictEnum.D_414.value
    QUE_PHONG_NA = DistrictEnum.D_415.value
    QUY_CHAU_NA = DistrictEnum.D_416.value
    KY_SON_NA = DistrictEnum.D_417.value
    TUONG_DUONG_NA = DistrictEnum.D_418.value
    NGHIA_DAN_NA = DistrictEnum.D_419.value
    QUY_HOP_NA = DistrictEnum.D_420.value
    QUYNH_LUU_NA = DistrictEnum.D_421.value
    CON_CUONG_NA = DistrictEnum.D_422.value
    TAN_KY_NA = DistrictEnum.D_423.value
    ANH_SON_NA = DistrictEnum.D_424.value
    DIEN_CHAU_NA = DistrictEnum.D_425.value
    YEN_THANH_NA = DistrictEnum.D_426.value
    DO_LUONG_NA = DistrictEnum.D_427.value
    THANH_CHUONG_NA = DistrictEnum.D_428.value
    NGHI_LOC_NA = DistrictEnum.D_429.value
    NAM_DAN_NA = DistrictEnum.D_430.value
    HUNG_NGUYEN_NA = DistrictEnum.D_431.value
    HOANG_MAI_NA = DistrictEnum.D_432.value
    HA_TINH_HT = DistrictEnum.D_436.value
    HONG_LINH_HT = DistrictEnum.D_437.value
    HUONG_SON_HT = DistrictEnum.D_439.value
    DUC_THO_HT = DistrictEnum.D_440.value
    VU_QUANG_HT = DistrictEnum.D_441.value
    NGHI_XUAN_HT = DistrictEnum.D_442.value
    CAN_LOC_HT = DistrictEnum.D_443.value
    HUONG_KHE_HT = DistrictEnum.D_444.value
    THACH_HA_HT = DistrictEnum.D_445.value
    CAM_XUYEN_HT = DistrictEnum.D_446.value
    HUYEN_KY_ANH_HT = DistrictEnum.D_447.value
    LOC_HA_HT = DistrictEnum.D_448.value
    KY_ANH_HT = DistrictEnum.D_449.value
    DONG_HOI_QB = DistrictEnum.D_450.value
    MINH_HOA_QB = DistrictEnum.D_452.value
    TUYEN_HOA_QB = DistrictEnum.D_453.value
    QUANG_TRACH_QB = DistrictEnum.D_454.value
    BO_TRACH_QB = DistrictEnum.D_455.value
    QUANG_NINH_QB = DistrictEnum.D_456.value
    LE_THUY_QB = DistrictEnum.D_457.value
    BA_DON_QB = DistrictEnum.D_458.value
    DONG_HA_QT = DistrictEnum.D_461.value
    QUANG_TRI_QT = DistrictEnum.D_462.value
    VINH_LINH_QT = DistrictEnum.D_464.value
    HUONG_HOA_QT = DistrictEnum.D_465.value
    GIO_LINH_QT = DistrictEnum.D_466.value
    DA_KRONG_QT = DistrictEnum.D_467.value
    CAM_LO_QT = DistrictEnum.D_468.value
    TRIEU_PHONG_QT = DistrictEnum.D_469.value
    HAI_LANG_QT = DistrictEnum.D_470.value
    HUE_TTH = DistrictEnum.D_474.value
    PHONG_DIEN_TTH = DistrictEnum.D_476.value
    QUANG_DIEN_TTH = DistrictEnum.D_477.value
    PHU_VANG_TTH = DistrictEnum.D_478.value
    HUONG_THUY_TTH = DistrictEnum.D_479.value
    HUONG_TRA_TTH = DistrictEnum.D_480.value
    A_LUOI_TTH = DistrictEnum.D_481.value
    PHU_LOC_TTH = DistrictEnum.D_482.value
    NAM_DONG_TTH = DistrictEnum.D_483.value
    LIEN_CHIEU_DN = DistrictEnum.D_490.value
    THANH_KHE_DN = DistrictEnum.D_491.value
    HAI_CHAU_DN = DistrictEnum.D_492.value
    SON_TRA_DN = DistrictEnum.D_493.value
    NGU_HANH_SON_DN = DistrictEnum.D_494.value
    CAM_LE_DN = DistrictEnum.D_495.value
    HOA_VANG_DN = DistrictEnum.D_497.value
    TAM_KY_QN = DistrictEnum.D_502.value
    HOI_AN_QN = DistrictEnum.D_503.value
    TAY_GIANG_QN = DistrictEnum.D_504.value
    DONG_GIANG_QN = DistrictEnum.D_505.value
    DAI_LOC_QN = DistrictEnum.D_506.value
    DIEN_BAN_QN = DistrictEnum.D_507.value
    DUY_XUYEN_QN = DistrictEnum.D_508.value
    QUE_SON_QN = DistrictEnum.D_509.value
    NAM_GIANG_QN = DistrictEnum.D_510.value
    PHUOC_SON_QN = DistrictEnum.D_511.value
    HIEP_DUC_QN = DistrictEnum.D_512.value
    THANG_BINH_QN = DistrictEnum.D_513.value
    TIEN_PHUOC_QN = DistrictEnum.D_514.value
    BAC_TRA_MY_QN = DistrictEnum.D_515.value
    NAM_TRA_MY_QN = DistrictEnum.D_516.value
    NUI_THANH_QN = DistrictEnum.D_517.value
    PHU_NINH_QN = DistrictEnum.D_518.value
    NONG_SON_QN = DistrictEnum.D_519.value
    QUANG_NGAI_QN = DistrictEnum.D_522.value
    BINH_SON_QN = DistrictEnum.D_524.value
    TRA_BONG_QN = DistrictEnum.D_525.value
    TAY_TRA_QN = DistrictEnum.D_526.value
    SON_TINH_QN = DistrictEnum.D_527.value
    TU_NGHIA_QN = DistrictEnum.D_528.value
    SON_HA_QN = DistrictEnum.D_529.value
    SON_TAY_QN = DistrictEnum.D_530.value
    MINH_LONG_QN = DistrictEnum.D_531.value
    NGHIA_HANH_QN = DistrictEnum.D_532.value
    MO_DUC_QN = DistrictEnum.D_533.value
    DUC_PHO_QN = DistrictEnum.D_534.value
    BA_TO_QN = DistrictEnum.D_535.value
    LY_SON_QN = DistrictEnum.D_536.value
    QUI_NHON_BD = DistrictEnum.D_540.value
    AN_LAO_BD = DistrictEnum.D_542.value
    HOAI_NHON_BD = DistrictEnum.D_543.value
    HOAI_AN_BD = DistrictEnum.D_544.value
    PHU_MY_BD = DistrictEnum.D_545.value
    VINH_THANH_BD = DistrictEnum.D_546.value
    TAY_SON_BD = DistrictEnum.D_547.value
    PHU_CAT_BD = DistrictEnum.D_548.value
    AN_NHON_BD = DistrictEnum.D_549.value
    TUY_PHUOC_BD = DistrictEnum.D_550.value
    VAN_CANH_BD = DistrictEnum.D_551.value
    TUY_HOA_PY = DistrictEnum.D_555.value
    SONG_CAU_PY = DistrictEnum.D_557.value
    DONG_XUAN_PY = DistrictEnum.D_558.value
    TUY_AN_PY = DistrictEnum.D_559.value
    SON_HOA_PY = DistrictEnum.D_560.value
    SONG_HINH_PY = DistrictEnum.D_561.value
    TAY_HOA_PY = DistrictEnum.D_562.value
    PHU_HOA_PY = DistrictEnum.D_563.value
    DONG_HOA_PY = DistrictEnum.D_564.value
    NHA_TRANG_KH = DistrictEnum.D_568.value
    CAM_RANH_KH = DistrictEnum.D_569.value
    CAM_LAM_KH = DistrictEnum.D_570.value
    VAN_NINH_KH = DistrictEnum.D_571.value
    NINH_HOA_KH = DistrictEnum.D_572.value
    KHANH_VINH_KH = DistrictEnum.D_573.value
    DIEN_KHANH_KH = DistrictEnum.D_574.value
    KHANH_SON_KH = DistrictEnum.D_575.value
    TRUONG_SA_KH = DistrictEnum.D_576.value
    PHAN_RANG_THAP_CHAM_NT = DistrictEnum.D_582.value
    BAC_AI_NT = DistrictEnum.D_584.value
    NINH_SON_NT = DistrictEnum.D_585.value
    NINH_HAI_NT = DistrictEnum.D_586.value
    NINH_PHUOC_NT = DistrictEnum.D_587.value
    THUAN_BAC_NT = DistrictEnum.D_588.value
    THUAN_NAM_NT = DistrictEnum.D_589.value
    PHAN_THIET_BT = DistrictEnum.D_593.value
    LA_GI_BT = DistrictEnum.D_594.value
    TUY_PHONG_BT = DistrictEnum.D_595.value
    BAC_BINH_BT = DistrictEnum.D_596.value
    HAM_THUAN_BAC_BT = DistrictEnum.D_597.value
    HAM_THUAN_NAM_BT = DistrictEnum.D_598.value
    TANH_LINH_BT = DistrictEnum.D_599.value
    DUC_LINH_BT = DistrictEnum.D_600.value
    HAM_TAN_BT = DistrictEnum.D_601.value
    PHU_QUI_BT = DistrictEnum.D_602.value
    KON_TUM_KT = DistrictEnum.D_608.value
    DAK_GLEI_KT = DistrictEnum.D_610.value
    NGOC_HOI_KT = DistrictEnum.D_611.value
    DAK_TO_KT = DistrictEnum.D_612.value
    KON_PLONG_KT = DistrictEnum.D_613.value
    KON_RAY_KT = DistrictEnum.D_614.value
    DAK_HA_KT = DistrictEnum.D_615.value
    SA_THAY_KT = DistrictEnum.D_616.value
    TU_MO_RONG_KT = DistrictEnum.D_617.value
    IA_H_DRAI_KT = DistrictEnum.D_618.value
    PLEIKU_GL = DistrictEnum.D_622.value
    AN_KHE_GL = DistrictEnum.D_623.value
    AYUN_PA_GL = DistrictEnum.D_624.value
    KBANG_GL = DistrictEnum.D_625.value
    DAK_DOA_GL = DistrictEnum.D_626.value
    CHU_PAH_GL = DistrictEnum.D_627.value
    IA_GRAI_GL = DistrictEnum.D_628.value
    MANG_YANG_GL = DistrictEnum.D_629.value
    KONG_CHRO_GL = DistrictEnum.D_630.value
    DUC_CO_GL = DistrictEnum.D_631.value
    CHU_PRONG_GL = DistrictEnum.D_632.value
    CHU_SE_GL = DistrictEnum.D_633.value
    DAK_PO_GL = DistrictEnum.D_634.value
    IA_PA_GL = DistrictEnum.D_635.value
    KRONG_PA_GL = DistrictEnum.D_637.value
    PHU_THIEN_GL = DistrictEnum.D_638.value
    CHU_PUH_GL = DistrictEnum.D_639.value
    BUON_MA_THUOT_DL = DistrictEnum.D_643.value
    BUON_HO_DL = DistrictEnum.D_644.value
    EA_HLEO_DL = DistrictEnum.D_645.value
    EA_SUP_DL = DistrictEnum.D_646.value
    BUON_DON_DL = DistrictEnum.D_647.value
    CU_MGAR_DL = DistrictEnum.D_648.value
    KRONG_BUK_DL = DistrictEnum.D_649.value
    KRONG_NANG_DL = DistrictEnum.D_650.value
    EA_KAR_DL = DistrictEnum.D_651.value
    MDRAK_DL = DistrictEnum.D_652.value
    KRONG_BONG_DL = DistrictEnum.D_653.value
    KRONG_PAC_DL = DistrictEnum.D_654.value
    KRONG_A_NA_DL = DistrictEnum.D_655.value
    LAK_DL = DistrictEnum.D_656.value
    CU_KUIN_DL = DistrictEnum.D_657.value
    GIA_NGHIA_DN = DistrictEnum.D_660.value
    DAK_GLONG_DN = DistrictEnum.D_661.value
    CU_JUT_DN = DistrictEnum.D_662.value
    DAK_MIL_DN = DistrictEnum.D_663.value
    KRONG_NO_DN = DistrictEnum.D_664.value
    DAK_SONG_DN = DistrictEnum.D_665.value
    DAK_RLAP_DN = DistrictEnum.D_666.value
    TUY_DUC_DN = DistrictEnum.D_667.value
    DA_LAT_LD = DistrictEnum.D_672.value
    BAO_LOC_LD = DistrictEnum.D_673.value
    DAM_RONG_LD = DistrictEnum.D_674.value
    LAC_DUONG_LD = DistrictEnum.D_675.value
    LAM_HA_LD = DistrictEnum.D_676.value
    DON_DUONG_LD = DistrictEnum.D_677.value
    DUC_TRONG_LD = DistrictEnum.D_678.value
    DI_LINH_LD = DistrictEnum.D_679.value
    BAO_LAM_LD = DistrictEnum.D_680.value
    DA_HUOAI_LD = DistrictEnum.D_681.value
    DA_TEH_LD = DistrictEnum.D_682.value
    CAT_TIEN_LD = DistrictEnum.D_683.value
    PHUOC_LONG_BP = DistrictEnum.D_688.value
    DONG_XOAI_BP = DistrictEnum.D_689.value
    BINH_LONG_BP = DistrictEnum.D_690.value
    BU_GIA_MAP_BP = DistrictEnum.D_691.value
    LOC_NINH_BP = DistrictEnum.D_692.value
    BU_DOP_BP = DistrictEnum.D_693.value
    HON_QUAN_BP = DistrictEnum.D_694.value
    DONG_PHU_BP = DistrictEnum.D_695.value
    BU_DANG_BP = DistrictEnum.D_696.value
    CHON_THANH_BP = DistrictEnum.D_697.value
    PHU_RIENG_BP = DistrictEnum.D_698.value
    TAY_NINH_TN = DistrictEnum.D_703.value
    TAN_BIEN_TN = DistrictEnum.D_705.value
    TAN_CHAU_TN = DistrictEnum.D_706.value
    DUONG_MINH_CHAU_TN = DistrictEnum.D_707.value
    CHAU_THANH_TN = DistrictEnum.D_708.value
    HOA_THANH_TN = DistrictEnum.D_709.value
    GO_DAU_TN = DistrictEnum.D_710.value
    BEN_CAU_TN = DistrictEnum.D_711.value
    TRANG_BANG_TN = DistrictEnum.D_712.value
    THU_DAU_MOT_BD = DistrictEnum.D_718.value
    BAU_BANG_BD = DistrictEnum.D_719.value
    DAU_TIENG_BD = DistrictEnum.D_720.value
    BEN_CAT_BD = DistrictEnum.D_721.value
    PHU_GIAO_BD = DistrictEnum.D_722.value
    TAN_UYEN_BD = DistrictEnum.D_723.value
    DI_AN_BD = DistrictEnum.D_724.value
    THUAN_AN_BD = DistrictEnum.D_725.value
    BAC_TAN_UYEN_BD = DistrictEnum.D_726.value
    BIEN_HOA_DN = DistrictEnum.D_731.value
    LONG_KHANH_DN = DistrictEnum.D_732.value
    TAN_PHU_DN = DistrictEnum.D_734.value
    VINH_CUU_DN = DistrictEnum.D_735.value
    DINH_QUAN_DN = DistrictEnum.D_736.value
    TRANG_BOM_DN = DistrictEnum.D_737.value
    THONG_NHAT_DN = DistrictEnum.D_738.value
    CAM_MY_DN = DistrictEnum.D_739.value
    LONG_THANH_DN = DistrictEnum.D_740.value
    XUAN_LOC_DN = DistrictEnum.D_741.value
    NHON_TRACH_DN = DistrictEnum.D_742.value
    VUNG_TAU_BRVT = DistrictEnum.D_747.value
    BA_RIA_BRVT = DistrictEnum.D_748.value
    CHAU_DUC_BRVT = DistrictEnum.D_750.value
    XUYEN_MOC_BRVT = DistrictEnum.D_751.value
    LONG_DIEN_BRVT = DistrictEnum.D_752.value
    DAT_DO_BRVT = DistrictEnum.D_753.value
    PHU_MY_BRVT = DistrictEnum.D_754.value
    QUAN_1_HCM = DistrictEnum.D_760.value
    QUAN_12_HCM = DistrictEnum.D_761.value
    THU_DUC_HCM = DistrictEnum.D_762.value
    QUAN_9_HCM = DistrictEnum.D_763.value
    GO_VAP_HCM = DistrictEnum.D_764.value
    BINH_THANH_HCM = DistrictEnum.D_765.value
    TAN_BINH_HCM = DistrictEnum.D_766.value
    TAN_PHU_HCM = DistrictEnum.D_767.value
    PHU_NHUAN_HCM = DistrictEnum.D_768.value
    QUAN_2_HCM = DistrictEnum.D_769.value
    QUAN_3_HCM = DistrictEnum.D_770.value
    QUAN_10_HCM = DistrictEnum.D_771.value
    QUAN_11_HCM = DistrictEnum.D_772.value
    QUAN_4_HCM = DistrictEnum.D_773.value
    QUAN_5_HCM = DistrictEnum.D_774.value
    QUAN_6_HCM = DistrictEnum.D_775.value
    QUAN_8_HCM = DistrictEnum.D_776.value
    BINH_TAN_HCM = DistrictEnum.D_777.value
    QUAN_7_HCM = DistrictEnum.D_778.value
    CU_CHI_HCM = DistrictEnum.D_783.value
    HOC_MON_HCM = DistrictEnum.D_784.value
    BINH_CHANH_HCM = DistrictEnum.D_785.value
    NHA_BE_HCM = DistrictEnum.D_786.value
    CAN_GIO_HCM = DistrictEnum.D_787.value
    TAN_AN_LA = DistrictEnum.D_794.value
    KIEN_TUONG_LA = DistrictEnum.D_795.value
    TAN_HUNG_LA = DistrictEnum.D_796.value
    VINH_HUNG_LA = DistrictEnum.D_797.value
    MOC_HOA_LA = DistrictEnum.D_798.value
    TAN_THANH_LA = DistrictEnum.D_799.value
    THANH_HOA_LA = DistrictEnum.D_800.value
    DUC_HUE_LA = DistrictEnum.D_801.value
    DUC_HOA_LA = DistrictEnum.D_802.value
    BEN_LUC_LA = DistrictEnum.D_803.value
    THU_THUA_LA = DistrictEnum.D_804.value
    TAN_TRU_LA = DistrictEnum.D_805.value
    CAN_DUOC_LA = DistrictEnum.D_806.value
    CAN_GIUOC_LA = DistrictEnum.D_807.value
    CHAU_THANH_LA = DistrictEnum.D_808.value
    MY_THO_TG = DistrictEnum.D_815.value
    GO_CONG_TG = DistrictEnum.D_816.value
    CAI_LAY_TG = DistrictEnum.D_817.value
    TAN_PHUOC_TG = DistrictEnum.D_818.value
    CAI_BE_TG = DistrictEnum.D_819.value
    HUYEN_CAI_LAY_TG = DistrictEnum.D_820.value
    CHAU_THANH_TG = DistrictEnum.D_821.value
    CHO_GAO_TG = DistrictEnum.D_822.value
    GO_CONG_TAY_TG = DistrictEnum.D_823.value
    GO_CONG_DONG_TG = DistrictEnum.D_824.value
    TAN_PHU_DONG_TG = DistrictEnum.D_825.value
    BEN_TRE_BT = DistrictEnum.D_829.value
    CHAU_THANH_BT = DistrictEnum.D_831.value
    CHO_LACH_BT = DistrictEnum.D_832.value
    MO_CAY_NAM_BT = DistrictEnum.D_833.value
    GIONG_TROM_BT = DistrictEnum.D_834.value
    BINH_DAI_BT = DistrictEnum.D_835.value
    BA_TRI_BT = DistrictEnum.D_836.value
    THANH_PHU_BT = DistrictEnum.D_837.value
    MO_CAY_BAC_BT = DistrictEnum.D_838.value
    TRA_VINH_TV = DistrictEnum.D_842.value
    CANG_LONG_TV = DistrictEnum.D_844.value
    CAU_KE_TV = DistrictEnum.D_845.value
    TIEU_CAN_TV = DistrictEnum.D_846.value
    CHAU_THANH_TV = DistrictEnum.D_847.value
    CAU_NGANG_TV = DistrictEnum.D_848.value
    TRA_CU_TV = DistrictEnum.D_849.value
    HUYEN_DUYEN_HAI_TV = DistrictEnum.D_850.value
    DUYEN_HAI_TV = DistrictEnum.D_851.value
    VINH_LONG_VL = DistrictEnum.D_855.value
    LONG_HO_VL = DistrictEnum.D_857.value
    MANG_THIT_VL = DistrictEnum.D_858.value
    VUNG_LIEM_VL = DistrictEnum.D_859.value
    TAM_BINH_VL = DistrictEnum.D_860.value
    BINH_MINH_VL = DistrictEnum.D_861.value
    TRA_ON_VL = DistrictEnum.D_862.value
    BINH_TAN_VL = DistrictEnum.D_863.value
    CAO_LANH_DT = DistrictEnum.D_866.value
    SA_DEC_DT = DistrictEnum.D_867.value
    HONG_NGU_DT = DistrictEnum.D_868.value
    TAN_HONG_DT = DistrictEnum.D_869.value
    HUYEN_HONG_NGU_DT = DistrictEnum.D_870.value
    TAM_NONG_DT = DistrictEnum.D_871.value
    THAP_MUOI_DT = DistrictEnum.D_872.value
    HUYEN_CAO_LANH_DT = DistrictEnum.D_873.value
    THANH_BINH_DT = DistrictEnum.D_874.value
    LAP_VO_DT = DistrictEnum.D_875.value
    LAI_VUNG_DT = DistrictEnum.D_876.value
    CHAU_THANH_DT = DistrictEnum.D_877.value
    LONG_XUYEN_AG = DistrictEnum.D_883.value
    CHAU_DOC_AG = DistrictEnum.D_884.value
    AN_PHU_AG = DistrictEnum.D_886.value
    TAN_CHAU_AG = DistrictEnum.D_887.value
    PHU_TAN_AG = DistrictEnum.D_888.value
    CHAU_PHU_AG = DistrictEnum.D_889.value
    TINH_BIEN_AG = DistrictEnum.D_890.value
    TRI_TON_AG = DistrictEnum.D_891.value
    CHAU_THANH_AG = DistrictEnum.D_892.value
    CHO_MOI_AG = DistrictEnum.D_893.value
    THOAI_SON_AG = DistrictEnum.D_894.value
    RACH_GIA_KG = DistrictEnum.D_899.value
    HA_TIEN_KG = DistrictEnum.D_900.value
    KIEN_LUONG_KG = DistrictEnum.D_902.value
    HON_DAT_KG = DistrictEnum.D_903.value
    TAN_HIEP_KG = DistrictEnum.D_904.value
    CHAU_THANH_KG = DistrictEnum.D_905.value
    GIONG_RIENG_KG = DistrictEnum.D_906.value
    GO_QUAO_KG = DistrictEnum.D_907.value
    AN_BIEN_KG = DistrictEnum.D_908.value
    AN_MINH_KG = DistrictEnum.D_909.value
    VINH_THUAN_KG = DistrictEnum.D_910.value
    PHU_QUOC_KG = DistrictEnum.D_911.value
    KIEN_HAI_KG = DistrictEnum.D_912.value
    U_MINH_THUONG_KG = DistrictEnum.D_913.value
    GIANG_THANH_KG = DistrictEnum.D_914.value
    NINH_KIEU_CT = DistrictEnum.D_916.value
    O_MON_CT = DistrictEnum.D_917.value
    BINH_THUY_CT = DistrictEnum.D_918.value
    CAI_RANG_CT = DistrictEnum.D_919.value
    THOT_NOT_CT = DistrictEnum.D_923.value
    VINH_THANH_CT = DistrictEnum.D_924.value
    CO_DO_CT = DistrictEnum.D_925.value
    PHONG_DIEN_CT = DistrictEnum.D_926.value
    THOI_LAI_CT = DistrictEnum.D_927.value
    VI_THANH_HG = DistrictEnum.D_930.value
    NGA_BAY_HG = DistrictEnum.D_931.value
    CHAU_THANH_A_HG = DistrictEnum.D_932.value
    CHAU_THANH_HG = DistrictEnum.D_933.value
    PHUNG_HIEP_HG = DistrictEnum.D_934.value
    VI_THUY_HG = DistrictEnum.D_935.value
    HUYEN_LONG_MY_HG = DistrictEnum.D_936.value
    LONG_MY_HG = DistrictEnum.D_937.value
    SOC_TRANG_ST = DistrictEnum.D_941.value
    CHAU_THANH_ST = DistrictEnum.D_942.value
    KE_SACH_ST = DistrictEnum.D_943.value
    MY_TU_ST = DistrictEnum.D_944.value
    CU_LAO_DUNG_ST = DistrictEnum.D_945.value
    LONG_PHU_ST = DistrictEnum.D_946.value
    MY_XUYEN_ST = DistrictEnum.D_947.value
    NGA_NAM_ST = DistrictEnum.D_948.value
    THANH_TRI_ST = DistrictEnum.D_949.value
    VINH_CHAU_ST = DistrictEnum.D_950.value
    TRAN_DE_ST = DistrictEnum.D_951.value
    BAC_LIEU_BL = DistrictEnum.D_954.value
    HONG_DAN_BL = DistrictEnum.D_956.value
    PHUOC_LONG_BL = DistrictEnum.D_957.value
    VINH_LOI_BL = DistrictEnum.D_958.value
    GIA_RAI_BL = DistrictEnum.D_959.value
    DONG_HAI_BL = DistrictEnum.D_960.value
    HOA_BINH_BL = DistrictEnum.D_961.value
    CA_MAU_CM = DistrictEnum.D_964.value
    U_MINH_CM = DistrictEnum.D_966.value
    THOI_BINH_CM = DistrictEnum.D_967.value
    TRAN_VAN_THOI_CM = DistrictEnum.D_968.value
    CAI_NUOC_CM = DistrictEnum.D_969.value
    DAM_DOI_CM = DistrictEnum.D_970.value
    NAM_CAN_CM = DistrictEnum.D_971.value
    PHU_TAN_CM = DistrictEnum.D_972.value
    NGOC_HIEN_CM = DistrictEnum.D_973.value
