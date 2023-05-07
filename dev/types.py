import re
import unicodedata

from unidecode import unidecode
from pydantic import ConstrainedStr


REGEX_THI_XA = re.compile('^Thị Xã')
REGEX_THI_TRAN = re.compile('^Thị Trấn')


class Name(ConstrainedStr):
    strip_whitespace = True

    @classmethod
    def validate(cls, value: str) -> str:
        value = super().validate(value)
        value = unicodedata.normalize('NFC', value)
        if not value:
            return ''
        # Reduce whitespaces
        value = ' '.join(value.split())
        value = REGEX_THI_XA.sub('Thị xã', value)
        value = REGEX_THI_TRAN.sub('Thị trấn', value)
        return value


def convert_to_codename(value: str) -> str:
    return '_'.join(unidecode(value).lower()
                    .replace('-', ' ').replace('.', ' ').replace("'", '').split())


def convert_to_id_friendly(value: str) -> str:
    return '_'.join(value.lower()
                    .replace('-', ' ').replace('.', ' ').replace("'", '').split())
