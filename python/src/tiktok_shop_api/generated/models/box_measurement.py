from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.box_measurement_length_unit import BoxMeasurementLengthUnit
from ..models.box_measurement_weight_unit import BoxMeasurementWeightUnit

T = TypeVar("T", bound="BoxMeasurement")


@_attrs_define
class BoxMeasurement:
    """
    Attributes:
        weight (str): Carton weight.
        weight_unit (BoxMeasurementWeightUnit): The unit used for the carton's `weight` value.

            **Possible values:**
            * `KILOGRAM` (kg)
            * `GRAM` (g)
            * `MILLIGRAM` (mg)
            * `POUNDS` (lbs)
            * `OUNCE` (oz)
        width (str): Carton width.
        height (str): Carton height.
        length (str): Carton length.
        length_unit (BoxMeasurementLengthUnit): The unit used for the carton's `length`, `width`, and `height` values.

            **Possible values:**
            * `METER` (m)
            * `CENTIMETER` (cm)
            * `MILLIMETER` (mm)
            * `FOOT` (ft)
            * `MICRON` (μm)
            * `INCH` (in)
    """

    weight: str
    weight_unit: BoxMeasurementWeightUnit
    width: str
    height: str
    length: str
    length_unit: BoxMeasurementLengthUnit
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weight = self.weight

        weight_unit = self.weight_unit.value

        width = self.width

        height = self.height

        length = self.length

        length_unit = self.length_unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "weight": weight,
                "weight_unit": weight_unit,
                "width": width,
                "height": height,
                "length": length,
                "length_unit": length_unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        weight = d.pop("weight")

        weight_unit = BoxMeasurementWeightUnit(d.pop("weight_unit"))

        width = d.pop("width")

        height = d.pop("height")

        length = d.pop("length")

        length_unit = BoxMeasurementLengthUnit(d.pop("length_unit"))

        box_measurement = cls(
            weight=weight,
            weight_unit=weight_unit,
            width=width,
            height=height,
            length=length,
            length_unit=length_unit,
        )

        box_measurement.additional_properties = d
        return box_measurement

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
