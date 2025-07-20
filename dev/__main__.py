#!/usr/bin/env python

import re
import sys
import csv
import subprocess
from datetime import datetime, UTC
from enum import Enum, StrEnum
from pathlib import Path

import click
import rapidjson
import logbook
from pydantic import TypeAdapter, OnErrorOmit
from logbook import Logger
from logbook.more import ColorizedStderrHandler

from .phones import load_phone_area_table
from .divisions import (
    WardCSVInputRow,
    WardCSVRecord,
    ProvinceCSVRecord,
    gen_python_province_enums,
    gen_python_ward_enums,
    convert_to_nested,
)

logger = Logger(__name__)


class ExportingFormat(StrEnum):
    FLAT_JSON = 'flat-json'
    NESTED_JSON = 'nested-json'
    PYTHON = 'python'


class MyChoice[T](click.Choice[T]):
    def normalize_choice(self, choice: T, ctx: click.Context | None) -> str:
        normed_value = choice.value if isinstance(choice, Enum) else str(choice)

        if ctx is not None and ctx.token_normalize_func is not None:
            normed_value = ctx.token_normalize_func(normed_value)

        if not self.case_sensitive:
            normed_value = normed_value.casefold()

        return normed_value


def echo(msg: str):
    click.secho(msg, file=sys.stderr, fg='green')


class MyColorizedStderrHandler(ColorizedStderrHandler):
    default_format_string = '{record.level_name}: {record.message}'

    def get_color(self, record):  # pyright: ignore[reportIncompatibleMethodOverride]
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
    with outfile.open('w') as f:
        p = subprocess.run(cmd, input=content, text=True, stdout=f)
    return p.returncode == 0


def validate_output(ctx: click.Context, param: click.Parameter, value: str):
    if ctx.params.get('output_format') in (ExportingFormat.FLAT_JSON, ExportingFormat.NESTED_JSON) and not value:
        raise click.BadParameter('Require a path')
    return value


@click.command()
@click.option('-w', '--ward-csv', 'ward_csv_file', required=True, type=click.Path(exists=True))
@click.option('-p', '--province-csv', 'province_csv_file', required=True, type=click.Path(exists=True))
@click.option(
    '-f',
    '--output-format',
    default=ExportingFormat.NESTED_JSON,
    type=MyChoice(ExportingFormat, case_sensitive=False),
)
@click.option(
    '-o',
    '--output',
    type=click.Path(exists=False, writable=True),
    callback=validate_output,
    help='Output file if exporting JSON, output folder if exporting Python code',
)
@click.option('-v', '--verbose', count=True, default=False, help='Show more log to debug (verbose mode).')
def main(ward_csv_file: str, province_csv_file: str, output_format: ExportingFormat, output: str, verbose: int):
    configure_logging(verbose)
    logger.debug('File {}', ward_csv_file)
    csv_wards: tuple[WardCSVRecord, ...] = tuple()
    with open(ward_csv_file, newline='') as f:
        reader = csv.reader(f)
        # Skip header row
        next(reader)
        rows = (WardCSVInputRow._make(r[:3])._asdict() for r in reader)
        csv_wards = TypeAdapter(tuple[OnErrorOmit[WardCSVRecord], ...]).validate_python(rows)
    with open(province_csv_file, newline='') as f:
        reader = csv.reader(f)
        csv_provinces = tuple(map(ProvinceCSVRecord.from_csv_row, reader))
    logger.debug('Wards data: {}', csv_wards)
    logger.debug('Provinces data: {}', csv_provinces)
    phone_codes = load_phone_area_table()
    if output_format == ExportingFormat.FLAT_JSON:
        with open(output, 'w') as f:
            f.write(rapidjson.dumps(tuple(a.model_dump() for a in csv_wards), indent=2, ensure_ascii=False))
        echo(f'Wrote to {output}')
    elif output_format == ExportingFormat.NESTED_JSON:
        provinces = convert_to_nested(csv_provinces, csv_wards, phone_codes)
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
        provinces = convert_to_nested(csv_provinces, csv_wards, phone_codes)
        logger.info('Built AST')
        out_provinces = gen_python_province_enums(provinces.values())
        out_wards = gen_python_ward_enums(provinces.values())
        logger.info('Prettify code with Ruff')
        file_provinces = folder / 'provinces.py'
        format_code(out_provinces, file_provinces)
        rel_path = file_provinces.relative_to(Path.cwd())
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
        now = datetime.now(UTC)
        init_content = pkg_init_file.read_text()
        echo(f'Update data version {now:%Y-%m-%d}')
        updated = re.sub(r'__data_version__ = .+', f"__data_version__ = '{now:%Y-%m-%d}'", init_content)
        pkg_init_file.write_text(updated)


if __name__ == '__main__':
    main(prog_name='vietnamese-provinces')
