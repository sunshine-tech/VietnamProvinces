from pathlib import Path

from single_version import get_version

from .base import Province, District, Ward  # noqa


__version__ = get_version('vietnamese_provinces', Path(__file__).parent.parent)
