from dataclasses import asdict

from devtools import debug
from pydantic import BaseModel, field_serializer

from vietnam_provinces import Province, ProvinceCode, Ward, WardCode
from vietnam_provinces.base import VietNamDivisionType


class Address(BaseModel):
    province: Province


class Profile(BaseModel):
    name: str
    address: Address


class DAddress(BaseModel):
    province: Province

    @field_serializer('province')
    def serialize_province(self, province: Province):
        return asdict(province)


class DProfile(BaseModel):
    name: str
    address: DAddress


def test_build_from_dict():
    p = Province.from_code(ProvinceCode.P_79)
    address = {'province': asdict(p)}
    profile = Profile(name='Nguyễn Hồng Quân', address=address)
    debug(profile)
    assert profile.address.province.code == ProvinceCode.P_79
    d = profile.model_dump()
    debug(d)
    assert d['address']['province'] == asdict(p)


def test_dump_as_dict():
    p = Province.from_code(ProvinceCode.P_79)
    address = {'province': p}
    profile = DProfile(name='Nguyễn Hồng Quân', address=address)
    debug(profile)
    assert profile.address.province.code == ProvinceCode.P_79
    d = profile.model_dump()
    debug(d)
    assert d['address']['province'] == asdict(p)


def test_ward_type_correctly_parsed_from_source():
    ward = Ward.from_code(WardCode.W_26878)
    assert ward.division_type == VietNamDivisionType.PHUONG
