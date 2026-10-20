from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductResponseDataCategoryChain")


@_attrs_define
class GetProductResponseDataCategoryChain:
    """
    Attributes:
        id (str | Unset): The ID of the category of this product.
        is_leaf (bool | Unset): A flag to indicate if the category is a leaf category.

            **Note**: You can only create or edit products that belong to a leaf category.
        local_name (str | Unset): The category name in the requested locale.
        parent_id (str | Unset): The parent category ID.
            For the root category, the parent ID is `0`.
    """

    id: str | Unset = UNSET
    is_leaf: bool | Unset = UNSET
    local_name: str | Unset = UNSET
    parent_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_leaf = self.is_leaf

        local_name = self.local_name

        parent_id = self.parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if is_leaf is not UNSET:
            field_dict["is_leaf"] = is_leaf
        if local_name is not UNSET:
            field_dict["local_name"] = local_name
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        is_leaf = d.pop("is_leaf", UNSET)

        local_name = d.pop("local_name", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        get_product_response_data_category_chain = cls(
            id=id,
            is_leaf=is_leaf,
            local_name=local_name,
            parent_id=parent_id,
        )

        get_product_response_data_category_chain.additional_properties = d
        return get_product_response_data_category_chain

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
