from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetOrCreateCreatorConversationRequest")



@_attrs_define
class GetOrCreateCreatorConversationRequest:
    """ 
        Attributes:
            creator_open_id (str): The creator's Open ID. Use the Open ID returned by the relevant API, not a user ID,
                creator ID, or seller ID. [More details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
            only_need_conversation_id (bool | Unset): - If `true`, only `conversation_id` in `data.conversation` is
                returned.
                - If `false`, all fields in `data.conversation` are returned.
                `true` by default.
     """

    creator_open_id: str
    only_need_conversation_id: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        creator_open_id = self.creator_open_id

        only_need_conversation_id = self.only_need_conversation_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "creator_open_id": creator_open_id,
        })
        if only_need_conversation_id is not UNSET:
            field_dict["only_need_conversation_id"] = only_need_conversation_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_open_id = d.pop("creator_open_id")

        only_need_conversation_id = d.pop("only_need_conversation_id", UNSET)

        get_or_create_creator_conversation_request = cls(
            creator_open_id=creator_open_id,
            only_need_conversation_id=only_need_conversation_id,
        )


        get_or_create_creator_conversation_request.additional_properties = d
        return get_or_create_creator_conversation_request

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
