from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetProductResponseDataSkuPrice")



@_attrs_define
class GetProductResponseDataSkuPrice:
    """ 
        Attributes:
            currency (str | Unset): The currency.
                Possible values based on the region:
                - BRL: Brazil
                - CZK: Czech Republic
                - EUR: France, Germany, Ireland, Italy, Spain, Netherlands, Belgium, Austria, Greece, Portugal
                - GBP: United Kingdom
                - HUF: Hungary
                - IDR: Indonesia
                - JPY: Japan
                - MXN: Mexico
                - MYR: Malaysia
                - PHP: Philippines
                - PLN: Poland
                - SGD: Singapore
                - THB: Thailand
                - USD: United States
                - VND: Vietnam
            sale_price (str | Unset): **All sellers**
                The SKU's **local display price** shown on the product page before any discounts.
            starting_bid_price (str | Unset): starting bid price for auction product
            tax_exclusive_price (str | Unset): **Global sellers**
                The SKU's **local pre-tax price**. This excludes any applicable charges such as cross-border shipping costs,
                taxes, and other fees, and therefore does not appear on the product page.

                **Note**: Tax-exclusive pricing does not apply to JP and US shops using China warehouses, therefore this value
                is the same as `sale_price`.
            unit_price (str | Unset): The unit price of the SKU.
                You can display the unit price to facilitate easier price comparisons across different products and packaging
                sizes.
                Applicable only for the EU market.

                **Note**:
                - This value is available only if you have defined the elements used to calculate this price when creating the
                product.
                - Unit price = Selling price/(SKU unit count/base unit count)
     """

    currency: str | Unset = UNSET
    sale_price: str | Unset = UNSET
    starting_bid_price: str | Unset = UNSET
    tax_exclusive_price: str | Unset = UNSET
    unit_price: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        sale_price = self.sale_price

        starting_bid_price = self.starting_bid_price

        tax_exclusive_price = self.tax_exclusive_price

        unit_price = self.unit_price


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if currency is not UNSET:
            field_dict["currency"] = currency
        if sale_price is not UNSET:
            field_dict["sale_price"] = sale_price
        if starting_bid_price is not UNSET:
            field_dict["starting_bid_price"] = starting_bid_price
        if tax_exclusive_price is not UNSET:
            field_dict["tax_exclusive_price"] = tax_exclusive_price
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        sale_price = d.pop("sale_price", UNSET)

        starting_bid_price = d.pop("starting_bid_price", UNSET)

        tax_exclusive_price = d.pop("tax_exclusive_price", UNSET)

        unit_price = d.pop("unit_price", UNSET)

        get_product_response_data_sku_price = cls(
            currency=currency,
            sale_price=sale_price,
            starting_bid_price=starting_bid_price,
            tax_exclusive_price=tax_exclusive_price,
            unit_price=unit_price,
        )


        get_product_response_data_sku_price.additional_properties = d
        return get_product_response_data_sku_price

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
