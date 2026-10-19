from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_product_request_replicated_product_sku_price_currency import (
    EditProductRequestReplicatedProductSkuPriceCurrency,
)

T = TypeVar("T", bound="EditProductRequestReplicatedProductSkuPrice")


@_attrs_define
class EditProductRequestReplicatedProductSkuPrice:
    """
    Attributes:
        currency (EditProductRequestReplicatedProductSkuPriceCurrency): The currency. You must specify the local
            currency in the target market.
            Possible values:
            - EUR: France, Germany, Ireland, Italy, Spain
            - GBP: United Kingdom
            - IDR: Indonesia
            - JPY: Japanese
            - MYR: Malaysia
            - PHP: Philippines
            - SGD: Singapore
            - THB: Thailand
            - USD: United States
            - VND: Vietnam
        sale_price (str): The SKU's local display price shown on the product page before any discounts.
            Refer to [Product Pricing](https://partner.tiktokshop.com/docv2/page/67e1288d76cfee049d9af858) for the allowed
            price ranges in each market.
    """

    currency: EditProductRequestReplicatedProductSkuPriceCurrency
    sale_price: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency.value

        sale_price = self.sale_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "sale_price": sale_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = EditProductRequestReplicatedProductSkuPriceCurrency(d.pop("currency"))

        sale_price = d.pop("sale_price")

        edit_product_request_replicated_product_sku_price = cls(
            currency=currency,
            sale_price=sale_price,
        )

        edit_product_request_replicated_product_sku_price.additional_properties = d
        return edit_product_request_replicated_product_sku_price

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
