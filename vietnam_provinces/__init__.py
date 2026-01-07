from pathlib import Path

from .base import Province, VietNamDivisionType, Ward
from .codes import ProvinceCode, WardCode


__version__ = '2026.01.0'
# Data retrieval date, in UTC
__data_version__ = '2026-01-07'
NESTED_DIVISIONS_JSON_PATH = Path(__file__).parent / 'data' / 'nested-divisions.json'
FLAT_DIVISIONS_JSON_PATH = Path(__file__).parent / 'data' / 'flat-divisions.json'

__all__ = (
    '__version__',
    '__data_version__',
    'VietNamDivisionType',
    'Province',
    'Ward',
    'ProvinceCode',
    'WardCode',
)
