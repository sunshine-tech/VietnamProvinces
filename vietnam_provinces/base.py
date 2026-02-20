from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterator
from dataclasses import dataclass
from enum import Enum

from .codes import ProvinceCode, WardCode


class VietNamDivisionType(str, Enum):
    # Level 1
    TINH = 'tỉnh'
    THANH_PHO_TRUNG_UONG = 'thành phố trung ương'
    # Level 2
    XA = 'xã'
    PHUONG = 'phường'
    DAC_KHU = 'đặc khu'


# We use dataclass instead of NamedTuple to allow this class
# to be mixed in Pydandic dataclass in application side.
@dataclass(frozen=True)
class Province:
    name: str
    code: ProvinceCode
    division_type: VietNamDivisionType
    codename: str
    phone_code: int

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Province):
            return False
        return other.code == self.code

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def from_code(code: ProvinceCode) -> Province:
        """Look up a Province from code."""
        from .lookup import PROVINCE_MAPPING

        try:
            return PROVINCE_MAPPING[code]
        except KeyError as e:
            msg = f'Province code {code} is invalid.'
            raise ValueError(msg) from e

    @staticmethod
    def iter_all() -> Iterator[Province]:
        """Get iterator over all provinces."""
        from .lookup import PROVINCE_MAPPING

        values = PROVINCE_MAPPING.values()
        return iter(values)


@dataclass(frozen=True)
class Ward:
    name: str
    code: WardCode
    division_type: VietNamDivisionType
    codename: str
    province_code: ProvinceCode

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Ward):
            return False
        return other.code == self.code

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def from_code(code: WardCode) -> Ward:
        """Look up a Ward from code."""
        from .lookup import WARD_MAPPING

        try:
            return WARD_MAPPING[code]
        except KeyError as e:
            msg = f'Ward code {code} is invalid.'
            raise ValueError(msg) from e

    @staticmethod
    def iter_all() -> Iterator[Ward]:
        """Get iterator over all wards."""
        from .lookup import WARD_MAPPING

        values = WARD_MAPPING.values()
        return iter(values)

    @staticmethod
    def iter_by_province(code: ProvinceCode) -> Iterator[Ward]:
        """Get iterator over wards belonging to a province."""
        from .lookup import WARD_MAPPING

        values = iter(w for w in WARD_MAPPING.values() if w.province_code == code)
        return values

    @classmethod
    def search_from_legacy(cls, name: str = '', code: int = 0) -> tuple[Ward, ...]:
        """Given a legacy ward code, or part of legacy ward name, return all matching wards."""
        from ._ward_conversion_2025 import OLD_TO_NEW

        if code > 0:
            entry = OLD_TO_NEW.get(code)
            return tuple(cls.from_code(WardCode(nw.code)) for nw in entry.new_wards) if entry else ()

        if not name:
            return ()

        query = _normalize_search_name(name)
        results: list[Ward] = []
        seen_codes: set[int] = set()

        for entry in OLD_TO_NEW.values():
            if query not in _normalize_search_name(entry.old_ward.name):
                continue

            for nw in entry.new_wards:
                if nw.code in seen_codes:
                    continue

                try:
                    results.append(cls.from_code(WardCode(nw.code)))
                    seen_codes.add(nw.code)
                except ValueError:
                    continue

        return tuple(results)


def _normalize_search_name(name: str) -> str:
    """Normalize Vietnamese name for fuzzy searching."""
    name = name.lower()
    # Remove common prefixes
    name = re.sub(r'^(xã|phường|thị trấn)\s+', '', name)
    # Remove diacritics
    name = unicodedata.normalize('NFD', name)
    name = ''.join(c for c in name if unicodedata.category(c) != 'Mn')
    name = name.replace('đ', 'd')
    return unicodedata.normalize('NFC', name)


@dataclass(frozen=True)
class LegacyWard:
    """Pre-2025 wards."""

    pass
