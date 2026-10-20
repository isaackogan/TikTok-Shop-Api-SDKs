from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetProductPackageRecommendationsResponseDataProductDimensionRecommendationWidth")



@_attrs_define
class GetProductPackageRecommendationsResponseDataProductDimensionRecommendationWidth:
    """ 
        Attributes:
            min_value (str | Unset): Recommended range minimum; unit: cm
            max_value (str | Unset): Recommended range maximum; unit: cm
     """

    min_value: str | Unset = UNSET
    max_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        min_value = self.min_value

        max_value = self.max_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if max_value is not UNSET:
            field_dict["max_value"] = max_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_value = d.pop("min_value", UNSET)

        max_value = d.pop("max_value", UNSET)

        get_product_package_recommendations_response_data_product_dimension_recommendation_width = cls(
            min_value=min_value,
            max_value=max_value,
        )


        get_product_package_recommendations_response_data_product_dimension_recommendation_width.additional_properties = d
        return get_product_package_recommendations_response_data_product_dimension_recommendation_width

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
