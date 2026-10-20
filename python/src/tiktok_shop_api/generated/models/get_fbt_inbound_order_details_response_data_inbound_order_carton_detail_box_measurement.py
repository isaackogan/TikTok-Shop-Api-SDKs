from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement")


@_attrs_define
class GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement:
    """
    Attributes:
        weight (str | Unset): Carton weight.
        weight_unit (str | Unset): The unit used for the carton's `weight` value.

            **Possible values:**
            * `KILOGRAM` (kg)
            * `GRAM` (g)
            * `MILLIGRAM` (mg)
            * `POUNDS` (lbs)
            * `OUNCE` (oz)
        width (str | Unset): Carton width.
        height (str | Unset): Carton height.
        length (str | Unset): Carton length.
        length_unit (str | Unset): The unit used for the carton's `length`, `width`, and `height` values.

            **Possible values:**
            * `METER` (m)
            * `CENTIMETER` (cm)
            * `MILLIMETER` (mm)
            * `FOOT` (ft)
            * `MICRON` (μm)
            * `INCH` (in)
    """

    weight: str | Unset = UNSET
    weight_unit: str | Unset = UNSET
    width: str | Unset = UNSET
    height: str | Unset = UNSET
    length: str | Unset = UNSET
    length_unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weight = self.weight

        weight_unit = self.weight_unit

        width = self.width

        height = self.height

        length = self.length

        length_unit = self.length_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weight is not UNSET:
            field_dict["weight"] = weight
        if weight_unit is not UNSET:
            field_dict["weight_unit"] = weight_unit
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if length is not UNSET:
            field_dict["length"] = length
        if length_unit is not UNSET:
            field_dict["length_unit"] = length_unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        weight = d.pop("weight", UNSET)

        weight_unit = d.pop("weight_unit", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        length = d.pop("length", UNSET)

        length_unit = d.pop("length_unit", UNSET)

        get_fbt_inbound_order_details_response_data_inbound_order_carton_detail_box_measurement = cls(
            weight=weight,
            weight_unit=weight_unit,
            width=width,
            height=height,
            length=length,
            length_unit=length_unit,
        )

        get_fbt_inbound_order_details_response_data_inbound_order_carton_detail_box_measurement.additional_properties = d
        return get_fbt_inbound_order_details_response_data_inbound_order_carton_detail_box_measurement

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
