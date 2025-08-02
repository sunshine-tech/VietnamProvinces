from devtools import debug
from pydantic import BaseModel

from vietnam_provinces import Province, ProvinceCode


class Address(BaseModel):
    province: Province


class Profile(BaseModel):
    name: str
    address: Address


def test_build_from_dict():
    p = Province.from_code(ProvinceCode.P_79)
    address = {'province': p}
    profile = Profile(name='Nguyễn Hồng Quân', address=address)
    debug(profile)
    assert profile.address.province.code == ProvinceCode.P_79
    d = profile.model_dump()
    debug(d)
    assert d['address']['province'] == p
