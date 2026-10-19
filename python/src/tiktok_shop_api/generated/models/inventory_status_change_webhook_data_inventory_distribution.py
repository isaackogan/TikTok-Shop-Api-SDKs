from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InventoryStatusChangeWebhookDataInventoryDistribution")


@_attrs_define
class InventoryStatusChangeWebhookDataInventoryDistribution:
    """
    Attributes:
        total_quantity (int | Unset): The total quantity of the stock physically in the warehouses.
            `total_quantity`=`available_quantity` + `creator_reserved_quantity` + `campaign_reserved_quantity` +
            `committed_quantity`.
        available_quantity (int | Unset): The total number of SKUs available for ordering in the warehouses.
        creator_reserved_quantity (int | Unset): The total number of SKUs reserved for creators in the warehouses.
        campaign_reserved_quantity (int | Unset): The total number of SKUs reserved for campaigns in the warehouses.
        committed_quantity (int | Unset): The total number of SKUs reserved by existing customer orders in the
            warehouses.
    """

    total_quantity: int | Unset = UNSET
    available_quantity: int | Unset = UNSET
    creator_reserved_quantity: int | Unset = UNSET
    campaign_reserved_quantity: int | Unset = UNSET
    committed_quantity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_quantity = self.total_quantity

        available_quantity = self.available_quantity

        creator_reserved_quantity = self.creator_reserved_quantity

        campaign_reserved_quantity = self.campaign_reserved_quantity

        committed_quantity = self.committed_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_quantity is not UNSET:
            field_dict["total_quantity"] = total_quantity
        if available_quantity is not UNSET:
            field_dict["available_quantity"] = available_quantity
        if creator_reserved_quantity is not UNSET:
            field_dict["creator_reserved_quantity"] = creator_reserved_quantity
        if campaign_reserved_quantity is not UNSET:
            field_dict["campaign_reserved_quantity"] = campaign_reserved_quantity
        if committed_quantity is not UNSET:
            field_dict["committed_quantity"] = committed_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_quantity = d.pop("total_quantity", UNSET)

        available_quantity = d.pop("available_quantity", UNSET)

        creator_reserved_quantity = d.pop("creator_reserved_quantity", UNSET)

        campaign_reserved_quantity = d.pop("campaign_reserved_quantity", UNSET)

        committed_quantity = d.pop("committed_quantity", UNSET)

        inventory_status_change_webhook_data_inventory_distribution = cls(
            total_quantity=total_quantity,
            available_quantity=available_quantity,
            creator_reserved_quantity=creator_reserved_quantity,
            campaign_reserved_quantity=campaign_reserved_quantity,
            committed_quantity=committed_quantity,
        )

        inventory_status_change_webhook_data_inventory_distribution.additional_properties = d
        return inventory_status_change_webhook_data_inventory_distribution

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
