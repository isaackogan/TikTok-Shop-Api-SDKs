from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetFBTInboundOrderDetailsResponseDataInboundOrderInboundGoodsLotReceiveItemDetail")


@_attrs_define
class GetFBTInboundOrderDetailsResponseDataInboundOrderInboundGoodsLotReceiveItemDetail:
    """
    Attributes:
        goods_id (str | Unset): The unique numeric identifier of the goods within Fulfilled by TikTok.
        lot_code (str | Unset): The batch or lot number assigned by the manufacturer for this group of items. This field
            is non-empty only for goods with lot code management.
        expiration_time (int | Unset): The expiration date of the items in this lot, represented as a Unix timestamp in
            seconds. This value is non-zero only for goods with expiration-date management.
        planned_count (int | Unset): The total quantity of this specific lot expected to be received as part of the
            inbound order.
        normal_received_count (int | Unset): The quantity of items received at **fulfillment centers** in sellable
            (good) condition for this lot. If the inbound order is sent to a hub, this value will only be updated when the
            goods are subsequently transferred to the fulfillment center.
        defective_received_count (int | Unset): The quantity of items received in a damaged or unsellable state.
        total_received_count (int | Unset): The sum of both `normal_received_count` and `defective_received_count`.
    """

    goods_id: str | Unset = UNSET
    lot_code: str | Unset = UNSET
    expiration_time: int | Unset = UNSET
    planned_count: int | Unset = UNSET
    normal_received_count: int | Unset = UNSET
    defective_received_count: int | Unset = UNSET
    total_received_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        goods_id = self.goods_id

        lot_code = self.lot_code

        expiration_time = self.expiration_time

        planned_count = self.planned_count

        normal_received_count = self.normal_received_count

        defective_received_count = self.defective_received_count

        total_received_count = self.total_received_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if goods_id is not UNSET:
            field_dict["goods_id"] = goods_id
        if lot_code is not UNSET:
            field_dict["lot_code"] = lot_code
        if expiration_time is not UNSET:
            field_dict["expiration_time"] = expiration_time
        if planned_count is not UNSET:
            field_dict["planned_count"] = planned_count
        if normal_received_count is not UNSET:
            field_dict["normal_received_count"] = normal_received_count
        if defective_received_count is not UNSET:
            field_dict["defective_received_count"] = defective_received_count
        if total_received_count is not UNSET:
            field_dict["total_received_count"] = total_received_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        goods_id = d.pop("goods_id", UNSET)

        lot_code = d.pop("lot_code", UNSET)

        expiration_time = d.pop("expiration_time", UNSET)

        planned_count = d.pop("planned_count", UNSET)

        normal_received_count = d.pop("normal_received_count", UNSET)

        defective_received_count = d.pop("defective_received_count", UNSET)

        total_received_count = d.pop("total_received_count", UNSET)

        get_fbt_inbound_order_details_response_data_inbound_order_inbound_goods_lot_receive_item_detail = cls(
            goods_id=goods_id,
            lot_code=lot_code,
            expiration_time=expiration_time,
            planned_count=planned_count,
            normal_received_count=normal_received_count,
            defective_received_count=defective_received_count,
            total_received_count=total_received_count,
        )

        get_fbt_inbound_order_details_response_data_inbound_order_inbound_goods_lot_receive_item_detail.additional_properties = d
        return get_fbt_inbound_order_details_response_data_inbound_order_inbound_goods_lot_receive_item_detail

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
