from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_product_package_recommendations_response_data_product_dimension_recommendation_height import (
        GetProductPackageRecommendationsResponseDataProductDimensionRecommendationHeight,
    )
    from ..models.get_product_package_recommendations_response_data_product_dimension_recommendation_length import (
        GetProductPackageRecommendationsResponseDataProductDimensionRecommendationLength,
    )
    from ..models.get_product_package_recommendations_response_data_product_dimension_recommendation_width import (
        GetProductPackageRecommendationsResponseDataProductDimensionRecommendationWidth,
    )


T = TypeVar("T", bound="GetProductPackageRecommendationsResponseDataProductDimensionRecommendation")


@_attrs_define
class GetProductPackageRecommendationsResponseDataProductDimensionRecommendation:
    """
    Attributes:
        unit (str | Unset): Unit of dimension, fixed as centimeter.
        length (GetProductPackageRecommendationsResponseDataProductDimensionRecommendationLength | Unset):
        height (GetProductPackageRecommendationsResponseDataProductDimensionRecommendationHeight | Unset):
        width (GetProductPackageRecommendationsResponseDataProductDimensionRecommendationWidth | Unset):
    """

    unit: str | Unset = UNSET
    length: GetProductPackageRecommendationsResponseDataProductDimensionRecommendationLength | Unset = UNSET
    height: GetProductPackageRecommendationsResponseDataProductDimensionRecommendationHeight | Unset = UNSET
    width: GetProductPackageRecommendationsResponseDataProductDimensionRecommendationWidth | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit = self.unit

        length: dict[str, Any] | Unset = UNSET
        if not isinstance(self.length, Unset):
            length = self.length.to_dict()

        height: dict[str, Any] | Unset = UNSET
        if not isinstance(self.height, Unset):
            height = self.height.to_dict()

        width: dict[str, Any] | Unset = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit is not UNSET:
            field_dict["unit"] = unit
        if length is not UNSET:
            field_dict["length"] = length
        if height is not UNSET:
            field_dict["height"] = height
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_package_recommendations_response_data_product_dimension_recommendation_height import (
            GetProductPackageRecommendationsResponseDataProductDimensionRecommendationHeight,  # noqa: PLC0415
        )
        from ..models.get_product_package_recommendations_response_data_product_dimension_recommendation_length import (
            GetProductPackageRecommendationsResponseDataProductDimensionRecommendationLength,  # noqa: PLC0415
        )
        from ..models.get_product_package_recommendations_response_data_product_dimension_recommendation_width import (
            GetProductPackageRecommendationsResponseDataProductDimensionRecommendationWidth,  # noqa: PLC0415
        )

        d = dict(src_dict)
        unit = d.pop("unit", UNSET)

        _length = d.pop("length", UNSET)
        length: GetProductPackageRecommendationsResponseDataProductDimensionRecommendationLength | Unset
        if isinstance(_length, Unset):
            length = UNSET
        else:
            length = GetProductPackageRecommendationsResponseDataProductDimensionRecommendationLength.from_dict(_length)

        _height = d.pop("height", UNSET)
        height: GetProductPackageRecommendationsResponseDataProductDimensionRecommendationHeight | Unset
        if isinstance(_height, Unset):
            height = UNSET
        else:
            height = GetProductPackageRecommendationsResponseDataProductDimensionRecommendationHeight.from_dict(_height)

        _width = d.pop("width", UNSET)
        width: GetProductPackageRecommendationsResponseDataProductDimensionRecommendationWidth | Unset
        if isinstance(_width, Unset):
            width = UNSET
        else:
            width = GetProductPackageRecommendationsResponseDataProductDimensionRecommendationWidth.from_dict(_width)

        get_product_package_recommendations_response_data_product_dimension_recommendation = cls(
            unit=unit,
            length=length,
            height=height,
            width=width,
        )

        get_product_package_recommendations_response_data_product_dimension_recommendation.additional_properties = d
        return get_product_package_recommendations_response_data_product_dimension_recommendation

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
