from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetBestsellingProductsResponseDataProductProductImage")


@_attrs_define
class GetBestsellingProductsResponseDataProductProductImage:
    """
    Attributes:
        height (int | Unset): The image height.
            Unit: px
        width (int | Unset): The image width.
            Unit: px
        thumb_urls (list[str] | Unset): The URLs to view the image thumbnails.
        uri (str | Unset): The URI of the image.
        urls (list[str] | Unset): The URLs to view the images.
    """

    height: int | Unset = UNSET
    width: int | Unset = UNSET
    thumb_urls: list[str] | Unset = UNSET
    uri: str | Unset = UNSET
    urls: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        width = self.width

        thumb_urls: list[str] | Unset = UNSET
        if not isinstance(self.thumb_urls, Unset):
            thumb_urls = self.thumb_urls

        uri = self.uri

        urls: list[str] | Unset = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width
        if thumb_urls is not UNSET:
            field_dict["thumb_urls"] = thumb_urls
        if uri is not UNSET:
            field_dict["uri"] = uri
        if urls is not UNSET:
            field_dict["urls"] = urls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        thumb_urls = cast(list[str], d.pop("thumb_urls", UNSET))

        uri = d.pop("uri", UNSET)

        urls = cast(list[str], d.pop("urls", UNSET))

        get_bestselling_products_response_data_product_product_image = cls(
            height=height,
            width=width,
            thumb_urls=thumb_urls,
            uri=uri,
            urls=urls,
        )

        get_bestselling_products_response_data_product_product_image.additional_properties = d
        return get_bestselling_products_response_data_product_product_image

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
