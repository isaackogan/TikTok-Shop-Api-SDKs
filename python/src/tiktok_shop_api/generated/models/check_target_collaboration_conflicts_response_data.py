from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.check_target_collaboration_conflicts_response_data_conflict_item import CheckTargetCollaborationConflictsResponseDataConflictItem





T = TypeVar("T", bound="CheckTargetCollaborationConflictsResponseData")



@_attrs_define
class CheckTargetCollaborationConflictsResponseData:
    """ 
        Attributes:
            has_conflict (bool | Unset): Indicates whether a conflict exists between the creator and the product. (Returns
                `true` if a conflict is detected.)
            conflict_items (list[CheckTargetCollaborationConflictsResponseDataConflictItem] | Unset): A list of creator-
                product combinations whose conflicts caused the target collaboration to fail. Each item identifies the creator,
                product, and existing target collaboration involved.
     """

    has_conflict: bool | Unset = UNSET
    conflict_items: list[CheckTargetCollaborationConflictsResponseDataConflictItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.check_target_collaboration_conflicts_response_data_conflict_item import CheckTargetCollaborationConflictsResponseDataConflictItem # noqa: PLC0415
        has_conflict = self.has_conflict

        conflict_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conflict_items, Unset):
            conflict_items = []
            for conflict_items_item_data in self.conflict_items:
                conflict_items_item = conflict_items_item_data.to_dict()
                conflict_items.append(conflict_items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if has_conflict is not UNSET:
            field_dict["has_conflict"] = has_conflict
        if conflict_items is not UNSET:
            field_dict["conflict_items"] = conflict_items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_target_collaboration_conflicts_response_data_conflict_item import CheckTargetCollaborationConflictsResponseDataConflictItem # noqa: PLC0415
        d = dict(src_dict)
        has_conflict = d.pop("has_conflict", UNSET)

        _conflict_items = d.pop("conflict_items", UNSET)
        conflict_items: list[CheckTargetCollaborationConflictsResponseDataConflictItem] | Unset = UNSET
        if _conflict_items is not UNSET:
            conflict_items = []
            for conflict_items_item_data in _conflict_items:
                conflict_items_item = CheckTargetCollaborationConflictsResponseDataConflictItem.from_dict(conflict_items_item_data)



                conflict_items.append(conflict_items_item)


        check_target_collaboration_conflicts_response_data = cls(
            has_conflict=has_conflict,
            conflict_items=conflict_items,
        )


        check_target_collaboration_conflicts_response_data.additional_properties = d
        return check_target_collaboration_conflicts_response_data

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
