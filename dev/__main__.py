import sys
import csv
from enum import Enum
from pathlib import Path

import click
import rapidjson
import black
import logbook
from logbook import Logger
from logbook.more import ColorizedStderrHandler

from .phones import load_phone_area_table
from .divisions import WardCSVRecord, convert_to_nested, gen_python_district_enums, gen_python_ward_enums, gen_python_ward_dict

logger = Logger(__name__)


class ExportingFormat(str, Enum):
    FLAT_JSON = 'flat-json'
    NESTED_JSON = 'nested-json'
    PYTHON = 'python'


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
@click.option('-o', '--output', required=True, type=click.Path(exists=False, writable=True),
              help='Output file if exporting JSON, output folder if exporting Python code')
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
        click.secho(f'Wrote to {output}', file=sys.stderr, fg='green')
    elif output_format == ExportingFormat.NESTED_JSON:
        provinces = convert_to_nested(originals, phone_codes)
        provinces_dicts = tuple(p.dict() for p in provinces.values())
        with open(output, 'w') as f:
            f.write(rapidjson.dumps(provinces_dicts, indent=2, ensure_ascii=False))
        click.secho(f'Wrote to {output}', file=sys.stderr, fg='green')
    elif output_format == ExportingFormat.PYTHON:
        folder = Path(output)
        if folder.exists() and folder.is_file():
            click.secho(f'{output} is not a folder.', file=sys.stderr, fg='red')
            sys.exit(1)
        if not folder.exists():
            folder.mkdir()
        provinces = convert_to_nested(originals, phone_codes)
        out_districts = gen_python_district_enums(provinces.values())
        # out_wards = gen_python_ward_enums(provinces.values())
        out_wards_dict = gen_python_ward_dict(provinces.values())
        logger.info('Built AST')
        logger.info('Prettify code with Black')
        out_districts = black.format_str(out_districts, mode=black.FileMode(line_length=120))
        # out_wards = black.format_str(out_wards, mode=black.FileMode(line_length=120))
        # out_wards_dict = black.format_str(out_wards_dict, mode=black.FileMode(line_length=120))
        file_districts = folder / 'districts.py'    # type: Path
        file_districts.write_text(out_districts)
        click.secho(f'Wrote to {file_districts}', file=sys.stderr, fg='green')
        # file_wards = folder / 'wards.py'    # type: Path
        # file_wards.write_text(out_wards)
        # click.secho(f'Wrote to {file_wards}', file=sys.stderr, fg='green')
        file_lookup = folder / 'lookup.py'  # type: Path
        file_lookup.write_text(out_wards_dict)
        click.secho(f'Wrote to {file_lookup}', file=sys.stderr, fg='green')
        # Create __init__ file
        init_file = folder / '__init__.py'   # type: Path
        if not init_file.exists():
            init_file.touch()


if __name__ == '__main__':
    main(prog_name='vietnamese-provinces')
