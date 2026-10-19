from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagnoseAndOptimizeProductResponseDataDiagnosisSuggestionImage")


@_attrs_define
class DiagnoseAndOptimizeProductResponseDataDiagnosisSuggestionImage:
    """
    Attributes:
        height (int | Unset): The image height after optimization.
        width (int | Unset): The image width after optimization.
        uri (str | Unset): The original URI of the image.
        url (str | Unset): The original URL of the image.
        optimized_uri (str | Unset): The URI of the image after optimization.
        optimized_url (str | Unset): The URL of the image after optimization.
    """

    height: int | Unset = UNSET
    width: int | Unset = UNSET
    uri: str | Unset = UNSET
    url: str | Unset = UNSET
    optimized_uri: str | Unset = UNSET
    optimized_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        width = self.width

        uri = self.uri

        url = self.url

        optimized_uri = self.optimized_uri

        optimized_url = self.optimized_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width
        if uri is not UNSET:
            field_dict["uri"] = uri
        if url is not UNSET:
            field_dict["url"] = url
        if optimized_uri is not UNSET:
            field_dict["optimized_uri"] = optimized_uri
        if optimized_url is not UNSET:
            field_dict["optimized_url"] = optimized_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height", UNSET)

        width = d.pop("width", UNSET)

        uri = d.pop("uri", UNSET)

        url = d.pop("url", UNSET)

        optimized_uri = d.pop("optimized_uri", UNSET)

        optimized_url = d.pop("optimized_url", UNSET)

        diagnose_and_optimize_product_response_data_diagnosis_suggestion_image = cls(
            height=height,
            width=width,
            uri=uri,
            url=url,
            optimized_uri=optimized_uri,
            optimized_url=optimized_url,
        )

        diagnose_and_optimize_product_response_data_diagnosis_suggestion_image.additional_properties = d
        return diagnose_and_optimize_product_response_data_diagnosis_suggestion_image

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
