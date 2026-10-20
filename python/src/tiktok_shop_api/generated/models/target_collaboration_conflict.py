from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TargetCollaborationConflict")



@_attrs_define
class TargetCollaborationConflict:
    """ 
        Attributes:
            creator_user_open_id (str | Unset): Creator Open ID. [More
                details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
            product_id (str | Unset): The product identifier.
     """

    creator_user_open_id: str | Unset = UNSET
    product_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        creator_user_open_id = self.creator_user_open_id

        product_id = self.product_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if creator_user_open_id is not UNSET:
            field_dict["creator_user_open_id"] = creator_user_open_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_user_open_id = d.pop("creator_user_open_id", UNSET)

        product_id = d.pop("product_id", UNSET)

        target_collaboration_conflict = cls(
            creator_user_open_id=creator_user_open_id,
            product_id=product_id,
        )


        target_collaboration_conflict.additional_properties = d
        return target_collaboration_conflict

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
