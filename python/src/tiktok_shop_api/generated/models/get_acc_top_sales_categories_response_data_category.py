from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_acc_top_sales_categories_response_data_category_children import GetACCTopSalesCategoriesResponseDataCategoryChildren
  from ..models.metric import Metric





T = TypeVar("T", bound="GetACCTopSalesCategoriesResponseDataCategory")



@_attrs_define
class GetACCTopSalesCategoriesResponseDataCategory:
    """ 
        Attributes:
            category_id (str | Unset): ID of the level-2 product category. Pass this ID as l2_category_id when querying
                PRODUCT in Get ACC Audience Preference List. These product category IDs are not the Market category IDs used for
                LIVE, VIDEO, or PHOTO.
            category_level (int | Unset): Product category level. The value is 2 for this node.
            category_name (str | Unset): Name of the level-2 product category.
            children (list[GetACCTopSalesCategoriesResponseDataCategoryChildren] | Unset): Level-3 categories under this
                level-2 category, after scope and keyword filtering, ordered by category ID in ascending numeric order. This
                list is not paginated.
            metrics (Metric | Unset):
     """

    category_id: str | Unset = UNSET
    category_level: int | Unset = UNSET
    category_name: str | Unset = UNSET
    children: list[GetACCTopSalesCategoriesResponseDataCategoryChildren] | Unset = UNSET
    metrics: Metric | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_top_sales_categories_response_data_category_children import GetACCTopSalesCategoriesResponseDataCategoryChildren # noqa: PLC0415
        from ..models.metric import Metric # noqa: PLC0415
        category_id = self.category_id

        category_level = self.category_level

        category_name = self.category_name

        children: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)



        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if category_level is not UNSET:
            field_dict["category_level"] = category_level
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if children is not UNSET:
            field_dict["children"] = children
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_acc_top_sales_categories_response_data_category_children import GetACCTopSalesCategoriesResponseDataCategoryChildren # noqa: PLC0415
        from ..models.metric import Metric # noqa: PLC0415
        d = dict(src_dict)
        category_id = d.pop("category_id", UNSET)

        category_level = d.pop("category_level", UNSET)

        category_name = d.pop("category_name", UNSET)

        _children = d.pop("children", UNSET)
        children: list[GetACCTopSalesCategoriesResponseDataCategoryChildren] | Unset = UNSET
        if _children is not UNSET:
            children = []
            for children_item_data in _children:
                children_item = GetACCTopSalesCategoriesResponseDataCategoryChildren.from_dict(children_item_data)



                children.append(children_item)


        _metrics = d.pop("metrics", UNSET)
        metrics: Metric | Unset
        if isinstance(_metrics,  Unset):
            metrics = UNSET
        else:
            metrics = Metric.from_dict(_metrics)




        get_acc_top_sales_categories_response_data_category = cls(
            category_id=category_id,
            category_level=category_level,
            category_name=category_name,
            children=children,
            metrics=metrics,
        )


        get_acc_top_sales_categories_response_data_category.additional_properties = d
        return get_acc_top_sales_categories_response_data_category

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
