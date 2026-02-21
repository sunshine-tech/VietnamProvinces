import pytest

from vietnam_provinces import Ward
from vietnam_provinces.codes import WardCode


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

    # Get the old ward names for verification
    from vietnam_provinces._ward_conversion_2025 import OLD_TO_NEW

    # Find wards with expected_first in their old names
    expected_first_codes = set()

    for entry in OLD_TO_NEW.values():
        if entry.old_ward.name == expected_first:
            expected_first_codes.update(w.code for w in entry.new_wards)

    # The first result should be one with the expected_first old name
    if expected_first_codes:
        assert results[0].code in expected_first_codes, (
            f"First result should have old name '{expected_first}', but got ward with code {results[0].code}"
        )


@pytest.mark.parametrize(
    ('legacy_code', 'expected_ward_name'),
    [
        (26707, 'Phường Tân Hải'),  # Phường Tân Hòa (legacy) -> Phường Tân Hải (new)
    ],
)
def test_search_from_legacy_by_code(legacy_code: int, expected_ward_name: str) -> None:
    """Test that search_from_legacy returns correct ward when searching by legacy code."""
    results = Ward.search_from_legacy(code=legacy_code)

    # Should return exactly one result for this case
    assert len(results) == 1

    # The result should have the expected name
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
