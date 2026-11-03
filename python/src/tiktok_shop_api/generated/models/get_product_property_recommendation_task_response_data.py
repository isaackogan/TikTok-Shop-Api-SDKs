from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_product_property_recommendation_task_response_data_recommended_property import GetProductPropertyRecommendationTaskResponseDataRecommendedProperty





T = TypeVar("T", bound="GetProductPropertyRecommendationTaskResponseData")



@_attrs_define
class GetProductPropertyRecommendationTaskResponseData:
    """ 
        Attributes:
            recommended_properties (list[GetProductPropertyRecommendationTaskResponseDataRecommendedProperty] | Unset):
                Ordered product properties and values predicted for the product. The array is empty when no property
                recommendation is available.
            task_id (str | Unset): ID of the product property recommendation task.
     """

    recommended_properties: list[GetProductPropertyRecommendationTaskResponseDataRecommendedProperty] | Unset = UNSET
    task_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_product_property_recommendation_task_response_data_recommended_property import GetProductPropertyRecommendationTaskResponseDataRecommendedProperty # noqa: PLC0415
        recommended_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recommended_properties, Unset):
            recommended_properties = []
            for recommended_properties_item_data in self.recommended_properties:
                recommended_properties_item = recommended_properties_item_data.to_dict()
                recommended_properties.append(recommended_properties_item)



        task_id = self.task_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if recommended_properties is not UNSET:
            field_dict["recommended_properties"] = recommended_properties
        if task_id is not UNSET:
            field_dict["task_id"] = task_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_property_recommendation_task_response_data_recommended_property import GetProductPropertyRecommendationTaskResponseDataRecommendedProperty # noqa: PLC0415
        d = dict(src_dict)
        _recommended_properties = d.pop("recommended_properties", UNSET)
        recommended_properties: list[GetProductPropertyRecommendationTaskResponseDataRecommendedProperty] | Unset = UNSET
        if _recommended_properties is not UNSET:
            recommended_properties = []
            for recommended_properties_item_data in _recommended_properties:
                recommended_properties_item = GetProductPropertyRecommendationTaskResponseDataRecommendedProperty.from_dict(recommended_properties_item_data)



                recommended_properties.append(recommended_properties_item)


        task_id = d.pop("task_id", UNSET)

        get_product_property_recommendation_task_response_data = cls(
            recommended_properties=recommended_properties,
            task_id=task_id,
        )


        get_product_property_recommendation_task_response_data.additional_properties = d
        return get_product_property_recommendation_task_response_data

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
