from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchProductsResponseDataProductSkuPrice")



@_attrs_define
class SearchProductsResponseDataProductSkuPrice:
    """ 
        Attributes:
            currency (str | Unset): The currency.
                Possible values:
                - BRL: Brazil
                - EUR: France, Germany, Ireland, Italy, Spain
                - GBP: United Kingdom
                - IDR: Indonesia
                - JPY: Japan
                - MXN: Mexico
                - MYR: Malaysia
                - PHP: Philippines
                - SGD: Singapore
                - THB: Thailand
                - USD: United States
                - VND: Vietnam
            tax_exclusive_price (str | Unset): **Local sellers/Intra-EU sellers**
                The SKU's **local display price** shown on the product page before any discounts.

                **Global sellers**
                The SKU's **local pre-tax price**. This excludes any applicable charges such as cross-border shipping costs,
                taxes, and other fees, and therefore does not appear on the product page.

                **Note**: Tax-exclusive pricing does not apply to the JP market, therefore this value is the same as
                `sale_price`.
            sale_price (str | Unset): **Global sellers**
                The SKU's **local display price** shown on the product page before any discounts.
            starting_bid_price (str | Unset): starting bid price for auction product
     """

    currency: str | Unset = UNSET
    tax_exclusive_price: str | Unset = UNSET
    sale_price: str | Unset = UNSET
    starting_bid_price: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        tax_exclusive_price = self.tax_exclusive_price

        sale_price = self.sale_price

        starting_bid_price = self.starting_bid_price


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if currency is not UNSET:
            field_dict["currency"] = currency
        if tax_exclusive_price is not UNSET:
            field_dict["tax_exclusive_price"] = tax_exclusive_price
        if sale_price is not UNSET:
            field_dict["sale_price"] = sale_price
        if starting_bid_price is not UNSET:
            field_dict["starting_bid_price"] = starting_bid_price

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        tax_exclusive_price = d.pop("tax_exclusive_price", UNSET)

        sale_price = d.pop("sale_price", UNSET)

        starting_bid_price = d.pop("starting_bid_price", UNSET)

        search_products_response_data_product_sku_price = cls(
            currency=currency,
            tax_exclusive_price=tax_exclusive_price,
            sale_price=sale_price,
            starting_bid_price=starting_bid_price,
        )


        search_products_response_data_product_sku_price.additional_properties = d
        return search_products_response_data_product_sku_price

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
