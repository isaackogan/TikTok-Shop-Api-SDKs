from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cur_session import CurSession
    from ..models.get_conversation_response_data_conversation_participant import (
        GetConversationResponseDataConversationParticipant,
    )


T = TypeVar("T", bound="GetConversationResponseDataConversation")


@_attrs_define
class GetConversationResponseDataConversation:
    """
    Attributes:
        id (str | Unset): Conversation ID
        participant_count (int | Unset): Number of participants in the conversation.
            - If there has been no customer service agent in the conversation, the value is `2`: the shop and the buyer;
            - Otherwise, the value is `3`: the shop, the buyer, and the customer service agent.
        participants (list[GetConversationResponseDataConversationParticipant] | Unset): Conversation participants.
        create_time (int | Unset): Unix timestamp when the conversation was created. In seconds.
        unread_count (int | Unset): Number of messages unread by the customer service agent.
        cur_session_id (str | Unset): ID of the current open session. This field is returned when `need_session_id` or
            `need_session_info` is `true` and current open session information is available.
        cur_session (CurSession | Unset):
    """

    id: str | Unset = UNSET
    participant_count: int | Unset = UNSET
    participants: list[GetConversationResponseDataConversationParticipant] | Unset = UNSET
    create_time: int | Unset = UNSET
    unread_count: int | Unset = UNSET
    cur_session_id: str | Unset = UNSET
    cur_session: CurSession | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        participant_count = self.participant_count

        participants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()
                participants.append(participants_item)

        create_time = self.create_time

        unread_count = self.unread_count

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
        if participants is not UNSET:
            field_dict["participants"] = participants
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if unread_count is not UNSET:
            field_dict["unread_count"] = unread_count
        if cur_session_id is not UNSET:
            field_dict["cur_session_id"] = cur_session_id
        if cur_session is not UNSET:
            field_dict["cur_session"] = cur_session

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cur_session import CurSession  # noqa: PLC0415
        from ..models.get_conversation_response_data_conversation_participant import (
            GetConversationResponseDataConversationParticipant,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        participant_count = d.pop("participant_count", UNSET)

        _participants = d.pop("participants", UNSET)
        participants: list[GetConversationResponseDataConversationParticipant] | Unset = UNSET
        if _participants is not UNSET:
            participants = []
            for participants_item_data in _participants:
                participants_item = GetConversationResponseDataConversationParticipant.from_dict(participants_item_data)

                participants.append(participants_item)

        create_time = d.pop("create_time", UNSET)

        unread_count = d.pop("unread_count", UNSET)

        cur_session_id = d.pop("cur_session_id", UNSET)

        _cur_session = d.pop("cur_session", UNSET)
        cur_session: CurSession | Unset
        if isinstance(_cur_session, Unset):
            cur_session = UNSET
        else:
            cur_session = CurSession.from_dict(_cur_session)

        get_conversation_response_data_conversation = cls(
            id=id,
            participant_count=participant_count,
            participants=participants,
            create_time=create_time,
            unread_count=unread_count,
            cur_session_id=cur_session_id,
            cur_session=cur_session,
        )

        get_conversation_response_data_conversation.additional_properties = d
        return get_conversation_response_data_conversation

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
