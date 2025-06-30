from vietnam_provinces.base import Province, District, Ward


def test_province_enum():
    from vietnam_provinces.enums.districts import ProvinceEnum, ProvinceDEnum

    assert isinstance(ProvinceEnum.P_11.value, Province)
    assert isinstance(ProvinceDEnum.KON_TUM.value, Province)
    assert ProvinceEnum.P_83.value.name == 'Tỉnh Bến Tre'
    assert ProvinceDEnum.HO_CHI_MINH.value.name == 'Thành phố Hồ Chí Minh'
    assert ProvinceDEnum.HA_NOI.value.name == 'Thành phố Hà Nội'
    assert ProvinceDEnum.PHU_YEN.value.phone_code == 257
    assert ProvinceDEnum.DAK_LAK.value.name == 'Tỉnh Đắk Lắk'


def test_district_enum():
    from vietnam_provinces.enums.districts import DistrictEnum, DistrictDEnum

    assert isinstance(DistrictEnum.D_672.value, District)
    assert isinstance(DistrictDEnum.PHAN_RANG_THAP_CHAM_NT.value, District)
    assert DistrictEnum.D_234.value.name == 'Huyện Yên Lập'
    assert DistrictEnum.D_234.value.province_code == 25
    assert DistrictDEnum.LAK_DL.value.name == 'Huyện Lắk'


def test_importable_ward_enum():
    from vietnam_provinces.enums.wards import WardDEnum

    assert isinstance(WardDEnum.AG_LAC_QUOI_30550.value, Ward)
    assert WardDEnum.GL_CHROH_PONAN_24060.value.name == 'Xã Chrôh Pơnan'
    assert WardDEnum.DL_EA_HMLAY_24424.value.name == "Xã Ea H'MLay"
