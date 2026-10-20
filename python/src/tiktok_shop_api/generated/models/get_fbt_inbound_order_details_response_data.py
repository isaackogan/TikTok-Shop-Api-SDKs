from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_fbt_inbound_order_details_response_data_inbound_order import (
        GetFBTInboundOrderDetailsResponseDataInboundOrder,
    )


T = TypeVar("T", bound="GetFBTInboundOrderDetailsResponseData")


@_attrs_define
class GetFBTInboundOrderDetailsResponseData:
    """
    Attributes:
        inbound_orders (list[GetFBTInboundOrderDetailsResponseDataInboundOrder] | Unset): A list of inbound order detail
            information.
    """

    inbound_orders: list[GetFBTInboundOrderDetailsResponseDataInboundOrder] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inbound_orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inbound_orders, Unset):
            inbound_orders = []
            for inbound_orders_item_data in self.inbound_orders:
                inbound_orders_item = inbound_orders_item_data.to_dict()
                inbound_orders.append(inbound_orders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inbound_orders is not UNSET:
            field_dict["inbound_orders"] = inbound_orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_fbt_inbound_order_details_response_data_inbound_order import (
            GetFBTInboundOrderDetailsResponseDataInboundOrder,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _inbound_orders = d.pop("inbound_orders", UNSET)
        inbound_orders: list[GetFBTInboundOrderDetailsResponseDataInboundOrder] | Unset = UNSET
        if _inbound_orders is not UNSET:
            inbound_orders = []
            for inbound_orders_item_data in _inbound_orders:
                inbound_orders_item = GetFBTInboundOrderDetailsResponseDataInboundOrder.from_dict(
                    inbound_orders_item_data
                )

                inbound_orders.append(inbound_orders_item)

        get_fbt_inbound_order_details_response_data = cls(
            inbound_orders=inbound_orders,
        )

        get_fbt_inbound_order_details_response_data.additional_properties = d
        return get_fbt_inbound_order_details_response_data

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
