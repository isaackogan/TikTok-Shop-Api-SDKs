from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditProductRequestReplicatedProductSkuInventory")


@_attrs_define
class EditProductRequestReplicatedProductSkuInventory:
    """
    Attributes:
        warehouse_id (str | Unset): The warehouse ID. Retrieve this value from the [Get Warehouse List
            API](650aa418defece02be6e66b6) or Get Inventory Rules API. This field is mandatory for other regions. But when
            syncing products from the US to MX, the MX product inventory field is optional.
        quantity (int | Unset): The SKU quantity available in the warehouse.
            Valid range: [1, 999,999]. This field is mandatory for other regions. But when syncing products from the US to
            MX, the MX product inventory field is optional.
    """

    warehouse_id: str | Unset = UNSET
    quantity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warehouse_id is not UNSET:
            field_dict["warehouse_id"] = warehouse_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        warehouse_id = d.pop("warehouse_id", UNSET)

        quantity = d.pop("quantity", UNSET)

        edit_product_request_replicated_product_sku_inventory = cls(
            warehouse_id=warehouse_id,
            quantity=quantity,
        )

        edit_product_request_replicated_product_sku_inventory.additional_properties = d
        return edit_product_request_replicated_product_sku_inventory

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
