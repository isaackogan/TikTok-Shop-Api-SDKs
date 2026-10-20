from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchSessionsResponseDataSession")



@_attrs_define
class SearchSessionsResponseDataSession:
    """ 
        Attributes:
            id (str | Unset): Session id.
            conversation_id (str | Unset): Conversation id.
            begin_time (int | Unset): The Unix timestamp, in seconds, when the session began.
            end_time (int | Unset): The timestamp when the session end.
            buyer_nickname (str | Unset): Buyer's nickname.
            chat_tags (list[str] | Unset): AfterSale/Logistics/Presale
            satisfaction_score (int | Unset): Customer satisfaction rating for the session (e.g., 1–5). Higher scores
                indicate greater satisfaction.
            dissatisfaction_reason (str | Unset): Reason provided by the buyer for a low satisfaction rating.
                The language of the reason is determined by the locale request parameter.
            first_response_late (bool | Unset): Indicates whether the first response exceeded the expected response time or
                SLA.
            first_response_time (int | Unset): Time elapsed in seconds between when the buyer sends the first message and
                when the seller sends the first response.
     """

    id: str | Unset = UNSET
    conversation_id: str | Unset = UNSET
    begin_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    buyer_nickname: str | Unset = UNSET
    chat_tags: list[str] | Unset = UNSET
    satisfaction_score: int | Unset = UNSET
    dissatisfaction_reason: str | Unset = UNSET
    first_response_late: bool | Unset = UNSET
    first_response_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        conversation_id = self.conversation_id

        begin_time = self.begin_time

        end_time = self.end_time

        buyer_nickname = self.buyer_nickname

        chat_tags: list[str] | Unset = UNSET
        if not isinstance(self.chat_tags, Unset):
            chat_tags = self.chat_tags



        satisfaction_score = self.satisfaction_score

        dissatisfaction_reason = self.dissatisfaction_reason

        first_response_late = self.first_response_late

        first_response_time = self.first_response_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if begin_time is not UNSET:
            field_dict["begin_time"] = begin_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if buyer_nickname is not UNSET:
            field_dict["buyer_nickname"] = buyer_nickname
        if chat_tags is not UNSET:
            field_dict["chat_tags"] = chat_tags
        if satisfaction_score is not UNSET:
            field_dict["satisfaction_score"] = satisfaction_score
        if dissatisfaction_reason is not UNSET:
            field_dict["dissatisfaction_reason"] = dissatisfaction_reason
        if first_response_late is not UNSET:
            field_dict["first_response_late"] = first_response_late
        if first_response_time is not UNSET:
            field_dict["first_response_time"] = first_response_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        begin_time = d.pop("begin_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        buyer_nickname = d.pop("buyer_nickname", UNSET)

        chat_tags = cast(list[str], d.pop("chat_tags", UNSET))


        satisfaction_score = d.pop("satisfaction_score", UNSET)

        dissatisfaction_reason = d.pop("dissatisfaction_reason", UNSET)

        first_response_late = d.pop("first_response_late", UNSET)

        first_response_time = d.pop("first_response_time", UNSET)

        search_sessions_response_data_session = cls(
            id=id,
            conversation_id=conversation_id,
            begin_time=begin_time,
            end_time=end_time,
            buyer_nickname=buyer_nickname,
            chat_tags=chat_tags,
            satisfaction_score=satisfaction_score,
            dissatisfaction_reason=dissatisfaction_reason,
            first_response_late=first_response_late,
            first_response_time=first_response_time,
        )


        search_sessions_response_data_session.additional_properties = d
        return search_sessions_response_data_session

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
