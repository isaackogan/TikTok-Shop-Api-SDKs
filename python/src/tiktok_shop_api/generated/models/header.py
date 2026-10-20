from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Header")



@_attrs_define
class Header:
    """ 
        Attributes:
            name (str): Header display name. Maximum length: 32 characters.
            id (str | Unset): Standard size-system or measurement ID.
                For standard measurement columns, call Get Category Rules for the corresponding category and use the ID from
                measurement_and_options[].options[].id under the applicable measurement_type.
                For size-system columns, use the following predefined IDs:
                - Size: size_chart_size_system_size
                - US: size_chart_size_system_us
                - UK: size_chart_size_system_uk
                - EU: size_chart_size_system_eu
                - JP: size_chart_size_system_jp
                - MX: size_chart_size_system_mx
                Omit this field for custom columns.
     """

    name: str
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        header = cls(
            name=name,
            id=id,
        )


        header.additional_properties = d
        return header

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
