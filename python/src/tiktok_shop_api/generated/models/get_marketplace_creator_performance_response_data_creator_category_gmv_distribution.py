from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetMarketplaceCreatorPerformanceResponseDataCreatorCategoryGmvDistribution")


@_attrs_define
class GetMarketplaceCreatorPerformanceResponseDataCreatorCategoryGmvDistribution:
    """
    Attributes:
        category_id (str | Unset): The top-level category identifier. A value of `-1` represents all other categories.
        value (str | Unset): The proportion of the creator's GMV attributed to this category, expressed as a decimal
            from `0` to `1` (for example, `0.3035` = 30.35%).
    """

    category_id: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_id = d.pop("category_id", UNSET)

        value = d.pop("value", UNSET)

        get_marketplace_creator_performance_response_data_creator_category_gmv_distribution = cls(
            category_id=category_id,
            value=value,
        )

        get_marketplace_creator_performance_response_data_creator_category_gmv_distribution.additional_properties = d
        return get_marketplace_creator_performance_response_data_creator_category_gmv_distribution

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
