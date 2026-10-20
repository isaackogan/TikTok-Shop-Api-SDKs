from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIsr")



@_attrs_define
class SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIsr:
    """ 
        Attributes:
            amount (str | Unset): The actual ISR tax amount without a currency symbol. Use `currency` to identify the
                currency.
            currency (str | Unset): Type of currency use
     """

    amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        search_tap_affiliate_orders_response_data_sku_order_actual_partner_isr = cls(
            amount=amount,
            currency=currency,
        )


        search_tap_affiliate_orders_response_data_sku_order_actual_partner_isr.additional_properties = d
        return search_tap_affiliate_orders_response_data_sku_order_actual_partner_isr

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
