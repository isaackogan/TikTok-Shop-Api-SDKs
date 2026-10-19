from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_creator_conversation_messages_response_data_message_message_body import (
        GetCreatorConversationMessagesResponseDataMessageMessageBody,
    )


T = TypeVar("T", bound="GetCreatorConversationMessagesResponseDataMessage")


@_attrs_define
class GetCreatorConversationMessagesResponseDataMessage:
    """
    Attributes:
        conversation_index (str | Unset): Index of the message in the conversation. Higher index corresponds to newer
            message.
        message_body (GetCreatorConversationMessagesResponseDataMessageMessageBody | Unset):
    """

    conversation_index: str | Unset = UNSET
    message_body: GetCreatorConversationMessagesResponseDataMessageMessageBody | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_index = self.conversation_index

        message_body: dict[str, Any] | Unset = UNSET
        if not isinstance(self.message_body, Unset):
            message_body = self.message_body.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversation_index is not UNSET:
            field_dict["conversation_index"] = conversation_index
        if message_body is not UNSET:
            field_dict["message_body"] = message_body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creator_conversation_messages_response_data_message_message_body import (
            GetCreatorConversationMessagesResponseDataMessageMessageBody,  # noqa: PLC0415
        )

        d = dict(src_dict)
        conversation_index = d.pop("conversation_index", UNSET)

        _message_body = d.pop("message_body", UNSET)
        message_body: GetCreatorConversationMessagesResponseDataMessageMessageBody | Unset
        if isinstance(_message_body, Unset):
            message_body = UNSET
        else:
            message_body = GetCreatorConversationMessagesResponseDataMessageMessageBody.from_dict(_message_body)

        get_creator_conversation_messages_response_data_message = cls(
            conversation_index=conversation_index,
            message_body=message_body,
        )

        get_creator_conversation_messages_response_data_message.additional_properties = d
        return get_creator_conversation_messages_response_data_message

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
