from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DistrictInfo")


@_attrs_define
class DistrictInfo:
    """
    Attributes:
        address_level_name (str | Unset): The name of administrative division that can be used by seller for ship. e.g.
            state/county/city/district/town etc.
        address_name (str | Unset): Administrative area name. eg: London
        address_level (str | Unset): Administrative district level code. Value can be L0/L1/L2/L3/L4. eg. US is L0
        iso_code (str | Unset): ISO code of the administrative district level
    """

    address_level_name: str | Unset = UNSET
    address_name: str | Unset = UNSET
    address_level: str | Unset = UNSET
    iso_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_level_name = self.address_level_name

        address_name = self.address_name

        address_level = self.address_level

        iso_code = self.iso_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_level_name is not UNSET:
            field_dict["address_level_name"] = address_level_name
        if address_name is not UNSET:
            field_dict["address_name"] = address_name
        if address_level is not UNSET:
            field_dict["address_level"] = address_level
        if iso_code is not UNSET:
            field_dict["iso_code"] = iso_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address_level_name = d.pop("address_level_name", UNSET)

        address_name = d.pop("address_name", UNSET)

        address_level = d.pop("address_level", UNSET)

        iso_code = d.pop("iso_code", UNSET)

        district_info = cls(
            address_level_name=address_level_name,
            address_name=address_name,
            address_level=address_level,
            iso_code=iso_code,
        )

        district_info.additional_properties = d
        return district_info

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
