"""
Province conversion table for 2025 administrative changes.

This module provides bidirectional lookup for converting between
old provinces (pre-2025) and new provinces (post-2025).

Auto-generated from ward conversion data.
"""

from typing import NamedTuple


class OldProvinceRef(NamedTuple):
    """Reference to an old province (pre-2025)."""

    code: int


class NewProvinceRef(NamedTuple):
    """Reference to a new province (post-2025)."""

    code: int


class OldToNewEntry(NamedTuple):
    """Mapping from old province to new province(s)."""

    old_province: OldProvinceRef
    new_provinces: tuple[NewProvinceRef, ...]


class NewToOldEntry(NamedTuple):
    """Mapping from new province to old province(s)."""

    new_province: NewProvinceRef
    old_provinces: tuple[OldProvinceRef, ...]


EFFECTIVE_DATE = '2025-07-01'

# Mapping from old province code to new province(s)
OLD_TO_NEW: dict[int, OldToNewEntry] = {
    1: OldToNewEntry(OldProvinceRef(1), (NewProvinceRef(1),)),
    2: OldToNewEntry(OldProvinceRef(2), (NewProvinceRef(8),)),
    4: OldToNewEntry(OldProvinceRef(4), (NewProvinceRef(4),)),
    6: OldToNewEntry(OldProvinceRef(6), (NewProvinceRef(19),)),
    8: OldToNewEntry(OldProvinceRef(8), (NewProvinceRef(8),)),
    10: OldToNewEntry(OldProvinceRef(10), (NewProvinceRef(15),)),
    11: OldToNewEntry(OldProvinceRef(11), (NewProvinceRef(11),)),
    12: OldToNewEntry(OldProvinceRef(12), (NewProvinceRef(12),)),
    14: OldToNewEntry(OldProvinceRef(14), (NewProvinceRef(14),)),
    15: OldToNewEntry(OldProvinceRef(15), (NewProvinceRef(15),)),
    17: OldToNewEntry(OldProvinceRef(17), (NewProvinceRef(25),)),
    19: OldToNewEntry(OldProvinceRef(19), (NewProvinceRef(19),)),
    20: OldToNewEntry(OldProvinceRef(20), (NewProvinceRef(20),)),
    22: OldToNewEntry(OldProvinceRef(22), (NewProvinceRef(22),)),
    24: OldToNewEntry(OldProvinceRef(24), (NewProvinceRef(24),)),
    25: OldToNewEntry(OldProvinceRef(25), (NewProvinceRef(25),)),
    26: OldToNewEntry(OldProvinceRef(26), (NewProvinceRef(25),)),
    27: OldToNewEntry(OldProvinceRef(27), (NewProvinceRef(24),)),
    30: OldToNewEntry(OldProvinceRef(30), (NewProvinceRef(31),)),
    31: OldToNewEntry(OldProvinceRef(31), (NewProvinceRef(31),)),
    33: OldToNewEntry(OldProvinceRef(33), (NewProvinceRef(33),)),
    34: OldToNewEntry(OldProvinceRef(34), (NewProvinceRef(33),)),
    35: OldToNewEntry(OldProvinceRef(35), (NewProvinceRef(37),)),
    36: OldToNewEntry(OldProvinceRef(36), (NewProvinceRef(37),)),
    37: OldToNewEntry(OldProvinceRef(37), (NewProvinceRef(37),)),
    38: OldToNewEntry(OldProvinceRef(38), (NewProvinceRef(38),)),
    40: OldToNewEntry(OldProvinceRef(40), (NewProvinceRef(40),)),
    42: OldToNewEntry(OldProvinceRef(42), (NewProvinceRef(42),)),
    44: OldToNewEntry(OldProvinceRef(44), (NewProvinceRef(44),)),
    45: OldToNewEntry(OldProvinceRef(45), (NewProvinceRef(44),)),
    46: OldToNewEntry(OldProvinceRef(46), (NewProvinceRef(46),)),
    48: OldToNewEntry(OldProvinceRef(48), (NewProvinceRef(48),)),
    49: OldToNewEntry(OldProvinceRef(49), (NewProvinceRef(48),)),
    51: OldToNewEntry(OldProvinceRef(51), (NewProvinceRef(51),)),
    52: OldToNewEntry(OldProvinceRef(52), (NewProvinceRef(52),)),
    54: OldToNewEntry(OldProvinceRef(54), (NewProvinceRef(66),)),
    56: OldToNewEntry(OldProvinceRef(56), (NewProvinceRef(56),)),
    58: OldToNewEntry(OldProvinceRef(58), (NewProvinceRef(56),)),
    60: OldToNewEntry(OldProvinceRef(60), (NewProvinceRef(68),)),
    62: OldToNewEntry(OldProvinceRef(62), (NewProvinceRef(51),)),
    64: OldToNewEntry(OldProvinceRef(64), (NewProvinceRef(52),)),
    66: OldToNewEntry(OldProvinceRef(66), (NewProvinceRef(66),)),
    67: OldToNewEntry(OldProvinceRef(67), (NewProvinceRef(68),)),
    68: OldToNewEntry(OldProvinceRef(68), (NewProvinceRef(68),)),
    70: OldToNewEntry(OldProvinceRef(70), (NewProvinceRef(75),)),
    72: OldToNewEntry(OldProvinceRef(72), (NewProvinceRef(80),)),
    74: OldToNewEntry(OldProvinceRef(74), (NewProvinceRef(79),)),
    75: OldToNewEntry(OldProvinceRef(75), (NewProvinceRef(75),)),
    77: OldToNewEntry(OldProvinceRef(77), (NewProvinceRef(79),)),
    79: OldToNewEntry(OldProvinceRef(79), (NewProvinceRef(79),)),
    80: OldToNewEntry(OldProvinceRef(80), (NewProvinceRef(80),)),
    82: OldToNewEntry(OldProvinceRef(82), (NewProvinceRef(80), NewProvinceRef(82))),
    83: OldToNewEntry(OldProvinceRef(83), (NewProvinceRef(86),)),
    84: OldToNewEntry(OldProvinceRef(84), (NewProvinceRef(86),)),
    86: OldToNewEntry(OldProvinceRef(86), (NewProvinceRef(86),)),
    87: OldToNewEntry(OldProvinceRef(87), (NewProvinceRef(82),)),
    89: OldToNewEntry(OldProvinceRef(89), (NewProvinceRef(91),)),
    91: OldToNewEntry(OldProvinceRef(91), (NewProvinceRef(91),)),
    92: OldToNewEntry(OldProvinceRef(92), (NewProvinceRef(92),)),
    93: OldToNewEntry(OldProvinceRef(93), (NewProvinceRef(92),)),
    94: OldToNewEntry(OldProvinceRef(94), (NewProvinceRef(92),)),
    95: OldToNewEntry(OldProvinceRef(95), (NewProvinceRef(96),)),
    96: OldToNewEntry(OldProvinceRef(96), (NewProvinceRef(96),)),
}

