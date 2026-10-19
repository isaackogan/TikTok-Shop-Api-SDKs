from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_product_response_data_sku_external_list_price_currency import (
    GetProductResponseDataSkuExternalListPriceCurrency,
)
from ..models.get_product_response_data_sku_external_list_price_source import (
    GetProductResponseDataSkuExternalListPriceSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductResponseDataSkuExternalListPrice")


@_attrs_define
class GetProductResponseDataSkuExternalListPrice:
    """
    Attributes:
        amount (str | Unset): The price amount.
        currency (GetProductResponseDataSkuExternalListPriceCurrency | Unset): The currency.
            Possible values: USD
        source (GetProductResponseDataSkuExternalListPriceSource | Unset): The external ecommerce platform from which
            the price is sourced.
            Possible values:
            - SHOPIFY_COMPARE_AT_PRICE: The compare_at_price in Shopify.
    """

    amount: str | Unset = UNSET
    currency: GetProductResponseDataSkuExternalListPriceCurrency | Unset = UNSET
    source: GetProductResponseDataSkuExternalListPriceSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency: str | Unset = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.value

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        _currency = d.pop("currency", UNSET)
        currency: GetProductResponseDataSkuExternalListPriceCurrency | Unset
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = GetProductResponseDataSkuExternalListPriceCurrency(_currency)

        _source = d.pop("source", UNSET)
        source: GetProductResponseDataSkuExternalListPriceSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = GetProductResponseDataSkuExternalListPriceSource(_source)

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
