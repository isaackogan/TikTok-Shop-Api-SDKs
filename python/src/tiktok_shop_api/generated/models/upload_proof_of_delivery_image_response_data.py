from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadProofOfDeliveryImageResponseData")


@_attrs_define
class UploadProofOfDeliveryImageResponseData:
    """
    Attributes:
        url (str | Unset): The URL returned from uploading the image that can be directly opened in a browser.
        height (int | Unset): The image height returned from uploading the image. This height refers to the processed
            image height, not the original image height.
            Units: pixels.
        width (int | Unset): The image width returned from uploading the image. This width refers to the processed image
            width, not the original image width.
            Units: pixels.
    """

    url: str | Unset = UNSET
    height: int | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        height = self.height

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        upload_proof_of_delivery_image_response_data = cls(
            url=url,
            height=height,
            width=width,
        )

        upload_proof_of_delivery_image_response_data.additional_properties = d
        return upload_proof_of_delivery_image_response_data

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
