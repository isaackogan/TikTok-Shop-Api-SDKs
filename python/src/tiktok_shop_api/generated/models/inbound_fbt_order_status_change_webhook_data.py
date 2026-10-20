from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InboundFBTOrderStatusChangeWebhookData")


@_attrs_define
class InboundFBTOrderStatusChangeWebhookData:
    """
    Attributes:
        inbound_order_id (str | Unset): FBT inbound order ID.
        order_status (str | Unset): Inbound order status. Possible enumerations:
            - TO_BE_RECEIVED
            - ARRIVE_HUB,
            - RECEIVING,
            - PARTIALLY_RECEIVED,
            - RECEIVED,
            - CANCELLED
        update_time (int | Unset): The time when the change occurred. Unix timestamp.
    """

    inbound_order_id: str | Unset = UNSET
    order_status: str | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbound_order_id = self.inbound_order_id

        order_status = self.order_status

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inbound_order_id is not UNSET:
            field_dict["inbound_order_id"] = inbound_order_id
        if order_status is not UNSET:
            field_dict["order_status"] = order_status
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inbound_order_id = d.pop("inbound_order_id", UNSET)

        order_status = d.pop("order_status", UNSET)

        update_time = d.pop("update_time", UNSET)

        inbound_fbt_order_status_change_webhook_data = cls(
            inbound_order_id=inbound_order_id,
            order_status=order_status,
            update_time=update_time,
        )

        inbound_fbt_order_status_change_webhook_data.additional_properties = d
        return inbound_fbt_order_status_change_webhook_data

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
