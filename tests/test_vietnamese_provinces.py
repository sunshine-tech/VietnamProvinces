from vietnam_provinces.base import Province, Ward


def test_province_enum():
    from vietnam_provinces.enums import ProvinceEnum, ProvinceDEnum

    assert isinstance(ProvinceEnum.P_11.value, Province)
    assert isinstance(ProvinceDEnum.DAK_LAK.value, Province)
    assert ProvinceEnum.P_86.value.name == 'Vĩnh Long'
    assert ProvinceDEnum.HO_CHI_MINH.value.name == 'Thành phố Hồ Chí Minh'
    assert ProvinceDEnum.HA_NOI.value.name == 'Thành phố Hà Nội'
    assert ProvinceDEnum.KHANH_HOA.value.phone_code == 258
    assert ProvinceDEnum.DAK_LAK.value.name == 'Đắk Lắk'


def test_importable_ward_enum():
    from vietnam_provinces.enums.wards import WardDEnum

    assert isinstance(WardDEnum.HN_HOAN_KIEM.value, Ward)
    assert WardDEnum.HN_HA_DONG.value.name == 'Phường Hà Đông'
    assert WardDEnum.HN_CHUONG_MY.value.name == 'Phường Chương Mỹ'
