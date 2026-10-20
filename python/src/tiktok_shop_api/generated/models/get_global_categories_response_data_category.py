from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGlobalCategoriesResponseDataCategory")


@_attrs_define
class GetGlobalCategoriesResponseDataCategory:
    """
    Attributes:
        id (str | Unset): The category ID.
        parent_id (str | Unset): The parent category ID.
            For the root category, the parent ID is `0`.
        local_name (str | Unset): The name of the category.
        is_leaf (bool | Unset): A flag to indicate if the category is a leaf category.
            **Note**: You can only create or edit products that belong to a leaf category.
        permission_statuses (list[str] | Unset): The shop's permission status for this category.
            Possible values:
            - AVAILABLE: You have the permission to create products in this category.
            - NON_MAIN_CATEGORY: This category is out of scope for this seller, and you do not have permission to use it.
            Contact your account manager for assistance.
    """

    id: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    local_name: str | Unset = UNSET
    is_leaf: bool | Unset = UNSET
    permission_statuses: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        parent_id = self.parent_id

        local_name = self.local_name

        is_leaf = self.is_leaf

        permission_statuses: list[str] | Unset = UNSET
        if not isinstance(self.permission_statuses, Unset):
            permission_statuses = self.permission_statuses

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if local_name is not UNSET:
            field_dict["local_name"] = local_name
        if is_leaf is not UNSET:
            field_dict["is_leaf"] = is_leaf
        if permission_statuses is not UNSET:
            field_dict["permission_statuses"] = permission_statuses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        local_name = d.pop("local_name", UNSET)

        is_leaf = d.pop("is_leaf", UNSET)

        permission_statuses = cast(list[str], d.pop("permission_statuses", UNSET))

        get_global_categories_response_data_category = cls(
            id=id,
            parent_id=parent_id,
            local_name=local_name,
            is_leaf=is_leaf,
            permission_statuses=permission_statuses,
        )

        get_global_categories_response_data_category.additional_properties = d
        return get_global_categories_response_data_category

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
