import csv
from enum import Enum

import click
import rapidjson
import logbook
from logbook import Logger
from logbook.more import ColorizedStderrHandler

from .phones import load_phone_area_table
from .divisions import WardCSVRecord, convert_to_nested

logger = Logger(__name__)


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


@click.command()
@click.option('-i', '--input', 'input_filename', required=True, type=click.Path(exists=True))
@click.option('-f', '--output-format', default=ExportingFormat.NESTED_JSON, type=EnumChoice(ExportingFormat))
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
    phone_codes = load_phone_area_table()
    if output_format == ExportingFormat.FLAT_JSON:
        with open(output, 'w') as f:
            f.write(rapidjson.dumps(tuple(a.dict() for a in originals), indent=2, ensure_ascii=False))
    elif output_format == ExportingFormat.NESTED_JSON:
        provinces = convert_to_nested(originals, phone_codes)
        with open(output, 'w') as f:
            f.write(rapidjson.dumps(provinces, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main(prog_name='vietnamese-provinces')
