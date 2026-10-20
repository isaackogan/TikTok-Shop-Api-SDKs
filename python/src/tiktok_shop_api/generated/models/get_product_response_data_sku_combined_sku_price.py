from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductResponseDataSkuCombinedSkuPrice")


@_attrs_define
class GetProductResponseDataSkuCombinedSkuPrice:
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
        sale_price (str | Unset): All sellers
            The source SKU's local display price shown on the product page before any discounts.
        tax_exclusive_price (str | Unset): Global sellers
            The source SKU's local pre-tax price. This excludes any applicable charges such as cross-border shipping costs,
            taxes, and other fees, and therefore does not appear on the product page.

            Note: Tax-exclusive pricing does not apply to JP and US shops using China warehouses, therefore this value is
            the same as sale_price.
    """

    currency: str | Unset = UNSET
    sale_price: str | Unset = UNSET
    tax_exclusive_price: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        sale_price = self.sale_price

        tax_exclusive_price = self.tax_exclusive_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if sale_price is not UNSET:
            field_dict["sale_price"] = sale_price
        if tax_exclusive_price is not UNSET:
            field_dict["tax_exclusive_price"] = tax_exclusive_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        sale_price = d.pop("sale_price", UNSET)

        tax_exclusive_price = d.pop("tax_exclusive_price", UNSET)

        get_product_response_data_sku_combined_sku_price = cls(
            currency=currency,
            sale_price=sale_price,
            tax_exclusive_price=tax_exclusive_price,
        )

        get_product_response_data_sku_combined_sku_price.additional_properties = d
        return get_product_response_data_sku_combined_sku_price

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
