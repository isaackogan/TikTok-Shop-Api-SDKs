from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShippingTemplateAvailabilityRequestProductAttributeWeight")


@_attrs_define
class GetShippingTemplateAvailabilityRequestProductAttributeWeight:
    """
    Attributes:
        weight (str | Unset): The weight of product
        unit (int | Unset): 1:gram
            2:pound
            3:ounce
            4:kilogram
    """

    weight: str | Unset = UNSET
    unit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weight = self.weight

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weight is not UNSET:
            field_dict["weight"] = weight
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        weight = d.pop("weight", UNSET)

        unit = d.pop("unit", UNSET)

        get_shipping_template_availability_request_product_attribute_weight = cls(
            weight=weight,
            unit=unit,
        )

        get_shipping_template_availability_request_product_attribute_weight.additional_properties = d
        return get_shipping_template_availability_request_product_attribute_weight

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
