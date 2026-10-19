from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResolveTargetCollaborationConflictsRequestConflictItem")


@_attrs_define
class ResolveTargetCollaborationConflictsRequestConflictItem:
    """
    Attributes:
        existing_collaboration_id (str): The confict target collaboration id
        creator_open_id (str): Creator Open ID. [More details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
    """

    existing_collaboration_id: str
    creator_open_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        existing_collaboration_id = self.existing_collaboration_id

        creator_open_id = self.creator_open_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "existing_collaboration_id": existing_collaboration_id,
                "creator_open_id": creator_open_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        existing_collaboration_id = d.pop("existing_collaboration_id")

        creator_open_id = d.pop("creator_open_id")

        resolve_target_collaboration_conflicts_request_conflict_item = cls(
            existing_collaboration_id=existing_collaboration_id,
            creator_open_id=creator_open_id,
        )

        resolve_target_collaboration_conflicts_request_conflict_item.additional_properties = d
        return resolve_target_collaboration_conflicts_request_conflict_item

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
