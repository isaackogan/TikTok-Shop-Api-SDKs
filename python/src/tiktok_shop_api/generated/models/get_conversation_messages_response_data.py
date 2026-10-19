from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_conversation_messages_response_data_message import GetConversationMessagesResponseDataMessage


T = TypeVar("T", bound="GetConversationMessagesResponseData")


@_attrs_define
class GetConversationMessagesResponseData:
    """
    Attributes:
        next_page_token (str | Unset): The index indicates where we should start on the next page.
            If there is no more record, this field will be ""(empty string).
            Put this value to request param "page_token" for the next page query.
        unsupported_msg_tips (str | Unset): If your app encounters a message type it doesn't support, you can display
            the text to guide the user to check the message in TikTok Shop. The content of the message depends on the
            specific `locale`.
        messages (list[GetConversationMessagesResponseDataMessage] | Unset): Messages in conversation.
    """

    next_page_token: str | Unset = UNSET
    unsupported_msg_tips: str | Unset = UNSET
    messages: list[GetConversationMessagesResponseDataMessage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_page_token = self.next_page_token

        unsupported_msg_tips = self.unsupported_msg_tips

        messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if unsupported_msg_tips is not UNSET:
            field_dict["unsupported_msg_tips"] = unsupported_msg_tips
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_conversation_messages_response_data_message import (
            GetConversationMessagesResponseDataMessage,  # noqa: PLC0415
        )

        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        unsupported_msg_tips = d.pop("unsupported_msg_tips", UNSET)

        _messages = d.pop("messages", UNSET)
        messages: list[GetConversationMessagesResponseDataMessage] | Unset = UNSET
        if _messages is not UNSET:
            messages = []
            for messages_item_data in _messages:
                messages_item = GetConversationMessagesResponseDataMessage.from_dict(messages_item_data)

                messages.append(messages_item)

        get_conversation_messages_response_data = cls(
            next_page_token=next_page_token,
            unsupported_msg_tips=unsupported_msg_tips,
            messages=messages,
        )

        get_conversation_messages_response_data.additional_properties = d
        return get_conversation_messages_response_data

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
