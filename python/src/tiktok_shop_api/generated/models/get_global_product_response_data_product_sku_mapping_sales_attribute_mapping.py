from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetGlobalProductResponseDataProductSkuMappingSalesAttributeMapping")



@_attrs_define
class GetGlobalProductResponseDataProductSkuMappingSalesAttributeMapping:
    """ 
        Attributes:
            global_attribute_id (str | Unset): The global sales attribute ID.
            local_attribute_id (str | Unset): The local sales attribute ID.
            global_value_id (str | Unset): The global sales attribute value ID.
            local_value_id (str | Unset): The local sales attribute value ID.
     """

    global_attribute_id: str | Unset = UNSET
    local_attribute_id: str | Unset = UNSET
    global_value_id: str | Unset = UNSET
    local_value_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        global_attribute_id = self.global_attribute_id

        local_attribute_id = self.local_attribute_id

        global_value_id = self.global_value_id

        local_value_id = self.local_value_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if global_attribute_id is not UNSET:
            field_dict["global_attribute_id"] = global_attribute_id
        if local_attribute_id is not UNSET:
            field_dict["local_attribute_id"] = local_attribute_id
        if global_value_id is not UNSET:
            field_dict["global_value_id"] = global_value_id
        if local_value_id is not UNSET:
            field_dict["local_value_id"] = local_value_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        global_attribute_id = d.pop("global_attribute_id", UNSET)

        local_attribute_id = d.pop("local_attribute_id", UNSET)

        global_value_id = d.pop("global_value_id", UNSET)

        local_value_id = d.pop("local_value_id", UNSET)

        get_global_product_response_data_product_sku_mapping_sales_attribute_mapping = cls(
            global_attribute_id=global_attribute_id,
            local_attribute_id=local_attribute_id,
            global_value_id=global_value_id,
            local_value_id=local_value_id,
        )


        get_global_product_response_data_product_sku_mapping_sales_attribute_mapping.additional_properties = d
        return get_global_product_response_data_product_sku_mapping_sales_attribute_mapping

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
