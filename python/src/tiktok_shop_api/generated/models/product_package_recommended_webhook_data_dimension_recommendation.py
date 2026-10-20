from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_package_recommended_webhook_data_dimension_recommendation_height import (
        ProductPackageRecommendedWebhookDataDimensionRecommendationHeight,
    )
    from ..models.product_package_recommended_webhook_data_dimension_recommendation_length import (
        ProductPackageRecommendedWebhookDataDimensionRecommendationLength,
    )
    from ..models.product_package_recommended_webhook_data_dimension_recommendation_width import (
        ProductPackageRecommendedWebhookDataDimensionRecommendationWidth,
    )


T = TypeVar("T", bound="ProductPackageRecommendedWebhookDataDimensionRecommendation")


@_attrs_define
class ProductPackageRecommendedWebhookDataDimensionRecommendation:
    """
    Attributes:
        unit (str | Unset): Recommended value unit
        length (ProductPackageRecommendedWebhookDataDimensionRecommendationLength | Unset):
        width (ProductPackageRecommendedWebhookDataDimensionRecommendationWidth | Unset):
        height (ProductPackageRecommendedWebhookDataDimensionRecommendationHeight | Unset):
    """

    unit: str | Unset = UNSET
    length: ProductPackageRecommendedWebhookDataDimensionRecommendationLength | Unset = UNSET
    width: ProductPackageRecommendedWebhookDataDimensionRecommendationWidth | Unset = UNSET
    height: ProductPackageRecommendedWebhookDataDimensionRecommendationHeight | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit = self.unit

        length: dict[str, Any] | Unset = UNSET
        if not isinstance(self.length, Unset):
            length = self.length.to_dict()

        width: dict[str, Any] | Unset = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.to_dict()

        height: dict[str, Any] | Unset = UNSET
        if not isinstance(self.height, Unset):
            height = self.height.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit is not UNSET:
            field_dict["unit"] = unit
        if length is not UNSET:
            field_dict["length"] = length
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_package_recommended_webhook_data_dimension_recommendation_height import (
            ProductPackageRecommendedWebhookDataDimensionRecommendationHeight,  # noqa: PLC0415
        )
        from ..models.product_package_recommended_webhook_data_dimension_recommendation_length import (
            ProductPackageRecommendedWebhookDataDimensionRecommendationLength,  # noqa: PLC0415
        )
        from ..models.product_package_recommended_webhook_data_dimension_recommendation_width import (
            ProductPackageRecommendedWebhookDataDimensionRecommendationWidth,  # noqa: PLC0415
        )

        d = dict(src_dict)
        unit = d.pop("unit", UNSET)

        _length = d.pop("length", UNSET)
        length: ProductPackageRecommendedWebhookDataDimensionRecommendationLength | Unset
        if isinstance(_length, Unset):
            length = UNSET
        else:
            length = ProductPackageRecommendedWebhookDataDimensionRecommendationLength.from_dict(_length)

        _width = d.pop("width", UNSET)
        width: ProductPackageRecommendedWebhookDataDimensionRecommendationWidth | Unset
        if isinstance(_width, Unset):
            width = UNSET
        else:
            width = ProductPackageRecommendedWebhookDataDimensionRecommendationWidth.from_dict(_width)

        _height = d.pop("height", UNSET)
        height: ProductPackageRecommendedWebhookDataDimensionRecommendationHeight | Unset
        if isinstance(_height, Unset):
            height = UNSET
        else:
            height = ProductPackageRecommendedWebhookDataDimensionRecommendationHeight.from_dict(_height)

        product_package_recommended_webhook_data_dimension_recommendation = cls(
            unit=unit,
            length=length,
            width=width,
            height=height,
        )

        product_package_recommended_webhook_data_dimension_recommendation.additional_properties = d
        return product_package_recommended_webhook_data_dimension_recommendation

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
