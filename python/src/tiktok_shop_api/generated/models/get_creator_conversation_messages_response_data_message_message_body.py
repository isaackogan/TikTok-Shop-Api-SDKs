from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCreatorConversationMessagesResponseDataMessageMessageBody")


@_attrs_define
class GetCreatorConversationMessagesResponseDataMessageMessageBody:
    """
    Attributes:
        id (str | Unset): Message ID.
        conversation_id (str | Unset): Conversation ID to which the message belongs.
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
        content (str | Unset): Message content serialized as a JSON string. The JSON object depends on `type`:
            - `TEXT`: `{"content": "simple text"}`
            - `PRODUCT_CARD`: `{"product_id": "12345"}`
            - `TARGET_COLLABORATION_CARD`: `{"invitation_group_id": "1234"}`
            - `FREE_SAMPLE_CARD`: `{"apply_id": "1234"}`
            - `IMAGE`: `{"height": "290", "url": "<image_url>", "width": "304"}`
            - `CRM_TEXT_WITH_IMAGE_CARD`: `{"title": "abc", "content": "efg", "url": "<image_url>"}`
            - `CRM_TEXT_WITH_PRODUCTS_CARD`: `{"title": "abc", "content": "efg", "product_ids": [123, 456, 789, 222]}`
            - `NOTIFICATION` or `SYSTEM`: `{"content": "notification/system message"}`
            - `EMOTICONS`: `{"height": "110", "url": "<image_url>", "width": "110"}`
        create_time (int | Unset): Message creation time, represented as a Unix timestamp (seconds).
        sender_id (str | Unset): The message sender im id
    """

    id: str | Unset = UNSET
    conversation_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    content: str | Unset = UNSET
    create_time: int | Unset = UNSET
    sender_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        conversation_id = self.conversation_id

        type_ = self.type_

        content = self.content

        create_time = self.create_time

        sender_id = self.sender_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if content is not UNSET:
            field_dict["content"] = content
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if sender_id is not UNSET:
            field_dict["sender_id"] = sender_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        type_ = d.pop("type", UNSET)

        content = d.pop("content", UNSET)

        create_time = d.pop("create_time", UNSET)

        sender_id = d.pop("sender_id", UNSET)

        get_creator_conversation_messages_response_data_message_message_body = cls(
            id=id,
            conversation_id=conversation_id,
            type_=type_,
            content=content,
            create_time=create_time,
            sender_id=sender_id,
        )

        get_creator_conversation_messages_response_data_message_message_body.additional_properties = d
        return get_creator_conversation_messages_response_data_message_message_body

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
