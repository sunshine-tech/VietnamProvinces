from .base import Province, VietNamDivisionType, Ward


PROVINCE_MAPPING = {1: Province('Thành phố Hà Nội', 1, VietNamDivisionType.TINH, 'ha_noi', 24)}

WARD_MAPPING = {4: Ward('Phường Ba Đình', 4, VietNamDivisionType.XA, 'phuong_ba_dinh', 1)}
