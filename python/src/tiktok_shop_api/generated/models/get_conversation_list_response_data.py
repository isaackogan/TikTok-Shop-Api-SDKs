from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_conversation_list_response_data_conversation import GetConversationListResponseDataConversation





T = TypeVar("T", bound="GetConversationListResponseData")



@_attrs_define
class GetConversationListResponseData:
    """ 
        Attributes:
            has_more (bool | Unset): Whether there are more conversations.
            next_page_token (str | Unset): Pagination cursor for the next page. When `has_more` is `true`, pass this value
                as `page_token` in the next request.
            conversations (list[GetConversationListResponseDataConversation] | Unset): The conversation list.
     """

    has_more: bool | Unset = UNSET
    next_page_token: str | Unset = UNSET
    conversations: list[GetConversationListResponseDataConversation] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_conversation_list_response_data_conversation import GetConversationListResponseDataConversation # noqa: PLC0415
        has_more = self.has_more

        next_page_token = self.next_page_token

        conversations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conversations, Unset):
            conversations = []
            for conversations_item_data in self.conversations:
                conversations_item = conversations_item_data.to_dict()
                conversations.append(conversations_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if conversations is not UNSET:
            field_dict["conversations"] = conversations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_conversation_list_response_data_conversation import GetConversationListResponseDataConversation # noqa: PLC0415
        d = dict(src_dict)
        has_more = d.pop("has_more", UNSET)

        next_page_token = d.pop("next_page_token", UNSET)

        _conversations = d.pop("conversations", UNSET)
        conversations: list[GetConversationListResponseDataConversation] | Unset = UNSET
        if _conversations is not UNSET:
            conversations = []
            for conversations_item_data in _conversations:
                conversations_item = GetConversationListResponseDataConversation.from_dict(conversations_item_data)



                conversations.append(conversations_item)


        get_conversation_list_response_data = cls(
            has_more=has_more,
            next_page_token=next_page_token,
            conversations=conversations,
        )


        get_conversation_list_response_data.additional_properties = d
        return get_conversation_list_response_data

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
