from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestDiscount")


@_attrs_define
class SearchAftersalesRequestsResponseDataAftersalesRequestSkuReturnRequestDiscount:
    """
    Attributes:
        product_platform_discount (str | Unset): The refund amount of platform discount.
        product_seller_discount (str | Unset): The refund amount of product seller discount.
        shipping_fee_platform_discount (str | Unset): The refund amount of shipping fee platform discount.
        shipping_fee_seller_discount (str | Unset): The refund amount of shipping fee seller discount.
    """

    product_platform_discount: str | Unset = UNSET
    product_seller_discount: str | Unset = UNSET
    shipping_fee_platform_discount: str | Unset = UNSET
    shipping_fee_seller_discount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_platform_discount = self.product_platform_discount

        product_seller_discount = self.product_seller_discount

        shipping_fee_platform_discount = self.shipping_fee_platform_discount

        shipping_fee_seller_discount = self.shipping_fee_seller_discount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_platform_discount is not UNSET:
            field_dict["product_platform_discount"] = product_platform_discount
        if product_seller_discount is not UNSET:
            field_dict["product_seller_discount"] = product_seller_discount
        if shipping_fee_platform_discount is not UNSET:
            field_dict["shipping_fee_platform_discount"] = shipping_fee_platform_discount
        if shipping_fee_seller_discount is not UNSET:
            field_dict["shipping_fee_seller_discount"] = shipping_fee_seller_discount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_platform_discount = d.pop("product_platform_discount", UNSET)

        product_seller_discount = d.pop("product_seller_discount", UNSET)

        shipping_fee_platform_discount = d.pop("shipping_fee_platform_discount", UNSET)

        shipping_fee_seller_discount = d.pop("shipping_fee_seller_discount", UNSET)

        search_aftersales_requests_response_data_aftersales_request_sku_return_request_discount = cls(
            product_platform_discount=product_platform_discount,
            product_seller_discount=product_seller_discount,
            shipping_fee_platform_discount=shipping_fee_platform_discount,
            shipping_fee_seller_discount=shipping_fee_seller_discount,
        )

        search_aftersales_requests_response_data_aftersales_request_sku_return_request_discount.additional_properties = d
        return search_aftersales_requests_response_data_aftersales_request_sku_return_request_discount

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
