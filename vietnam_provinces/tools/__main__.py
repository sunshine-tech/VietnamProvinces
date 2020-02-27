import csv
from enum import Enum
from typing import NamedTuple, List, Optional, Sequence, Dict, Tuple, Union

import click
import rapidjson
import logbook
from logbook import Logger
from logbook.more import ColorizedStderrHandler
from unidecode import unidecode
from pydantic import BaseModel, validator, ConstrainedStr

logger = Logger(__name__)


class Name(ConstrainedStr):
    strip_whitespace = True

    @classmethod
    def validate(cls, value: Union[str]) -> Union[str]:
        value = super().validate(value)
        if value:
            return ' '.join(value.split())
        return value


class WardCSVInputRow(NamedTuple):
    province_name: str
    province_code: int
    district_name: str
    district_code: int
    ward_name: str
    ward_code: int

    @classmethod
    def strip_make(cls, value):
        return cls._make(value[:6])


class VietNamDivisionType(str, Enum):
    # Level 1
    TINH = 'tỉnh'
    THANH_PHO_TRUNG_UONG = 'thành phố trung ương'
    # Level 2
    HUYEN = 'huyện'
    QUAN = 'quận'
    THANH_PHO = 'thành phố'
    THI_XA = 'thị xã'
    # Level 3
    XA = 'xã'
    THI_TRAN = 'thị trấn'
    PHUONG = 'phường'


class ExportingFormat(str, Enum):
    FLAT_JSON = 'flat-json'
    NESTED_JSON = 'nested-json'


class EnumChoice(click.Choice):
    def __init__(self, enum_class):
        super().__init__(tuple(e.value for e in enum_class))
        self.enum_class = enum_class

    def convert(self, value, param, ctx):
        value = super().convert(value, param, ctx)
        return next(e for e in self.enum_class if e.value == value)


def convert_to_codename(value: str):
    return '_'.join(unidecode(value).lower().split())


class WardCSVRecord(BaseModel):
    province_name: Name
    province_code: int
    province_codename: Optional[str]
    district_name: Name
    district_code: int
    district_codename: Optional[str]
    ward_name: Name
    ward_code: int
    ward_codename: Optional[str]

    @validator('province_codename', always=True)
    def set_province_codename(cls, v, values):
        return convert_to_codename(values['province_name'])

    @validator('district_codename', always=True)
    def set_district_codename(cls, v, values):
        return convert_to_codename(values['district_name'])

    @validator('ward_codename', always=True)
    def set_ward_codename(cls, v, values):
        return convert_to_codename(values['ward_name'])

    @classmethod
    def from_csv_row(cls, values: List[str]):
        row = WardCSVInputRow.strip_make(values)
        return cls.parse_obj(row._asdict())


class BaseRegion(BaseModel):
    name: str
    code: int
    codename: Optional[str]


class Ward(BaseRegion):
    # Redefine here, or the validator won't run
    division_type: VietNamDivisionType = None

    @validator('division_type', pre=True, always=True)
    def parse_division_type(cls, v, values):
        if v:
            return v
        name = values['name'].lower()
        possibles = (VietNamDivisionType.THI_TRAN, VietNamDivisionType.XA, VietNamDivisionType.PHUONG)
        return next((t for t in possibles if name.startswith(f'{t.value} ')), None)


class District(BaseRegion):
    # Redefine here, or the validator won't run
    division_type: VietNamDivisionType = None
    wards: Tuple[Ward, ...] = ()
    # Actual wards are saved here for fast searching
    indexed_wards: Dict[int, Ward] = None

    def __init__(self, **data):
        super().__init__(**data)
        self.indexed_wards = {}

    @validator('division_type', pre=True, always=True)
    def parse_division_type(cls, v, values):
        if v:
            return v
        name = values['name'].lower()
        possibles = (VietNamDivisionType.THANH_PHO, VietNamDivisionType.THI_XA, VietNamDivisionType.QUAN, VietNamDivisionType.HUYEN)
        return next((t for t in possibles if name.startswith(f'{t.value} ')), None)

    def dict(self, exclude={}, **kwargs):
        self.wards = tuple(self.indexed_wards.values())
        out = super().dict(exclude={'indexed_wards'}, **kwargs)
        return out


