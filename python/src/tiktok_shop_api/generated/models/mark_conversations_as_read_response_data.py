from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkConversationsAsReadResponseData")


@_attrs_define
class MarkConversationsAsReadResponseData:
    """
    Attributes:
        failed_conversation_ids (list[str] | Unset): The conversation IDs that could not be marked as read. Retry the
            request using only these IDs.
    """

    failed_conversation_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failed_conversation_ids: list[str] | Unset = UNSET
        if not isinstance(self.failed_conversation_ids, Unset):
            failed_conversation_ids = self.failed_conversation_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if failed_conversation_ids is not UNSET:
            field_dict["failed_conversation_ids"] = failed_conversation_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failed_conversation_ids = cast(list[str], d.pop("failed_conversation_ids", UNSET))

        mark_conversations_as_read_response_data = cls(
            failed_conversation_ids=failed_conversation_ids,
        )

        mark_conversations_as_read_response_data.additional_properties = d
        return mark_conversations_as_read_response_data

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
