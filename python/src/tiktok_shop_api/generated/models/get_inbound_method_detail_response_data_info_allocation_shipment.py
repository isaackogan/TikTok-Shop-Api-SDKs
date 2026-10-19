from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_inbound_method_detail_response_data_info_allocation_shipment_carton import (
        GetInboundMethodDetailResponseDataInfoAllocationShipmentCarton,
    )
    from ..models.get_inbound_method_detail_response_data_info_allocation_shipment_goods_item import (
        GetInboundMethodDetailResponseDataInfoAllocationShipmentGoodsItem,
    )
    from ..models.get_inbound_method_detail_response_data_info_allocation_shipment_shipment_option import (
        GetInboundMethodDetailResponseDataInfoAllocationShipmentShipmentOption,
    )


T = TypeVar("T", bound="GetInboundMethodDetailResponseDataInfoAllocationShipment")


@_attrs_define
class GetInboundMethodDetailResponseDataInfoAllocationShipment:
    """
    Attributes:
        warehouse_id (str | Unset): Warehouse identifier.
        goods_items (list[GetInboundMethodDetailResponseDataInfoAllocationShipmentGoodsItem] | Unset): Goods item list.
        cartons (list[GetInboundMethodDetailResponseDataInfoAllocationShipmentCarton] | Unset): Carton List.
        shipment_options (list[GetInboundMethodDetailResponseDataInfoAllocationShipmentShipmentOption] | Unset):
            Shipment options.
    """

    warehouse_id: str | Unset = UNSET
    goods_items: list[GetInboundMethodDetailResponseDataInfoAllocationShipmentGoodsItem] | Unset = UNSET
    cartons: list[GetInboundMethodDetailResponseDataInfoAllocationShipmentCarton] | Unset = UNSET
    shipment_options: list[GetInboundMethodDetailResponseDataInfoAllocationShipmentShipmentOption] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        goods_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.goods_items, Unset):
            goods_items = []
            for goods_items_item_data in self.goods_items:
                goods_items_item = goods_items_item_data.to_dict()
                goods_items.append(goods_items_item)

        cartons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cartons, Unset):
            cartons = []
            for cartons_item_data in self.cartons:
                cartons_item = cartons_item_data.to_dict()
                cartons.append(cartons_item)

        shipment_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shipment_options, Unset):
            shipment_options = []
            for shipment_options_item_data in self.shipment_options:
                shipment_options_item = shipment_options_item_data.to_dict()
                shipment_options.append(shipment_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warehouse_id is not UNSET:
            field_dict["warehouse_id"] = warehouse_id
        if goods_items is not UNSET:
            field_dict["goods_items"] = goods_items
        if cartons is not UNSET:
            field_dict["cartons"] = cartons
        if shipment_options is not UNSET:
            field_dict["shipment_options"] = shipment_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_inbound_method_detail_response_data_info_allocation_shipment_carton import (
            GetInboundMethodDetailResponseDataInfoAllocationShipmentCarton,  # noqa: PLC0415
        )
        from ..models.get_inbound_method_detail_response_data_info_allocation_shipment_goods_item import (
            GetInboundMethodDetailResponseDataInfoAllocationShipmentGoodsItem,  # noqa: PLC0415
        )
        from ..models.get_inbound_method_detail_response_data_info_allocation_shipment_shipment_option import (
            GetInboundMethodDetailResponseDataInfoAllocationShipmentShipmentOption,  # noqa: PLC0415
        )

        d = dict(src_dict)
        warehouse_id = d.pop("warehouse_id", UNSET)

        _goods_items = d.pop("goods_items", UNSET)
        goods_items: list[GetInboundMethodDetailResponseDataInfoAllocationShipmentGoodsItem] | Unset = UNSET
        if _goods_items is not UNSET:
            goods_items = []
            for goods_items_item_data in _goods_items:
                goods_items_item = GetInboundMethodDetailResponseDataInfoAllocationShipmentGoodsItem.from_dict(
                    goods_items_item_data
                )

                goods_items.append(goods_items_item)

        _cartons = d.pop("cartons", UNSET)
        cartons: list[GetInboundMethodDetailResponseDataInfoAllocationShipmentCarton] | Unset = UNSET
        if _cartons is not UNSET:
            cartons = []
            for cartons_item_data in _cartons:
                cartons_item = GetInboundMethodDetailResponseDataInfoAllocationShipmentCarton.from_dict(
                    cartons_item_data
                )

                cartons.append(cartons_item)

        _shipment_options = d.pop("shipment_options", UNSET)
        shipment_options: list[GetInboundMethodDetailResponseDataInfoAllocationShipmentShipmentOption] | Unset = UNSET
        if _shipment_options is not UNSET:
            shipment_options = []
            for shipment_options_item_data in _shipment_options:
                shipment_options_item = (
                    GetInboundMethodDetailResponseDataInfoAllocationShipmentShipmentOption.from_dict(
                        shipment_options_item_data
                    )
                )

                shipment_options.append(shipment_options_item)

        get_inbound_method_detail_response_data_info_allocation_shipment = cls(
            warehouse_id=warehouse_id,
            goods_items=goods_items,
            cartons=cartons,
            shipment_options=shipment_options,
        )

        get_inbound_method_detail_response_data_info_allocation_shipment.additional_properties = d
        return get_inbound_method_detail_response_data_info_allocation_shipment

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
