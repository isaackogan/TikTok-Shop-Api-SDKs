from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_available_inbound_methods_response_data_available_inbound_method_list import ListAvailableInboundMethodsResponseDataAvailableInboundMethodList





T = TypeVar("T", bound="ListAvailableInboundMethodsResponseData")



@_attrs_define
class ListAvailableInboundMethodsResponseData:
    """ 
        Attributes:
            available_inbound_method_list (list[ListAvailableInboundMethodsResponseDataAvailableInboundMethodList] | Unset):
                List of available inbound methods for the specified plan, including arrival time windows, placement fee
                estimates, and warehouses.
     """

    available_inbound_method_list: list[ListAvailableInboundMethodsResponseDataAvailableInboundMethodList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_available_inbound_methods_response_data_available_inbound_method_list import ListAvailableInboundMethodsResponseDataAvailableInboundMethodList # noqa: PLC0415
        available_inbound_method_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.available_inbound_method_list, Unset):
            available_inbound_method_list = []
            for available_inbound_method_list_item_data in self.available_inbound_method_list:
                available_inbound_method_list_item = available_inbound_method_list_item_data.to_dict()
                available_inbound_method_list.append(available_inbound_method_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if available_inbound_method_list is not UNSET:
            field_dict["available_inbound_method_list"] = available_inbound_method_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_available_inbound_methods_response_data_available_inbound_method_list import ListAvailableInboundMethodsResponseDataAvailableInboundMethodList # noqa: PLC0415
        d = dict(src_dict)
        _available_inbound_method_list = d.pop("available_inbound_method_list", UNSET)
        available_inbound_method_list: list[ListAvailableInboundMethodsResponseDataAvailableInboundMethodList] | Unset = UNSET
        if _available_inbound_method_list is not UNSET:
            available_inbound_method_list = []
            for available_inbound_method_list_item_data in _available_inbound_method_list:
                available_inbound_method_list_item = ListAvailableInboundMethodsResponseDataAvailableInboundMethodList.from_dict(available_inbound_method_list_item_data)



                available_inbound_method_list.append(available_inbound_method_list_item)


        list_available_inbound_methods_response_data = cls(
            available_inbound_method_list=available_inbound_method_list,
        )


        list_available_inbound_methods_response_data.additional_properties = d
        return list_available_inbound_methods_response_data

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
