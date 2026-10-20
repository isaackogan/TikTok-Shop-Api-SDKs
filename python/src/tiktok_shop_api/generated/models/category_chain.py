from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CategoryChain")


@_attrs_define
class CategoryChain:
    """
    Attributes:
        id (str | Unset): The current category id of this product.
        local_name (str | Unset): The current level category name of this product.
        is_leaf (bool | Unset): Indicate whether current node is leaf node
        parent_id (str | Unset): The category id of its parent category
    """

    id: str | Unset = UNSET
    local_name: str | Unset = UNSET
    is_leaf: bool | Unset = UNSET
    parent_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        local_name = self.local_name

        is_leaf = self.is_leaf

        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if local_name is not UNSET:
            field_dict["local_name"] = local_name
        if is_leaf is not UNSET:
            field_dict["is_leaf"] = is_leaf
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        local_name = d.pop("local_name", UNSET)

        is_leaf = d.pop("is_leaf", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        category_chain = cls(
            id=id,
            local_name=local_name,
            is_leaf=is_leaf,
            parent_id=parent_id,
        )

        category_chain.additional_properties = d
        return category_chain

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
