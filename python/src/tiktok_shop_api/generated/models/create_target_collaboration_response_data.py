from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_target_collaboration_response_data_target_collaboration import (
        CreateTargetCollaborationResponseDataTargetCollaboration,
    )
    from ..models.target_collaboration_conflict import TargetCollaborationConflict


T = TypeVar("T", bound="CreateTargetCollaborationResponseData")


@_attrs_define
class CreateTargetCollaborationResponseData:
    """
    Attributes:
        target_collaboration (CreateTargetCollaborationResponseDataTargetCollaboration | Unset):
        target_collaboration_conflicts (list[TargetCollaborationConflict] | Unset): A list of user and product
            identifiers with target collaboration conflicts that caused target collaboration failure.
        invalid_open_id_list (list[str] | Unset): The list of open id that caused the create to fail.
        invalid_product_id_list (list[str] | Unset): The list of product id that caused the create to fail.
        create_time (int | Unset): The create time of the target collaboration.
    """

    target_collaboration: CreateTargetCollaborationResponseDataTargetCollaboration | Unset = UNSET
    target_collaboration_conflicts: list[TargetCollaborationConflict] | Unset = UNSET
    invalid_open_id_list: list[str] | Unset = UNSET
    invalid_product_id_list: list[str] | Unset = UNSET
    create_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_collaboration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_collaboration, Unset):
            target_collaboration = self.target_collaboration.to_dict()

        target_collaboration_conflicts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.target_collaboration_conflicts, Unset):
            target_collaboration_conflicts = []
            for target_collaboration_conflicts_item_data in self.target_collaboration_conflicts:
                target_collaboration_conflicts_item = target_collaboration_conflicts_item_data.to_dict()
                target_collaboration_conflicts.append(target_collaboration_conflicts_item)

        invalid_open_id_list: list[str] | Unset = UNSET
        if not isinstance(self.invalid_open_id_list, Unset):
            invalid_open_id_list = self.invalid_open_id_list

        invalid_product_id_list: list[str] | Unset = UNSET
        if not isinstance(self.invalid_product_id_list, Unset):
            invalid_product_id_list = self.invalid_product_id_list

        create_time = self.create_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_collaboration is not UNSET:
            field_dict["target_collaboration"] = target_collaboration
        if target_collaboration_conflicts is not UNSET:
            field_dict["target_collaboration_conflicts"] = target_collaboration_conflicts
        if invalid_open_id_list is not UNSET:
            field_dict["invalid_open_id_list"] = invalid_open_id_list
        if invalid_product_id_list is not UNSET:
            field_dict["invalid_product_id_list"] = invalid_product_id_list
        if create_time is not UNSET:
            field_dict["create_time"] = create_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_target_collaboration_response_data_target_collaboration import (
            CreateTargetCollaborationResponseDataTargetCollaboration,  # noqa: PLC0415
        )
        from ..models.target_collaboration_conflict import TargetCollaborationConflict  # noqa: PLC0415

        d = dict(src_dict)
        _target_collaboration = d.pop("target_collaboration", UNSET)
        target_collaboration: CreateTargetCollaborationResponseDataTargetCollaboration | Unset
        if isinstance(_target_collaboration, Unset):
            target_collaboration = UNSET
        else:
            target_collaboration = CreateTargetCollaborationResponseDataTargetCollaboration.from_dict(
                _target_collaboration
            )

        _target_collaboration_conflicts = d.pop("target_collaboration_conflicts", UNSET)
        target_collaboration_conflicts: list[TargetCollaborationConflict] | Unset = UNSET
        if _target_collaboration_conflicts is not UNSET:
            target_collaboration_conflicts = []
            for target_collaboration_conflicts_item_data in _target_collaboration_conflicts:
                target_collaboration_conflicts_item = TargetCollaborationConflict.from_dict(
                    target_collaboration_conflicts_item_data
                )

                target_collaboration_conflicts.append(target_collaboration_conflicts_item)

        invalid_open_id_list = cast(list[str], d.pop("invalid_open_id_list", UNSET))

        invalid_product_id_list = cast(list[str], d.pop("invalid_product_id_list", UNSET))

        create_time = d.pop("create_time", UNSET)

        create_target_collaboration_response_data = cls(
            target_collaboration=target_collaboration,
            target_collaboration_conflicts=target_collaboration_conflicts,
            invalid_open_id_list=invalid_open_id_list,
            invalid_product_id_list=invalid_product_id_list,
            create_time=create_time,
        )

        create_target_collaboration_response_data.additional_properties = d
        return create_target_collaboration_response_data

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
