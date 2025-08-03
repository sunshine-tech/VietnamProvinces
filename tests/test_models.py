from devtools import debug
from pydantic import BaseModel, field_serializer

from vietnam_provinces import Province, ProvinceCode


class Address(BaseModel):
    province: Province


class Profile(BaseModel):
    name: str
    address: Address


class DAddress(BaseModel):
    province: Province

    @field_serializer('province')
    def serialize_province(self, province: Province):
        return province._asdict()


class DProfile(BaseModel):
    name: str
    address: DAddress


def test_build_from_dict():
    p = Province.from_code(ProvinceCode.P_79)
    address = {'province': p._asdict()}
    profile = Profile(name='Nguyễn Hồng Quân', address=address)
    debug(profile)
    assert profile.address.province.code == ProvinceCode.P_79
    d = profile.model_dump()
    debug(d)
    assert d['address']['province'] == p


def test_dump_as_dict():
    p = Province.from_code(ProvinceCode.P_79)
    address = {'province': p}
    profile = DProfile(name='Nguyễn Hồng Quân', address=address)
    debug(profile)
    assert profile.address.province.code == ProvinceCode.P_79
    d = profile.model_dump()
    debug(d)
    assert d['address']['province'] == p._asdict()
