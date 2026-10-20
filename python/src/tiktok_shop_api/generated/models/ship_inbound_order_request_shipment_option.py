from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ship_inbound_order_request_shipment_option_freight_type import ShipInboundOrderRequestShipmentOptionFreightType
from ..models.ship_inbound_order_request_shipment_option_shipping_method import ShipInboundOrderRequestShipmentOptionShippingMethod
from ..types import UNSET, Unset






T = TypeVar("T", bound="ShipInboundOrderRequestShipmentOption")



@_attrs_define
class ShipInboundOrderRequestShipmentOption:
    """ 
        Attributes:
            shipping_method (ShipInboundOrderRequestShipmentOptionShippingMethod): Shipping method. Possible values:
                SMALL_PARCEL (small parcel shipping); FREIGHT (freight shipping).
            freight_type (ShipInboundOrderRequestShipmentOptionFreightType | Unset): Freight load type. Required when
                `shipping_method` is `FREIGHT` for EU and UK shops. It is optional for US shops and is not required when
                `shipping_method` is `SMALL_PARCEL`.

                **Possible values:**
                * `FTL`
                * `LTL`
     """

    shipping_method: ShipInboundOrderRequestShipmentOptionShippingMethod
    freight_type: ShipInboundOrderRequestShipmentOptionFreightType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        shipping_method = self.shipping_method.value

        freight_type: str | Unset = UNSET
        if not isinstance(self.freight_type, Unset):
            freight_type = self.freight_type.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "shipping_method": shipping_method,
        })
        if freight_type is not UNSET:
            field_dict["freight_type"] = freight_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shipping_method = ShipInboundOrderRequestShipmentOptionShippingMethod(d.pop("shipping_method"))




        _freight_type = d.pop("freight_type", UNSET)
        freight_type: ShipInboundOrderRequestShipmentOptionFreightType | Unset
        if isinstance(_freight_type,  Unset):
            freight_type = UNSET
        else:
            freight_type = ShipInboundOrderRequestShipmentOptionFreightType(_freight_type)




        ship_inbound_order_request_shipment_option = cls(
            shipping_method=shipping_method,
            freight_type=freight_type,
        )


        ship_inbound_order_request_shipment_option.additional_properties = d
        return ship_inbound_order_request_shipment_option

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
