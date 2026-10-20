from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadProductImageResponseData")


@_attrs_define
class UploadProductImageResponseData:
    """
    Attributes:
        uri (str | Unset): The URI to identify the image in API requests and responses.
            Pass this value when creating or editing a product to associate the image with the product.
        url (str | Unset): The URL to access and view the image.
            Use this URL in product descriptions by embedding it within an HTML `<img>` tag.
        height (int | Unset): The height of the image after aspect ratio adjustment.
        width (int | Unset): The width of the image after aspect ratio adjustment.
        use_case (str | Unset): The usage scenario specified during upload.
            Possible values:
            - MAIN_IMAGE
            - ATTRIBUTE_IMAGE
            - DESCRIPTION_IMAGE
            - CERTIFICATION_IMAGE
            - SIZE_CHART_IMAGE
            - CUSTOMIZATION_IMAGE
    """

    uri: str | Unset = UNSET
    url: str | Unset = UNSET
    height: int | Unset = UNSET
    width: int | Unset = UNSET
    use_case: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        url = self.url

        height = self.height

        width = self.width

        use_case = self.use_case

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uri is not UNSET:
            field_dict["uri"] = uri
        if url is not UNSET:
            field_dict["url"] = url
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width
        if use_case is not UNSET:
            field_dict["use_case"] = use_case

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri", UNSET)

        url = d.pop("url", UNSET)

        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        use_case = d.pop("use_case", UNSET)

        upload_product_image_response_data = cls(
            uri=uri,
            url=url,
            height=height,
            width=width,
            use_case=use_case,
        )

        upload_product_image_response_data.additional_properties = d
        return upload_product_image_response_data

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
