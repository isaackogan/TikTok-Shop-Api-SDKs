from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetEngagementTaskPerformancesResponseDataTaskPerformance")



@_attrs_define
class GetEngagementTaskPerformancesResponseDataTaskPerformance:
    """ 
        Attributes:
            id (str | Unset): The customer engagement task ID for this performance record.
            status (str | Unset): The status of the task.
                Possible values:
                - `UNKNOWN`: The task status is unknown.
                - `DRAFT`: The task is in draft status.
                - `WAITING`: The task is waiting.
                - `SENDING`: The task is sending messages.
                - `FAILED`: The task failed to send messages.
                - `CANCELED`: The task was canceled.
                - `SUCCESS`: The task completed successfully.
                - `DELETED`: The task was deleted.
            sent_recipient_count (int | Unset): The number of users that received the message.
            read_recipient_count (int | Unset): The number of users that read the message.
            order_count (int | Unset): The number of orders resulting from the message.
            gmv_amount (str | Unset): The revenue from the converted orders.
            claimed_coupons_count (int | Unset): The number of coupons claimed.
     """

    id: str | Unset = UNSET
    status: str | Unset = UNSET
    sent_recipient_count: int | Unset = UNSET
    read_recipient_count: int | Unset = UNSET
    order_count: int | Unset = UNSET
    gmv_amount: str | Unset = UNSET
    claimed_coupons_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        sent_recipient_count = self.sent_recipient_count

        read_recipient_count = self.read_recipient_count

        order_count = self.order_count

        gmv_amount = self.gmv_amount

        claimed_coupons_count = self.claimed_coupons_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if sent_recipient_count is not UNSET:
            field_dict["sent_recipient_count"] = sent_recipient_count
        if read_recipient_count is not UNSET:
            field_dict["read_recipient_count"] = read_recipient_count
        if order_count is not UNSET:
            field_dict["order_count"] = order_count
        if gmv_amount is not UNSET:
            field_dict["gmv_amount"] = gmv_amount
        if claimed_coupons_count is not UNSET:
            field_dict["claimed_coupons_count"] = claimed_coupons_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        sent_recipient_count = d.pop("sent_recipient_count", UNSET)

        read_recipient_count = d.pop("read_recipient_count", UNSET)

        order_count = d.pop("order_count", UNSET)

        gmv_amount = d.pop("gmv_amount", UNSET)

        claimed_coupons_count = d.pop("claimed_coupons_count", UNSET)

        get_engagement_task_performances_response_data_task_performance = cls(
            id=id,
            status=status,
            sent_recipient_count=sent_recipient_count,
            read_recipient_count=read_recipient_count,
            order_count=order_count,
            gmv_amount=gmv_amount,
            claimed_coupons_count=claimed_coupons_count,
        )


        get_engagement_task_performances_response_data_task_performance.additional_properties = d
        return get_engagement_task_performances_response_data_task_performance

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
