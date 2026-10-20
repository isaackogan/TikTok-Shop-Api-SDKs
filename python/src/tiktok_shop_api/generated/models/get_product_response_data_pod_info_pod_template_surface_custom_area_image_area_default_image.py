from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductResponseDataPodInfoPodTemplateSurfaceCustomAreaImageAreaDefaultImage")


@_attrs_define
class GetProductResponseDataPodInfoPodTemplateSurfaceCustomAreaImageAreaDefaultImage:
    """
    Attributes:
        height (int | Unset): The height of the default image, in pixels.
        thumb_urls (list[str] | Unset): A list of thumbnail URLs for the default image.
        uri (str | Unset): The URI of the default image.
            Obtain this URI by uploading the images through the [Upload Product Image API](6509df95defece02be598a22)  with
            `use_case=CUSTOMIZATION_IMAGE`.
        urls (list[str] | Unset): A list of URLs for the default image.
        width (int | Unset): The width of the default image, in pixels.
    """

    height: int | Unset = UNSET
    thumb_urls: list[str] | Unset = UNSET
    uri: str | Unset = UNSET
    urls: list[str] | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        thumb_urls: list[str] | Unset = UNSET
        if not isinstance(self.thumb_urls, Unset):
            thumb_urls = self.thumb_urls

        uri = self.uri

        urls: list[str] | Unset = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if thumb_urls is not UNSET:
            field_dict["thumb_urls"] = thumb_urls
        if uri is not UNSET:
            field_dict["uri"] = uri
        if urls is not UNSET:
            field_dict["urls"] = urls
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height", UNSET)

        thumb_urls = cast(list[str], d.pop("thumb_urls", UNSET))

        uri = d.pop("uri", UNSET)

        urls = cast(list[str], d.pop("urls", UNSET))

        width = d.pop("width", UNSET)

        get_product_response_data_pod_info_pod_template_surface_custom_area_image_area_default_image = cls(
            height=height,
            thumb_urls=thumb_urls,
            uri=uri,
            urls=urls,
            width=width,
        )

        get_product_response_data_pod_info_pod_template_surface_custom_area_image_area_default_image.additional_properties = d
        return get_product_response_data_pod_info_pod_template_surface_custom_area_image_area_default_image

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
