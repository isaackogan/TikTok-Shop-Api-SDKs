from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventorySearchResponseDataInventorySkuWarehouseInventory")


@_attrs_define
class InventorySearchResponseDataInventorySkuWarehouseInventory:
    """
    Attributes:
        warehouse_id (str | Unset): The ID of the warehouse where the SKU is stored.
            Retrieve details of the warehouse from the  [Get Warehouse List
            API](https://partner.tiktokshop.com/docv2/page/650aa418defece02be6e66b6).
        available_quantity (int | Unset): The total number of units available for ordering in this warehouse.
            This is equivalent to the `inventory.quantity` value returned in the [Get Product
            API](https://partner.tiktokshop.com/docv2/page/6509d85b4a0bb702c057fdda).
        committed_quantity (int | Unset): The total number of units reserved by existing customer orders in this
            warehouse (and therefore not available for ordering).
    """

    warehouse_id: str | Unset = UNSET
    available_quantity: int | Unset = UNSET
    committed_quantity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        available_quantity = self.available_quantity

        committed_quantity = self.committed_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warehouse_id is not UNSET:
            field_dict["warehouse_id"] = warehouse_id
        if available_quantity is not UNSET:
            field_dict["available_quantity"] = available_quantity
        if committed_quantity is not UNSET:
            field_dict["committed_quantity"] = committed_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        warehouse_id = d.pop("warehouse_id", UNSET)

        available_quantity = d.pop("available_quantity", UNSET)

        committed_quantity = d.pop("committed_quantity", UNSET)

        inventory_search_response_data_inventory_sku_warehouse_inventory = cls(
            warehouse_id=warehouse_id,
            available_quantity=available_quantity,
            committed_quantity=committed_quantity,
        )

        inventory_search_response_data_inventory_sku_warehouse_inventory.additional_properties = d
        return inventory_search_response_data_inventory_sku_warehouse_inventory

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
