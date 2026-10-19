from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewMessageListenerWebhookDataSender")


@_attrs_define
class NewMessageListenerWebhookDataSender:
    """
    Attributes:
        sender_im_user_id (str | Unset): ID in IM system for the sender.
    """

    sender_im_user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sender_im_user_id = self.sender_im_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sender_im_user_id is not UNSET:
            field_dict["sender_im_user_id"] = sender_im_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sender_im_user_id = d.pop("sender_im_user_id", UNSET)

        new_message_listener_webhook_data_sender = cls(
            sender_im_user_id=sender_im_user_id,
        )

        new_message_listener_webhook_data_sender.additional_properties = d
        return new_message_listener_webhook_data_sender

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
