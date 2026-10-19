from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.confirm_package_shipment_request_package_dimension_unit import (
    ConfirmPackageShipmentRequestPackageDimensionUnit,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfirmPackageShipmentRequestPackageDimension")


@_attrs_define
class ConfirmPackageShipmentRequestPackageDimension:
    """
    Attributes:
        length (int | Unset): Package length. Must be greater than or equal to `0`.
        width (int | Unset): Package width. Must be greater than or equal to `0`.
        height (int | Unset): Package height. Must be greater than or equal to `0`.
        unit (ConfirmPackageShipmentRequestPackageDimensionUnit | Unset): Package dimension unit
            Possible values:
            - METER
            - CENTIMETER
            - MILLIMETER
            - MICRON
            - FOOT
            - INCH
    """

    length: int | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    unit: ConfirmPackageShipmentRequestPackageDimensionUnit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        length = self.length

        width = self.width

        height = self.height

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if length is not UNSET:
            field_dict["length"] = length
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        length = d.pop("length", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: ConfirmPackageShipmentRequestPackageDimensionUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = ConfirmPackageShipmentRequestPackageDimensionUnit(_unit)

        confirm_package_shipment_request_package_dimension = cls(
            length=length,
            width=width,
            height=height,
            unit=unit,
        )

        confirm_package_shipment_request_package_dimension.additional_properties = d
        return confirm_package_shipment_request_package_dimension

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
