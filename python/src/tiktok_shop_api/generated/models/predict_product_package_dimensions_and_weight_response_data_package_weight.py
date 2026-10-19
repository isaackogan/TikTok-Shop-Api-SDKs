from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.predict_product_package_dimensions_and_weight_response_data_package_weight_unit import (
    PredictProductPackageDimensionsAndWeightResponseDataPackageWeightUnit,
)

T = TypeVar("T", bound="PredictProductPackageDimensionsAndWeightResponseDataPackageWeight")


@_attrs_define
class PredictProductPackageDimensionsAndWeightResponseDataPackageWeight:
    """
    Attributes:
        unit (PredictProductPackageDimensionsAndWeightResponseDataPackageWeightUnit): Unit of the predicted package
            weight.
            Possible values:
            - `GRAM`
            - `POUND`
            - `OUNCE`
            - `KILOGRAM`
        value (str): Predicted positive package weight.
    """

    unit: PredictProductPackageDimensionsAndWeightResponseDataPackageWeightUnit
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit = self.unit.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unit": unit,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit = PredictProductPackageDimensionsAndWeightResponseDataPackageWeightUnit(d.pop("unit"))

        value = d.pop("value")

        predict_product_package_dimensions_and_weight_response_data_package_weight = cls(
            unit=unit,
            value=value,
        )

        predict_product_package_dimensions_and_weight_response_data_package_weight.additional_properties = d
        return predict_product_package_dimensions_and_weight_response_data_package_weight

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
