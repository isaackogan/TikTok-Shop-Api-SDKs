from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.inventory_status_change_webhook_data_inventory_distribution import InventoryStatusChangeWebhookDataInventoryDistribution
  from ..models.inventory_status_change_webhook_data_trigger_reason import InventoryStatusChangeWebhookDataTriggerReason





T = TypeVar("T", bound="InventoryStatusChangeWebhookData")



@_attrs_define
class InventoryStatusChangeWebhookData:
    """ 
        Attributes:
            product_id (str | Unset): The ID of the product.
            sku_id (str | Unset): The ID of the SKU.
            trigger_reason (InventoryStatusChangeWebhookDataTriggerReason | Unset):
            current_inventory_status (str | Unset): SUFFICIENT_STOCK: defined as having enough stocks.
                 LOW_STOCK: defined as available stock ≤ stock alert value
                 OUT_OF_STOCK: defined as having 0 available stock.
            inventory_distribution (InventoryStatusChangeWebhookDataInventoryDistribution | Unset):
            update_time (int | Unset): The time when the status changed, represented as a Unix timestamp (seconds).
     """

    product_id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    trigger_reason: InventoryStatusChangeWebhookDataTriggerReason | Unset = UNSET
    current_inventory_status: str | Unset = UNSET
    inventory_distribution: InventoryStatusChangeWebhookDataInventoryDistribution | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.inventory_status_change_webhook_data_inventory_distribution import InventoryStatusChangeWebhookDataInventoryDistribution # noqa: PLC0415
        from ..models.inventory_status_change_webhook_data_trigger_reason import InventoryStatusChangeWebhookDataTriggerReason # noqa: PLC0415
        product_id = self.product_id

        sku_id = self.sku_id

        trigger_reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger_reason, Unset):
            trigger_reason = self.trigger_reason.to_dict()

        current_inventory_status = self.current_inventory_status

        inventory_distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inventory_distribution, Unset):
            inventory_distribution = self.inventory_distribution.to_dict()

        update_time = self.update_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if trigger_reason is not UNSET:
            field_dict["trigger_reason"] = trigger_reason
        if current_inventory_status is not UNSET:
            field_dict["current_inventory_status"] = current_inventory_status
        if inventory_distribution is not UNSET:
            field_dict["inventory_distribution"] = inventory_distribution
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_status_change_webhook_data_inventory_distribution import InventoryStatusChangeWebhookDataInventoryDistribution # noqa: PLC0415
        from ..models.inventory_status_change_webhook_data_trigger_reason import InventoryStatusChangeWebhookDataTriggerReason # noqa: PLC0415
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        _trigger_reason = d.pop("trigger_reason", UNSET)
        trigger_reason: InventoryStatusChangeWebhookDataTriggerReason | Unset
        if isinstance(_trigger_reason,  Unset):
            trigger_reason = UNSET
        else:
            trigger_reason = InventoryStatusChangeWebhookDataTriggerReason.from_dict(_trigger_reason)




        current_inventory_status = d.pop("current_inventory_status", UNSET)

        _inventory_distribution = d.pop("inventory_distribution", UNSET)
        inventory_distribution: InventoryStatusChangeWebhookDataInventoryDistribution | Unset
        if isinstance(_inventory_distribution,  Unset):
            inventory_distribution = UNSET
        else:
            inventory_distribution = InventoryStatusChangeWebhookDataInventoryDistribution.from_dict(_inventory_distribution)




        update_time = d.pop("update_time", UNSET)

        inventory_status_change_webhook_data = cls(
            product_id=product_id,
            sku_id=sku_id,
            trigger_reason=trigger_reason,
            current_inventory_status=current_inventory_status,
            inventory_distribution=inventory_distribution,
            update_time=update_time,
        )


        inventory_status_change_webhook_data.additional_properties = d
        return inventory_status_change_webhook_data

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
