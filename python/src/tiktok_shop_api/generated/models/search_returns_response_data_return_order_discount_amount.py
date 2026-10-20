from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchReturnsResponseDataReturnOrderDiscountAmount")


@_attrs_define
class SearchReturnsResponseDataReturnOrderDiscountAmount:
    """
    Attributes:
        currency (str | Unset): The discount currency.
        product_seller_discount (str | Unset): The refund amount of product seller discount.
        shipping_fee_platform_discount (str | Unset): The refund amount of shipping fee platform discount.
        shipping_fee_seller_discount (str | Unset): The refund amount of shipping fee seller discount.
        product_platform_discount (str | Unset): The refund amount of platform discount.
    """

    currency: str | Unset = UNSET
    product_seller_discount: str | Unset = UNSET
    shipping_fee_platform_discount: str | Unset = UNSET
    shipping_fee_seller_discount: str | Unset = UNSET
    product_platform_discount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        product_seller_discount = self.product_seller_discount

        shipping_fee_platform_discount = self.shipping_fee_platform_discount

        shipping_fee_seller_discount = self.shipping_fee_seller_discount

        product_platform_discount = self.product_platform_discount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if product_seller_discount is not UNSET:
            field_dict["product_seller_discount"] = product_seller_discount
        if shipping_fee_platform_discount is not UNSET:
            field_dict["shipping_fee_platform_discount"] = shipping_fee_platform_discount
        if shipping_fee_seller_discount is not UNSET:
            field_dict["shipping_fee_seller_discount"] = shipping_fee_seller_discount
        if product_platform_discount is not UNSET:
            field_dict["product_platform_discount"] = product_platform_discount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        product_seller_discount = d.pop("product_seller_discount", UNSET)

        shipping_fee_platform_discount = d.pop("shipping_fee_platform_discount", UNSET)

        shipping_fee_seller_discount = d.pop("shipping_fee_seller_discount", UNSET)

        product_platform_discount = d.pop("product_platform_discount", UNSET)

        search_returns_response_data_return_order_discount_amount = cls(
            currency=currency,
            product_seller_discount=product_seller_discount,
            shipping_fee_platform_discount=shipping_fee_platform_discount,
            shipping_fee_seller_discount=shipping_fee_seller_discount,
            product_platform_discount=product_platform_discount,
        )

        search_returns_response_data_return_order_discount_amount.additional_properties = d
        return search_returns_response_data_return_order_discount_amount

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
