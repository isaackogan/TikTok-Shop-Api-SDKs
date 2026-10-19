from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchProductsResponseDataProductSkuInventory")


@_attrs_define
class SearchProductsResponseDataProductSkuInventory:
    """
    Attributes:
        warehouse_id (str | Unset): The ID of the warehouse where the SKU is stored.
            Retrieve details of the warehouse from the [Get Warehouse List
            API](https://partner.tiktokshop.com/docv2/page/650aa418defece02be6e66b6).
        quantity (int | Unset): The total SKU quantity available in the warehouse.
            Valid range: [1, 99,999]

            Note: This quantity specifically refers to the in-stock inventory that can be shipped immediately.
        backorder_quantity (int | Unset): The `backorder_quantity` will automatically be converted to `quantity` once
            in-stock inventory is sold out. The fulfillment of this inventory follows the `handling_time` specified below.
            Note: Made-to-order (MTO), pre-order, and custom products cannot be backordered, and thus are incompatible with
            backorder_quantity.
        handling_time (int | Unset): The estimated number of working days needed for a backorder to be shipped.
            Currently, different warehouses for the same SKU are not allowed to have different `handling_time`
    """

    warehouse_id: str | Unset = UNSET
    quantity: int | Unset = UNSET
    backorder_quantity: int | Unset = UNSET
    handling_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        quantity = self.quantity

        backorder_quantity = self.backorder_quantity

        handling_time = self.handling_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warehouse_id is not UNSET:
            field_dict["warehouse_id"] = warehouse_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if backorder_quantity is not UNSET:
            field_dict["backorder_quantity"] = backorder_quantity
        if handling_time is not UNSET:
            field_dict["handling_time"] = handling_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        warehouse_id = d.pop("warehouse_id", UNSET)

        quantity = d.pop("quantity", UNSET)

        backorder_quantity = d.pop("backorder_quantity", UNSET)

        handling_time = d.pop("handling_time", UNSET)

        search_products_response_data_product_sku_inventory = cls(
            warehouse_id=warehouse_id,
            quantity=quantity,
            backorder_quantity=backorder_quantity,
            handling_time=handling_time,
        )

        search_products_response_data_product_sku_inventory.additional_properties = d
        return search_products_response_data_product_sku_inventory

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
