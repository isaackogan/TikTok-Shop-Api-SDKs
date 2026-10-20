from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_packages_request_dimension_unit import CreatePackagesRequestDimensionUnit

T = TypeVar("T", bound="CreatePackagesRequestDimension")


@_attrs_define
class CreatePackagesRequestDimension:
    """
    Attributes:
        length (str): Package length.

            The length, width, and height must be passed together.
        width (str): Package width.

            The length, width, and height must be passed together.
        height (str): Package height.

            The length, width, and height must be passed together.
        unit (CreatePackagesRequestDimensionUnit): The unit of measurement for the package dimensions. For packages in
            the US, use `INCH`.

            Available values:
            - `CM`
            - `INCH`
    """

    length: str
    width: str
    height: str
    unit: CreatePackagesRequestDimensionUnit
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        length = self.length

        width = self.width

        height = self.height

        unit = self.unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "length": length,
                "width": width,
                "height": height,
                "unit": unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        length = d.pop("length")

        width = d.pop("width")

        height = d.pop("height")

        unit = CreatePackagesRequestDimensionUnit(d.pop("unit"))

        create_packages_request_dimension = cls(
            length=length,
            width=width,
            height=height,
            unit=unit,
        )

        create_packages_request_dimension.additional_properties = d
        return create_packages_request_dimension

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
