from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OptimizeImagesResponseDataImage")



@_attrs_define
class OptimizeImagesResponseDataImage:
    """ 
        Attributes:
            height (int | Unset): The height of the original image, in pixels.
            width (int | Unset): The width of the original image, in pixels.
            original_uri (str | Unset): The original URI of the image to be optimized.
            original_url (str | Unset): The original URL of the image to be optimized.
            optimized_uri (str | Unset): The URI of the image after optimization.
                Pass this value when creating or editing a product to associate the image with the product.

                Applicable only if `optimize_status`is `SUCCESS`.
            optimized_url (str | Unset): The URL of the image after optimization.
                Use this URL in product descriptions by embedding it within an HTML `<img>` tag.

                Applicable only if `optimize_status`is `SUCCESS`.
            optimize_status (str | Unset): The optimization status.
                Possible values:
                - SUCCESS: The image has been successfully optimized.
                - IGNORE: The image already has a white background, so no optimization was applied.
                - PROCESSING: The optimization is in progress, and typically completes within a few seconds. Call this API again
                to obtain the final optimization status.
     """

    height: int | Unset = UNSET
    width: int | Unset = UNSET
    original_uri: str | Unset = UNSET
    original_url: str | Unset = UNSET
    optimized_uri: str | Unset = UNSET
    optimized_url: str | Unset = UNSET
    optimize_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        height = self.height

        width = self.width

        original_uri = self.original_uri

        original_url = self.original_url

        optimized_uri = self.optimized_uri

        optimized_url = self.optimized_url

        optimize_status = self.optimize_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width
        if original_uri is not UNSET:
            field_dict["original_uri"] = original_uri
        if original_url is not UNSET:
            field_dict["original_url"] = original_url
        if optimized_uri is not UNSET:
            field_dict["optimized_uri"] = optimized_uri
        if optimized_url is not UNSET:
            field_dict["optimized_url"] = optimized_url
        if optimize_status is not UNSET:
            field_dict["optimize_status"] = optimize_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        original_uri = d.pop("original_uri", UNSET)

        original_url = d.pop("original_url", UNSET)

        optimized_uri = d.pop("optimized_uri", UNSET)

        optimized_url = d.pop("optimized_url", UNSET)

        optimize_status = d.pop("optimize_status", UNSET)

        optimize_images_response_data_image = cls(
            height=height,
            width=width,
            original_uri=original_uri,
            original_url=original_url,
            optimized_uri=optimized_uri,
            optimized_url=optimized_url,
            optimize_status=optimize_status,
        )


        optimize_images_response_data_image.additional_properties = d
        return optimize_images_response_data_image

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
