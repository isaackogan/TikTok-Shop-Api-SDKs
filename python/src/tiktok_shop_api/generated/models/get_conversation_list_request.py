from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetConversationListRequest")


@_attrs_define
class GetConversationListRequest:
    """
    Attributes:
        only_need_conversation_id (bool | Unset): - If `true`, only `conversation_id` in `data.conversation` is
            returned.
            - If `false`, all fields in `data.conversation` are returned.
            `true` by default.
    """

    only_need_conversation_id: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        only_need_conversation_id = self.only_need_conversation_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if only_need_conversation_id is not UNSET:
            field_dict["only_need_conversation_id"] = only_need_conversation_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        only_need_conversation_id = d.pop("only_need_conversation_id", UNSET)

        get_conversation_list_request = cls(
            only_need_conversation_id=only_need_conversation_id,
        )

        get_conversation_list_request.additional_properties = d
        return get_conversation_list_request

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
