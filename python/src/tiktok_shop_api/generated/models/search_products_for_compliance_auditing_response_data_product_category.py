from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchProductsForComplianceAuditingResponseDataProductCategory")



@_attrs_define
class SearchProductsForComplianceAuditingResponseDataProductCategory:
    """ 
        Attributes:
            id (str | Unset): The ID of the category of this product.
            name (str | Unset): The name of the category in the country where the shop operates.
            level (int | Unset): The level of the category in the country where the shop operates.
            parent_id (str | Unset): The parent category ID.
                For the root category, the parent ID is 0
            is_leaf (bool | Unset): A flag to indicate if the category is a leaf category.

                Note: You can only create or edit products that belong to a leaf category.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    level: int | Unset = UNSET
    parent_id: str | Unset = UNSET
    is_leaf: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        level = self.level

        parent_id = self.parent_id

        is_leaf = self.is_leaf


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if level is not UNSET:
            field_dict["level"] = level
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if is_leaf is not UNSET:
            field_dict["is_leaf"] = is_leaf

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        level = d.pop("level", UNSET)

        parent_id = d.pop("parent_id", UNSET)

        is_leaf = d.pop("is_leaf", UNSET)

        search_products_for_compliance_auditing_response_data_product_category = cls(
            id=id,
            name=name,
            level=level,
            parent_id=parent_id,
            is_leaf=is_leaf,
        )


        search_products_for_compliance_auditing_response_data_product_category.additional_properties = d
        return search_products_for_compliance_auditing_response_data_product_category

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
