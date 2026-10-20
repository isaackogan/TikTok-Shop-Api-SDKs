from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubmitStrikethroughPriceRequestSkuExternalRetailPrice")


@_attrs_define
class SubmitStrikethroughPriceRequestSkuExternalRetailPrice:
    """
    Attributes:
        amount (str): The retail price amount. The valid range is 0.01 to 7600.
        currency (str): The ISO 4217 currency code. The supported value is `USD`.
    """

    amount: str
    currency: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency = self.currency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "currency": currency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        currency = d.pop("currency")

        submit_strikethrough_price_request_sku_external_retail_price = cls(
            amount=amount,
            currency=currency,
        )

        submit_strikethrough_price_request_sku_external_retail_price.additional_properties = d
        return submit_strikethrough_price_request_sku_external_retail_price

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
