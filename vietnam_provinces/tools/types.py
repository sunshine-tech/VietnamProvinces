from typing import Union

from unidecode import unidecode
from pydantic import ConstrainedStr


class Name(ConstrainedStr):
    strip_whitespace = True

    @classmethod
    def validate(cls, value: Union[str]) -> Union[str]:
        value = super().validate(value)
        if value:
            return ' '.join(value.split())
        return value


def convert_to_codename(value: str) -> str:
    return '_'.join(unidecode(value).lower().replace('-', '').replace('.', '').split())
