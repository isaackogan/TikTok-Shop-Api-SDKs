from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWarehouseDeliveryOptionsResponseDataDeliveryOptionWeightLimit")


@_attrs_define
class GetWarehouseDeliveryOptionsResponseDataDeliveryOptionWeightLimit:
    """
    Attributes:
        max_weight (int | Unset): Maximum weight limit.
        min_weight (int | Unset): Minimum weight limit.
        unit (str | Unset): The unit of measurement for the weight.
            Possible values:
            - GRAM
            - POUND
            - OUNCE
            - KILOGRAM
    """

    max_weight: int | Unset = UNSET
    min_weight: int | Unset = UNSET
    unit: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_weight = self.max_weight

        min_weight = self.min_weight

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_weight is not UNSET:
            field_dict["max_weight"] = max_weight
        if min_weight is not UNSET:
            field_dict["min_weight"] = min_weight
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_weight = d.pop("max_weight", UNSET)

        min_weight = d.pop("min_weight", UNSET)

        unit = d.pop("unit", UNSET)

        get_warehouse_delivery_options_response_data_delivery_option_weight_limit = cls(
            max_weight=max_weight,
            min_weight=min_weight,
            unit=unit,
        )

        get_warehouse_delivery_options_response_data_delivery_option_weight_limit.additional_properties = d
        return get_warehouse_delivery_options_response_data_delivery_option_weight_limit

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
