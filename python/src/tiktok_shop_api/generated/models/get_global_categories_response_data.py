from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_global_categories_response_data_category import GetGlobalCategoriesResponseDataCategory





T = TypeVar("T", bound="GetGlobalCategoriesResponseData")



@_attrs_define
class GetGlobalCategoriesResponseData:
    """ 
        Attributes:
            categories (list[GetGlobalCategoriesResponseDataCategory] | Unset): The list of categories that meet the query
                conditions.
     """

    categories: list[GetGlobalCategoriesResponseDataCategory] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_global_categories_response_data_category import GetGlobalCategoriesResponseDataCategory # noqa: PLC0415
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
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_global_categories_response_data_category import GetGlobalCategoriesResponseDataCategory # noqa: PLC0415
        d = dict(src_dict)
        _categories = d.pop("categories", UNSET)
        categories: list[GetGlobalCategoriesResponseDataCategory] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = GetGlobalCategoriesResponseDataCategory.from_dict(categories_item_data)



                categories.append(categories_item)


        get_global_categories_response_data = cls(
            categories=categories,
        )


        get_global_categories_response_data.additional_properties = d
        return get_global_categories_response_data

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
