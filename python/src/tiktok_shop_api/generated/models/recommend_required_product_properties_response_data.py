from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recommend_required_product_properties_response_data_recommended_property import (
        RecommendRequiredProductPropertiesResponseDataRecommendedProperty,
    )


T = TypeVar("T", bound="RecommendRequiredProductPropertiesResponseData")


@_attrs_define
class RecommendRequiredProductPropertiesResponseData:
    """
    Attributes:
        recommended_properties (list[RecommendRequiredProductPropertiesResponseDataRecommendedProperty] | Unset):
            Ordered required properties predicted for the product. The array is empty when no property recommendation is
            available.
    """

    recommended_properties: list[RecommendRequiredProductPropertiesResponseDataRecommendedProperty] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recommended_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recommended_properties, Unset):
            recommended_properties = []
            for recommended_properties_item_data in self.recommended_properties:
                recommended_properties_item = recommended_properties_item_data.to_dict()
                recommended_properties.append(recommended_properties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recommended_properties is not UNSET:
            field_dict["recommended_properties"] = recommended_properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recommend_required_product_properties_response_data_recommended_property import (
            RecommendRequiredProductPropertiesResponseDataRecommendedProperty,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _recommended_properties = d.pop("recommended_properties", UNSET)
        recommended_properties: list[RecommendRequiredProductPropertiesResponseDataRecommendedProperty] | Unset = UNSET
        if _recommended_properties is not UNSET:
            recommended_properties = []
            for recommended_properties_item_data in _recommended_properties:
                recommended_properties_item = (
                    RecommendRequiredProductPropertiesResponseDataRecommendedProperty.from_dict(
                        recommended_properties_item_data
                    )
                )

                recommended_properties.append(recommended_properties_item)

        recommend_required_product_properties_response_data = cls(
            recommended_properties=recommended_properties,
        )

        recommend_required_product_properties_response_data.additional_properties = d
        return recommend_required_product_properties_response_data

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
