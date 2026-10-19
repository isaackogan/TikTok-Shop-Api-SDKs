from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FBTInventoryUpdateWebhookDataFbtWarehouseInventoryOnHandDetail")


@_attrs_define
class FBTInventoryUpdateWebhookDataFbtWarehouseInventoryOnHandDetail:
    """
    Attributes:
        total_quantity (int | Unset): The total number of units.
        reserved_quantity (int | Unset): The number of units reserved for confirmed orders and yet to be outbound.
        available_quantity (int | Unset): The number of units available for sale. This does not include reserved units.
    """

    total_quantity: int | Unset = UNSET
    reserved_quantity: int | Unset = UNSET
    available_quantity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_quantity = self.total_quantity

        reserved_quantity = self.reserved_quantity

        available_quantity = self.available_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_quantity is not UNSET:
            field_dict["total_quantity"] = total_quantity
        if reserved_quantity is not UNSET:
            field_dict["reserved_quantity"] = reserved_quantity
        if available_quantity is not UNSET:
            field_dict["available_quantity"] = available_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_quantity = d.pop("total_quantity", UNSET)

        reserved_quantity = d.pop("reserved_quantity", UNSET)

        available_quantity = d.pop("available_quantity", UNSET)

        fbt_inventory_update_webhook_data_fbt_warehouse_inventory_on_hand_detail = cls(
            total_quantity=total_quantity,
            reserved_quantity=reserved_quantity,
            available_quantity=available_quantity,
        )

        fbt_inventory_update_webhook_data_fbt_warehouse_inventory_on_hand_detail.additional_properties = d
        return fbt_inventory_update_webhook_data_fbt_warehouse_inventory_on_hand_detail

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
