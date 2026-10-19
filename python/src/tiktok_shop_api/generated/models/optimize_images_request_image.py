from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.optimize_images_request_image_optimization_mode_item import OptimizeImagesRequestImageOptimizationModeItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="OptimizeImagesRequestImage")


@_attrs_define
class OptimizeImagesRequestImage:
    """
    Attributes:
        uri (str | Unset): The URI of the image.
            Retrieve the URI from the [Upload Product Image
            API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22).
        optimization_mode (list[OptimizeImagesRequestImageOptimizationModeItem] | Unset): The optimization type.
            Possible values:
            - WHITE_BACKGROUND: Change the background to white.
    """

    uri: str | Unset = UNSET
    optimization_mode: list[OptimizeImagesRequestImageOptimizationModeItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        optimization_mode: list[str] | Unset = UNSET
        if not isinstance(self.optimization_mode, Unset):
            optimization_mode = []
            for optimization_mode_item_data in self.optimization_mode:
                optimization_mode_item = optimization_mode_item_data.value
                optimization_mode.append(optimization_mode_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uri is not UNSET:
            field_dict["uri"] = uri
        if optimization_mode is not UNSET:
            field_dict["optimization_mode"] = optimization_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri", UNSET)

        _optimization_mode = d.pop("optimization_mode", UNSET)
        optimization_mode: list[OptimizeImagesRequestImageOptimizationModeItem] | Unset = UNSET
        if _optimization_mode is not UNSET:
            optimization_mode = []
            for optimization_mode_item_data in _optimization_mode:
                optimization_mode_item = OptimizeImagesRequestImageOptimizationModeItem(optimization_mode_item_data)

                optimization_mode.append(optimization_mode_item)

        optimize_images_request_image = cls(
            uri=uri,
            optimization_mode=optimization_mode,
        )

        optimize_images_request_image.additional_properties = d
        return optimize_images_request_image

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
