from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.inventory_changed_by_shop_webhook_data import InventoryChangedByShopWebhookData


T = TypeVar("T", bound="InventoryChangedByShopWebhook")


@_attrs_define
class InventoryChangedByShopWebhook:
    """
    Attributes:
        type_ (Literal[71]): The ID of the webhook type.
        tts_notification_id (str): The notification ID.
        shop_id (str): The shop ID.
        timestamp (int): The time when the webhook is triggered, expressed as a Unix timestamp.
        data (InventoryChangedByShopWebhookData):
    """

    type_: Literal[71]
    tts_notification_id: str
    shop_id: str
    timestamp: int
    data: InventoryChangedByShopWebhookData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        tts_notification_id = self.tts_notification_id

        shop_id = self.shop_id

        timestamp = self.timestamp

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "tts_notification_id": tts_notification_id,
                "shop_id": shop_id,
                "timestamp": timestamp,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_changed_by_shop_webhook_data import InventoryChangedByShopWebhookData  # noqa: PLC0415

        d = dict(src_dict)
        type_ = cast(Literal[71], d.pop("type"))
        if type_ != 71:
            raise ValueError(f"type must match const 71, got '{type_}'")

        tts_notification_id = d.pop("tts_notification_id")

        shop_id = d.pop("shop_id")

        timestamp = d.pop("timestamp")

        data = InventoryChangedByShopWebhookData.from_dict(d.pop("data"))

        inventory_changed_by_shop_webhook = cls(
            type_=type_,
            tts_notification_id=tts_notification_id,
            shop_id=shop_id,
            timestamp=timestamp,
            data=data,
        )

        inventory_changed_by_shop_webhook.additional_properties = d
        return inventory_changed_by_shop_webhook

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
