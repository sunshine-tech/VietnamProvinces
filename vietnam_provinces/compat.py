from enum import EnumMeta
from typing import TypeVar


try:
    from enum_tools.documentation import document_enum
except ModuleNotFoundError:
    EnumType = TypeVar('EnumType', bound=EnumMeta)

    def document_enum(an_enum: EnumType) -> EnumType:
        return an_enum


__all__ = ['document_enum']
