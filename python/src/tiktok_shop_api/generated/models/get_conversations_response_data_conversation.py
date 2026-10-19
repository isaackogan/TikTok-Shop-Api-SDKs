from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cur_session import CurSession
    from ..models.get_conversations_response_data_conversation_latest_message import (
        GetConversationsResponseDataConversationLatestMessage,
    )
    from ..models.get_conversations_response_data_conversation_participant import (
        GetConversationsResponseDataConversationParticipant,
    )


T = TypeVar("T", bound="GetConversationsResponseDataConversation")


@_attrs_define
class GetConversationsResponseDataConversation:
    """
    Attributes:
        id (str | Unset): Conversation ID
        participant_count (int | Unset): Number of participants in the conversation.
            - If there has been no customer service agent in the conversation, the value is `2`: the shop and the buyer;
            - Otherwise, the value is `3`: the shop, the buyer, and the customer service agent.
        can_send_message (bool | Unset): Whether customer service agent can send message in this conversation. Under any
            of the following circumstances, the CS agent can send messages:
            1. There has been a prior conversation between the buyer and the shop within the last 30 days.
            2. The buyer placed an order at the shop within the past 60 days.
            3. The buyer has a history of returns or refunds at the shop.
        unread_count (int | Unset): Number of messages unread by the customer service agent.
        create_time (int | Unset): Unix timestamp when the conversation was created. In seconds.
        participants (list[GetConversationsResponseDataConversationParticipant] | Unset): Conversation participants.
        latest_message (GetConversationsResponseDataConversationLatestMessage | Unset):
        cur_session_id (str | Unset): Current session id.
        cur_session (CurSession | Unset):
    """

    id: str | Unset = UNSET
    participant_count: int | Unset = UNSET
    can_send_message: bool | Unset = UNSET
    unread_count: int | Unset = UNSET
    create_time: int | Unset = UNSET
    participants: list[GetConversationsResponseDataConversationParticipant] | Unset = UNSET
    latest_message: GetConversationsResponseDataConversationLatestMessage | Unset = UNSET
    cur_session_id: str | Unset = UNSET
    cur_session: CurSession | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        participant_count = self.participant_count

        can_send_message = self.can_send_message

        unread_count = self.unread_count

        create_time = self.create_time

        participants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()
                participants.append(participants_item)

        latest_message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.latest_message, Unset):
            latest_message = self.latest_message.to_dict()

        cur_session_id = self.cur_session_id

        cur_session: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cur_session, Unset):
            cur_session = self.cur_session.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if participant_count is not UNSET:
            field_dict["participant_count"] = participant_count
        if can_send_message is not UNSET:
            field_dict["can_send_message"] = can_send_message
        if unread_count is not UNSET:
            field_dict["unread_count"] = unread_count
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if participants is not UNSET:
            field_dict["participants"] = participants
        if latest_message is not UNSET:
            field_dict["latest_message"] = latest_message
        if cur_session_id is not UNSET:
            field_dict["cur_session_id"] = cur_session_id
        if cur_session is not UNSET:
            field_dict["cur_session"] = cur_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cur_session import CurSession  # noqa: PLC0415
        from ..models.get_conversations_response_data_conversation_latest_message import (
            GetConversationsResponseDataConversationLatestMessage,  # noqa: PLC0415
        )
        from ..models.get_conversations_response_data_conversation_participant import (
            GetConversationsResponseDataConversationParticipant,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        participant_count = d.pop("participant_count", UNSET)

        can_send_message = d.pop("can_send_message", UNSET)

        unread_count = d.pop("unread_count", UNSET)

        create_time = d.pop("create_time", UNSET)

        _participants = d.pop("participants", UNSET)
        participants: list[GetConversationsResponseDataConversationParticipant] | Unset = UNSET
        if _participants is not UNSET:
            participants = []
            for participants_item_data in _participants:
                participants_item = GetConversationsResponseDataConversationParticipant.from_dict(
                    participants_item_data
                )

                participants.append(participants_item)

        _latest_message = d.pop("latest_message", UNSET)
        latest_message: GetConversationsResponseDataConversationLatestMessage | Unset
        if isinstance(_latest_message, Unset):
            latest_message = UNSET
        else:
            latest_message = GetConversationsResponseDataConversationLatestMessage.from_dict(_latest_message)

        cur_session_id = d.pop("cur_session_id", UNSET)

        _cur_session = d.pop("cur_session", UNSET)
        cur_session: CurSession | Unset
        if isinstance(_cur_session, Unset):
            cur_session = UNSET
        else:
            cur_session = CurSession.from_dict(_cur_session)

        get_conversations_response_data_conversation = cls(
            id=id,
            participant_count=participant_count,
            can_send_message=can_send_message,
            unread_count=unread_count,
            create_time=create_time,
            participants=participants,
            latest_message=latest_message,
            cur_session_id=cur_session_id,
            cur_session=cur_session,
        )

        get_conversations_response_data_conversation.additional_properties = d
        return get_conversations_response_data_conversation

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
