from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestShippingFee")


@_attrs_define
class SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestShippingFee:
    """
    Attributes:
        seller_paid_return_shipping_fee_amount (str | Unset): The amount of return shipping fee seller paid.
        buyer_paid_return_shipping_fee_amount (str | Unset): The amount of return shipping fee buyer paid.
        platform_paid_return_shipping_fee_amount (str | Unset): The amount of return shipping fee platform paid.
    """

    seller_paid_return_shipping_fee_amount: str | Unset = UNSET
    buyer_paid_return_shipping_fee_amount: str | Unset = UNSET
    platform_paid_return_shipping_fee_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        seller_paid_return_shipping_fee_amount = self.seller_paid_return_shipping_fee_amount

        buyer_paid_return_shipping_fee_amount = self.buyer_paid_return_shipping_fee_amount

        platform_paid_return_shipping_fee_amount = self.platform_paid_return_shipping_fee_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seller_paid_return_shipping_fee_amount is not UNSET:
            field_dict["seller_paid_return_shipping_fee_amount"] = seller_paid_return_shipping_fee_amount
        if buyer_paid_return_shipping_fee_amount is not UNSET:
            field_dict["buyer_paid_return_shipping_fee_amount"] = buyer_paid_return_shipping_fee_amount
        if platform_paid_return_shipping_fee_amount is not UNSET:
            field_dict["platform_paid_return_shipping_fee_amount"] = platform_paid_return_shipping_fee_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        seller_paid_return_shipping_fee_amount = d.pop("seller_paid_return_shipping_fee_amount", UNSET)

        buyer_paid_return_shipping_fee_amount = d.pop("buyer_paid_return_shipping_fee_amount", UNSET)

        platform_paid_return_shipping_fee_amount = d.pop("platform_paid_return_shipping_fee_amount", UNSET)

        search_aftersales_requests_response_data_aftersales_request_sku_return_request_shipping_fee = cls(
            seller_paid_return_shipping_fee_amount=seller_paid_return_shipping_fee_amount,
            buyer_paid_return_shipping_fee_amount=buyer_paid_return_shipping_fee_amount,
            platform_paid_return_shipping_fee_amount=platform_paid_return_shipping_fee_amount,
        )

        search_aftersales_requests_response_data_aftersales_request_sku_return_request_shipping_fee.additional_properties = d
        return search_aftersales_requests_response_data_aftersales_request_sku_return_request_shipping_fee

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
