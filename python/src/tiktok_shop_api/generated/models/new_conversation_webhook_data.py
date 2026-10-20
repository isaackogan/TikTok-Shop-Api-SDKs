from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="NewConversationWebhookData")



@_attrs_define
class NewConversationWebhookData:
    """ 
        Attributes:
            conversation_id (str | Unset): The identification of the conversation
            create_time (int | Unset): Conversation creation time, represented as a Unix timestamp (in seconds).
     """

    conversation_id: str | Unset = UNSET
    create_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        conversation_id = self.conversation_id

        create_time = self.create_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if create_time is not UNSET:
            field_dict["create_time"] = create_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_id = d.pop("conversation_id", UNSET)

        create_time = d.pop("create_time", UNSET)

        new_conversation_webhook_data = cls(
            conversation_id=conversation_id,
            create_time=create_time,
        )


        new_conversation_webhook_data.additional_properties = d
        return new_conversation_webhook_data

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
