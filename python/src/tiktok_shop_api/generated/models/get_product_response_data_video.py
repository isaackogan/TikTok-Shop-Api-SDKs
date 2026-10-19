from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductResponseDataVideo")


@_attrs_define
class GetProductResponseDataVideo:
    """
    Attributes:
        cover_url (str | Unset): The URL to view the video cover image.
        format_ (str | Unset): The video format.
        height (int | Unset): The video height.
            Unit: px
        id (str | Unset): The video ID.
        size (int | Unset): The video's original file size.
            Unit: MB
        url (str | Unset): The URL to view the video.
        width (int | Unset): The video width.
            Unit: px
    """

    cover_url: str | Unset = UNSET
    format_: str | Unset = UNSET
    height: int | Unset = UNSET
    id: str | Unset = UNSET
    size: int | Unset = UNSET
    url: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cover_url = self.cover_url

        format_ = self.format_

        height = self.height

        id = self.id

        size = self.size

        url = self.url

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if format_ is not UNSET:
            field_dict["format"] = format_
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if size is not UNSET:
            field_dict["size"] = size
        if url is not UNSET:
            field_dict["url"] = url
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cover_url = d.pop("cover_url", UNSET)

        format_ = d.pop("format", UNSET)

        height = d.pop("height", UNSET)

        id = d.pop("id", UNSET)

        size = d.pop("size", UNSET)

        url = d.pop("url", UNSET)

        width = d.pop("width", UNSET)

        get_product_response_data_video = cls(
            cover_url=cover_url,
            format_=format_,
            height=height,
            id=id,
            size=size,
            url=url,
            width=width,
        )

        get_product_response_data_video.additional_properties = d
        return get_product_response_data_video

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
