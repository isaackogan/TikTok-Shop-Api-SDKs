from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PartialEditProductRequestSkuInventory")



@_attrs_define
class PartialEditProductRequestSkuInventory:
    """ 
        Attributes:
            quantity (int): The total SKU quantity available in the warehouse.
                Valid range: [1, 99,999]

                Note: This quantity specifically refers to the in-stock inventory that can be shipped immediately.
            warehouse_id (str): The ID of the warehouse where the SKU is stored.
                Retrieve the list of warehouses available for your shop from the [Get Warehouse List
                API](https://partner.tiktokshop.com/docv2/page/650aa418defece02be6e66b6).
            backorder_quantity (int | Unset): The `backorder_quantity` is automatically converted to `quantity` once in-
                stock inventory is sold out. Its fulfillment follows the specified `handling_time`.

                **Note**:
                - For non-virtual products, provide `backorder_quantity` and `handling_time` together.
                - Made-to-order (MTO), pre-order, and custom products cannot be backordered and therefore cannot use
                `backorder_quantity`.
            handling_time (int | Unset): The estimated number of working days needed for a backorder to be shipped. For non-
                virtual products, provide `handling_time` and `backorder_quantity` together. Different warehouses for the same
                SKU cannot use different `handling_time` values.
     """

    quantity: int
    warehouse_id: str
    backorder_quantity: int | Unset = UNSET
    handling_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        warehouse_id = self.warehouse_id

        backorder_quantity = self.backorder_quantity

        handling_time = self.handling_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "quantity": quantity,
            "warehouse_id": warehouse_id,
        })
        if backorder_quantity is not UNSET:
            field_dict["backorder_quantity"] = backorder_quantity
        if handling_time is not UNSET:
            field_dict["handling_time"] = handling_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity")

        warehouse_id = d.pop("warehouse_id")

        backorder_quantity = d.pop("backorder_quantity", UNSET)

        handling_time = d.pop("handling_time", UNSET)

        partial_edit_product_request_sku_inventory = cls(
            quantity=quantity,
            warehouse_id=warehouse_id,
            backorder_quantity=backorder_quantity,
            handling_time=handling_time,
        )


        partial_edit_product_request_sku_inventory.additional_properties = d
        return partial_edit_product_request_sku_inventory

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
