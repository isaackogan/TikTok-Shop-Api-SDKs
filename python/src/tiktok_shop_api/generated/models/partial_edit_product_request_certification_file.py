from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PartialEditProductRequestCertificationFile")


@_attrs_define
class PartialEditProductRequestCertificationFile:
    """
    Attributes:
        format_ (str): The format of the certification file. Only PDF is supported.
        id (str): The ID of the certification file.
            Use the [Upload Product File API](https://partner.tiktokshop.com/docv2/page/6509dffdc16ffe02b8dc10c5) to upload
            the files first and obtain the corresponding file ID.
        name (str): The name of the certification file, including the file extension.
    """

    format_: str
    id: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        format_ = self.format_

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
                "id": id,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        format_ = d.pop("format")

        id = d.pop("id")

        name = d.pop("name")

        partial_edit_product_request_certification_file = cls(
            format_=format_,
            id=id,
            name=name,
        )

        partial_edit_product_request_certification_file.additional_properties = d
        return partial_edit_product_request_certification_file

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
