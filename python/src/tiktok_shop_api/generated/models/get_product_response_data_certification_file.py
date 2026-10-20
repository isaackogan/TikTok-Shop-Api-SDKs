from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetProductResponseDataCertificationFile")



@_attrs_define
class GetProductResponseDataCertificationFile:
    """ 
        Attributes:
            format_ (str | Unset): The format of the certification file.
            id (str | Unset): The ID of the certification file.
            name (str | Unset): The name of the certification file.
            urls (list[str] | Unset): The URLs to view the certification files.
     """

    format_: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    urls: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        id = self.id

        name = self.name

        urls: list[str] | Unset = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if format_ is not UNSET:
            field_dict["format"] = format_
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if urls is not UNSET:
            field_dict["urls"] = urls

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        format_ = d.pop("format", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        urls = cast(list[str], d.pop("urls", UNSET))


        get_product_response_data_certification_file = cls(
            format_=format_,
            id=id,
            name=name,
            urls=urls,
        )


        get_product_response_data_certification_file.additional_properties = d
        return get_product_response_data_certification_file

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
