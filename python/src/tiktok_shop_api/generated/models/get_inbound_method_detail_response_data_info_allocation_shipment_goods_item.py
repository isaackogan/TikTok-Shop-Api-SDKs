from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetInboundMethodDetailResponseDataInfoAllocationShipmentGoodsItem")



@_attrs_define
class GetInboundMethodDetailResponseDataInfoAllocationShipmentGoodsItem:
    """ 
        Attributes:
            goods_id (str | Unset): Goods identifier.
            quantity (int | Unset): Quantity of this goods.
     """

    goods_id: str | Unset = UNSET
    quantity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        goods_id = self.goods_id

        quantity = self.quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if goods_id is not UNSET:
            field_dict["goods_id"] = goods_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        goods_id = d.pop("goods_id", UNSET)

        quantity = d.pop("quantity", UNSET)

        get_inbound_method_detail_response_data_info_allocation_shipment_goods_item = cls(
            goods_id=goods_id,
            quantity=quantity,
        )


        get_inbound_method_detail_response_data_info_allocation_shipment_goods_item.additional_properties = d
        return get_inbound_method_detail_response_data_info_allocation_shipment_goods_item

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
