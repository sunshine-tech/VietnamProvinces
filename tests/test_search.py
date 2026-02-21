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

    # The first result should be one with the expected_first old name
    old_names = [w.name for w in results[0].get_legacy_sources()]
    assert expected_first in old_names, (
        f"First result should have old name '{expected_first}', but got ward with old names {old_names}"
    )


@pytest.mark.parametrize(
    ('legacy_code', 'expected_ward_name'),
    [
        (26707, 'Phường Tân Hải'),  # Phường Tân Hòa (legacy) -> Phường Tân Hải (new)
        (
            22768,
            'Phường Đông Hải',
        ),  # Phường Đông Hải (legacy, Phan Rang-Tháp Chàm) -> partly merged into new Phường Đông Hải
        (26731, 'Xã Châu Pha'),  # Xã Tóc Tiên (legacy, Phú Mỹ) -> Xã Châu Pha (new)
        (26725, 'Phường Tân Thành'),  # Phường Hắc Dịch (legacy, Phú Mỹ) -> Phường Tân Thành (new)
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
    ('legacy_name', 'expected_ward_name'),
    [
        ('toc tien', 'Xã Châu Pha'),  # Xã Tóc Tiên (legacy) -> Xã Châu Pha (new)
        ('Tóc Tiên', 'Xã Châu Pha'),  # Search with diacritics
        ('hac dich', 'Phường Tân Thành'),  # Phường Hắc Dịch (legacy) -> Phường Tân Thành (new)
        ('Hắc Dịch', 'Phường Tân Thành'),  # Search with diacritics
        ("D'Ran", 'Xã D’Ran'),  # D'Ran with straight apostrophe
        ('dran', 'Xã D’Ran'),  # dran without apostrophe
    ],
)
def test_search_from_legacy_by_name_specific_wards(legacy_name: str, expected_ward_name: str) -> None:
    """Test that search_from_legacy returns correct ward when searching by specific legacy ward names."""
    results = Ward.search_from_legacy(name=legacy_name)

    # Should return results
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
    ('ward_code', 'expected_codes'),
    [
        (4, {4, 13, 16, 19, 22, 28, 40, 55, 73, 112}),  # Phường Ba Đình - merged from multiple wards
        (22861, {22855, 22858, 22861}),  # Merged from Xã Tân Hải and others
        (23246, {23245, 23246}),  # Another ward
    ],
)
def test_get_legacy_sources_has_correct_codes(ward_code: int, expected_codes: set[int]) -> None:
    """Test that get_legacy_sources returns wards with correct codes."""
    ward = Ward.from_code(WardCode(ward_code))
    legacy_sources = ward.get_legacy_sources()

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
    ('province_code', 'expected_codes'),
    [
        (79, {74, 77, 79}),  # Thành phố Hồ Chí Minh - merged from multiple provinces
        (8, {2, 8}),  # Tỉnh Tuyên Quang - merged from Tỉnh Hà Giang and Tỉnh Tuyên Quang
        (66, {54, 66}),  # Tỉnh Đắk Lắk - merged from Tỉnh Phú Yên and Tỉnh Đắk Lắk
    ],
)
def test_province_get_legacy_sources_has_correct_codes(province_code: int, expected_codes: set[int]) -> None:
    """Test that Province.get_legacy_sources returns provinces with correct codes."""
    province = Province.from_code(ProvinceCode(province_code))
    legacy_sources = province.get_legacy_sources()

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


# District tests


@pytest.mark.parametrize(
    ('legacy_district_code', 'expected_ward_names'),
    [
        (748, ['Phường Bà Rịa', 'Phường Long Hương', 'Phường Tam Long']),  # Thành phố Bà Rịa
    ],
)
def test_search_from_legacy_district_by_code(legacy_district_code: int, expected_ward_names: list[str]) -> None:
    """Test that search_from_legacy_district returns correct wards when searching by legacy district code."""
    results = Ward.search_from_legacy_district(code=legacy_district_code)

    # Should return results
    assert len(results) > 0

    # Check that expected ward names are in the results
    result_names = {w.name for w in results}
    for expected_name in expected_ward_names:
        assert expected_name in result_names


@pytest.mark.parametrize(
    ('legacy_district_name', 'expected_ward_name'),
    [
        ('ba ria', 'Phường Bà Rịa'),  # Thành phố Bà Rịa (without diacritics)
        ('Bà Rịa', 'Phường Bà Rịa'),  # Search with diacritics
    ],
)
def test_search_from_legacy_district_by_name(legacy_district_name: str, expected_ward_name: str) -> None:
    """Test that search_from_legacy_district returns correct wards when searching by legacy district name."""
    results = Ward.search_from_legacy_district(name=legacy_district_name)

    # Should return results
    assert len(results) > 0

    # Check that expected ward name is in the results
    result_names = {w.name for w in results}
    assert expected_ward_name in result_names


def test_search_from_legacy_district_empty_query() -> None:
    """Test that search_from_legacy_district returns empty tuple for empty query."""
    results = Ward.search_from_legacy_district()
    assert results == ()


def test_search_from_legacy_district_invalid_code() -> None:
    """Test that search_from_legacy_district returns empty tuple for invalid district code."""
    results = Ward.search_from_legacy_district(code=99999)
    assert results == ()
