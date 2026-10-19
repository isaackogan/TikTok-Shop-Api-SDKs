from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGlobalProductResponseDataSkuInventory")


@_attrs_define
class GetGlobalProductResponseDataSkuInventory:
    """
    Attributes:
        global_warehouse_id (str | Unset): The ID of the global warehouse where the SKU is stored.
        quantity (int | Unset): The SKU quantity available in the warehouse.
    """

    global_warehouse_id: str | Unset = UNSET
    quantity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_warehouse_id = self.global_warehouse_id

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if global_warehouse_id is not UNSET:
            field_dict["global_warehouse_id"] = global_warehouse_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        global_warehouse_id = d.pop("global_warehouse_id", UNSET)

        quantity = d.pop("quantity", UNSET)

        get_global_product_response_data_sku_inventory = cls(
            global_warehouse_id=global_warehouse_id,
            quantity=quantity,
        )

        get_global_product_response_data_sku_inventory.additional_properties = d
        return get_global_product_response_data_sku_inventory

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
