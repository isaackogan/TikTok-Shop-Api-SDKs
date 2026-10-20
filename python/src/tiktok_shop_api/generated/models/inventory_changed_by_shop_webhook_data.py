from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.inventory_changed_by_shop_webhook_data_change_detail import InventoryChangedByShopWebhookDataChangeDetail
  from ..models.inventory_changed_by_shop_webhook_data_quantity_snapshot_after_change import InventoryChangedByShopWebhookDataQuantitySnapshotAfterChange





T = TypeVar("T", bound="InventoryChangedByShopWebhookData")



@_attrs_define
class InventoryChangedByShopWebhookData:
    """ 
        Attributes:
            event_id (str): An identifier for the inventory event; use it to deduplicate events.
            occurred_at (datetime.datetime): The event time in UTC, formatted as ISO 8601.
            shop_id (int): The ID of the shop whose inventory changed.
            product_id (int): The ID of the affected product.
            sku_id (int): The ID of the affected SKU.
            quantity_snapshot_after_change (InventoryChangedByShopWebhookDataQuantitySnapshotAfterChange):
            change_detail (list[InventoryChangedByShopWebhookDataChangeDetail]): The individual inventory changes associated
                with the event.
     """

    event_id: str
    occurred_at: datetime.datetime
    shop_id: int
    product_id: int
    sku_id: int
    quantity_snapshot_after_change: InventoryChangedByShopWebhookDataQuantitySnapshotAfterChange
    change_detail: list[InventoryChangedByShopWebhookDataChangeDetail]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.inventory_changed_by_shop_webhook_data_change_detail import InventoryChangedByShopWebhookDataChangeDetail # noqa: PLC0415
        from ..models.inventory_changed_by_shop_webhook_data_quantity_snapshot_after_change import InventoryChangedByShopWebhookDataQuantitySnapshotAfterChange # noqa: PLC0415
        event_id = self.event_id

        occurred_at = self.occurred_at.isoformat()

        shop_id = self.shop_id

        product_id = self.product_id

        sku_id = self.sku_id

        quantity_snapshot_after_change = self.quantity_snapshot_after_change.to_dict()

        change_detail = []
        for change_detail_item_data in self.change_detail:
            change_detail_item = change_detail_item_data.to_dict()
            change_detail.append(change_detail_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "event_id": event_id,
            "occurred_at": occurred_at,
            "shop_id": shop_id,
            "product_id": product_id,
            "sku_id": sku_id,
            "quantity_snapshot_after_change": quantity_snapshot_after_change,
            "change_detail": change_detail,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_changed_by_shop_webhook_data_change_detail import InventoryChangedByShopWebhookDataChangeDetail # noqa: PLC0415
        from ..models.inventory_changed_by_shop_webhook_data_quantity_snapshot_after_change import InventoryChangedByShopWebhookDataQuantitySnapshotAfterChange # noqa: PLC0415
        d = dict(src_dict)
        event_id = d.pop("event_id")

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))




        shop_id = d.pop("shop_id")

        product_id = d.pop("product_id")

        sku_id = d.pop("sku_id")

        quantity_snapshot_after_change = InventoryChangedByShopWebhookDataQuantitySnapshotAfterChange.from_dict(d.pop("quantity_snapshot_after_change"))




        change_detail = []
        _change_detail = d.pop("change_detail")
        for change_detail_item_data in (_change_detail):
            change_detail_item = InventoryChangedByShopWebhookDataChangeDetail.from_dict(change_detail_item_data)



            change_detail.append(change_detail_item)


        inventory_changed_by_shop_webhook_data = cls(
            event_id=event_id,
            occurred_at=occurred_at,
            shop_id=shop_id,
            product_id=product_id,
            sku_id=sku_id,
            quantity_snapshot_after_change=quantity_snapshot_after_change,
            change_detail=change_detail,
        )


        inventory_changed_by_shop_webhook_data.additional_properties = d
        return inventory_changed_by_shop_webhook_data

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
