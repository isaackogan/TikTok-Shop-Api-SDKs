from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.external_list_price_currency import ExternalListPriceCurrency
from ..models.external_list_price_source import ExternalListPriceSource






T = TypeVar("T", bound="ExternalListPrice")



@_attrs_define
class ExternalListPrice:
    """ 
        Attributes:
            source (ExternalListPriceSource): The external ecommerce platform from which the price is sourced.
                Possible values:
                - SHOPIFY_COMPARE_AT_PRICE: The compare_at_price in Shopify.
            amount (str): The price amount.
                Valid range: [0.01, 7600]
            currency (ExternalListPriceCurrency): The currency.
                Possible values: USD
     """

    source: ExternalListPriceSource
    amount: str
    currency: ExternalListPriceCurrency
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        source = self.source.value

        amount = self.amount

        currency = self.currency.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "source": source,
            "amount": amount,
            "currency": currency,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = ExternalListPriceSource(d.pop("source"))




        amount = d.pop("amount")

        currency = ExternalListPriceCurrency(d.pop("currency"))




        external_list_price = cls(
            source=source,
            amount=amount,
            currency=currency,
        )


        external_list_price.additional_properties = d
        return external_list_price

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
