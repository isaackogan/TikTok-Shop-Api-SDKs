from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inventory_search_response_data_inventory import InventorySearchResponseDataInventory


T = TypeVar("T", bound="InventorySearchResponseData")


@_attrs_define
class InventorySearchResponseData:
    """
    Attributes:
        inventory (list[InventorySearchResponseDataInventory] | Unset): Inventory information for the requested products
            or SKUs.
    """

    inventory: list[InventorySearchResponseDataInventory] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inventory: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = []
            for inventory_item_data in self.inventory:
                inventory_item = inventory_item_data.to_dict()
                inventory.append(inventory_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inventory is not UNSET:
            field_dict["inventory"] = inventory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_search_response_data_inventory import (
            InventorySearchResponseDataInventory,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _inventory = d.pop("inventory", UNSET)
        inventory: list[InventorySearchResponseDataInventory] | Unset = UNSET
        if _inventory is not UNSET:
            inventory = []
            for inventory_item_data in _inventory:
                inventory_item = InventorySearchResponseDataInventory.from_dict(inventory_item_data)

                inventory.append(inventory_item)

        inventory_search_response_data = cls(
            inventory=inventory,
        )

        inventory_search_response_data.additional_properties = d
        return inventory_search_response_data

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
