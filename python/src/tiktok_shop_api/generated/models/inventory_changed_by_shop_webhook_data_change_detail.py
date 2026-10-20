from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InventoryChangedByShopWebhookDataChangeDetail")


@_attrs_define
class InventoryChangedByShopWebhookDataChangeDetail:
    """
    Attributes:
        idempotency_key (str): An identifier for an individual change; use it to deduplicate change details.
        trigger_source (str): The cause of the change. See the trigger sources in Section 1.
        occurred_at (datetime.datetime): The UTC time of the individual change.
        total_quantity_delta (int): The change in `total_quantity`.
        available_quantity_delta (int): The change in `total_available_quantity`.
        committed_quantity_delta (int): The change in `total_committed_quantity`.
        in_shop_quantity_delta (int): The change in `in_shop_quantity`.
        campaign_locked_quantity_delta (int): The change in `campaign_locked_quantity`.
        creator_locked_quantity_delta (int): The change in `creator_locked_quantity`.
    """

    idempotency_key: str
    trigger_source: str
    occurred_at: datetime.datetime
    total_quantity_delta: int
    available_quantity_delta: int
    committed_quantity_delta: int
    in_shop_quantity_delta: int
    campaign_locked_quantity_delta: int
    creator_locked_quantity_delta: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idempotency_key = self.idempotency_key

        trigger_source = self.trigger_source

        occurred_at = self.occurred_at.isoformat()

        total_quantity_delta = self.total_quantity_delta

        available_quantity_delta = self.available_quantity_delta

        committed_quantity_delta = self.committed_quantity_delta

        in_shop_quantity_delta = self.in_shop_quantity_delta

        campaign_locked_quantity_delta = self.campaign_locked_quantity_delta

        creator_locked_quantity_delta = self.creator_locked_quantity_delta

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idempotency_key": idempotency_key,
                "trigger_source": trigger_source,
                "occurred_at": occurred_at,
                "total_quantity_delta": total_quantity_delta,
                "available_quantity_delta": available_quantity_delta,
                "committed_quantity_delta": committed_quantity_delta,
                "in_shop_quantity_delta": in_shop_quantity_delta,
                "campaign_locked_quantity_delta": campaign_locked_quantity_delta,
                "creator_locked_quantity_delta": creator_locked_quantity_delta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idempotency_key = d.pop("idempotency_key")

        trigger_source = d.pop("trigger_source")

        occurred_at = datetime.datetime.fromisoformat(d.pop("occurred_at"))

        total_quantity_delta = d.pop("total_quantity_delta")

        available_quantity_delta = d.pop("available_quantity_delta")

        committed_quantity_delta = d.pop("committed_quantity_delta")

        in_shop_quantity_delta = d.pop("in_shop_quantity_delta")

        campaign_locked_quantity_delta = d.pop("campaign_locked_quantity_delta")

        creator_locked_quantity_delta = d.pop("creator_locked_quantity_delta")

        inventory_changed_by_shop_webhook_data_change_detail = cls(
            idempotency_key=idempotency_key,
            trigger_source=trigger_source,
            occurred_at=occurred_at,
            total_quantity_delta=total_quantity_delta,
            available_quantity_delta=available_quantity_delta,
            committed_quantity_delta=committed_quantity_delta,
            in_shop_quantity_delta=in_shop_quantity_delta,
            campaign_locked_quantity_delta=campaign_locked_quantity_delta,
            creator_locked_quantity_delta=creator_locked_quantity_delta,
        )

        inventory_changed_by_shop_webhook_data_change_detail.additional_properties = d
        return inventory_changed_by_shop_webhook_data_change_detail

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
