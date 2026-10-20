from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.carton import Carton
    from ..models.ship_inbound_order_request_shipment_option import ShipInboundOrderRequestShipmentOption


T = TypeVar("T", bound="ShipInboundOrderRequest")


@_attrs_define
class ShipInboundOrderRequest:
    """
    Attributes:
        inbound_order_id (str): Identifier of the inbound order to ship.
        shipment_option (ShipInboundOrderRequestShipmentOption):
        cartons (list[Carton] | Unset): Carton details. Required when the inbound plan was created or updated using
            `goods_items` instead of `cartons` and the order has not already been shipped. Not required when retrying an
            order that has already been shipped.
    """

    inbound_order_id: str
    shipment_option: ShipInboundOrderRequestShipmentOption
    cartons: list[Carton] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbound_order_id = self.inbound_order_id

        shipment_option = self.shipment_option.to_dict()

        cartons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cartons, Unset):
            cartons = []
            for cartons_item_data in self.cartons:
                cartons_item = cartons_item_data.to_dict()
                cartons.append(cartons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inbound_order_id": inbound_order_id,
                "shipment_option": shipment_option,
            }
        )
        if cartons is not UNSET:
            field_dict["cartons"] = cartons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.carton import Carton  # noqa: PLC0415
        from ..models.ship_inbound_order_request_shipment_option import (
            ShipInboundOrderRequestShipmentOption,  # noqa: PLC0415
        )

        d = dict(src_dict)
        inbound_order_id = d.pop("inbound_order_id")

        shipment_option = ShipInboundOrderRequestShipmentOption.from_dict(d.pop("shipment_option"))

        _cartons = d.pop("cartons", UNSET)
        cartons: list[Carton] | Unset = UNSET
        if _cartons is not UNSET:
            cartons = []
            for cartons_item_data in _cartons:
                cartons_item = Carton.from_dict(cartons_item_data)

                cartons.append(cartons_item)

        ship_inbound_order_request = cls(
            inbound_order_id=inbound_order_id,
            shipment_option=shipment_option,
            cartons=cartons,
        )

        ship_inbound_order_request.additional_properties = d
        return ship_inbound_order_request

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
