#!/usr/bin/env python

import re
import sys
import csv
import subprocess
from datetime import datetime
from enum import Enum
from pathlib import Path

import click
import rapidjson
import logbook
from logbook import Logger
from logbook.more import ColorizedStderrHandler

from .phones import load_phone_area_table
from .divisions import WardCSVRecord, convert_to_nested, gen_python_district_enums, gen_python_ward_enums

logger = Logger(__name__)


class ExportingFormat(str, Enum):
    FLAT_JSON = 'flat-json'
    NESTED_JSON = 'nested-json'
    PYTHON = 'python'


def echo(msg: str):
    click.secho(msg, file=sys.stderr, fg='green')


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


# Beautify code using Ruff and save to file
def format_code(content: str, outfile: Path) -> bool:
    cmd = ('ruff', 'format', '-', '--stdin-filename', 'code.py')
    with outfile.open() as f:
        p = subprocess.run(cmd, input=content, text=True, stdout=f)
    return p.returncode == 0


@click.command()
@click.option('-i', '--input', 'input_filename', required=True, type=click.Path(exists=True))
@click.option('-f', '--output-format', default=ExportingFormat.NESTED_JSON, type=EnumChoice(ExportingFormat))
@click.option('-o', '--output', type=click.Path(exists=False, writable=True),
              help='Output file if exporting JSON, output folder if exporting Python code')
@click.option('-v', '--verbose', count=True, default=False, help='Show more log to debug (verbose mode).')
def main(input_filename: str, output_format: ExportingFormat, output: str, verbose: int):
    configure_logging(verbose)
    logger.debug('File {}', input_filename)
    originals: tuple[WardCSVRecord, ...] = tuple()
    with open(input_filename, newline='') as f:
        reader = csv.reader(f)
        # Skip header row
        next(reader)
        originals = tuple(map(WardCSVRecord.from_csv_row, reader))
    logger.debug('Data: {}', originals)
    phone_codes = load_phone_area_table()
    if output_format == ExportingFormat.FLAT_JSON:
        with open(output, 'w') as f:
            f.write(rapidjson.dumps(tuple(a.model_dump() for a in originals), indent=2, ensure_ascii=False))
        echo(f'Wrote to {output}')
    elif output_format == ExportingFormat.NESTED_JSON:
        provinces = convert_to_nested(originals, phone_codes)
        provinces_dicts = tuple(p.model_dump() for p in provinces.values())
        with open(output, 'w') as f:
            f.write(rapidjson.dumps(provinces_dicts, indent=2, ensure_ascii=False))
        echo(f'Wrote to {output}')
    elif output_format == ExportingFormat.PYTHON:
        folder: Path = Path(__file__).parent.parent / 'vietnam_provinces' / 'enums'
        if folder.exists() and folder.is_file():
            click.secho(f'{output} is not a folder.', file=sys.stderr, fg='red')
            sys.exit(1)
        if not folder.exists():
            folder.mkdir()
        provinces = convert_to_nested(originals, phone_codes)
        out_districts = gen_python_district_enums(provinces.values())
        out_wards = gen_python_ward_enums(provinces.values())
        logger.info('Built AST')
        logger.info('Prettify code with Ruff')
        file_districts = folder / 'districts.py'
        format_code(out_districts, file_districts)
        rel_path = file_districts.relative_to(Path.cwd())
        echo(f'Wrote to {rel_path}')
        file_wards = folder / 'wards.py'
        format_code(out_wards, file_wards)
        rel_path = file_wards.relative_to(Path.cwd())
        echo(f'Wrote to {rel_path}')
        # Create __init__ file
        init_file = folder / '__init__.py'
        if not init_file.exists():
            init_file.touch()
        pkg_init_file = folder.parent / '__init__.py'
        now = datetime.utcnow()
        init_content = pkg_init_file.read_text()
        echo(f'Update data version {now:%Y-%m-%d}')
        updated = re.sub(r'__data_version__ = .+', f"__data_version__ = '{now:%Y-%m-%d}'", init_content)
        pkg_init_file.write_text(updated)


if __name__ == '__main__':
    main(prog_name='vietnamese-provinces')
