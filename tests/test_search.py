import pytest

from vietnam_provinces import Province, Ward
from vietnam_provinces.codes import ProvinceCode, WardCode
from vietnam_provinces.helpers import normalize_search_name
from vietnam_provinces.legacy import District as LegacyDistrict
from vietnam_provinces.legacy import Province as LegacyProvince
from vietnam_provinces.legacy import Ward as LegacyWard


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
        (4, 'Phường Ba Đình'),  # Legacy ward -> Phường Ba Đình (new)
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
        ("D'Ran", "Xã D'Ran"),  # D'Ran with straight apostrophe
        ('dran', "Xã D'Ran"),  # dran without apostrophe
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
        (859, 'Xã Ngọc Long'),  # Merged from Xã Ngọc Long (single source)
    ],
)
def test_get_legacy_sources_returns_legacy_wards(ward_code: int, expected_old_ward_name: str) -> None:
    """Test that get_legacy_sources returns legacy wards for a merged ward."""
    ward = Ward.from_code(WardCode(ward_code))
    legacy_sources = ward.get_legacy_sources()

    # Should have legacy sources
    assert len(legacy_sources) > 0

    # Check that all returned items are legacy Ward objects

    for lw in legacy_sources:
        assert isinstance(lw, LegacyWard)

    # Check that expected old ward name is in the legacy sources
    old_names = {lw.name for lw in legacy_sources}
    assert expected_old_ward_name in old_names


