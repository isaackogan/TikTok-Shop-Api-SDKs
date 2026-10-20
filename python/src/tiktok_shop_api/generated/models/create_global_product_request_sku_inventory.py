from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CreateGlobalProductRequestSkuInventory")



@_attrs_define
class CreateGlobalProductRequestSkuInventory:
    """ 
        Attributes:
            global_warehouse_id (str): The ID of the global warehouse where the SKU is stored.
                Retrieve the list of global warehouses available for the seller from the [Get Global Seller Warehouse
                API](https://partner.tiktokshop.com/docv2/page/650aa3f0defece02be6e5ffb).
            quantity (int): The SKU quantity available in the warehouse.
                Valid range: [1, 99,999]
     """

    global_warehouse_id: str
    quantity: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        global_warehouse_id = self.global_warehouse_id

        quantity = self.quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "global_warehouse_id": global_warehouse_id,
            "quantity": quantity,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        global_warehouse_id = d.pop("global_warehouse_id")

        quantity = d.pop("quantity")

        create_global_product_request_sku_inventory = cls(
            global_warehouse_id=global_warehouse_id,
            quantity=quantity,
        )


        create_global_product_request_sku_inventory.additional_properties = d
        return create_global_product_request_sku_inventory

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
