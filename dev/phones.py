import csv
from pathlib import Path
from typing import NamedTuple, List

from pydantic import BaseModel, field_validator

from .types import Name, convert_to_codename


DATA_SOURCE_NAME = 'Ma_vung_dien_thoai_co_dinh_mat_dat_2017-09-01.csv'


class PhoneCodeInputRow(NamedTuple):
    order: int
    province_name: str
    code: int


class PhoneCodeCSVRecord(BaseModel):
    province_name: Name
    code: int

    # Some provinces are renamed after the data of phone code is published
    @field_validator('province_name', mode='after')
    @classmethod
    def rename(cls, value: str) -> str:
        if value == 'Thừa Thiên - Huế':
            return 'Thành phố Huế'
        return value

    @property
    def province_codename(self):
        codename = convert_to_codename(self.province_name)
        # The province name in source data of phone doesn't always follow spelling in Tổng cục Thống kê, so
        # we need to adjust it.
        if codename.startswith('tp_'):   # tp_ho_chi_minh
            codename = codename[3:]
        elif codename == 'bac_can':
            codename = 'bac_kan'
        return codename

    @classmethod
    def from_csv_row(cls, values: List[str]):
        row = PhoneCodeInputRow._make(values)
        return cls.model_validate(row._asdict())


def load_phone_area_table():
    data_source = Path(__file__).parent / 'seed-data' / DATA_SOURCE_NAME
    with open(data_source, newline='') as f:
        reader = csv.reader(f)
        # Skip header
        next(reader)
        codes = tuple(map(PhoneCodeCSVRecord.from_csv_row, reader))
    return codes
