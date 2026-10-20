from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.create_fbtmcf_order_request_consignee import CreateFBTMCFOrderRequestConsignee
  from ..models.create_fbtmcf_order_request_good import CreateFBTMCFOrderRequestGood





T = TypeVar("T", bound="CreateFBTMCFOrderRequest")



@_attrs_define
class CreateFBTMCFOrderRequest:
    """ 
        Attributes:
            external_order_id (str): The corresponding order ID in your OMS. Maximum UTF-8 length: 127 bytes. It must be
                unique among active MCF orders for the same merchant. Reusing an `external_order_id` from an active order is
                rejected as a duplicate and is not an idempotent retry.
            goods (list[CreateFBTMCFOrderRequestGood]): The item IDs and quantities included in the order. The array must
                contain at least one item, and each item must be managed in the FBT system. The sum of `quantity` across all
                entries in `goods` must not exceed 50.
            consignee (CreateFBTMCFOrderRequestConsignee):
     """

    external_order_id: str
    goods: list[CreateFBTMCFOrderRequestGood]
    consignee: CreateFBTMCFOrderRequestConsignee
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_fbtmcf_order_request_consignee import CreateFBTMCFOrderRequestConsignee # noqa: PLC0415
        from ..models.create_fbtmcf_order_request_good import CreateFBTMCFOrderRequestGood # noqa: PLC0415
        external_order_id = self.external_order_id

        goods = []
        for goods_item_data in self.goods:
            goods_item = goods_item_data.to_dict()
            goods.append(goods_item)



        consignee = self.consignee.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "external_order_id": external_order_id,
            "goods": goods,
            "consignee": consignee,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_fbtmcf_order_request_consignee import CreateFBTMCFOrderRequestConsignee # noqa: PLC0415
        from ..models.create_fbtmcf_order_request_good import CreateFBTMCFOrderRequestGood # noqa: PLC0415
        d = dict(src_dict)
        external_order_id = d.pop("external_order_id")

        goods = []
        _goods = d.pop("goods")
        for goods_item_data in (_goods):
            goods_item = CreateFBTMCFOrderRequestGood.from_dict(goods_item_data)



            goods.append(goods_item)


        consignee = CreateFBTMCFOrderRequestConsignee.from_dict(d.pop("consignee"))




        create_fbtmcf_order_request = cls(
            external_order_id=external_order_id,
            goods=goods,
            consignee=consignee,
        )


        create_fbtmcf_order_request.additional_properties = d
        return create_fbtmcf_order_request

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
