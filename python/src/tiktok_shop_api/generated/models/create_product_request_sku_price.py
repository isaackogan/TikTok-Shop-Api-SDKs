from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_product_request_sku_price_currency import CreateProductRequestSkuPriceCurrency
from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateProductRequestSkuPrice")



@_attrs_define
class CreateProductRequestSkuPrice:
    """ 
        Attributes:
            currency (CreateProductRequestSkuPriceCurrency): The currency.
                Possible values based on the region:
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
            amount (str | Unset): **Local sellers/Intra-EU sellers**
                The SKU's **local display price** shown on the product page before any discounts. Refer to [Product
                Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) for the allowed price ranges in
                each market.
            sale_price (str | Unset): **Global sellers**
                The SKU's **local display price** shown on the product page before any discounts.
                Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) for the allowed
                price ranges in each market.

                **Note**:
                - Applicable only for global sellers.
                -  Required for JP and US shops using China warehouses, optional for others.
                - This is the definitive final price shown on the product page, all other prices will be ignored.
            starting_bid_price (str | Unset): starting bit price for auction product
     """

    currency: CreateProductRequestSkuPriceCurrency
    amount: str | Unset = UNSET
    sale_price: str | Unset = UNSET
    starting_bid_price: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        currency = self.currency.value

        amount = self.amount

        sale_price = self.sale_price

        starting_bid_price = self.starting_bid_price


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "currency": currency,
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if sale_price is not UNSET:
            field_dict["sale_price"] = sale_price
        if starting_bid_price is not UNSET:
            field_dict["starting_bid_price"] = starting_bid_price

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = CreateProductRequestSkuPriceCurrency(d.pop("currency"))




        amount = d.pop("amount", UNSET)

        sale_price = d.pop("sale_price", UNSET)

        starting_bid_price = d.pop("starting_bid_price", UNSET)

        create_product_request_sku_price = cls(
            currency=currency,
            amount=amount,
            sale_price=sale_price,
            starting_bid_price=starting_bid_price,
        )


        create_product_request_sku_price.additional_properties = d
        return create_product_request_sku_price

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
