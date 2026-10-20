from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.target_collaboration_conflict import TargetCollaborationConflict
    from ..models.update_target_collaboration_response_data_update_failed import (
        UpdateTargetCollaborationResponseDataUpdateFailed,
    )


T = TypeVar("T", bound="UpdateTargetCollaborationResponseData")


@_attrs_define
class UpdateTargetCollaborationResponseData:
    """
    Attributes:
        target_collaboration_conflicts (list[TargetCollaborationConflict] | Unset): A list of creators and products with
            target collaboration conflicts that caused target collaboration update failure.
        update_failed (UpdateTargetCollaborationResponseDataUpdateFailed | Unset):
    """

    target_collaboration_conflicts: list[TargetCollaborationConflict] | Unset = UNSET
    update_failed: UpdateTargetCollaborationResponseDataUpdateFailed | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_collaboration_conflicts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.target_collaboration_conflicts, Unset):
            target_collaboration_conflicts = []
            for target_collaboration_conflicts_item_data in self.target_collaboration_conflicts:
                target_collaboration_conflicts_item = target_collaboration_conflicts_item_data.to_dict()
                target_collaboration_conflicts.append(target_collaboration_conflicts_item)

        update_failed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_failed, Unset):
            update_failed = self.update_failed.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_collaboration_conflicts is not UNSET:
            field_dict["target_collaboration_conflicts"] = target_collaboration_conflicts
        if update_failed is not UNSET:
            field_dict["update_failed"] = update_failed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.target_collaboration_conflict import TargetCollaborationConflict  # noqa: PLC0415
        from ..models.update_target_collaboration_response_data_update_failed import (
            UpdateTargetCollaborationResponseDataUpdateFailed,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _target_collaboration_conflicts = d.pop("target_collaboration_conflicts", UNSET)
        target_collaboration_conflicts: list[TargetCollaborationConflict] | Unset = UNSET
        if _target_collaboration_conflicts is not UNSET:
            target_collaboration_conflicts = []
            for target_collaboration_conflicts_item_data in _target_collaboration_conflicts:
                target_collaboration_conflicts_item = TargetCollaborationConflict.from_dict(
                    target_collaboration_conflicts_item_data
                )

                target_collaboration_conflicts.append(target_collaboration_conflicts_item)

        _update_failed = d.pop("update_failed", UNSET)
        update_failed: UpdateTargetCollaborationResponseDataUpdateFailed | Unset
        if isinstance(_update_failed, Unset):
            update_failed = UNSET
        else:
            update_failed = UpdateTargetCollaborationResponseDataUpdateFailed.from_dict(_update_failed)

        update_target_collaboration_response_data = cls(
            target_collaboration_conflicts=target_collaboration_conflicts,
            update_failed=update_failed,
        )

        update_target_collaboration_response_data.additional_properties = d
        return update_target_collaboration_response_data

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
