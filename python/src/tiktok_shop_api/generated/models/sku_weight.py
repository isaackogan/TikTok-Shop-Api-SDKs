from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SkuWeight")



@_attrs_define
class SkuWeight:
    """ 
        Attributes:
            value (str): The package weight, which must be a positive number.
                The number format varies based on the unit:
                - GRAM: integer
                - KILOGRAM: up to 3 decimal places
                - POUND: up to 2 decimal places
            unit (str): The unit for the SKU weight.
                Possible values based on region:
                - US: KILOGRAM, POUND
                - BR, JP, MX: KILOGRAM, GRAM
                - Other countries: KILOGRAM

                Note: Use the same measurement system (metric or imperial) for `sku_weight` and `sku_dimensions`. For example,
                use `KILOGRAM` with `CENTIMETER`.
     """

    value: str
    unit: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        value = self.value

        unit = self.unit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "value": value,
            "unit": unit,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        unit = d.pop("unit")

        sku_weight = cls(
            value=value,
            unit=unit,
        )


        sku_weight.additional_properties = d
        return sku_weight

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
