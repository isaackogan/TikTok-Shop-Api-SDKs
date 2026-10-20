from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PublishGlobalProductResponseDataProductSkuSaleAttribute")



@_attrs_define
class PublishGlobalProductResponseDataProductSkuSaleAttribute:
    """ 
        Attributes:
            id (str | Unset): The newly generated local sales attribute ID.
            value_id (str | Unset): The newly generated local sales attribute value ID.
     """

    id: str | Unset = UNSET
    value_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        value_id = self.value_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if value_id is not UNSET:
            field_dict["value_id"] = value_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        value_id = d.pop("value_id", UNSET)

        publish_global_product_response_data_product_sku_sale_attribute = cls(
            id=id,
            value_id=value_id,
        )


        publish_global_product_response_data_product_sku_sale_attribute.additional_properties = d
        return publish_global_product_response_data_product_sku_sale_attribute

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
