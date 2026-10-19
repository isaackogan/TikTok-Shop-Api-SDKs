from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_status_change_webhook_data_order_status import OrderStatusChangeWebhookDataOrderStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderStatusChangeWebhookData")


@_attrs_define
class OrderStatusChangeWebhookData:
    """
    Attributes:
        order_id (str | Unset): The identification of a TikTok Shop order
        order_status (OrderStatusChangeWebhookDataOrderStatus | Unset): The most recent order status, with possible
            values:

             * `UNPAID`
             * `ON_HOLD`
             * `AWAITING_SHIPMENT`
             * `AWAITING_COLLECTION`
             * `CANCEL`
             * `IN_TRANSIT`
             * `DELIVERED`
             * `COMPLETED`
        is_on_hold_order (bool | Unset): Indicates whether the order has experienced or will experience `ON_HOLD` status
        update_time (int | Unset): The order status update time, represented as a Unix timestamp (seconds).
    """

    order_id: str | Unset = UNSET
    order_status: OrderStatusChangeWebhookDataOrderStatus | Unset = UNSET
    is_on_hold_order: bool | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        order_status: str | Unset = UNSET
        if not isinstance(self.order_status, Unset):
            order_status = self.order_status.value

        is_on_hold_order = self.is_on_hold_order

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if order_status is not UNSET:
            field_dict["order_status"] = order_status
        if is_on_hold_order is not UNSET:
            field_dict["is_on_hold_order"] = is_on_hold_order
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        _order_status = d.pop("order_status", UNSET)
        order_status: OrderStatusChangeWebhookDataOrderStatus | Unset
        if isinstance(_order_status, Unset):
            order_status = UNSET
        else:
            order_status = OrderStatusChangeWebhookDataOrderStatus(_order_status)

        is_on_hold_order = d.pop("is_on_hold_order", UNSET)

        update_time = d.pop("update_time", UNSET)

        order_status_change_webhook_data = cls(
            order_id=order_id,
            order_status=order_status,
            is_on_hold_order=is_on_hold_order,
            update_time=update_time,
        )

        order_status_change_webhook_data.additional_properties = d
        return order_status_change_webhook_data

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
