from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RecommendCategoryResponseDataCategory")



@_attrs_define
class RecommendCategoryResponseDataCategory:
    """ 
        Attributes:
            id (str | Unset): The category ID.
            is_leaf (bool | Unset): A flag to indicate if the category is a leaf category.

                **Note**: You can only create or edit products that belong to a leaf category.
            level (int | Unset): The category level.
            name (str | Unset): The category name.
            permission_statuses (list[str] | Unset): The shop's permission status for this category.
                Possible values:
                - AVAILABLE: You have the permission to create products in this category.
                - INVITE_ONLY: This is a restricted category and you do not have permission to use it. Submit an application
                through the Qualification Center on TikTok Shop Seller Center to gain access. In Seller Center, `INVITE_ONLY` is
                also known as "restricted".
                - NON_MAIN_CATEGORY: This category is not in the shop's main category.
                - PROHIBITED: This category is prohibited on TikTok Shop. If your product falls under this category, do not
                attempt to list it, as it will be rejected during audit. Applicable only for BR and MX markets.
     """

    id: str | Unset = UNSET
    is_leaf: bool | Unset = UNSET
    level: int | Unset = UNSET
    name: str | Unset = UNSET
    permission_statuses: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_leaf = self.is_leaf

        level = self.level

        name = self.name

        permission_statuses: list[str] | Unset = UNSET
        if not isinstance(self.permission_statuses, Unset):
            permission_statuses = self.permission_statuses




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if is_leaf is not UNSET:
            field_dict["is_leaf"] = is_leaf
        if level is not UNSET:
            field_dict["level"] = level
        if name is not UNSET:
            field_dict["name"] = name
        if permission_statuses is not UNSET:
            field_dict["permission_statuses"] = permission_statuses

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        is_leaf = d.pop("is_leaf", UNSET)

        level = d.pop("level", UNSET)

        name = d.pop("name", UNSET)

        permission_statuses = cast(list[str], d.pop("permission_statuses", UNSET))


        recommend_category_response_data_category = cls(
            id=id,
            is_leaf=is_leaf,
            level=level,
            name=name,
            permission_statuses=permission_statuses,
        )


        recommend_category_response_data_category.additional_properties = d
        return recommend_category_response_data_category

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
