from devtools import debug
from pydantic import BaseModel

from vietnam_provinces.enums import ProvinceEnum


class Address(BaseModel):
    province: ProvinceEnum


class Profile(BaseModel):
    name: str
    address: Address


def test_build_from_dict():
    address = {'province': ProvinceEnum.P_79}
    profile = Profile(name='Nguyễn Hồng Quân', address=address)
    debug(profile)
    assert profile.address.province == ProvinceEnum.P_79
    d = profile.model_dump()
    debug(d)
    assert d['address']['province'] == ProvinceEnum.P_79
