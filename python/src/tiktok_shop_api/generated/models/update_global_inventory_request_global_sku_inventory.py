from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateGlobalInventoryRequestGlobalSkuInventory")


@_attrs_define
class UpdateGlobalInventoryRequestGlobalSkuInventory:
    """
    Attributes:
        global_warehouse_id (str): The ID of the global warehouse where the SKU is stored. The warehouse must be enabled
            and belong to this shop or seller. Retrieve this value from [Get Global Product](6509e2b0bace3e02b7490c96) or
            [Get Global Seller Warehouse](650aa3f0defece02be6e5ffb).
        quantity (int): The number of inventory units to set for this global SKU in the specified global warehouse. Must
            be 0 or greater.
    """

    global_warehouse_id: str
    quantity: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_warehouse_id = self.global_warehouse_id

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "global_warehouse_id": global_warehouse_id,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        global_warehouse_id = d.pop("global_warehouse_id")

        quantity = d.pop("quantity")

        update_global_inventory_request_global_sku_inventory = cls(
            global_warehouse_id=global_warehouse_id,
            quantity=quantity,
        )

        update_global_inventory_request_global_sku_inventory.additional_properties = d
        return update_global_inventory_request_global_sku_inventory

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
