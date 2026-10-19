from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.weight_unit import WeightUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="Weight")


@_attrs_define
class Weight:
    """
    Attributes:
        value (str | Unset): The numerical value of the package weight.
        unit (WeightUnit | Unset): The unit of measurement for the package weight.

            Available values:
            - `GRAM`
            - `POUND`
    """

    value: str | Unset = UNSET
    unit: WeightUnit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: WeightUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = WeightUnit(_unit)

        weight = cls(
            value=value,
            unit=unit,
        )

        weight.additional_properties = d
        return weight

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
