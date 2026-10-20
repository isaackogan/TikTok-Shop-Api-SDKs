from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="OriginalPrice")



@_attrs_define
class OriginalPrice:
    """ 
        Attributes:
            currency (str | Unset): The currency in the sale region.
            minimum_amount (str | Unset): The minimum original price of all skus of this product.
            maximum_amount (str | Unset): The maximum original price of all skus of this product.
     """

    currency: str | Unset = UNSET
    minimum_amount: str | Unset = UNSET
    maximum_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        minimum_amount = self.minimum_amount

        maximum_amount = self.maximum_amount


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if currency is not UNSET:
            field_dict["currency"] = currency
        if minimum_amount is not UNSET:
            field_dict["minimum_amount"] = minimum_amount
        if maximum_amount is not UNSET:
            field_dict["maximum_amount"] = maximum_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        minimum_amount = d.pop("minimum_amount", UNSET)

        maximum_amount = d.pop("maximum_amount", UNSET)

        original_price = cls(
            currency=currency,
            minimum_amount=minimum_amount,
            maximum_amount=maximum_amount,
        )


        original_price.additional_properties = d
        return original_price

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
