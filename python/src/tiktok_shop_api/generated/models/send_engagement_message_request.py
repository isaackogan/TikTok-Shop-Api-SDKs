from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SendEngagementMessageRequest")


@_attrs_define
class SendEngagementMessageRequest:
    """
    Attributes:
        buyer_emails (list[str]): The anonymized email addresses of the buyers. Retrieve these values from the [Get
            Order Details API](650aa8ccc16ffe02b8f167a0).

            Provide 1 to 50 addresses per request.

            **Note**: You can only send messages to buyers who have placed at least one order with the shop in the past 365
            days.
        task_id (str | Unset): The ID of the associated customer engagement task. Use the value returned when you call
            the [Create Engagement Task API](67777e436b61b002f60f01da).
            **Note**: Ensure the task is still active. You cannot send messages to tasks that have ended.
    """

    buyer_emails: list[str]
    task_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buyer_emails = self.buyer_emails

        task_id = self.task_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buyer_emails": buyer_emails,
            }
        )
        if task_id is not UNSET:
            field_dict["task_id"] = task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        buyer_emails = cast(list[str], d.pop("buyer_emails"))

        task_id = d.pop("task_id", UNSET)

        send_engagement_message_request = cls(
            buyer_emails=buyer_emails,
            task_id=task_id,
        )

        send_engagement_message_request.additional_properties = d
        return send_engagement_message_request

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
