from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_product_package_recommendations_response_data_product_weight_recommendation_weight import GetProductPackageRecommendationsResponseDataProductWeightRecommendationWeight





T = TypeVar("T", bound="GetProductPackageRecommendationsResponseDataProductWeightRecommendation")



@_attrs_define
class GetProductPackageRecommendationsResponseDataProductWeightRecommendation:
    """ 
        Attributes:
            unit (str | Unset): Unit of weight, fixed as GRAM.
            weight (GetProductPackageRecommendationsResponseDataProductWeightRecommendationWeight | Unset):
     """

    unit: str | Unset = UNSET
    weight: GetProductPackageRecommendationsResponseDataProductWeightRecommendationWeight | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_product_package_recommendations_response_data_product_weight_recommendation_weight import GetProductPackageRecommendationsResponseDataProductWeightRecommendationWeight # noqa: PLC0415
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
        from ..models.get_product_package_recommendations_response_data_product_weight_recommendation_weight import GetProductPackageRecommendationsResponseDataProductWeightRecommendationWeight # noqa: PLC0415
        d = dict(src_dict)
        unit = d.pop("unit", UNSET)

        _weight = d.pop("weight", UNSET)
        weight: GetProductPackageRecommendationsResponseDataProductWeightRecommendationWeight | Unset
        if isinstance(_weight,  Unset):
            weight = UNSET
        else:
            weight = GetProductPackageRecommendationsResponseDataProductWeightRecommendationWeight.from_dict(_weight)




        get_product_package_recommendations_response_data_product_weight_recommendation = cls(
            unit=unit,
            weight=weight,
        )


        get_product_package_recommendations_response_data_product_weight_recommendation.additional_properties = d
        return get_product_package_recommendations_response_data_product_weight_recommendation

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
