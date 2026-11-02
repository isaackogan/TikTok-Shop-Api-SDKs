from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.stat import Stat





T = TypeVar("T", bound="GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductCategoryTopItemChildren")



@_attrs_define
class GetACCAudiencePreferenceSummaryResponseDataChannelSummaryProductCategoryTopItemChildren:
    """ 
        Attributes:
            category_id (str | Unset): ID of this level-3 product category.
            category_name (str | Unset): Name of this level-3 product category.
            level (int | Unset): Product category level. This node is level 3.
            stats (Stat | Unset):
     """

    category_id: str | Unset = UNSET
    category_name: str | Unset = UNSET
    level: int | Unset = UNSET
    stats: Stat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.stat import Stat # noqa: PLC0415
        category_id = self.category_id

        category_name = self.category_name

        level = self.level

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if category_name is not UNSET:
            field_dict["category_name"] = category_name
        if level is not UNSET:
            field_dict["level"] = level
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stat import Stat # noqa: PLC0415
        d = dict(src_dict)
        category_id = d.pop("category_id", UNSET)

        category_name = d.pop("category_name", UNSET)

        level = d.pop("level", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: Stat | Unset
        if isinstance(_stats,  Unset):
            stats = UNSET
        else:
            stats = Stat.from_dict(_stats)




        get_acc_audience_preference_summary_response_data_channel_summary_product_category_top_item_children = cls(
            category_id=category_id,
            category_name=category_name,
            level=level,
            stats=stats,
        )


        get_acc_audience_preference_summary_response_data_channel_summary_product_category_top_item_children.additional_properties = d
        return get_acc_audience_preference_summary_response_data_channel_summary_product_category_top_item_children

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