class Province(BaseRegion):
    # Redefine here, or the validator won't run
    division_type: VietNamDivisionType = None
    districts: Tuple[District, ...] = ()
    # Actual districts are saved here for fast searching
    indexed_districts: Dict[int, District] = None

    def __init__(self, **data):
        super().__init__(**data)
        self.indexed_districts = {}

    @validator('division_type', pre=True, always=True)
    def parse_division_type(cls, v, values):
        if v:
            return v
        name = values['name'].lower()
        if name.startswith(f'{VietNamDivisionType.THANH_PHO} '):
            return VietNamDivisionType.THANH_PHO_TRUNG_UONG
        if name.startswith(f'{VietNamDivisionType.TINH} '):
            return VietNamDivisionType.TINH

    def dict(self, exclude={}, **kwargs):
        self.districts = tuple(self.indexed_districts.values())
        out = super().dict(exclude={'indexed_districts'}, **kwargs)
        return out


class MyColorizedStderrHandler(ColorizedStderrHandler):
    default_format_string = '{record.level_name}: {record.message}'

    def get_color(self, record):
        color = super().get_color(record)
        if logbook.DEBUG < record.level <= logbook.INFO:
            return 'darkteal'
        return color


def configure_logging(verbose):
    levels = (logbook.WARNING, logbook.INFO, logbook.DEBUG)
    l = min(verbose, len(levels) - 1)  # noqa
    colored_handler = MyColorizedStderrHandler(level=levels[l])
    colored_handler.push_application()


def add_to_existing_province(w: WardCSVRecord, province: Province) -> Ward:
    ward = Ward(name=w.ward_name, code=w.ward_code, codename=w.ward_codename)
    try:
        district = province.indexed_districts[w.district_code]
        district.indexed_wards[w.ward_code] = ward
    except KeyError:
        district = District(name=w.district_name, code=w.district_code, codename=w.district_codename)
        province.indexed_districts[w.district_code] = district
        district.indexed_wards = {w.ward_code: ward}
    return ward


def convert_to_nested(records: Sequence[WardCSVRecord]) -> Tuple[Province, ...]:
    out = {}    # type: Dict[int, Province]
    for w in records:
        province_code = w.province_code
        try:
            province = out[province_code]
            add_to_existing_province(w, province)
        except KeyError:
            province = Province(name=w.province_name, code=province_code, codename=w.province_codename)
            district = District(name=w.district_name, code=w.district_code, codename=w.district_codename)
            province.indexed_districts[w.district_code] = district
            ward = Ward(name=w.ward_name, code=w.ward_code, codename=w.ward_codename)
            district.indexed_wards[w.ward_code] = ward
            out[province_code] = province
    return tuple(p.dict() for p in out.values())


@click.command()
@click.option('-i', '--input', 'input_filename', required=True, type=click.Path(exists=True))
@click.option('-f', '--output-format', default=ExportingFormat.FLAT_JSON, type=EnumChoice(ExportingFormat))
@click.option('-o', '--output', required=True, type=click.Path(exists=False, writable=True))
@click.option('-v', '--verbose', count=True, default=False, help='Show more log to debug (verbose mode).')
def main(input_filename: str, output_format: ExportingFormat, output: str, verbose: int):
    configure_logging(verbose)
    logger.debug('File {}', input_filename)
    originals = tuple()
    with open(input_filename, newline='') as f:
        reader = csv.reader(f)
        # Skip header row
        next(reader)
        originals = tuple(map(WardCSVRecord.from_csv_row, reader))
    logger.debug('Data: {}', originals)
    if output_format == ExportingFormat.FLAT_JSON:
        with open(output, 'w') as f:
            f.write(rapidjson.dumps(tuple(a.dict() for a in originals), indent=2, ensure_ascii=False))
    elif output_format == ExportingFormat.NESTED_JSON:
        provinces = convert_to_nested(originals)
        with open(output, 'w') as f:
            f.write(rapidjson.dumps(provinces, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main(prog_name='vietnamese-provinces')
