from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SalesPriceRange")



@_attrs_define
class SalesPriceRange:
    """ 
        Attributes:
            amount_ge (str | Unset): The product price must be greater than this value in order to be included in the search
                results. The value must be greater than `0`.
            amount_lt (str | Unset): The product price must be greater than this value in order to be included in the search
                results. The value must be greater than `0`. No upper bound is set if this property is not included.
     """

    amount_ge: str | Unset = UNSET
    amount_lt: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount_ge = self.amount_ge

        amount_lt = self.amount_lt


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount_ge is not UNSET:
            field_dict["amount_ge"] = amount_ge
        if amount_lt is not UNSET:
            field_dict["amount_lt"] = amount_lt

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount_ge = d.pop("amount_ge", UNSET)

        amount_lt = d.pop("amount_lt", UNSET)

        sales_price_range = cls(
            amount_ge=amount_ge,
            amount_lt=amount_lt,
        )


        sales_price_range.additional_properties = d
        return sales_price_range

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
