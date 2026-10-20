from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetGlobalProductResponseDataCertificationFile")



@_attrs_define
class GetGlobalProductResponseDataCertificationFile:
    """ 
        Attributes:
            id (str | Unset): The ID of the certification file.
            urls (list[str] | Unset): The URLs to view the certification files.
            name (str | Unset): The name of the certification file
            format_ (str | Unset): The format of the certification file.
     """

    id: str | Unset = UNSET
    urls: list[str] | Unset = UNSET
    name: str | Unset = UNSET
    format_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        urls: list[str] | Unset = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls



        name = self.name

        format_ = self.format_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if urls is not UNSET:
            field_dict["urls"] = urls
        if name is not UNSET:
            field_dict["name"] = name
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        urls = cast(list[str], d.pop("urls", UNSET))


        name = d.pop("name", UNSET)

        format_ = d.pop("format", UNSET)

        get_global_product_response_data_certification_file = cls(
            id=id,
            urls=urls,
            name=name,
            format_=format_,
        )


        get_global_product_response_data_certification_file.additional_properties = d
        return get_global_product_response_data_certification_file

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
