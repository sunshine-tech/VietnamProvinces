import re
import unicodedata
from typing import Annotated

from pydantic import AfterValidator
from unidecode import unidecode


REGEX_THI_XA = re.compile('^Thị Xã')
REGEX_THI_TRAN = re.compile('^Thị Trấn')


def clean_name(value: str) -> str:
    value = unicodedata.normalize('NFC', value)
    if not value:
        return ''
    # Reduce whitespaces
    value = ' '.join(value.split())
    value = REGEX_THI_XA.sub('Thị xã', value)
    value = REGEX_THI_TRAN.sub('Thị trấn', value)
    return value


Name = Annotated[str, AfterValidator(clean_name)]


def convert_to_codename(value: str) -> str:
    return '_'.join(unidecode(value).lower().replace('-', ' ').replace('.', ' ').replace("'", '').split())


def convert_to_id_friendly(value: str) -> str:
    return '_'.join(value.lower().replace('-', ' ').replace('.', ' ').replace("'", '').split())


def make_province_codename(name: str) -> str:
    # Since 2025, we no longer keep devision type in codename
    return convert_to_codename(name).removeprefix('tinh_').removeprefix('thanh_pho_').removeprefix('tp_')


def make_ward_short_codename(codename: str) -> str:
    return codename.removeprefix('xa_').removeprefix('phuong_').removeprefix('dac_khu_')
