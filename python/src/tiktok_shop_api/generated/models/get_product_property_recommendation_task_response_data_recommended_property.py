from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_global_attributes_response_data_attribute_value import GetGlobalAttributesResponseDataAttributeValue





T = TypeVar("T", bound="GetProductPropertyRecommendationTaskResponseDataRecommendedProperty")



@_attrs_define
class GetProductPropertyRecommendationTaskResponseDataRecommendedProperty:
    """ 
        Attributes:
            id (str | Unset): ID of the recommended property.
            is_customizable (bool | Unset): Whether the seller can enter a custom value when no recommended value applies.
            is_multiple_selection (bool | Unset): Whether the seller can select more than one value for the property.
            is_required (bool | Unset): Whether the property must be provided when the product is created or edited.
            name (str | Unset): Display name of the recommended property for the shop's region.
            values (list[GetGlobalAttributesResponseDataAttributeValue] | Unset): Ordered values recommended for the
                property. The array is empty when the property requires a custom value or no value is recommended.
     """

    id: str | Unset = UNSET
    is_customizable: bool | Unset = UNSET
    is_multiple_selection: bool | Unset = UNSET
    is_required: bool | Unset = UNSET
    name: str | Unset = UNSET
    values: list[GetGlobalAttributesResponseDataAttributeValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_global_attributes_response_data_attribute_value import GetGlobalAttributesResponseDataAttributeValue # noqa: PLC0415
        id = self.id

        is_customizable = self.is_customizable

        is_multiple_selection = self.is_multiple_selection

        is_required = self.is_required

        name = self.name

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if is_customizable is not UNSET:
            field_dict["is_customizable"] = is_customizable
        if is_multiple_selection is not UNSET:
            field_dict["is_multiple_selection"] = is_multiple_selection
        if is_required is not UNSET:
            field_dict["is_required"] = is_required
        if name is not UNSET:
            field_dict["name"] = name
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_global_attributes_response_data_attribute_value import GetGlobalAttributesResponseDataAttributeValue # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        is_customizable = d.pop("is_customizable", UNSET)

        is_multiple_selection = d.pop("is_multiple_selection", UNSET)

        is_required = d.pop("is_required", UNSET)

        name = d.pop("name", UNSET)

        _values = d.pop("values", UNSET)
        values: list[GetGlobalAttributesResponseDataAttributeValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = GetGlobalAttributesResponseDataAttributeValue.from_dict(values_item_data)



                values.append(values_item)


        get_product_property_recommendation_task_response_data_recommended_property = cls(
            id=id,
            is_customizable=is_customizable,
            is_multiple_selection=is_multiple_selection,
            is_required=is_required,
            name=name,
            values=values,
        )


        get_product_property_recommendation_task_response_data_recommended_property.additional_properties = d
        return get_product_property_recommendation_task_response_data_recommended_property

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
