import pytest

from vietnam_provinces import Ward


@pytest.mark.parametrize(
    'query,expected_first',
    [
        ('phú mỹ', 'Thị trấn Phú Mỹ'),
        ('Phú Mỹ', 'Thị trấn Phú Mỹ'),
        ('phường phú mỹ', 'Phường Phú Mỹ'),
    ],
)
def test_search_from_legacy_prioritizes_diacritics_match(query, expected_first):
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
