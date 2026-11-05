from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PriceRange")



@_attrs_define
class PriceRange:
    """ 
        Attributes:
            max_price (str | Unset): Maximum product price encoded as a decimal numeric string.
            max_price_format (str | Unset): Formatted maximum product price, which may include a currency symbol.
            min_price (str | Unset): Minimum product price encoded as a decimal numeric string.
            min_price_format (str | Unset): Formatted minimum product price, which may include a currency symbol.
     """

    max_price: str | Unset = UNSET
    max_price_format: str | Unset = UNSET
    min_price: str | Unset = UNSET
    min_price_format: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        max_price = self.max_price

        max_price_format = self.max_price_format

        min_price = self.min_price

        min_price_format = self.min_price_format


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if max_price is not UNSET:
            field_dict["max_price"] = max_price
        if max_price_format is not UNSET:
            field_dict["max_price_format"] = max_price_format
        if min_price is not UNSET:
            field_dict["min_price"] = min_price
        if min_price_format is not UNSET:
            field_dict["min_price_format"] = min_price_format

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_price = d.pop("max_price", UNSET)

        max_price_format = d.pop("max_price_format", UNSET)

        min_price = d.pop("min_price", UNSET)

        min_price_format = d.pop("min_price_format", UNSET)

        price_range = cls(
            max_price=max_price,
            max_price_format=max_price_format,
            min_price=min_price,
            min_price_format=min_price_format,
        )


        price_range.additional_properties = d
        return price_range

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
