#!/usr/bin/env python

import csv
import re
import subprocess
import sys
from collections.abc import Sequence
from datetime import UTC, datetime
from enum import Enum, StrEnum
from pathlib import Path

import click
import logbook
import rapidjson
from logbook import Logger
from logbook.base import LogRecord
from logbook.more import ColorizedStderrHandler
from pydantic import OnErrorOmit, TypeAdapter

from .amend import fix_ward
from .conversion_table import (
    generate_province_conversion_table,
    generate_ward_conversion_table,
)
from .divisions import (
    ProvinceSourceRecord,
    WardCSVInputRow,
    WardSourceRecord,
    convert_to_nested,
    gen_python_code_enums,
    gen_python_province_lookup,
)
from .legacy_divisions import (
    convert_to_nested as convert_pre2025_to_nested,
)
from .legacy_divisions import (
    gen_python_code_enums as gen_legacy_python_code_enums,
)
from .legacy_divisions import (
    gen_python_lookup as gen_legacy_python_lookup,
)
from .legacy_divisions import (
    parse_pre2025_csv,
)
from .phones import load_phone_area_table
from .scraping import scrape_danhmuchanhchinh


logger = Logger(__name__)


class ExportingFormat(StrEnum):
    FLAT_JSON = 'flat-json'
    NESTED_JSON = 'nested-json'
    PYTHON = 'python'


class MyChoice[T](click.Choice):
    def normalize_choice(self, choice: T, ctx: click.Context | None) -> str:
        normed_value = choice.value if isinstance(choice, Enum) else str(choice)

        if ctx is not None and ctx.token_normalize_func is not None:
            normed_value = ctx.token_normalize_func(normed_value)

        if not self.case_sensitive:
            normed_value = normed_value.casefold()

        return normed_value


def echo(msg: str) -> None:
    click.secho(msg, file=sys.stderr, fg='green')


class MyColorizedStderrHandler(ColorizedStderrHandler):
    default_format_string: str = '{record.level_name}: {record.message}'

    def get_color(self, record: LogRecord):  # pyright: ignore[reportIncompatibleMethodOverride]
        color = super().get_color(record)
        if logbook.DEBUG < record.level <= logbook.INFO:
            return 'darkteal'
        return color


def configure_logging(verbose: int) -> None:
    levels = (logbook.WARNING, logbook.INFO, logbook.DEBUG)
    l = min(verbose, len(levels) - 1)  # noqa
    colored_handler = MyColorizedStderrHandler(level=levels[l])
    colored_handler.push_application()


# Format, lint and fix code using Ruff
def format_and_lint_code(dirpath: Path) -> bool:
    fmt_cmd = ('ruff', 'format', str(dirpath))
    subprocess.run(fmt_cmd, check=False)
    check_cmd = ('ruff', 'check', '--fix', str(dirpath))
    p = subprocess.run(check_cmd, check=False)
    return p.returncode == 0


def validate_output(ctx: click.Context, _param: click.Parameter, value: str | None) -> Path | None:
    if ctx.params.get('output_format') in (ExportingFormat.FLAT_JSON, ExportingFormat.NESTED_JSON) and not value:
        raise click.BadParameter('Require a path')
    return Path(value) if value else None


@click.group()
def app() -> None:
    pass


