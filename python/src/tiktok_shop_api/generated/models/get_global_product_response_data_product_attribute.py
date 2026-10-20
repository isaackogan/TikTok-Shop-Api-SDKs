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





T = TypeVar("T", bound="GetGlobalProductResponseDataProductAttribute")



@_attrs_define
class GetGlobalProductResponseDataProductAttribute:
    """ 
        Attributes:
            id (str | Unset): The ID of the product attribute.
            name (str | Unset): The product attribute name.
            values (list[GetGlobalAttributesResponseDataAttributeValue] | Unset): A list of selectable values for the
                product attribute.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    values: list[GetGlobalAttributesResponseDataAttributeValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_global_attributes_response_data_attribute_value import GetGlobalAttributesResponseDataAttributeValue # noqa: PLC0415
        id = self.id

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

        name = d.pop("name", UNSET)

        _values = d.pop("values", UNSET)
        values: list[GetGlobalAttributesResponseDataAttributeValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = GetGlobalAttributesResponseDataAttributeValue.from_dict(values_item_data)



                values.append(values_item)


        get_global_product_response_data_product_attribute = cls(
            id=id,
            name=name,
            values=values,
        )


        get_global_product_response_data_product_attribute.additional_properties = d
        return get_global_product_response_data_product_attribute

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
