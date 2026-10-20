from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.resolve_target_collaboration_conflicts_response_data_failed_item import ResolveTargetCollaborationConflictsResponseDataFailedItem
  from ..models.resolve_target_collaboration_conflicts_response_data_success_item import ResolveTargetCollaborationConflictsResponseDataSuccessItem





T = TypeVar("T", bound="ResolveTargetCollaborationConflictsResponseData")



@_attrs_define
class ResolveTargetCollaborationConflictsResponseData:
    """ 
        Attributes:
            success_items (list[ResolveTargetCollaborationConflictsResponseDataSuccessItem] | Unset): success update items
            failed_items (list[ResolveTargetCollaborationConflictsResponseDataFailedItem] | Unset): failed update items
     """

    success_items: list[ResolveTargetCollaborationConflictsResponseDataSuccessItem] | Unset = UNSET
    failed_items: list[ResolveTargetCollaborationConflictsResponseDataFailedItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.resolve_target_collaboration_conflicts_response_data_failed_item import ResolveTargetCollaborationConflictsResponseDataFailedItem # noqa: PLC0415
        from ..models.resolve_target_collaboration_conflicts_response_data_success_item import ResolveTargetCollaborationConflictsResponseDataSuccessItem # noqa: PLC0415
        success_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.success_items, Unset):
            success_items = []
            for success_items_item_data in self.success_items:
                success_items_item = success_items_item_data.to_dict()
                success_items.append(success_items_item)



        failed_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed_items, Unset):
            failed_items = []
            for failed_items_item_data in self.failed_items:
                failed_items_item = failed_items_item_data.to_dict()
                failed_items.append(failed_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if success_items is not UNSET:
            field_dict["success_items"] = success_items
        if failed_items is not UNSET:
            field_dict["failed_items"] = failed_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resolve_target_collaboration_conflicts_response_data_failed_item import ResolveTargetCollaborationConflictsResponseDataFailedItem # noqa: PLC0415
        from ..models.resolve_target_collaboration_conflicts_response_data_success_item import ResolveTargetCollaborationConflictsResponseDataSuccessItem # noqa: PLC0415
        d = dict(src_dict)
        _success_items = d.pop("success_items", UNSET)
        success_items: list[ResolveTargetCollaborationConflictsResponseDataSuccessItem] | Unset = UNSET
        if _success_items is not UNSET:
            success_items = []
            for success_items_item_data in _success_items:
                success_items_item = ResolveTargetCollaborationConflictsResponseDataSuccessItem.from_dict(success_items_item_data)



                success_items.append(success_items_item)


        _failed_items = d.pop("failed_items", UNSET)
        failed_items: list[ResolveTargetCollaborationConflictsResponseDataFailedItem] | Unset = UNSET
        if _failed_items is not UNSET:
            failed_items = []
            for failed_items_item_data in _failed_items:
                failed_items_item = ResolveTargetCollaborationConflictsResponseDataFailedItem.from_dict(failed_items_item_data)



                failed_items.append(failed_items_item)


        resolve_target_collaboration_conflicts_response_data = cls(
            success_items=success_items,
            failed_items=failed_items,
        )


        resolve_target_collaboration_conflicts_response_data.additional_properties = d
        return resolve_target_collaboration_conflicts_response_data

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
