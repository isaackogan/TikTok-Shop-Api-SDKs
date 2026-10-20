from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_fbtmcf_order_status_webhook_data_mcf_order_consign_order import (
        GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrder,
    )


T = TypeVar("T", bound="GetFBTMCFOrderStatusWebhookDataMcfOrder")


@_attrs_define
class GetFBTMCFOrderStatusWebhookDataMcfOrder:
    """
    Attributes:
        external_order_id (str | Unset): The corresponding order ID in your OMS.
        mcf_order_id (str | Unset): A unique ID that identifies different MCF orders
        consign_orders (list[GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrder] | Unset): Once the order has been
            shipped, the `consign_orders` field will display the consignment details of the order.
        create_time (int | Unset): The time when the mcf order is created
    """

    external_order_id: str | Unset = UNSET
    mcf_order_id: str | Unset = UNSET
    consign_orders: list[GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrder] | Unset = UNSET
    create_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        external_order_id = self.external_order_id

        mcf_order_id = self.mcf_order_id

        consign_orders: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.consign_orders, Unset):
            consign_orders = []
            for consign_orders_item_data in self.consign_orders:
                consign_orders_item = consign_orders_item_data.to_dict()
                consign_orders.append(consign_orders_item)

        create_time = self.create_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_order_id is not UNSET:
            field_dict["external_order_id"] = external_order_id
        if mcf_order_id is not UNSET:
            field_dict["mcf_order_id"] = mcf_order_id
        if consign_orders is not UNSET:
            field_dict["consign_orders"] = consign_orders
        if create_time is not UNSET:
            field_dict["create_time"] = create_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_fbtmcf_order_status_webhook_data_mcf_order_consign_order import (
            GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrder,  # noqa: PLC0415
        )

        d = dict(src_dict)
        external_order_id = d.pop("external_order_id", UNSET)

        mcf_order_id = d.pop("mcf_order_id", UNSET)

        _consign_orders = d.pop("consign_orders", UNSET)
        consign_orders: list[GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrder] | Unset = UNSET
        if _consign_orders is not UNSET:
            consign_orders = []
            for consign_orders_item_data in _consign_orders:
                consign_orders_item = GetFBTMCFOrderStatusWebhookDataMcfOrderConsignOrder.from_dict(
                    consign_orders_item_data
                )

                consign_orders.append(consign_orders_item)

        create_time = d.pop("create_time", UNSET)

        get_fbtmcf_order_status_webhook_data_mcf_order = cls(
            external_order_id=external_order_id,
            mcf_order_id=mcf_order_id,
            consign_orders=consign_orders,
            create_time=create_time,
        )

        get_fbtmcf_order_status_webhook_data_mcf_order.additional_properties = d
        return get_fbtmcf_order_status_webhook_data_mcf_order

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
