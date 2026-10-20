from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLatestUnreadMessagesResponseDataNewestMessageList")


@_attrs_define
class GetLatestUnreadMessagesResponseDataNewestMessageList:
    """
    Attributes:
        conversation_id (str | Unset): The converastion id to which the message belongs
        content (str | Unset): Message content as a JSON-serialized string. Parse the string as a JSON object; its shape
            depends on `type`:
            - `TEXT`: `{"content": "simple text"}`
            - `PRODUCT_CARD`: `{"product_id": "12345"}`
            - `TARGET_COLLABORATION_CARD`: `{"invitation_group_id": "1234"}`
            - `FREE_SAMPLE_CARD`: `{"apply_id": "1234"}`
            - `IMAGE`: `{"height": "290", "url": "<image URL>", "width": "304"}`
            - `CRM_TEXT_WITH_IMAGE_CARD`: `{"title": "abc", "content": "efg", "url": "<image URL>"}`
            - `CRM_TEXT_WITH_PRODUCTS_CARD`: `{"title": "abc", "content": "efg", "product_ids": [123, 456, 789, 222]}`
            - `NOTIFICATION` or `SYSTEM`: `{"content": "notification or system message"}`
            - `EMOTICONS`: `{"height": "110", "url": "<image URL>", "width": "110"}`
        type_ (str | Unset): Message type. Possible values:
            - TEXT
            - PRODUCT_CARD
            - TARGET_COLLABORATION_CARD
            - FREE_SAMPLE_CARD
            - IMAGE
            - CRM_TEXT_WITH_IMAGE_CARD
            - CRM_TEXT_WITH_PRODUCTS_CARD
            - NOTIFICATION
            - EMOTICONS
            - SYSTEM
        sender_id (str | Unset): sender's IM id
        unread_message_count (int | Unset): The number of unread messages of the sender in the conversation.
    """

    conversation_id: str | Unset = UNSET
    content: str | Unset = UNSET
    type_: str | Unset = UNSET
    sender_id: str | Unset = UNSET
    unread_message_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        content = self.content

        type_ = self.type_

        sender_id = self.sender_id

        unread_message_count = self.unread_message_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if content is not UNSET:
            field_dict["content"] = content
        if type_ is not UNSET:
            field_dict["type"] = type_
        if sender_id is not UNSET:
            field_dict["sender_id"] = sender_id
        if unread_message_count is not UNSET:
            field_dict["unread_message_count"] = unread_message_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_id = d.pop("conversation_id", UNSET)

        content = d.pop("content", UNSET)

        type_ = d.pop("type", UNSET)

        sender_id = d.pop("sender_id", UNSET)

        unread_message_count = d.pop("unread_message_count", UNSET)

        get_latest_unread_messages_response_data_newest_message_list = cls(
            conversation_id=conversation_id,
            content=content,
            type_=type_,
            sender_id=sender_id,
            unread_message_count=unread_message_count,
        )

        get_latest_unread_messages_response_data_newest_message_list.additional_properties = d
        return get_latest_unread_messages_response_data_newest_message_list

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
