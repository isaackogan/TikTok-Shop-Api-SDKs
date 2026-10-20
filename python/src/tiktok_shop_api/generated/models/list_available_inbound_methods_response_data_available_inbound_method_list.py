from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_available_inbound_methods_response_data_available_inbound_method_list_available_time_window_list import ListAvailableInboundMethodsResponseDataAvailableInboundMethodListAvailableTimeWindowList
  from ..models.list_available_inbound_methods_response_data_available_inbound_method_list_placement_fee_estimate import ListAvailableInboundMethodsResponseDataAvailableInboundMethodListPlacementFeeEstimate
  from ..models.list_available_inbound_methods_response_data_available_inbound_method_list_warehouse_list import ListAvailableInboundMethodsResponseDataAvailableInboundMethodListWarehouseList





T = TypeVar("T", bound="ListAvailableInboundMethodsResponseDataAvailableInboundMethodList")



@_attrs_define
class ListAvailableInboundMethodsResponseDataAvailableInboundMethodList:
    """ 
        Attributes:
            inbound_method (str | Unset): Inbound method.
                - D2FC
                - ONE_HUB
            available_time_window_list
                (list[ListAvailableInboundMethodsResponseDataAvailableInboundMethodListAvailableTimeWindowList] | Unset): Weekly
                arrival time windows available for this inbound method.
            warehouse_list (list[ListAvailableInboundMethodsResponseDataAvailableInboundMethodListWarehouseList] | Unset):
                List of warehouses available for this inbound method option.
            placement_fee_estimate (ListAvailableInboundMethodsResponseDataAvailableInboundMethodListPlacementFeeEstimate |
                Unset):
     """

    inbound_method: str | Unset = UNSET
    available_time_window_list: list[ListAvailableInboundMethodsResponseDataAvailableInboundMethodListAvailableTimeWindowList] | Unset = UNSET
    warehouse_list: list[ListAvailableInboundMethodsResponseDataAvailableInboundMethodListWarehouseList] | Unset = UNSET
    placement_fee_estimate: ListAvailableInboundMethodsResponseDataAvailableInboundMethodListPlacementFeeEstimate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_available_inbound_methods_response_data_available_inbound_method_list_available_time_window_list import ListAvailableInboundMethodsResponseDataAvailableInboundMethodListAvailableTimeWindowList # noqa: PLC0415
        from ..models.list_available_inbound_methods_response_data_available_inbound_method_list_placement_fee_estimate import ListAvailableInboundMethodsResponseDataAvailableInboundMethodListPlacementFeeEstimate # noqa: PLC0415
        from ..models.list_available_inbound_methods_response_data_available_inbound_method_list_warehouse_list import ListAvailableInboundMethodsResponseDataAvailableInboundMethodListWarehouseList # noqa: PLC0415
        inbound_method = self.inbound_method

        available_time_window_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.available_time_window_list, Unset):
            available_time_window_list = []
            for available_time_window_list_item_data in self.available_time_window_list:
                available_time_window_list_item = available_time_window_list_item_data.to_dict()
                available_time_window_list.append(available_time_window_list_item)



        warehouse_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warehouse_list, Unset):
            warehouse_list = []
            for warehouse_list_item_data in self.warehouse_list:
                warehouse_list_item = warehouse_list_item_data.to_dict()
                warehouse_list.append(warehouse_list_item)



        placement_fee_estimate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.placement_fee_estimate, Unset):
            placement_fee_estimate = self.placement_fee_estimate.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if inbound_method is not UNSET:
            field_dict["inbound_method"] = inbound_method
        if available_time_window_list is not UNSET:
            field_dict["available_time_window_list"] = available_time_window_list
        if warehouse_list is not UNSET:
            field_dict["warehouse_list"] = warehouse_list
        if placement_fee_estimate is not UNSET:
            field_dict["placement_fee_estimate"] = placement_fee_estimate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_available_inbound_methods_response_data_available_inbound_method_list_available_time_window_list import ListAvailableInboundMethodsResponseDataAvailableInboundMethodListAvailableTimeWindowList # noqa: PLC0415
        from ..models.list_available_inbound_methods_response_data_available_inbound_method_list_placement_fee_estimate import ListAvailableInboundMethodsResponseDataAvailableInboundMethodListPlacementFeeEstimate # noqa: PLC0415
        from ..models.list_available_inbound_methods_response_data_available_inbound_method_list_warehouse_list import ListAvailableInboundMethodsResponseDataAvailableInboundMethodListWarehouseList # noqa: PLC0415
        d = dict(src_dict)
        inbound_method = d.pop("inbound_method", UNSET)

        _available_time_window_list = d.pop("available_time_window_list", UNSET)
        available_time_window_list: list[ListAvailableInboundMethodsResponseDataAvailableInboundMethodListAvailableTimeWindowList] | Unset = UNSET
        if _available_time_window_list is not UNSET:
            available_time_window_list = []
            for available_time_window_list_item_data in _available_time_window_list:
                available_time_window_list_item = ListAvailableInboundMethodsResponseDataAvailableInboundMethodListAvailableTimeWindowList.from_dict(available_time_window_list_item_data)



                available_time_window_list.append(available_time_window_list_item)


        _warehouse_list = d.pop("warehouse_list", UNSET)
        warehouse_list: list[ListAvailableInboundMethodsResponseDataAvailableInboundMethodListWarehouseList] | Unset = UNSET
        if _warehouse_list is not UNSET:
            warehouse_list = []
            for warehouse_list_item_data in _warehouse_list:
                warehouse_list_item = ListAvailableInboundMethodsResponseDataAvailableInboundMethodListWarehouseList.from_dict(warehouse_list_item_data)



                warehouse_list.append(warehouse_list_item)


        _placement_fee_estimate = d.pop("placement_fee_estimate", UNSET)
        placement_fee_estimate: ListAvailableInboundMethodsResponseDataAvailableInboundMethodListPlacementFeeEstimate | Unset
        if isinstance(_placement_fee_estimate,  Unset):
            placement_fee_estimate = UNSET
        else:
            placement_fee_estimate = ListAvailableInboundMethodsResponseDataAvailableInboundMethodListPlacementFeeEstimate.from_dict(_placement_fee_estimate)




        list_available_inbound_methods_response_data_available_inbound_method_list = cls(
            inbound_method=inbound_method,
            available_time_window_list=available_time_window_list,
            warehouse_list=warehouse_list,
            placement_fee_estimate=placement_fee_estimate,
        )


        list_available_inbound_methods_response_data_available_inbound_method_list.additional_properties = d
        return list_available_inbound_methods_response_data_available_inbound_method_list

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
