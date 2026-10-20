from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.recommend_required_product_properties_response_data_recommended_property_value import RecommendRequiredProductPropertiesResponseDataRecommendedPropertyValue





T = TypeVar("T", bound="RecommendRequiredProductPropertiesResponseDataRecommendedProperty")



@_attrs_define
class RecommendRequiredProductPropertiesResponseDataRecommendedProperty:
    """ 
        Attributes:
            id (str): ID of the recommended property.
            is_customizable (bool): Whether the seller can enter a custom value when no recommended value applies.
            is_multiple_selection (bool): Whether the seller can select more than one value for the property.
            is_required (bool): Whether the property must be provided when the product is created or edited.
            name (str): Display name of the recommended property for the shop's region.
            type_ (str): Type of the recommended property.
                Possible values:
                - `UNSPECIFIED`: The service could not classify the property type.
                - `KEY_PROPERTY`: A key property used to identify the product.
                - `SALES_PROPERTY`: A sales property that defines product variants.
                - `PRODUCT_PROPERTY`: A property that describes the product as a whole.
            values (list[RecommendRequiredProductPropertiesResponseDataRecommendedPropertyValue]): Ordered values
                recommended for the property. The array is empty when the property requires a custom value or no value is
                recommended.
     """

    id: str
    is_customizable: bool
    is_multiple_selection: bool
    is_required: bool
    name: str
    type_: str
    values: list[RecommendRequiredProductPropertiesResponseDataRecommendedPropertyValue]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.recommend_required_product_properties_response_data_recommended_property_value import RecommendRequiredProductPropertiesResponseDataRecommendedPropertyValue # noqa: PLC0415
        id = self.id

        is_customizable = self.is_customizable

        is_multiple_selection = self.is_multiple_selection

        is_required = self.is_required

        name = self.name

        type_ = self.type_

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "is_customizable": is_customizable,
            "is_multiple_selection": is_multiple_selection,
            "is_required": is_required,
            "name": name,
            "type": type_,
            "values": values,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recommend_required_product_properties_response_data_recommended_property_value import RecommendRequiredProductPropertiesResponseDataRecommendedPropertyValue # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        is_customizable = d.pop("is_customizable")

        is_multiple_selection = d.pop("is_multiple_selection")

        is_required = d.pop("is_required")

        name = d.pop("name")

        type_ = d.pop("type")

        values = []
        _values = d.pop("values")
        for values_item_data in (_values):
            values_item = RecommendRequiredProductPropertiesResponseDataRecommendedPropertyValue.from_dict(values_item_data)



            values.append(values_item)


        recommend_required_product_properties_response_data_recommended_property = cls(
            id=id,
            is_customizable=is_customizable,
            is_multiple_selection=is_multiple_selection,
            is_required=is_required,
            name=name,
            type_=type_,
            values=values,
        )


        recommend_required_product_properties_response_data_recommended_property.additional_properties = d
        return recommend_required_product_properties_response_data_recommended_property

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
