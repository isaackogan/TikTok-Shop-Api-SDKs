from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetInboxCategoryCountsResponseDataDataGroupCount")


@_attrs_define
class GetInboxCategoryCountsResponseDataDataGroupCount:
    """
    Attributes:
        group_type (str | Unset): Group type name, e.g.
            - UNREAD
            -UNREPLIED
            -STARRED
            -ARCHIVED
        count (int | Unset): Conversation count in this group
    """

    group_type: str | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_type = self.group_type

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_type is not UNSET:
            field_dict["group_type"] = group_type
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_type = d.pop("group_type", UNSET)

        count = d.pop("count", UNSET)

        get_inbox_category_counts_response_data_data_group_count = cls(
            group_type=group_type,
            count=count,
        )

        get_inbox_category_counts_response_data_data_group_count.additional_properties = d
        return get_inbox_category_counts_response_data_data_group_count

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
