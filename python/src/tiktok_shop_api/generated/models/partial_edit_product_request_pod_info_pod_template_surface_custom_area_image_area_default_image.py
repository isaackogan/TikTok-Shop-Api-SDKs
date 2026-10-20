from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PartialEditProductRequestPodInfoPodTemplateSurfaceCustomAreaImageAreaDefaultImage")


@_attrs_define
class PartialEditProductRequestPodInfoPodTemplateSurfaceCustomAreaImageAreaDefaultImage:
    """
    Attributes:
        uri (str | Unset): The URI of the default image.
            Obtain this URI by uploading the images through the [Upload Product Image API](6509df95defece02be598a22)  with
            `use_case=CUSTOMIZATION_IMAGE`.
    """

    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri", UNSET)

        partial_edit_product_request_pod_info_pod_template_surface_custom_area_image_area_default_image = cls(
            uri=uri,
        )

        partial_edit_product_request_pod_info_pod_template_surface_custom_area_image_area_default_image.additional_properties = d
        return partial_edit_product_request_pod_info_pod_template_surface_custom_area_image_area_default_image

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
