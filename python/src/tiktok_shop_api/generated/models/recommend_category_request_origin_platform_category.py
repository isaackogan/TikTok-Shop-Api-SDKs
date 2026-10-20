from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecommendCategoryRequestOriginPlatformCategory")


@_attrs_define
class RecommendCategoryRequestOriginPlatformCategory:
    """
    Attributes:
        id (str | Unset): The category ID on the source platform.
        name (str | Unset): The category name on the source platform.
        full_name (str | Unset): The full category path or full category name on the source platform.
        is_leaf (bool | Unset): Whether the category is a leaf category.
        is_root (bool | Unset): Whether the category is a root category.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    full_name: str | Unset = UNSET
    is_leaf: bool | Unset = UNSET
    is_root: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        full_name = self.full_name

        is_leaf = self.is_leaf

        is_root = self.is_root

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if is_leaf is not UNSET:
            field_dict["is_leaf"] = is_leaf
        if is_root is not UNSET:
            field_dict["is_root"] = is_root

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        full_name = d.pop("full_name", UNSET)

        is_leaf = d.pop("is_leaf", UNSET)

        is_root = d.pop("is_root", UNSET)

        recommend_category_request_origin_platform_category = cls(
            id=id,
            name=name,
            full_name=full_name,
            is_leaf=is_leaf,
            is_root=is_root,
        )

        recommend_category_request_origin_platform_category.additional_properties = d
        return recommend_category_request_origin_platform_category

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
