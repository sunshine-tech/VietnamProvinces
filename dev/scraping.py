from dataclasses import dataclass
from pathlib import Path
from typing import cast

import httpx
import markupever
import pyjson5
from logbook import Logger
from markupever.dom import Element
from pydantic import TypeAdapter

from .dmhc_sample import SAMPLE_POST_DATA


SITE_URL = 'https://danhmuchanhchinh.nso.gov.vn/'
API_URL = 'https://danhmuchanhchinh.nso.gov.vn/default.aspx'
PROV_TABLE_ELM_ID = '#ctl00_PlaceHolderMain_grid1N_DXMainTable'
WARDS_TABLE_ELM_ID = '#ctl00_PlaceHolderMain_grid1N_dxdt{idx}_grid12N_DXMainTable'
logger = Logger(__name__)


@dataclass
class ScrapedProvince:
    code: int
    name: str
    level: str


@dataclass
class ScrapedWard:
    code: int
    name: str
    level: str
    province: int


@dataclass
class WardListResponse:
    result: str


def get_provinces() -> tuple[ScrapedProvince, ...]:
    logger.info('Scraping provinces from {}', SITE_URL)
    text = httpx.get(SITE_URL).text
    tree = markupever.parse(text)
    if not (prov_table := tree.select_one(PROV_TABLE_ELM_ID)):
        logger.error('Province table not found')
        return ()
    code_cells = prov_table.select('tr td:nth-child(2)')
    codes = tuple(cast(Element, c).text().strip() for c in code_cells)
    name_cells = prov_table.select('tr td:nth-child(3)')
    names = tuple(cast(Element, c).text().strip() for c in name_cells)
    level_cells = prov_table.select('tr td:nth-child(5)')
    levels = tuple(cast(Element, c).text().strip() for c in level_cells)
    provinces = tuple(ScrapedProvince(int(c), n, v) for c, n, v in zip(codes, names, levels))
    logger.info('Found {} provinces', len(provinces))
    return provinces


def get_wards(index: int, province_code: int) -> tuple[ScrapedWard, ...]:
    logger.debug('Scraping wards for province code {}', province_code)
    api_param = f'GB|19;13|SHOWDETAILROW1|{index};' if index < 10 else f'GB|20;13|SHOWDETAILROW2|{index};'
    post_data = SAMPLE_POST_DATA | {'__CALLBACKPARAM': api_param}
    resp = httpx.post(API_URL, data=post_data)
    raw = resp.text
    # Response text will be like:
    # 0|/*^^^DX^^^*/({'result':'<div></div>'})
    # We will extract the JSON string from it
    head, sep, tail = raw.partition('({')
    if sep == '':
        logger.warning('Unrecognized data for province {}', province_code)
        Path(f'/tmp/province-{province_code}.txt').write_text(raw)
        # Not found
        return ()
    interesting = sep + tail
    # Remove the surrounding ()
    json_string = interesting.removeprefix('(').removesuffix(')')
    # Path('/tmp/json5-data.json5').write_text(json_string)
    jdata = pyjson5.decode(json_string)
    vjdata = TypeAdapter(WardListResponse).validate_python(jdata)
    # click.echo(vjdata.result)
    tree = markupever.parse(vjdata.result)
    if not (table := tree.select_one(WARDS_TABLE_ELM_ID.format(idx=index))):
        logger.warning('HTML table for wards of province {} is not found', province_code)
        Path(f'/tmp/province-{province_code}.html').write_text(vjdata.result)
        return ()
    rows = table.select('tr:not(:first-child):not(:last-child)')
    wards = []
    for row in rows:
        info = tuple(cast(Element, c).text().strip() for c in row.select('td'))
        wards.append(ScrapedWard(int(info[0]), info[1], info[3], province_code))
    logger.debug('Found {} wards for province {}', len(wards), province_code)
    return tuple(wards)


def scrape_danhmuchanhchinh() -> tuple[tuple[ScrapedProvince, ...], list[ScrapedWard]]:
    logger.info('Starting scrape from NSO website: {}', SITE_URL)
    provinces = get_provinces()
    all_wards = []
    for i, p in enumerate(provinces):
        logger.info('Scraping wards for province {} ({}/{})', p.name, i + 1, len(provinces))
        wards = get_wards(i, p.code)
        all_wards.extend(wards)
    logger.info('Scraping completed. Total: {} provinces, {} wards', len(provinces), len(all_wards))
    return provinces, all_wards
