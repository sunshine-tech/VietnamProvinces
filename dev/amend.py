# Fix data per report from https://github.com/hongquan/vn-open-api-provinces/issues/8

from .divisions import WardCSVRecord


def fix_ward(ward: WardCSVRecord) -> WardCSVRecord:
    match ward.code:
        case 29857:
            ward.name = 'Xã Lục Sĩ Thành'
        case 6187:
            # Phường Hoàng Văn Thụ -> Phường Kỳ Lừa
            ward.name = 'Phường Kỳ Lừa'
        case 6172:
            # Xã Tân Thanh -> Xã Hoàng Văn Thụ
            ward.name = 'Xã Hoàng Văn Thụ'
        case 16609:
            ward.name = 'Phường Đào Duy Từ'
        case 23954:
            ward.name = 'Xã Al Bá'
        case _:
            pass
    return ward
