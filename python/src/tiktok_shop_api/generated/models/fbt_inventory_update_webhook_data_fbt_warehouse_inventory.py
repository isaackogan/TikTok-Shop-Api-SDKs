from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.fbt_inventory_update_webhook_data_fbt_warehouse_inventory_on_hand_detail import FBTInventoryUpdateWebhookDataFbtWarehouseInventoryOnHandDetail





T = TypeVar("T", bound="FBTInventoryUpdateWebhookDataFbtWarehouseInventory")



@_attrs_define
class FBTInventoryUpdateWebhookDataFbtWarehouseInventory:
    """ 
        Attributes:
            fbt_warehouse_id (str | Unset): ID of the FBT warehouse.
            on_hand_detail (FBTInventoryUpdateWebhookDataFbtWarehouseInventoryOnHandDetail | Unset):
     """

    fbt_warehouse_id: str | Unset = UNSET
    on_hand_detail: FBTInventoryUpdateWebhookDataFbtWarehouseInventoryOnHandDetail | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.fbt_inventory_update_webhook_data_fbt_warehouse_inventory_on_hand_detail import FBTInventoryUpdateWebhookDataFbtWarehouseInventoryOnHandDetail # noqa: PLC0415
        fbt_warehouse_id = self.fbt_warehouse_id

        on_hand_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.on_hand_detail, Unset):
            on_hand_detail = self.on_hand_detail.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fbt_warehouse_id is not UNSET:
            field_dict["fbt_warehouse_id"] = fbt_warehouse_id
        if on_hand_detail is not UNSET:
            field_dict["on_hand_detail"] = on_hand_detail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fbt_inventory_update_webhook_data_fbt_warehouse_inventory_on_hand_detail import FBTInventoryUpdateWebhookDataFbtWarehouseInventoryOnHandDetail # noqa: PLC0415
        d = dict(src_dict)
        fbt_warehouse_id = d.pop("fbt_warehouse_id", UNSET)

        _on_hand_detail = d.pop("on_hand_detail", UNSET)
        on_hand_detail: FBTInventoryUpdateWebhookDataFbtWarehouseInventoryOnHandDetail | Unset
        if isinstance(_on_hand_detail,  Unset):
            on_hand_detail = UNSET
        else:
            on_hand_detail = FBTInventoryUpdateWebhookDataFbtWarehouseInventoryOnHandDetail.from_dict(_on_hand_detail)




        fbt_inventory_update_webhook_data_fbt_warehouse_inventory = cls(
            fbt_warehouse_id=fbt_warehouse_id,
            on_hand_detail=on_hand_detail,
        )


        fbt_inventory_update_webhook_data_fbt_warehouse_inventory.additional_properties = d
        return fbt_inventory_update_webhook_data_fbt_warehouse_inventory

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
