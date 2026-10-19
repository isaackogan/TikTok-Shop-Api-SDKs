from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_message_webhook_data_sender_role import NewMessageWebhookDataSenderRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewMessageWebhookDataSender")


@_attrs_define
class NewMessageWebhookDataSender:
    """
    Attributes:
        im_user_id (str | Unset): Sender's ID
             These are IM IDs, and can not be used to query orders.
        role (NewMessageWebhookDataSenderRole | Unset): Sender's role, with possible values:
             * BUYER
             * SHOP
             * CUSTOMER_SERVICE
             * SYSTEM
             * ROBOT
    """

    im_user_id: str | Unset = UNSET
    role: NewMessageWebhookDataSenderRole | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        im_user_id = self.im_user_id

        role: str | Unset = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if im_user_id is not UNSET:
            field_dict["im_user_id"] = im_user_id
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        im_user_id = d.pop("im_user_id", UNSET)

        _role = d.pop("role", UNSET)
        role: NewMessageWebhookDataSenderRole | Unset
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = NewMessageWebhookDataSenderRole(_role)

        new_message_webhook_data_sender = cls(
            im_user_id=im_user_id,
            role=role,
        )

        new_message_webhook_data_sender.additional_properties = d
        return new_message_webhook_data_sender

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
