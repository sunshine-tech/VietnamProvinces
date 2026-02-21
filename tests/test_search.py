import pytest

from vietnam_provinces import Province, Ward
from vietnam_provinces.codes import ProvinceCode, WardCode


@pytest.mark.parametrize(
    ('query', 'expected_first'),
    [
        ('phú mỹ', 'Thị trấn Phú Mỹ'),
        ('Phú Mỹ', 'Thị trấn Phú Mỹ'),
        ('phường phú mỹ', 'Phường Phú Mỹ'),
    ],
)
def test_search_from_legacy_by_name_prioritizes_diacritics_match(query: str, expected_first: str) -> None:
    """Test that search results prioritize exact diacritics matches."""
    results = Ward.search_from_legacy(query)

    # Should return results
    assert len(results) > 0

    # Get the old ward names for verification from legacy dataclass
    from vietnam_provinces._ward_conversion_2025 import OLD_TO_NEW
    from vietnam_provinces.legacy import Ward as LegacyWard
    from vietnam_provinces.legacy.codes import WardCode as LegacyWardCode

    # Find wards with expected_first in their old names
    expected_first_codes = set()

    for old_code, entry in OLD_TO_NEW.items():
        try:
            legacy_ward = LegacyWard.from_code(LegacyWardCode(old_code))
            if legacy_ward.name == expected_first:
                expected_first_codes.update(w.code for w in entry.new_wards)
        except (ValueError, KeyError):
            continue

    # The first result should be one with the expected_first old name
    if expected_first_codes:
        assert results[0].code in expected_first_codes, (
            f"First result should have old name '{expected_first}', but got ward with code {results[0].code}"
        )


@pytest.mark.parametrize(
    ('legacy_code', 'expected_ward_name'),
    [
        (26707, 'Phường Tân Hải'),  # Phường Tân Hòa (legacy) -> Phường Tân Hải (new)
        (
            22768,
            'Phường Đông Hải',
        ),  # Phường Đông Hải (legacy, Phan Rang-Tháp Chàm) -> partly merged into new Phường Đông Hải
    ],
)
def test_search_from_legacy_by_code(legacy_code: int, expected_ward_name: str) -> None:
    """Test that search_from_legacy returns correct ward when searching by legacy code."""
    results = Ward.search_from_legacy(code=legacy_code)

    # Should return results (may be multiple if partly merged)
    assert len(results) > 0

    # The first result should have the expected name
    assert results[0].name == expected_ward_name


@pytest.mark.parametrize(
    ('ward_code', 'expected_old_ward_name'),
    [
        (4, 'Phường Trúc Bạch'),  # Phường Ba Đình - merged from multiple wards
        (22861, 'Xã Tân Hải'),  # Merged from Xã Tân Hải
    ],
)
def test_get_legacy_sources_returns_legacy_wards(ward_code: int, expected_old_ward_name: str) -> None:
    """Test that get_legacy_sources returns legacy wards for a merged ward."""
    ward = Ward.from_code(WardCode(ward_code))
    legacy_sources = ward.get_legacy_sources()

    # Should have legacy sources
    assert len(legacy_sources) > 0

    # Check that all returned items are legacy Ward objects
    from vietnam_provinces.legacy import Ward as LegacyWard

    for lw in legacy_sources:
        assert isinstance(lw, LegacyWard)

    # Check that expected old ward name is in the legacy sources
    old_names = {lw.name for lw in legacy_sources}
    assert expected_old_ward_name in old_names


@pytest.mark.parametrize(
    'ward_code',
    [
        4,  # Phường Ba Đình - merged from multiple wards
        22861,  # Merged from Xã Tân Hải
        23246,  # Another ward merged from Xã Tân Hải
    ],
)
def test_get_legacy_sources_has_correct_codes(ward_code: int) -> None:
    """Test that get_legacy_sources returns wards with correct codes."""
    from vietnam_provinces._ward_conversion_2025 import NEW_TO_OLD

    ward = Ward.from_code(WardCode(ward_code))
    legacy_sources = ward.get_legacy_sources()

    # Get expected old ward codes from conversion table
    entry = NEW_TO_OLD.get(ward_code)
    assert entry is not None
    expected_codes = {ow.code for ow in entry.old_wards}

    # Verify all legacy sources have the expected codes
    actual_codes = {lw.code.value for lw in legacy_sources}
    assert actual_codes == expected_codes


@pytest.mark.parametrize(
    'ward_code',
    [
        4,  # Phường Ba Đình
        22861,  # Merged from Xã Tân Hải
    ],
)
def test_get_legacy_sources_returns_tuple(ward_code: int) -> None:
    """Test that get_legacy_sources returns a tuple."""
    ward = Ward.from_code(WardCode(ward_code))
    legacy_sources = ward.get_legacy_sources()

    # Should return a tuple (not None, not list)
    assert isinstance(legacy_sources, tuple)


# Province tests


