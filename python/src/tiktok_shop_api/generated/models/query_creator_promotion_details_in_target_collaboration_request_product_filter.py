from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="QueryCreatorPromotionDetailsInTargetCollaborationRequestProductFilter")



@_attrs_define
class QueryCreatorPromotionDetailsInTargetCollaborationRequestProductFilter:
    """ 
        Attributes:
            added_types (list[str] | Unset): Product added type list, support status:
                -ALL: all status
                -ADDED: creator added product
                NOT_ADDED: creator not added product
     """

    added_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        added_types: list[str] | Unset = UNSET
        if not isinstance(self.added_types, Unset):
            added_types = self.added_types




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if added_types is not UNSET:
            field_dict["added_types"] = added_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        added_types = cast(list[str], d.pop("added_types", UNSET))


        query_creator_promotion_details_in_target_collaboration_request_product_filter = cls(
            added_types=added_types,
        )


        query_creator_promotion_details_in_target_collaboration_request_product_filter.additional_properties = d
        return query_creator_promotion_details_in_target_collaboration_request_product_filter

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
