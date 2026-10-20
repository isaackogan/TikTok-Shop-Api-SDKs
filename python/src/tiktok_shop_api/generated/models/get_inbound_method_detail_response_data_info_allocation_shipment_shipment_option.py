from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetInboundMethodDetailResponseDataInfoAllocationShipmentShipmentOption")



@_attrs_define
class GetInboundMethodDetailResponseDataInfoAllocationShipmentShipmentOption:
    """ 
        Attributes:
            shipping_method (str | Unset): Shipping method for this shipment option. Possible values: SMALL_PARCEL, a parcel
                shipment method; FREIGHT, a freight shipment method.
     """

    shipping_method: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        shipping_method = self.shipping_method


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if shipping_method is not UNSET:
            field_dict["shipping_method"] = shipping_method

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shipping_method = d.pop("shipping_method", UNSET)

        get_inbound_method_detail_response_data_info_allocation_shipment_shipment_option = cls(
            shipping_method=shipping_method,
        )


        get_inbound_method_detail_response_data_info_allocation_shipment_shipment_option.additional_properties = d
        return get_inbound_method_detail_response_data_info_allocation_shipment_shipment_option

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
