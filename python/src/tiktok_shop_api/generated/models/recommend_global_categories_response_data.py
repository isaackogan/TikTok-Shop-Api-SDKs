from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.recommend_global_categories_response_data_category import RecommendGlobalCategoriesResponseDataCategory





T = TypeVar("T", bound="RecommendGlobalCategoriesResponseData")



@_attrs_define
class RecommendGlobalCategoriesResponseData:
    """ 
        Attributes:
            leaf_category_id (str | Unset): The recommended category ID. This is always a leaf category.
            categories (list[RecommendGlobalCategoriesResponseDataCategory] | Unset): The category hierarchy for the
                recommended leaf category, ordered from the top-level category to the leaf category.
     """

    leaf_category_id: str | Unset = UNSET
    categories: list[RecommendGlobalCategoriesResponseDataCategory] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.recommend_global_categories_response_data_category import RecommendGlobalCategoriesResponseDataCategory # noqa: PLC0415
        leaf_category_id = self.leaf_category_id

        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if leaf_category_id is not UNSET:
            field_dict["leaf_category_id"] = leaf_category_id
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recommend_global_categories_response_data_category import RecommendGlobalCategoriesResponseDataCategory # noqa: PLC0415
        d = dict(src_dict)
        leaf_category_id = d.pop("leaf_category_id", UNSET)

        _categories = d.pop("categories", UNSET)
        categories: list[RecommendGlobalCategoriesResponseDataCategory] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = RecommendGlobalCategoriesResponseDataCategory.from_dict(categories_item_data)



                categories.append(categories_item)


        recommend_global_categories_response_data = cls(
            leaf_category_id=leaf_category_id,
            categories=categories,
        )


        recommend_global_categories_response_data.additional_properties = d
        return recommend_global_categories_response_data

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
