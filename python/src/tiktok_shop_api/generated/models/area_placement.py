from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AreaPlacement")


@_attrs_define
class AreaPlacement:
    """
    Attributes:
        height (str | Unset): The height of the customizable area.
            Supports two decimal places.
        rotate_degree (str | Unset): The rotation angle of the customizable area, in degrees.
            Supports two decimal places.
        width (str | Unset): The width of the customizable area.
            Supports two decimal places.
        x_coordinate (str | Unset): The X-coordinate of the customizable area's starting point on the surface.
            Supports two decimal places.
        y_coordinate (str | Unset): The Y-coordinate of the customizable area's starting point on the surface.
            Supports two decimal places.
    """

    height: str | Unset = UNSET
    rotate_degree: str | Unset = UNSET
    width: str | Unset = UNSET
    x_coordinate: str | Unset = UNSET
    y_coordinate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        rotate_degree = self.rotate_degree

        width = self.width

        x_coordinate = self.x_coordinate

        y_coordinate = self.y_coordinate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if rotate_degree is not UNSET:
            field_dict["rotate_degree"] = rotate_degree
        if width is not UNSET:
            field_dict["width"] = width
        if x_coordinate is not UNSET:
            field_dict["x_coordinate"] = x_coordinate
        if y_coordinate is not UNSET:
            field_dict["y_coordinate"] = y_coordinate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height", UNSET)

        rotate_degree = d.pop("rotate_degree", UNSET)

        width = d.pop("width", UNSET)

        x_coordinate = d.pop("x_coordinate", UNSET)

        y_coordinate = d.pop("y_coordinate", UNSET)

        area_placement = cls(
            height=height,
            rotate_degree=rotate_degree,
            width=width,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
        )

        area_placement.additional_properties = d
        return area_placement

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