@pytest.mark.parametrize(
    ('ward_code', 'expected_codes'),
    [
        (4, {4, 13, 16, 19, 22, 28, 40, 55, 73, 112}),  # Phường Ba Đình - merged from multiple wards
        (859, {859}),  # Merged from Xã Ngọc Long (single source)
        (919, {919}),  # Another ward with single source
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
        859,  # Xã Ngọc Long (single source)
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


class TestPhanRangThapCham:
    """Test cases for Phan Rang - Tháp Chàm (old city dissolved to wards in 2025)."""

    def test_legacy_district_search_phan_rang_thap_cham(self) -> None:
        """Test searching for the old Phan Rang-Tháp Chàm city."""

        results = LegacyDistrict.search('phan rang')

        # Should find Thành phố Phan Rang - Tháp Chàm (with spaces around hyphen)
        assert len(results) > 0
        result_names = {d.name for d in results}
        assert 'Thành phố Phan Rang - Tháp Chàm' in result_names

    def test_legacy_district_search_phan_rang_with_hyphen(self) -> None:
        """Test searching for Phan Rang with hyphenated name."""

        # The hyphen should be normalized to " - " (space hyphen space)
        results = LegacyDistrict.search('phan rang thap cham')

        # Should find Thành phố Phan Rang - Tháp Chàm (with spaces around hyphen)
        assert len(results) > 0
        result_names = {d.name for d in results}
        assert 'Thành phố Phan Rang - Tháp Chàm' in result_names

    def test_search_from_legacy_district_by_code_phan_rang(self) -> None:
        """Test finding new wards from old Phan Rang-Tháp Chàm by district code."""
        # District code 582 was Thành phố Phan Rang-Tháp Chàm
        results = Ward.search_from_legacy_district(code=582)

        # Should return 6 new wards
        assert len(results) == 6

        # Check expected ward names
        result_names = {w.name for w in results}
        expected_names = {
            'Phường Đô Vinh',
            'Phường Bảo An',
            'Phường Phan Rang',
            'Phường Đông Hải',
            'Phường Ninh Chử',
            'Xã Phước Dinh',
        }
        assert result_names == expected_names

    def test_search_from_legacy_district_by_name_phan_rang(self) -> None:
        """Test finding new wards from old Phan Rang-Tháp Chàm by district name."""
        results = Ward.search_from_legacy_district(name='phan rang')

        # Should return 6 new wards
        assert len(results) == 6

        # Check expected ward names
        result_names = {w.name for w in results}
        expected_names = {
            'Phường Đô Vinh',
            'Phường Bảo An',
            'Phường Phan Rang',
            'Phường Đông Hải',
            'Phường Ninh Chử',
            'Xã Phước Dinh',
        }
        assert result_names == expected_names

    def test_search_from_legacy_district_phan_rang_with_diacritics(self) -> None:
        """Test finding new wards from old Phan Rang-Tháp Chàm with diacritics."""
        # Search with diacritics but without hyphen
        results = Ward.search_from_legacy_district(name='Phan Rang')

        # Should return 6 new wards
        assert len(results) == 6

        # Check that Phường Phan Rang is in results
        result_names = {w.name for w in results}
        assert 'Phường Phan Rang' in result_names


# Ward.search() tests


def test_ward_search_empty_query() -> None:
    """Test that Ward.search returns empty tuple for empty query."""
    results = Ward.search('')
    assert results == ()


def test_ward_search_single_word() -> None:
    """Test Ward.search with a single word query."""
    results = Ward.search('phú mỹ')

    # Should return results
    assert len(results) > 0

    # All results should contain the query words (normalized comparison)
    # Normalized form of 'phú mỹ' is 'phu my'

    for ward in results:
        normalized_name = normalize_search_name(ward.name)
        assert 'phu' in normalized_name
        assert 'my' in normalized_name


@pytest.mark.parametrize(
    ('query', 'expected_ward_name'),
    [
        ('phú mỹ', 'Xã Phú Mỹ'),  # Exact match with diacritics
        ('Phú Mỹ', 'Xã Phú Mỹ'),  # Case insensitive with diacritics
        ('phu my', 'Xã Phú Mỹ'),  # Without diacritics
        ('Phu My', 'Xã Phú Mỹ'),  # Case insensitive without diacritics
    ],
)
def test_ward_search_prioritizes_diacritics_match(query: str, expected_ward_name: str) -> None:
    """Test that Ward.search prioritizes exact diacritics matches."""
    results = Ward.search(query)

    # Should return results
    assert len(results) > 0

    # The first result should be the expected ward
    assert results[0].name == expected_ward_name


@pytest.mark.parametrize(
    ('query', 'expected_in_results'),
    [
        ('tan hai', ['Xã Tân Hải', 'Phường Tân Hải']),  # Multi-word without diacritics
        ('Tân Hải', ['Xã Tân Hải', 'Phường Tân Hải']),  # Multi-word with diacritics
        ('phuong tan hai', ['Phường Tân Hải']),  # With division type prefix
        ('xa tan hai', ['Xã Tân Hải']),  # With division type prefix
    ],
)
def test_ward_search_multi_word(query: str, expected_in_results: list[str]) -> None:
    """Test Ward.search with multi-word queries."""
    results = Ward.search(query)

    # Should return results
    assert len(results) > 0

    # Check that expected wards are in results
    result_names = {w.name for w in results}
    for expected_name in expected_in_results:
        assert expected_name in result_names, f"Expected '{expected_name}' in results, got {result_names}"


def test_ward_search_multi_word_requires_all_words() -> None:
    """Test that Ward.search requires all words to match for multi-word queries."""
    # Search for "phu my" - both words must be present
    results = Ward.search('phu my')

    # Should return results
    assert len(results) > 0

    # All results should contain both "phu" and "my" as whole words in normalized form

    for ward in results:
        normalized_name = normalize_search_name(ward.name)
        name_words = set(normalized_name.split())
        assert 'phu' in name_words, f"Expected 'phu' as whole word in '{name_words}' for ward '{ward.name}'"
        assert 'my' in name_words, f"Expected 'my' as whole word in '{name_words}' for ward '{ward.name}'"


def test_ward_search_whole_word_matching() -> None:
    """Test that Ward.search matches whole words only, not substrings."""
    # Search for "phu my" - should NOT match "phuoc" (which contains "phu" as substring)
    results = Ward.search('phu my')

    result_names = {w.name for w in results}

    # These should NOT be in results because "phuoc" != "phu"
    assert 'Xã Phước Mỹ Trung' not in result_names, "'phuoc' should not match 'phu'"
    assert 'Phường Mỹ Phước Tây' not in result_names, "'phuoc' should not match 'phu'"


def test_ward_search_with_apostrophe() -> None:
    """Test Ward.search with apostrophe in query."""
    results = Ward.search("D'Ran")

    # Should return results
    assert len(results) > 0

    # Should find Xã D'Ran (with straight apostrophe)
    result_names = {w.name for w in results}
    assert "Xã D'Ran" in result_names  # Straight apostrophe (U+0027)


def test_ward_search_returns_tuple() -> None:
    """Test that Ward.search returns a tuple."""
    results = Ward.search('phu my')

    # Should return a tuple (not None, not list)
    assert isinstance(results, tuple)


def test_ward_search_no_results() -> None:
    """Test Ward.search with a query that returns no results."""
    results = Ward.search('xyz123nonexistent')

    # Should return empty tuple
    assert results == ()


def test_ward_search_results_sorted_by_match_score() -> None:
    """Test that Ward.search results are sorted by match score (best matches first)."""
    results = Ward.search('phu my')

    # Should return multiple results
    assert len(results) > 1

    # Exact matches should come before partial matches
    # The first result should be an exact or close match
    first_result = results[0]
    normalized_first = first_result.name.lower().replace('xã ', '').replace('phường ', '')

    # First result should start with "phú mỹ" or be very close
    assert normalized_first.startswith('phú mỹ') or normalized_first.startswith('phu my')


# Legacy classes tests


class TestLegacyProvinceSearch:
    """Test cases for legacy Province.search()"""

    def test_legacy_province_search_empty_query(self) -> None:
        """Test that legacy Province.search returns empty tuple for empty query."""

        results = LegacyProvince.search('')
        assert results == ()

    def test_legacy_province_search_single_word(self) -> None:
        """Test legacy Province.search with a single word query."""

        results = LegacyProvince.search('hà giang')

        # Should return results
        assert len(results) > 0

        # First result should be Tỉnh Hà Giang
        assert results[0].name == 'Tỉnh Hà Giang'

    def test_legacy_province_search_multi_word(self) -> None:
        """Test legacy Province.search with multi-word queries."""

        results = LegacyProvince.search('ho chi minh')

        # Should return results
        assert len(results) > 0

        # Should find Thành phố Hồ Chí Minh
        result_names = {p.name for p in results}
        assert 'Thành phố Hồ Chí Minh' in result_names

    def test_legacy_province_search_with_division_type_prefix(self) -> None:
        """Test legacy Province.search with division type prefix."""

        results = LegacyProvince.search('tinh ha giang')

        # Should return results (division type prefix should be filtered)
        assert len(results) > 0

        # Should find Tỉnh Hà Giang
        result_names = {p.name for p in results}
        assert 'Tỉnh Hà Giang' in result_names

    def test_legacy_province_search_whole_word_matching(self) -> None:
        """Test that legacy Province.search matches whole words only."""

        # Search for a term that could match substrings
        results = LegacyProvince.search('ha')

        # Should match Tỉnh Hà Giang (whole word "ha")
        result_names = {p.name for p in results}
        assert 'Tỉnh Hà Giang' in result_names

    def test_legacy_province_search_returns_tuple(self) -> None:
        """Test that legacy Province.search returns a tuple."""

        results = LegacyProvince.search('ha noi')
        assert isinstance(results, tuple)


class TestLegacyDistrictSearch:
    """Test cases for legacy District.search()"""

    def test_legacy_district_search_empty_query(self) -> None:
        """Test that legacy District.search returns empty tuple for empty query."""

        results = LegacyDistrict.search('')
        assert results == ()

    def test_legacy_district_search_single_word(self) -> None:
        """Test legacy District.search with a single word query."""

        results = LegacyDistrict.search('ba ria')

        # Should return results
        assert len(results) > 0

        # Should find Thành phố Bà Rịa
        result_names = {d.name for d in results}
        assert 'Thành phố Bà Rịa' in result_names

    def test_legacy_district_search_multi_word(self) -> None:
        """Test legacy District.search with multi-word queries."""

        results = LegacyDistrict.search('ba ria')

        # Should return results
        assert len(results) > 0

        # Should find Thành phố Bà Rịa
        result_names = {d.name for d in results}
        assert 'Thành phố Bà Rịa' in result_names

    def test_legacy_district_search_hyphenated_name(self) -> None:
        """Test legacy District.search with hyphenated names (data entry fix)."""

        # "Phan Rang-Tháp Chàm" should be searchable as "phan rang"
        # The hyphen is normalized to " - " (space hyphen space)
        results = LegacyDistrict.search('phan rang')

        # Should return results
        assert len(results) > 0

        # Should find Thành phố Phan Rang - Tháp Chàm (with spaces around hyphen)
        result_names = {d.name for d in results}
        assert 'Thành phố Phan Rang - Tháp Chàm' in result_names

    def test_legacy_district_search_with_division_type_prefix(self) -> None:
        """Test legacy District.search with division type prefix."""

        results = LegacyDistrict.search('thanh pho ba ria')

        # Should return results (division type prefix should be filtered)
        assert len(results) > 0

        # Should find Thành phố Bà Rịa
        result_names = {d.name for d in results}
        assert 'Thành phố Bà Rịa' in result_names

    def test_legacy_district_search_whole_word_matching(self) -> None:
        """Test that legacy District.search matches whole words only."""

        # Search for a term
        results = LegacyDistrict.search('ba ria')

        # Should return results
        assert len(results) > 0

        # All results should have both "ba" and "ria" as whole words in normalized form
        for district in results:
            normalized_name = normalize_search_name(district.name)
            name_words = set(normalized_name.split())
            assert 'ba' in name_words, f"Expected 'ba' as whole word in '{name_words}'"
            assert 'ria' in name_words, f"Expected 'ria' as whole word in '{name_words}'"

    def test_legacy_district_search_returns_tuple(self) -> None:
        """Test that legacy District.search returns a tuple."""

        results = LegacyDistrict.search('ba ria')
        assert isinstance(results, tuple)


class TestLegacyWardSearch:
    """Test cases for legacy Ward.search()"""

    def test_legacy_ward_search_empty_query(self) -> None:
        """Test that legacy Ward.search returns empty tuple for empty query."""

        results = LegacyWard.search('')
        assert results == ()

    def test_legacy_ward_search_single_word(self) -> None:
        """Test legacy Ward.search with a single word query."""

        results = LegacyWard.search('phú mỹ')

        # Should return results
        assert len(results) > 0

        # Should find wards with "Phú Mỹ" in name
        result_names = {w.name for w in results}
        assert any('Phú Mỹ' in name for name in result_names)

    def test_legacy_ward_search_apostrophe_normalization(self) -> None:
        """Test legacy Ward.search with curly apostrophe (data entry fix)."""

        # Search with straight apostrophe should find ward with curly apostrophe
        results = LegacyWard.search("D'Ran")

        # Should return results
        assert len(results) > 0

        # Should find Thị trấn D'Ran (with straight apostrophe in data)
        result_names = {w.name for w in results}
        assert "Thị trấn D'Ran" in result_names  # Straight apostrophe (U+0027)

    def test_legacy_ward_search_multi_word(self) -> None:
        """Test legacy Ward.search with multi-word queries."""

        results = LegacyWard.search('tan hai')

        # Should return results
        assert len(results) > 0

        # Should find wards with "Tân Hải" in name
        result_names = {w.name for w in results}
        assert any('Tân Hải' in name for name in result_names)

    def test_legacy_ward_search_with_division_type_prefix(self) -> None:
        """Test legacy Ward.search with division type prefix."""

        results = LegacyWard.search('phuong phu my')

        # Should return results (division type prefix should be filtered)
        assert len(results) > 0

        # Should find wards with "Phú Mỹ" in name
        result_names = {w.name for w in results}
        assert any('Phú Mỹ' in name for name in result_names)

    def test_legacy_ward_search_whole_word_matching(self) -> None:
        """Test that legacy Ward.search matches whole words only."""

        # Search for "phu my" - should NOT match "phuoc"
        results = LegacyWard.search('phu my')

        result_names = {w.name for w in results}

        # These should NOT be in results because "phuoc" != "phu"
        assert not any('Phước' in name for name in result_names), "'phuoc' should not match 'phu'"

    def test_legacy_ward_search_returns_tuple(self) -> None:
        """Test that legacy Ward.search returns a tuple."""

        results = LegacyWard.search('phu my')
        assert isinstance(results, tuple)
