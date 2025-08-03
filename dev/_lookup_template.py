from .base import Province, VietNamDivisionType, Ward, ProvinceCode, WardCode


PROVINCE_MAPPING = {1: Province('Thành phố Hà Nội', ProvinceCode.P_01, VietNamDivisionType.TINH, 'ha_noi', 24)}

WARD_MAPPING = {
    4: Ward('Phường Ba Đình', WardCode.W_00004, VietNamDivisionType.XA, 'phuong_ba_dinh', ProvinceCode.P_01)
}
