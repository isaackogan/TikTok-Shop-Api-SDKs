from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetProductResponseDataSkuExternalListPrice")



@_attrs_define
class GetProductResponseDataSkuExternalListPrice:
    """ 
        Attributes:
            amount (str | Unset): The price amount.
            currency (str | Unset): The currency.
                Possible values: USD
            source (str | Unset): The external ecommerce platform from which the price is sourced.
                Possible values:
                - SHOPIFY_COMPARE_AT_PRICE: The compare_at_price in Shopify.
     """

    amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency = self.currency

        source = self.source


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        source = d.pop("source", UNSET)

        get_product_response_data_sku_external_list_price = cls(
            amount=amount,
            currency=currency,
            source=source,
        )


        get_product_response_data_sku_external_list_price.additional_properties = d
        return get_product_response_data_sku_external_list_price

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
