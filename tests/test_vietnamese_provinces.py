from vietnam_provinces.base import Province, Ward


def test_province_enum():
    from vietnam_provinces.enums.districts import ProvinceEnum
    assert isinstance(ProvinceEnum.KON_TUM.value, Province)
    assert ProvinceEnum.BEN_TRE.value.name == 'Tỉnh Bến Tre'
    assert ProvinceEnum.HO_CHI_MINH.value.name == 'Thành phố Hồ Chí Minh'
    assert ProvinceEnum.HA_NOI.value.name == 'Thành phố Hà Nội'
    assert ProvinceEnum.PHU_YEN.value.phone_code == 257


def test_importable_ward_enum():
    from vietnam_provinces.enums.wards import WardEnum
    assert isinstance(WardEnum.AG_LAC_QUOI_30550.value, Ward)
    assert WardEnum.GL_CHROH_PONAN_24060.value.name == 'Xã Chrôh Pơnan'
