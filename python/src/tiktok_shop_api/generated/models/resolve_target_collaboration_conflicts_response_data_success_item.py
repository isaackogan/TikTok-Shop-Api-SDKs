from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResolveTargetCollaborationConflictsResponseDataSuccessItem")


@_attrs_define
class ResolveTargetCollaborationConflictsResponseDataSuccessItem:
    """
    Attributes:
        creator_open_id (str | Unset): Creator Open ID. [More
            details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
        existing_collaboration_id (str | Unset): The confict target collaboration id
    """

    creator_open_id: str | Unset = UNSET
    existing_collaboration_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator_open_id = self.creator_open_id

        existing_collaboration_id = self.existing_collaboration_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if creator_open_id is not UNSET:
            field_dict["creator_open_id"] = creator_open_id
        if existing_collaboration_id is not UNSET:
            field_dict["existing_collaboration_id"] = existing_collaboration_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_open_id = d.pop("creator_open_id", UNSET)

        existing_collaboration_id = d.pop("existing_collaboration_id", UNSET)

        resolve_target_collaboration_conflicts_response_data_success_item = cls(
            creator_open_id=creator_open_id,
            existing_collaboration_id=existing_collaboration_id,
        )

        resolve_target_collaboration_conflicts_response_data_success_item.additional_properties = d
        return resolve_target_collaboration_conflicts_response_data_success_item

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
