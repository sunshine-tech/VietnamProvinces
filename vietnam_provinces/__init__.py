from pathlib import Path

from .base import VietNamDivisionType, Province, Ward


__version__ = '0.6.0'
# Data retrieval date, in UTC
__data_version__ = '2025-07-23'
NESTED_DIVISIONS_JSON_PATH = Path(__file__).parent / 'data' / 'nested-divisions.json'
FLAT_DIVISIONS_JSON_PATH = Path(__file__).parent / 'data' / 'flat-divisions.json'
