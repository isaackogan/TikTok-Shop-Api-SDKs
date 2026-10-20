from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="MarkConversationsAsReadRequest")



@_attrs_define
class MarkConversationsAsReadRequest:
    """ 
        Attributes:
            conversation_ids (list[str]): The array of conversations to read.
                After the API is called, all the messages in the specified conversations will be read, and the read timestamp is
                set to the time when the API is called.
                The length of the array must not exceed `20`.
     """

    conversation_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        conversation_ids = self.conversation_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "conversation_ids": conversation_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_ids = cast(list[str], d.pop("conversation_ids"))


        mark_conversations_as_read_request = cls(
            conversation_ids=conversation_ids,
        )


        mark_conversations_as_read_request.additional_properties = d
        return mark_conversations_as_read_request

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
