from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Item")



@_attrs_define
class Item:
    """ 
        Attributes:
            goods_id (str): The Fulfilled by TikTok goods identifier for this carton item. The goods must belong to the
                merchant associated with the authenticated seller, be approved for fulfillment, and be matched to an SKU.
            quantity (int): Quantity of this goods item in each carton. Must be greater than 0.
            lot_code (str | Unset): Lot code for this goods item. Required when lot-code management is enabled for the
                goods. Every occurrence of the same `goods_id` in `cartons` must use the same `lot_code` and
                `expiration_timestamp` values.
            expiration_timestamp (str | Unset): The expiration date for this item, as a Unix timestamp in seconds. Required
                when expiration management is enabled for the goods. It must be no earlier than the current time plus the goods-
                specific `inbound_cutoff_days`. Obtain this value from `data.goods[].lot_expiration_info.inbound_cutoff_days` in
                Search Goods Info (`POST /fbt/202607/goods/search`).
     """

    goods_id: str
    quantity: int
    lot_code: str | Unset = UNSET
    expiration_timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        goods_id = self.goods_id

        quantity = self.quantity

        lot_code = self.lot_code

        expiration_timestamp = self.expiration_timestamp


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "goods_id": goods_id,
            "quantity": quantity,
        })
        if lot_code is not UNSET:
            field_dict["lot_code"] = lot_code
        if expiration_timestamp is not UNSET:
            field_dict["expiration_timestamp"] = expiration_timestamp

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        goods_id = d.pop("goods_id")

        quantity = d.pop("quantity")

        lot_code = d.pop("lot_code", UNSET)

        expiration_timestamp = d.pop("expiration_timestamp", UNSET)

        item = cls(
            goods_id=goods_id,
            quantity=quantity,
            lot_code=lot_code,
            expiration_timestamp=expiration_timestamp,
        )


        item.additional_properties = d
        return item

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
