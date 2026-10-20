from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchReturnsResponseDataReturnOrderShippingFeeAmount")



@_attrs_define
class SearchReturnsResponseDataReturnOrderShippingFeeAmount:
    """ 
        Attributes:
            currency (str | Unset): Return shipping fee currency.
            seller_paid_return_shipping_fee (str | Unset): The amount of return shipping fee seller paid.
            platform_paid_return_shipping_fee (str | Unset): The amount of return shipping fee platform paid.
            buyer_paid_return_shipping_fee (str | Unset): The amount of return shipping fee buyer paid.
     """

    currency: str | Unset = UNSET
    seller_paid_return_shipping_fee: str | Unset = UNSET
    platform_paid_return_shipping_fee: str | Unset = UNSET
    buyer_paid_return_shipping_fee: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        seller_paid_return_shipping_fee = self.seller_paid_return_shipping_fee

        platform_paid_return_shipping_fee = self.platform_paid_return_shipping_fee

        buyer_paid_return_shipping_fee = self.buyer_paid_return_shipping_fee


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if currency is not UNSET:
            field_dict["currency"] = currency
        if seller_paid_return_shipping_fee is not UNSET:
            field_dict["seller_paid_return_shipping_fee"] = seller_paid_return_shipping_fee
        if platform_paid_return_shipping_fee is not UNSET:
            field_dict["platform_paid_return_shipping_fee"] = platform_paid_return_shipping_fee
        if buyer_paid_return_shipping_fee is not UNSET:
            field_dict["buyer_paid_return_shipping_fee"] = buyer_paid_return_shipping_fee

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        seller_paid_return_shipping_fee = d.pop("seller_paid_return_shipping_fee", UNSET)

        platform_paid_return_shipping_fee = d.pop("platform_paid_return_shipping_fee", UNSET)

        buyer_paid_return_shipping_fee = d.pop("buyer_paid_return_shipping_fee", UNSET)

        search_returns_response_data_return_order_shipping_fee_amount = cls(
            currency=currency,
            seller_paid_return_shipping_fee=seller_paid_return_shipping_fee,
            platform_paid_return_shipping_fee=platform_paid_return_shipping_fee,
            buyer_paid_return_shipping_fee=buyer_paid_return_shipping_fee,
        )


        search_returns_response_data_return_order_shipping_fee_amount.additional_properties = d
        return search_returns_response_data_return_order_shipping_fee_amount

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
