from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_conversation_response_data_conversation import GetConversationResponseDataConversation





T = TypeVar("T", bound="GetConversationResponseData")



@_attrs_define
class GetConversationResponseData:
    """ 
        Attributes:
            conversation (GetConversationResponseDataConversation | Unset):
     """

    conversation: GetConversationResponseDataConversation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_conversation_response_data_conversation import GetConversationResponseDataConversation # noqa: PLC0415
        conversation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conversation, Unset):
            conversation = self.conversation.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if conversation is not UNSET:
            field_dict["conversation"] = conversation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_conversation_response_data_conversation import GetConversationResponseDataConversation # noqa: PLC0415
        d = dict(src_dict)
        _conversation = d.pop("conversation", UNSET)
        conversation: GetConversationResponseDataConversation | Unset
        if isinstance(_conversation,  Unset):
            conversation = UNSET
        else:
            conversation = GetConversationResponseDataConversation.from_dict(_conversation)




        get_conversation_response_data = cls(
            conversation=conversation,
        )


        get_conversation_response_data.additional_properties = d
        return get_conversation_response_data

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
