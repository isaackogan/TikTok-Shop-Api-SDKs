from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGlobalProductResponseDataMainImage")


@_attrs_define
class GetGlobalProductResponseDataMainImage:
    """
    Attributes:
        height (int | Unset): The image height.
            Unit: px
        width (int | Unset): The image width.
            Unit: px
        uri (str | Unset): The URI of the image.
    """

    height: int | Unset = UNSET
    width: int | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        width = self.width

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        uri = d.pop("uri", UNSET)

        get_global_product_response_data_main_image = cls(
            height=height,
            width=width,
            uri=uri,
        )

        get_global_product_response_data_main_image.additional_properties = d
        return get_global_product_response_data_main_image

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