def generate_output(
    provinces: Sequence[ProvinceSourceRecord],
    wards: Sequence[WardSourceRecord],
    output_format: ExportingFormat,
    output: Path,
) -> None:
    """Common logic for generating output files."""
    phone_codes = load_phone_area_table()
    if output_format == ExportingFormat.FLAT_JSON:
        with open(output, 'w') as f:
            f.write(rapidjson.dumps(tuple(a.model_dump() for a in wards), indent=2, ensure_ascii=False))
        echo(f'Wrote to {output}')
    elif output_format == ExportingFormat.NESTED_JSON:
        provinces_dict = convert_to_nested(provinces, wards, phone_codes)
        provinces_dicts = tuple(p.model_dump() for p in provinces_dict.values())
        with open(output, 'w') as f:
            f.write(rapidjson.dumps(provinces_dicts, indent=2, ensure_ascii=False))
        echo(f'Wrote to {output}')
    elif output_format == ExportingFormat.PYTHON:
        provinces_dict = convert_to_nested(provinces, wards, phone_codes)
        logger.info('Built AST')
        out_enums = gen_python_code_enums(provinces_dict.values())
        pkg_folder = Path(__file__).parent.parent / 'vietnam_provinces'
        file_path = pkg_folder / 'codes.py'
        logger.info('Save code')
        file_path.write_text(out_enums)
        rel_path = file_path.relative_to(Path.cwd())
        echo(f'Wrote to {rel_path}')
        file_path = pkg_folder / '_lookup.py'
        out_lookup = gen_python_province_lookup(provinces_dict.values())
        file_path.write_text(out_lookup)
        rel_path = file_path.relative_to(Path.cwd())
        echo(f'Wrote to {rel_path}')
        # Format and lint the whole vietnam_provinces folder after code generation
        logger.info('Formatting and linting code with Ruff for the whole vietnam_provinces folder...')
        format_and_lint_code(pkg_folder)

        pkg_init_file = pkg_folder / '__init__.py'
        now = datetime.now(UTC)
        init_content = pkg_init_file.read_text()
        echo(f'Update data version {now:%Y-%m-%d}')
        updated = re.sub(r'__data_version__ = .+', f"__data_version__ = '{now:%Y-%m-%d}'", init_content)
        pkg_init_file.write_text(updated)


@app.command()
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
def scrape(output_format: ExportingFormat, output: Path, verbose: int) -> None:
    """Generate Python code or JSON data by scraping government website."""
    configure_logging(verbose)
    scraped_provinces, scraped_wards = scrape_danhmuchanhchinh()
    provinces = [ProvinceSourceRecord(code=p.code, name=p.name) for p in scraped_provinces]
    wards = [
        WardSourceRecord(
            code=w.code, name=w.name, province_name=next(p.name for p in scraped_provinces if p.code == w.province)
        )
        for w in scraped_wards
    ]
    generate_output(provinces, wards, output_format, output)


@app.command()
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
def process_csv(
    ward_csv_file: str, province_csv_file: str, output_format: ExportingFormat, output: Path, verbose: int
) -> None:
    """Generate Python code or JSON data from pre-saved CSV files."""
    configure_logging(verbose)
    logger.debug('File {}', ward_csv_file)
    csv_wards: list[WardSourceRecord] = []
    with open(ward_csv_file, newline='') as f:
        reader = csv.reader(f)
        # Skip header row
        _heading_row = next(reader)
        rows = (WardCSVInputRow._make(r[:3])._asdict() for r in reader)
        csv_wards = TypeAdapter(list[OnErrorOmit[WardSourceRecord]]).validate_python(rows)
    with open(province_csv_file, newline='') as f:
        reader = csv.reader(f)
        csv_provinces = tuple(map(ProvinceSourceRecord.from_csv_row, reader))
    csv_wards = [fix_ward(w) for w in csv_wards]
    logger.debug('Wards data: {}', csv_wards)
    logger.debug('Provinces data: {}', csv_provinces)
    generate_output(list(csv_provinces), csv_wards, output_format, output)


