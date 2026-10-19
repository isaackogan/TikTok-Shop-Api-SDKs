from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_products_response_data_product_sku_external_list_price_currency import (
    SearchProductsResponseDataProductSkuExternalListPriceCurrency,
)
from ..models.search_products_response_data_product_sku_external_list_price_source import (
    SearchProductsResponseDataProductSkuExternalListPriceSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchProductsResponseDataProductSkuExternalListPrice")


@_attrs_define
class SearchProductsResponseDataProductSkuExternalListPrice:
    """
    Attributes:
        source (SearchProductsResponseDataProductSkuExternalListPriceSource | Unset): The external ecommerce platform
            from which the price is sourced.
            Possible values:
            - SHOPIFY_COMPARE_AT_PRICE: The compare_at_price in Shopify.
        amount (str | Unset): The price amount.
        currency (SearchProductsResponseDataProductSkuExternalListPriceCurrency | Unset): The currency.
            Possible values: USD
    """

    source: SearchProductsResponseDataProductSkuExternalListPriceSource | Unset = UNSET
    amount: str | Unset = UNSET
    currency: SearchProductsResponseDataProductSkuExternalListPriceCurrency | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        amount = self.amount

        currency: str | Unset = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _source = d.pop("source", UNSET)
        source: SearchProductsResponseDataProductSkuExternalListPriceSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = SearchProductsResponseDataProductSkuExternalListPriceSource(_source)

        amount = d.pop("amount", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: SearchProductsResponseDataProductSkuExternalListPriceCurrency | Unset
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = SearchProductsResponseDataProductSkuExternalListPriceCurrency(_currency)

        search_products_response_data_product_sku_external_list_price = cls(
            source=source,
            amount=amount,
            currency=currency,
        )

        search_products_response_data_product_sku_external_list_price.additional_properties = d
        return search_products_response_data_product_sku_external_list_price

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
