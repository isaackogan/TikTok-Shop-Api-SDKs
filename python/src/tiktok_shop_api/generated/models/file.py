from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="File")



@_attrs_define
class File:
    """ 
        Attributes:
            id (str): The ID of the certification file.
                Use the [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) to upload
                the files first and obtain the corresponding file ID.
            name (str): The name of the certification file, including the file extension.
            format_ (str): The format of the certification file. Only PDF is supported.
     """

    id: str
    name: str
    format_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        format_ = self.format_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "format": format_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        format_ = d.pop("format")

        file = cls(
            id=id,
            name=name,
            format_=format_,
        )


        file.additional_properties = d
        return file

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