@app.command('gen-conversion-table')
@click.option('-v', '--verbose', count=True, default=False, help='Show more log to debug (verbose mode).')
def gen_conversion_table(verbose: int) -> None:
    """Generate ward and province conversion table Python code from CSV source.

    This command creates bidirectional lookup tables for converting between
    old wards/provinces (pre-2025) and new wards/provinces (post-2025).
    The ward table includes a flag to indicate if an old ward was partly merged
    (split across multiple new wards).
    """
    configure_logging(verbose)

    project_root = Path(__file__).parent.parent
    input_path = project_root / 'dev/seed-data/2025-07/BangChuyendoiĐVHCmoi_cu_khong_merge.csv'

    # Generate ward conversion table
    ward_output_path = project_root / 'vietnam_provinces' / '_ward_conversion_2025.py'
    ward_output_path.parent.mkdir(parents=True, exist_ok=True)

    logger.info('Parsing conversion CSV: {}', input_path)
    ward_metadata = generate_ward_conversion_table(input_path, ward_output_path)

    # Generate province conversion table
    province_output_path = project_root / 'vietnam_provinces' / '_province_conversion_2025.py'

    logger.info('Generating province conversion table...')
    province_metadata = generate_province_conversion_table(input_path, province_output_path)

    logger.info('Formatting and linting code with Ruff...')
    format_and_lint_code(ward_output_path.parent)

    rel_ward_path = ward_output_path.relative_to(Path.cwd(), walk_up=True)
    rel_province_path = province_output_path.relative_to(Path.cwd(), walk_up=True)

    echo(f'Generated ward conversion table: {rel_ward_path}')
    echo(f'  Old wards: {ward_metadata.stats.old_wards_count}')
    echo(f'  New wards: {ward_metadata.stats.new_wards_count}')
    echo(f'  Partly merged: {ward_metadata.stats.partly_merged_count}')
    echo(f'Generated province conversion table: {rel_province_path}')
    echo(f'  Old provinces: {province_metadata.stats.old_provinces_count}')
    echo(f'  New provinces: {province_metadata.stats.new_provinces_count}')


@app.command('gen-legacy')
@click.option(
    '-c',
    '--csv-file',
    required=True,
    type=click.Path(exists=True),
    help='Path to pre-2025 ward CSV file (with province, district, ward data)',
)
@click.option('-v', '--verbose', count=True, default=False, help='Show more log to debug (verbose mode).')
def gen_legacy(csv_file: str, verbose: int) -> None:
    """Generate Python code for pre-2025 administrative divisions from CSV.

    This command reads a CSV file containing pre-2025 administrative data
    (with 3 levels: Province -> District -> Ward) and generates:

    \b
    1. vietnam_provinces/legacy/codes.py - Enum definitions for codes
    2. vietnam_provinces/legacy/_lookup.py - Lookup mappings for Province, District, Ward objects

    \b
    The CSV file should have these columns:
    - Province name, Province code, District name, District code, Ward name, Ward code
    """
    configure_logging(verbose)

    csv_path = Path(csv_file)
    pkg_folder = Path(__file__).parent.parent / 'vietnam_provinces' / 'legacy'
    pkg_folder.mkdir(parents=True, exist_ok=True)

    logger.info('Parsing pre-2025 CSV: {}', csv_path)
    records = parse_pre2025_csv(csv_path)
    logger.info('Parsed {} records', len(records))

    phone_codes = load_phone_area_table()
    logger.info('Converting to nested structure...')
    provinces_dict = convert_pre2025_to_nested(records, phone_codes)
    logger.info('Built nested structure: {} provinces', len(provinces_dict))

    # Generate enum code
    logger.info('Generating enum code...')
    out_enums = gen_legacy_python_code_enums(provinces_dict.values())
    file_path = pkg_folder / 'codes.py'
    logger.info('Saving enum code...')
    file_path.write_text(out_enums)
    rel_path = file_path.relative_to(Path.cwd())
    echo(f'Wrote to {rel_path}')

    # Generate lookup code
    logger.info('Generating lookup code...')
    out_lookup = gen_legacy_python_lookup(provinces_dict.values())
    file_path = pkg_folder / '_lookup.py'
    logger.info('Saving lookup code...')
    file_path.write_text(out_lookup)
    rel_path = file_path.relative_to(Path.cwd())
    echo(f'Wrote to {rel_path}.')

    # Lint the entire legacy folder
    logger.info('Formatting and linting code with Ruff...')
    format_and_lint_code(pkg_folder)

    echo('🎉 Finished generating code for pre-2025 provinces, districts and wards.')


if __name__ == '__main__':
    app(prog_name='vietnamese-provinces')
