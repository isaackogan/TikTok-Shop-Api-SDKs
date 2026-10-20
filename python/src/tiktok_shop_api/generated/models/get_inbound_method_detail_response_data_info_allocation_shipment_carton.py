from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_fbt_inbound_order_details_response_data_inbound_order_carton_detail_box_measurement import GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement
  from ..models.get_inbound_method_detail_response_data_info_allocation_shipment_carton_item import GetInboundMethodDetailResponseDataInfoAllocationShipmentCartonItem





T = TypeVar("T", bound="GetInboundMethodDetailResponseDataInfoAllocationShipmentCarton")



@_attrs_define
class GetInboundMethodDetailResponseDataInfoAllocationShipmentCarton:
    """ 
        Attributes:
            carton_type (str | Unset): Indicates if this is a single SKU carton or multi SKU carton.
                **Possible values:**
                * `SINGLE_SKU`
                * `MULTI_SKU`
            items (list[GetInboundMethodDetailResponseDataInfoAllocationShipmentCartonItem] | Unset): Goods item list of a
                carton.
            quantity (int | Unset): Carton quantity.
            carton_nums (list[str] | Unset): Carton numbers.
            box_measurements (GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement | Unset):
     """

    carton_type: str | Unset = UNSET
    items: list[GetInboundMethodDetailResponseDataInfoAllocationShipmentCartonItem] | Unset = UNSET
    quantity: int | Unset = UNSET
    carton_nums: list[str] | Unset = UNSET
    box_measurements: GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_fbt_inbound_order_details_response_data_inbound_order_carton_detail_box_measurement import GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement # noqa: PLC0415
        from ..models.get_inbound_method_detail_response_data_info_allocation_shipment_carton_item import GetInboundMethodDetailResponseDataInfoAllocationShipmentCartonItem # noqa: PLC0415
        carton_type = self.carton_type

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        quantity = self.quantity

        carton_nums: list[str] | Unset = UNSET
        if not isinstance(self.carton_nums, Unset):
            carton_nums = self.carton_nums



        box_measurements: dict[str, Any] | Unset = UNSET
        if not isinstance(self.box_measurements, Unset):
            box_measurements = self.box_measurements.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if carton_type is not UNSET:
            field_dict["carton_type"] = carton_type
        if items is not UNSET:
            field_dict["items"] = items
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if carton_nums is not UNSET:
            field_dict["carton_nums"] = carton_nums
        if box_measurements is not UNSET:
            field_dict["box_measurements"] = box_measurements

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_fbt_inbound_order_details_response_data_inbound_order_carton_detail_box_measurement import GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement # noqa: PLC0415
        from ..models.get_inbound_method_detail_response_data_info_allocation_shipment_carton_item import GetInboundMethodDetailResponseDataInfoAllocationShipmentCartonItem # noqa: PLC0415
        d = dict(src_dict)
        carton_type = d.pop("carton_type", UNSET)

        _items = d.pop("items", UNSET)
        items: list[GetInboundMethodDetailResponseDataInfoAllocationShipmentCartonItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = GetInboundMethodDetailResponseDataInfoAllocationShipmentCartonItem.from_dict(items_item_data)



                items.append(items_item)


        quantity = d.pop("quantity", UNSET)

        carton_nums = cast(list[str], d.pop("carton_nums", UNSET))


        _box_measurements = d.pop("box_measurements", UNSET)
        box_measurements: GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement | Unset
        if isinstance(_box_measurements,  Unset):
            box_measurements = UNSET
        else:
            box_measurements = GetFBTInboundOrderDetailsResponseDataInboundOrderCartonDetailBoxMeasurement.from_dict(_box_measurements)




        get_inbound_method_detail_response_data_info_allocation_shipment_carton = cls(
            carton_type=carton_type,
            items=items,
            quantity=quantity,
            carton_nums=carton_nums,
            box_measurements=box_measurements,
        )


        get_inbound_method_detail_response_data_info_allocation_shipment_carton.additional_properties = d
        return get_inbound_method_detail_response_data_info_allocation_shipment_carton

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
