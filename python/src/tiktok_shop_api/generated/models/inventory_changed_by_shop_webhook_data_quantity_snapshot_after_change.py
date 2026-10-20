from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="InventoryChangedByShopWebhookDataQuantitySnapshotAfterChange")



@_attrs_define
class InventoryChangedByShopWebhookDataQuantitySnapshotAfterChange:
    """ 
        Attributes:
            total_quantity (int): Total inventory: `total_available_quantity + total_committed_quantity`.
            total_available_quantity (int): Available inventory, including quantities reserved for campaigns and creator
                collaborations.
            total_committed_quantity (int): Inventory committed to orders that have not yet shipped.
            in_shop_quantity (int): Available shop inventory: `total_available_quantity - campaign_locked_quantity -
                creator_locked_quantity`.
            campaign_locked_quantity (int): Inventory reserved for marketing campaigns.
            creator_locked_quantity (int): Inventory reserved for creator collaborations.
     """

    total_quantity: int
    total_available_quantity: int
    total_committed_quantity: int
    in_shop_quantity: int
    campaign_locked_quantity: int
    creator_locked_quantity: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total_quantity = self.total_quantity

        total_available_quantity = self.total_available_quantity

        total_committed_quantity = self.total_committed_quantity

        in_shop_quantity = self.in_shop_quantity

        campaign_locked_quantity = self.campaign_locked_quantity

        creator_locked_quantity = self.creator_locked_quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "total_quantity": total_quantity,
            "total_available_quantity": total_available_quantity,
            "total_committed_quantity": total_committed_quantity,
            "in_shop_quantity": in_shop_quantity,
            "campaign_locked_quantity": campaign_locked_quantity,
            "creator_locked_quantity": creator_locked_quantity,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_quantity = d.pop("total_quantity")

        total_available_quantity = d.pop("total_available_quantity")

        total_committed_quantity = d.pop("total_committed_quantity")

        in_shop_quantity = d.pop("in_shop_quantity")

        campaign_locked_quantity = d.pop("campaign_locked_quantity")

        creator_locked_quantity = d.pop("creator_locked_quantity")

        inventory_changed_by_shop_webhook_data_quantity_snapshot_after_change = cls(
            total_quantity=total_quantity,
            total_available_quantity=total_available_quantity,
            total_committed_quantity=total_committed_quantity,
            in_shop_quantity=in_shop_quantity,
            campaign_locked_quantity=campaign_locked_quantity,
            creator_locked_quantity=creator_locked_quantity,
        )


        inventory_changed_by_shop_webhook_data_quantity_snapshot_after_change.additional_properties = d
        return inventory_changed_by_shop_webhook_data_quantity_snapshot_after_change

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
