from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_seller_affiliate_orders_response_data_order import SearchSellerAffiliateOrdersResponseDataOrder


T = TypeVar("T", bound="SearchSellerAffiliateOrdersResponseData")


@_attrs_define
class SearchSellerAffiliateOrdersResponseData:
    """
    Attributes:
        orders (list[SearchSellerAffiliateOrdersResponseDataOrder] | Unset): The orders represented by the SKU-order
            records selected for this page, grouped by order ID. Pagination is applied before grouping, so `orders` can
            contain fewer objects than `page_size`, and SKU entries for the same order can appear on different pages.
            Aggregate SKU entries with the same order ID across all retrieved pages.
        next_page_token (str | Unset): An opaque token for retrieving the next page. To keep the effective time filter
            fixed across pages, provide explicit `create_time_ge` and `create_time_lt` values in the first request. If this
            value is non-empty, pass it as `page_token` in the next request and reuse those exact time values and the same
            `program_id` value or omission. An empty string indicates that there is no next page.
        total_count (int | Unset): The total number of sku orders that matches the query conditions.
    """

    orders: list[SearchSellerAffiliateOrdersResponseDataOrder] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)

        next_page_token = self.next_page_token

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if orders is not UNSET:
            field_dict["orders"] = orders
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_seller_affiliate_orders_response_data_order import (
            SearchSellerAffiliateOrdersResponseDataOrder,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _orders = d.pop("orders", UNSET)
        orders: list[SearchSellerAffiliateOrdersResponseDataOrder] | Unset = UNSET
        if _orders is not UNSET:
            orders = []
            for orders_item_data in _orders:
                orders_item = SearchSellerAffiliateOrdersResponseDataOrder.from_dict(orders_item_data)

                orders.append(orders_item)

        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        search_seller_affiliate_orders_response_data = cls(
            orders=orders,
            next_page_token=next_page_token,
            total_count=total_count,
        )

        search_seller_affiliate_orders_response_data.additional_properties = d
        return search_seller_affiliate_orders_response_data

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
