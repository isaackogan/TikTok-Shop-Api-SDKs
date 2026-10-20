from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.product_package_recommended_webhook_data_weight_recommendation_weight import ProductPackageRecommendedWebhookDataWeightRecommendationWeight





T = TypeVar("T", bound="ProductPackageRecommendedWebhookDataWeightRecommendation")



@_attrs_define
class ProductPackageRecommendedWebhookDataWeightRecommendation:
    """ 
        Attributes:
            unit (str | Unset): Recommended value unit
            weight (ProductPackageRecommendedWebhookDataWeightRecommendationWeight | Unset):
     """

    unit: str | Unset = UNSET
    weight: ProductPackageRecommendedWebhookDataWeightRecommendationWeight | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.product_package_recommended_webhook_data_weight_recommendation_weight import ProductPackageRecommendedWebhookDataWeightRecommendationWeight # noqa: PLC0415
        unit = self.unit

        weight: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weight, Unset):
            weight = self.weight.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if unit is not UNSET:
            field_dict["unit"] = unit
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_package_recommended_webhook_data_weight_recommendation_weight import ProductPackageRecommendedWebhookDataWeightRecommendationWeight # noqa: PLC0415
        d = dict(src_dict)
        unit = d.pop("unit", UNSET)

        _weight = d.pop("weight", UNSET)
        weight: ProductPackageRecommendedWebhookDataWeightRecommendationWeight | Unset
        if isinstance(_weight,  Unset):
            weight = UNSET
        else:
            weight = ProductPackageRecommendedWebhookDataWeightRecommendationWeight.from_dict(_weight)




        product_package_recommended_webhook_data_weight_recommendation = cls(
            unit=unit,
            weight=weight,
        )


        product_package_recommended_webhook_data_weight_recommendation.additional_properties = d
        return product_package_recommended_webhook_data_weight_recommendation

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