# Mapping from new province code to old province(s)
NEW_TO_OLD: dict[int, NewToOldEntry] = {
    1: NewToOldEntry(NewProvinceRef(1), (OldProvinceRef(1),)),
    4: NewToOldEntry(NewProvinceRef(4), (OldProvinceRef(4),)),
    8: NewToOldEntry(NewProvinceRef(8), (OldProvinceRef(2), OldProvinceRef(8))),
    11: NewToOldEntry(NewProvinceRef(11), (OldProvinceRef(11),)),
    12: NewToOldEntry(NewProvinceRef(12), (OldProvinceRef(12),)),
    14: NewToOldEntry(NewProvinceRef(14), (OldProvinceRef(14),)),
    15: NewToOldEntry(NewProvinceRef(15), (OldProvinceRef(10), OldProvinceRef(15))),
    19: NewToOldEntry(NewProvinceRef(19), (OldProvinceRef(6), OldProvinceRef(19))),
    20: NewToOldEntry(NewProvinceRef(20), (OldProvinceRef(20),)),
    22: NewToOldEntry(NewProvinceRef(22), (OldProvinceRef(22),)),
    24: NewToOldEntry(NewProvinceRef(24), (OldProvinceRef(24), OldProvinceRef(27))),
    25: NewToOldEntry(NewProvinceRef(25), (OldProvinceRef(17), OldProvinceRef(25), OldProvinceRef(26))),
    31: NewToOldEntry(NewProvinceRef(31), (OldProvinceRef(30), OldProvinceRef(31))),
    33: NewToOldEntry(NewProvinceRef(33), (OldProvinceRef(33), OldProvinceRef(34))),
    37: NewToOldEntry(NewProvinceRef(37), (OldProvinceRef(35), OldProvinceRef(36), OldProvinceRef(37))),
    38: NewToOldEntry(NewProvinceRef(38), (OldProvinceRef(38),)),
    40: NewToOldEntry(NewProvinceRef(40), (OldProvinceRef(40),)),
    42: NewToOldEntry(NewProvinceRef(42), (OldProvinceRef(42),)),
    44: NewToOldEntry(NewProvinceRef(44), (OldProvinceRef(44), OldProvinceRef(45))),
    46: NewToOldEntry(NewProvinceRef(46), (OldProvinceRef(46),)),
    48: NewToOldEntry(NewProvinceRef(48), (OldProvinceRef(48), OldProvinceRef(49))),
    51: NewToOldEntry(NewProvinceRef(51), (OldProvinceRef(51), OldProvinceRef(62))),
    52: NewToOldEntry(NewProvinceRef(52), (OldProvinceRef(52), OldProvinceRef(64))),
    56: NewToOldEntry(NewProvinceRef(56), (OldProvinceRef(56), OldProvinceRef(58))),
    66: NewToOldEntry(NewProvinceRef(66), (OldProvinceRef(54), OldProvinceRef(66))),
    68: NewToOldEntry(NewProvinceRef(68), (OldProvinceRef(60), OldProvinceRef(67), OldProvinceRef(68))),
    75: NewToOldEntry(NewProvinceRef(75), (OldProvinceRef(70), OldProvinceRef(75))),
    79: NewToOldEntry(NewProvinceRef(79), (OldProvinceRef(74), OldProvinceRef(77), OldProvinceRef(79))),
    80: NewToOldEntry(NewProvinceRef(80), (OldProvinceRef(72), OldProvinceRef(80), OldProvinceRef(82))),
    82: NewToOldEntry(NewProvinceRef(82), (OldProvinceRef(82), OldProvinceRef(87))),
    86: NewToOldEntry(NewProvinceRef(86), (OldProvinceRef(83), OldProvinceRef(84), OldProvinceRef(86))),
    91: NewToOldEntry(NewProvinceRef(91), (OldProvinceRef(89), OldProvinceRef(91))),
    92: NewToOldEntry(NewProvinceRef(92), (OldProvinceRef(92), OldProvinceRef(93), OldProvinceRef(94))),
    96: NewToOldEntry(NewProvinceRef(96), (OldProvinceRef(95), OldProvinceRef(96))),
}
