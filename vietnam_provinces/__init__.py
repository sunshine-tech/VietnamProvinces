from pathlib import Path

from single_version import get_version

from .base import VietNamDivisionType, Province, District, Ward


__version__ = get_version('vietnamese_provinces', Path(__file__).parent.parent)
# Data retrieval date, in UTC
__data_version__ = '2023-05-07'
NESTED_DIVISIONS_JSON_PATH = Path(__file__).parent / 'data' / 'nested-divisions.json'
FLAT_DIVISIONS_JSON_PATH = Path(__file__).parent / 'data' / 'flat-divisions.json'
