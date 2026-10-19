from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_order_list_response_data_order import GetOrderListResponseDataOrder


T = TypeVar("T", bound="GetOrderListResponseData")


@_attrs_define
class GetOrderListResponseData:
    """
    Attributes:
        next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. Provide
            this value in the `page_token` parameter of your request if the current response does not return all the
            results.
        total_count (int | Unset): Total number of orders in the search result.
        orders (list[GetOrderListResponseDataOrder] | Unset): Order information.
    """

    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    orders: list[GetOrderListResponseDataOrder] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_page_token = self.next_page_token

        total_count = self.total_count

        orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if orders is not UNSET:
            field_dict["orders"] = orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_order_list_response_data_order import GetOrderListResponseDataOrder  # noqa: PLC0415

        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        _orders = d.pop("orders", UNSET)
        orders: list[GetOrderListResponseDataOrder] | Unset = UNSET
        if _orders is not UNSET:
            orders = []
            for orders_item_data in _orders:
                orders_item = GetOrderListResponseDataOrder.from_dict(orders_item_data)

                orders.append(orders_item)

        get_order_list_response_data = cls(
            next_page_token=next_page_token,
            total_count=total_count,
            orders=orders,
        )

        get_order_list_response_data.additional_properties = d
        return get_order_list_response_data

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
