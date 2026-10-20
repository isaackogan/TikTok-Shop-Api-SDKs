from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.fbt_inventory_update_webhook_data_fbt_warehouse_inventory import FBTInventoryUpdateWebhookDataFbtWarehouseInventory





T = TypeVar("T", bound="FBTInventoryUpdateWebhookData")



@_attrs_define
class FBTInventoryUpdateWebhookData:
    """ 
        Attributes:
            goods_id (str | Unset): FBT goods ID.
            sku_id (str | Unset): TikTok Shop SKU ID.
            fbt_warehouse_inventory (list[FBTInventoryUpdateWebhookDataFbtWarehouseInventory] | Unset): Inventory in
                different FBT warehouses.
            update_time (int | Unset): The time when the action occurred. Unix timestamp.
     """

    goods_id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    fbt_warehouse_inventory: list[FBTInventoryUpdateWebhookDataFbtWarehouseInventory] | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.fbt_inventory_update_webhook_data_fbt_warehouse_inventory import FBTInventoryUpdateWebhookDataFbtWarehouseInventory # noqa: PLC0415
        goods_id = self.goods_id

        sku_id = self.sku_id

        fbt_warehouse_inventory: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fbt_warehouse_inventory, Unset):
            fbt_warehouse_inventory = []
            for fbt_warehouse_inventory_item_data in self.fbt_warehouse_inventory:
                fbt_warehouse_inventory_item = fbt_warehouse_inventory_item_data.to_dict()
                fbt_warehouse_inventory.append(fbt_warehouse_inventory_item)



        update_time = self.update_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if goods_id is not UNSET:
            field_dict["goods_id"] = goods_id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if fbt_warehouse_inventory is not UNSET:
            field_dict["fbt_warehouse_inventory"] = fbt_warehouse_inventory
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fbt_inventory_update_webhook_data_fbt_warehouse_inventory import FBTInventoryUpdateWebhookDataFbtWarehouseInventory # noqa: PLC0415
        d = dict(src_dict)
        goods_id = d.pop("goods_id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        _fbt_warehouse_inventory = d.pop("fbt_warehouse_inventory", UNSET)
        fbt_warehouse_inventory: list[FBTInventoryUpdateWebhookDataFbtWarehouseInventory] | Unset = UNSET
        if _fbt_warehouse_inventory is not UNSET:
            fbt_warehouse_inventory = []
            for fbt_warehouse_inventory_item_data in _fbt_warehouse_inventory:
                fbt_warehouse_inventory_item = FBTInventoryUpdateWebhookDataFbtWarehouseInventory.from_dict(fbt_warehouse_inventory_item_data)



                fbt_warehouse_inventory.append(fbt_warehouse_inventory_item)


        update_time = d.pop("update_time", UNSET)

        fbt_inventory_update_webhook_data = cls(
            goods_id=goods_id,
            sku_id=sku_id,
            fbt_warehouse_inventory=fbt_warehouse_inventory,
            update_time=update_time,
        )


        fbt_inventory_update_webhook_data.additional_properties = d
        return fbt_inventory_update_webhook_data

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
