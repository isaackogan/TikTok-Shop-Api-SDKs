from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.list_price_currency import ListPriceCurrency

T = TypeVar("T", bound="ListPrice")


@_attrs_define
class ListPrice:
    """
    Attributes:
        amount (str): The price amount.
            Valid range: [0.01, 7600]

            **Note**: The value must be equal to or greater than `skus.price.amount`. Otherwise, it will be discarded.
        currency (ListPriceCurrency): The currency.
            Possible values: USD
    """

    amount: str
    currency: ListPriceCurrency
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency = self.currency.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        currency = ListPriceCurrency(d.pop("currency"))

        list_price = cls(
            amount=amount,
            currency=currency,
        )

        list_price.additional_properties = d
        return list_price

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
