from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishGlobalProductRequestPublishTargetSkuInventory")


@_attrs_define
class PublishGlobalProductRequestPublishTargetSkuInventory:
    """
    Attributes:
        warehouse_id (str | Unset): The warehouse ID. Retrieve this value from the [Get Warehouse List
            API](https://partner.tiktokshop.com/docv2/page/650aa418defece02be6e66b6).

            Default:
            - Sellers without multiple warehouses: The available warehouses will be used, prioritizing local warehouses in
            the specified market over warehouses in the seller's base country.
            - Sellers with multiple warehouses: The global warehouse ID
        quantity (int | Unset): The SKU quantity available in the warehouse.
            Valid range: [1, 99,999]

            **Note**: If the local SKU inventory quantity exceeds the global SKU quantity, the global SKU quantity will be
            updated to be the sum of all local inventories.
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

        publish_global_product_request_publish_target_sku_inventory = cls(
            warehouse_id=warehouse_id,
            quantity=quantity,
        )

        publish_global_product_request_publish_target_sku_inventory.additional_properties = d
        return publish_global_product_request_publish_target_sku_inventory

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