@pytest.mark.parametrize(
    ('legacy_code', 'expected_province_name'),
    [
        (77, 'Thành phố Hồ Chí Minh'),  # Tỉnh Bà Rịa - Vũng Tàu (legacy) -> Thành phố Hồ Chí Minh (new)
        (2, 'Tỉnh Tuyên Quang'),  # Tỉnh Hà Giang (legacy) -> merged into Tỉnh Tuyên Quang (new)
        (54, 'Tỉnh Đắk Lắk'),  # Tỉnh Phú Yên (legacy) -> merged into Tỉnh Đắk Lắk (new)
    ],
)
def test_province_search_from_legacy_by_code(legacy_code: int, expected_province_name: str) -> None:
    """Test that Province.search_from_legacy returns correct province when searching by legacy code."""
    results = Province.search_from_legacy(code=legacy_code)

    # Should return exactly one result for this case
    assert len(results) == 1

    # The result should have the expected name
    assert results[0].name == expected_province_name


@pytest.mark.parametrize(
    ('legacy_name', 'expected_province_name'),
    [
        ('ha giang', 'Tỉnh Tuyên Quang'),  # Tỉnh Hà Giang (legacy) -> merged into Tỉnh Tuyên Quang
        ('Hà Giang', 'Tỉnh Tuyên Quang'),  # Search with diacritics
        ('phu yen', 'Tỉnh Đắk Lắk'),  # Tỉnh Phú Yên (legacy) -> merged into Tỉnh Đắk Lắk
        ('Phú Yên', 'Tỉnh Đắk Lắk'),  # Search with diacritics
    ],
)
def test_province_search_from_legacy_by_name(legacy_name: str, expected_province_name: str) -> None:
    """Test that Province.search_from_legacy returns correct province when searching by legacy name."""
    results = Province.search_from_legacy(name=legacy_name)

    # Should return results
    assert len(results) > 0

    # The first result should be the expected province
    assert results[0].name == expected_province_name


@pytest.mark.parametrize(
    ('province_code', 'expected_old_province_name'),
    [
        (
            79,
            'Tỉnh Bà Rịa - Vũng Tàu',
        ),  # Thành phố Hồ Chí Minh - merged from multiple provinces including Bà Rịa - Vũng Tàu
        (8, 'Tỉnh Hà Giang'),  # Tỉnh Tuyên Quang - merged from Tỉnh Hà Giang and Tỉnh Tuyên Quang
        (66, 'Tỉnh Phú Yên'),  # Tỉnh Đắk Lắk - merged from Tỉnh Phú Yên and Tỉnh Đắk Lắk
    ],
)
def test_province_get_legacy_sources_returns_legacy_provinces(
    province_code: int, expected_old_province_name: str
) -> None:
    """Test that Province.get_legacy_sources returns legacy provinces for a merged province."""
    province = Province.from_code(ProvinceCode(province_code))
    legacy_sources = province.get_legacy_sources()

    # Should have legacy sources
    assert len(legacy_sources) > 0

    # Check that all returned items are legacy Province objects
    from vietnam_provinces.legacy import Province as LegacyProvince

    for lp in legacy_sources:
        assert isinstance(lp, LegacyProvince)

    # Check that expected old province name is in the legacy sources
    old_names = {lp.name for lp in legacy_sources}
    assert expected_old_province_name in old_names


@pytest.mark.parametrize(
    'province_code',
    [
        79,  # Thành phố Hồ Chí Minh - merged from multiple provinces
        8,  # Tỉnh Tuyên Quang - merged from Tỉnh Hà Giang and Tỉnh Tuyên Quang
        66,  # Tỉnh Đắk Lắk - merged from Tỉnh Phú Yên and Tỉnh Đắk Lắk
    ],
)
def test_province_get_legacy_sources_has_correct_codes(province_code: int) -> None:
    """Test that Province.get_legacy_sources returns provinces with correct codes."""
    from vietnam_provinces._province_conversion_2025 import NEW_TO_OLD

    province = Province.from_code(ProvinceCode(province_code))
    legacy_sources = province.get_legacy_sources()

    # Get expected old province codes from conversion table
    entry = NEW_TO_OLD.get(province_code)
    assert entry is not None
    expected_codes = {op.code for op in entry.old_provinces}

    # Verify all legacy sources have the expected codes
    actual_codes = {lp.code.value for lp in legacy_sources}
    assert actual_codes == expected_codes


@pytest.mark.parametrize(
    'province_code',
    [
        79,  # Thành phố Hồ Chí Minh
        8,  # Tỉnh Tuyên Quang
        66,  # Tỉnh Đắk Lắk
    ],
)
def test_province_get_legacy_sources_returns_tuple(province_code: int) -> None:
    """Test that Province.get_legacy_sources returns a tuple."""
    province = Province.from_code(ProvinceCode(province_code))
    legacy_sources = province.get_legacy_sources()

    # Should return a tuple (not None, not list)
    assert isinstance(legacy_sources, tuple)
