from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_global_product_response_data_sku_price_currency import GetGlobalProductResponseDataSkuPriceCurrency
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGlobalProductResponseDataSkuPrice")


@_attrs_define
class GetGlobalProductResponseDataSkuPrice:
    """
    Attributes:
        amount (str | Unset): The price amount.
        currency (GetGlobalProductResponseDataSkuPriceCurrency | Unset): The currency.
            Possible values:
            - `USD`: Applicable for global sellers
            - `EUR`: Applicable for intra-EU sellers
        unit_price (str | Unset): The unit price of the SKU.
            You can display the unit price to facilitate easier price comparisons across different products and packaging
            sizes.
            Applicable only for the EU market.

            **Note**:
            - This value is available only if you have defined the elements used to calculate this price when creating the
            product.
            - Unit price = Selling price/(SKU unit count/base unit count)
    """

    amount: str | Unset = UNSET
    currency: GetGlobalProductResponseDataSkuPriceCurrency | Unset = UNSET
    unit_price: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency: str | Unset = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.value

        unit_price = self.unit_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: GetGlobalProductResponseDataSkuPriceCurrency | Unset
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = GetGlobalProductResponseDataSkuPriceCurrency(_currency)

        unit_price = d.pop("unit_price", UNSET)

        get_global_product_response_data_sku_price = cls(
            amount=amount,
            currency=currency,
            unit_price=unit_price,
        )

        get_global_product_response_data_sku_price.additional_properties = d
        return get_global_product_response_data_sku_price

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
