from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CancellationStatusChangeWebhookData")



@_attrs_define
class CancellationStatusChangeWebhookData:
    """ 
        Attributes:
            order_id (str | Unset): The identification of a TikTok Shop order
            cancellations_role (str | Unset): The user who initiated a cancellation, with possible values:

                 * BUYER
                 * SELLER
                 * SYSTEM
            cancel_status (str | Unset): Order cancellation status, with possible values:

                 * CANCELLATION_REQUEST_PENDING
                 * CANCELLATION_REQUEST_SUCCESS
                 * CANCELLATION_REQUEST_CANCELLED
                 * CANCELLATION_REQUEST_COMPLETE
            cancel_id (str | Unset): The identifier of a specific order cancellation
            create_time (int | Unset): The time when the buyer initiated the cancellation request, represented as a Unix
                timestamp (seconds).
     """

    order_id: str | Unset = UNSET
    cancellations_role: str | Unset = UNSET
    cancel_status: str | Unset = UNSET
    cancel_id: str | Unset = UNSET
    create_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        cancellations_role = self.cancellations_role

        cancel_status = self.cancel_status

        cancel_id = self.cancel_id

        create_time = self.create_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if cancellations_role is not UNSET:
            field_dict["cancellations_role"] = cancellations_role
        if cancel_status is not UNSET:
            field_dict["cancel_status"] = cancel_status
        if cancel_id is not UNSET:
            field_dict["cancel_id"] = cancel_id
        if create_time is not UNSET:
            field_dict["create_time"] = create_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        cancellations_role = d.pop("cancellations_role", UNSET)

        cancel_status = d.pop("cancel_status", UNSET)

        cancel_id = d.pop("cancel_id", UNSET)

        create_time = d.pop("create_time", UNSET)

        cancellation_status_change_webhook_data = cls(
            order_id=order_id,
            cancellations_role=cancellations_role,
            cancel_status=cancel_status,
            cancel_id=cancel_id,
            create_time=create_time,
        )


        cancellation_status_change_webhook_data.additional_properties = d
        return cancellation_status_change_webhook_data

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
