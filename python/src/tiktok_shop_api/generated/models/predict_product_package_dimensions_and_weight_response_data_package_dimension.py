from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PredictProductPackageDimensionsAndWeightResponseDataPackageDimension")


@_attrs_define
class PredictProductPackageDimensionsAndWeightResponseDataPackageDimension:
    """
    Attributes:
        height (int): Predicted positive package height.
        length (int): Predicted positive package length.
        unit (str): Unit of the predicted package dimensions.
            Possible values:
            - `CENTIMETER`
            - `INCH`
            - `FOOT`
            - `MILLIMETER`
            - `METER`
        width (int): Predicted positive package width.
    """

    height: int
    length: int
    unit: str
    width: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        length = self.length

        unit = self.unit

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "height": height,
                "length": length,
                "unit": unit,
                "width": width,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height")

        length = d.pop("length")

        unit = d.pop("unit")

        width = d.pop("width")

        predict_product_package_dimensions_and_weight_response_data_package_dimension = cls(
            height=height,
            length=length,
            unit=unit,
            width=width,
        )

        predict_product_package_dimensions_and_weight_response_data_package_dimension.additional_properties = d
        return predict_product_package_dimensions_and_weight_response_data_package_dimension

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
