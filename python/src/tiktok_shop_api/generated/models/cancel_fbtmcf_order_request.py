from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cancel_fbtmcf_order_request_consign_order import CancelFBTMCFOrderRequestConsignOrder


T = TypeVar("T", bound="CancelFBTMCFOrderRequest")


@_attrs_define
class CancelFBTMCFOrderRequest:
    """
    Attributes:
        mcf_order_id (str): The MCF order ID as a numeric string.
        consign_orders (list[CancelFBTMCFOrderRequestConsignOrder] | Unset): The consign orders to cancel. Omit this
            field to cancel all consign orders in the specified MCF order.
    """

    mcf_order_id: str
    consign_orders: list[CancelFBTMCFOrderRequestConsignOrder] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mcf_order_id = self.mcf_order_id

        consign_orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.consign_orders, Unset):
            consign_orders = []
            for consign_orders_item_data in self.consign_orders:
                consign_orders_item = consign_orders_item_data.to_dict()
                consign_orders.append(consign_orders_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mcf_order_id": mcf_order_id,
            }
        )
        if consign_orders is not UNSET:
            field_dict["consign_orders"] = consign_orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cancel_fbtmcf_order_request_consign_order import (
            CancelFBTMCFOrderRequestConsignOrder,  # noqa: PLC0415
        )

        d = dict(src_dict)
        mcf_order_id = d.pop("mcf_order_id")

        _consign_orders = d.pop("consign_orders", UNSET)
        consign_orders: list[CancelFBTMCFOrderRequestConsignOrder] | Unset = UNSET
        if _consign_orders is not UNSET:
            consign_orders = []
            for consign_orders_item_data in _consign_orders:
                consign_orders_item = CancelFBTMCFOrderRequestConsignOrder.from_dict(consign_orders_item_data)

                consign_orders.append(consign_orders_item)

        cancel_fbtmcf_order_request = cls(
            mcf_order_id=mcf_order_id,
            consign_orders=consign_orders,
        )

        cancel_fbtmcf_order_request.additional_properties = d
        return cancel_fbtmcf_order_request

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
