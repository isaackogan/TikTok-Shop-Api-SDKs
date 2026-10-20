from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ListAvailableInboundMethodsResponseDataAvailableInboundMethodListWarehouseList")



@_attrs_define
class ListAvailableInboundMethodsResponseDataAvailableInboundMethodListWarehouseList:
    """ 
        Attributes:
            warehouse_name (str | Unset): Warehouse name for this available inbound method option.
            warehouse_id (str | Unset): Warehouse identifier for this available inbound method option.
     """

    warehouse_name: str | Unset = UNSET
    warehouse_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        warehouse_name = self.warehouse_name

        warehouse_id = self.warehouse_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if warehouse_name is not UNSET:
            field_dict["warehouse_name"] = warehouse_name
        if warehouse_id is not UNSET:
            field_dict["warehouse_id"] = warehouse_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        warehouse_name = d.pop("warehouse_name", UNSET)

        warehouse_id = d.pop("warehouse_id", UNSET)

        list_available_inbound_methods_response_data_available_inbound_method_list_warehouse_list = cls(
            warehouse_name=warehouse_name,
            warehouse_id=warehouse_id,
        )


        list_available_inbound_methods_response_data_available_inbound_method_list_warehouse_list.additional_properties = d
        return list_available_inbound_methods_response_data_available_inbound_method_list_warehouse_list

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
