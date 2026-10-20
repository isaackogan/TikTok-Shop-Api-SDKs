from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resolve_target_collaboration_conflicts_request_conflict_item import (
        ResolveTargetCollaborationConflictsRequestConflictItem,
    )


T = TypeVar("T", bound="ResolveTargetCollaborationConflictsRequest")


@_attrs_define
class ResolveTargetCollaborationConflictsRequest:
    """
    Attributes:
        conflict_items (list[ResolveTargetCollaborationConflictsRequestConflictItem]): A list of creators and their
            existing target collaborations involved in conflicts that caused target collaboration failure. Each item
            identifies a creator and the existing target collaboration from which that creator will be removed.
    """

    conflict_items: list[ResolveTargetCollaborationConflictsRequestConflictItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conflict_items = []
        for conflict_items_item_data in self.conflict_items:
            conflict_items_item = conflict_items_item_data.to_dict()
            conflict_items.append(conflict_items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conflict_items": conflict_items,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resolve_target_collaboration_conflicts_request_conflict_item import (
            ResolveTargetCollaborationConflictsRequestConflictItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        conflict_items = []
        _conflict_items = d.pop("conflict_items")
        for conflict_items_item_data in _conflict_items:
            conflict_items_item = ResolveTargetCollaborationConflictsRequestConflictItem.from_dict(
                conflict_items_item_data
            )

            conflict_items.append(conflict_items_item)

        resolve_target_collaboration_conflicts_request = cls(
            conflict_items=conflict_items,
        )

        resolve_target_collaboration_conflicts_request.additional_properties = d
        return resolve_target_collaboration_conflicts_request

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
