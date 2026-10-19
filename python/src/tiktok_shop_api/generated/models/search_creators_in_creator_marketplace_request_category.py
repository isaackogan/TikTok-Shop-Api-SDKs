from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchCreatorsInCreatorMarketplaceRequestCategory")


@_attrs_define
class SearchCreatorsInCreatorMarketplaceRequestCategory:
    """
    Attributes:
        parent_category_id (str | Unset): Category of the parent category. If you are only using a parent category, you
            do not need to pass in a child category ID.
        child_category_id_list (list[str] | Unset): If you are using the category ID for a child category, you must pass
            the parent category as well. A child category is only 1 level deeper than the parent category. We do not support
            going deeper down the category tree (some countries have 4 levels, others have 7)
    """

    parent_category_id: str | Unset = UNSET
    child_category_id_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_category_id = self.parent_category_id

        child_category_id_list: list[str] | Unset = UNSET
        if not isinstance(self.child_category_id_list, Unset):
            child_category_id_list = self.child_category_id_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_category_id is not UNSET:
            field_dict["parent_category_id"] = parent_category_id
        if child_category_id_list is not UNSET:
            field_dict["child_category_id_list"] = child_category_id_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parent_category_id = d.pop("parent_category_id", UNSET)

        child_category_id_list = cast(list[str], d.pop("child_category_id_list", UNSET))

        search_creators_in_creator_marketplace_request_category = cls(
            parent_category_id=parent_category_id,
            child_category_id_list=child_category_id_list,
        )

        search_creators_in_creator_marketplace_request_category.additional_properties = d
        return search_creators_in_creator_marketplace_request_category

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
