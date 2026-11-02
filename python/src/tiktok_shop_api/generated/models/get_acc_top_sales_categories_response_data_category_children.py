from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.metric import Metric





T = TypeVar("T", bound="GetACCTopSalesCategoriesResponseDataCategoryChildren")



@_attrs_define
class GetACCTopSalesCategoriesResponseDataCategoryChildren:
    """ 
        Attributes:
            category_id (str | Unset): ID of the level-3 product category. To query PRODUCT preferences for this node, pass
                this ID as l3_category_id together with the parent level-2 category_id as l2_category_id.
            category_level (int | Unset): Product category level. The value is 3 for this node.
            category_name (str | Unset): Name of the level-3 product category.
            metrics (Metric | Unset):
     """

    category_id: str | Unset = UNSET
    category_level: int | Unset = UNSET
    category_name: str | Unset = UNSET
    metrics: Metric | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.metric import Metric # noqa: PLC0415
        category_id = self.category_id

        category_level = self.category_level

        category_name = self.category_name

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
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metric import Metric # noqa: PLC0415
        d = dict(src_dict)
        category_id = d.pop("category_id", UNSET)

        category_level = d.pop("category_level", UNSET)

        category_name = d.pop("category_name", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: Metric | Unset
        if isinstance(_metrics,  Unset):
            metrics = UNSET
        else:
            metrics = Metric.from_dict(_metrics)




        get_acc_top_sales_categories_response_data_category_children = cls(
            category_id=category_id,
            category_level=category_level,
            category_name=category_name,
            metrics=metrics,
        )


        get_acc_top_sales_categories_response_data_category_children.additional_properties = d
        return get_acc_top_sales_categories_response_data_category_children

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
