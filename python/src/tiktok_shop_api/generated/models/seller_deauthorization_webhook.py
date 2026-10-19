from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.seller_deauthorization_webhook_data import SellerDeauthorizationWebhookData


T = TypeVar("T", bound="SellerDeauthorizationWebhook")


@_attrs_define
class SellerDeauthorizationWebhook:
    """
    Attributes:
        type_ (Literal[6]): The ID of the webhook type.
        shop_id (str | Unset): The identification of the shop
        timestamp (int | Unset): The time when the notification is pushed, represented as a Unix timestamp (seconds).
        tts_notification_id (str | Unset): The ID of the notification.
        data (SellerDeauthorizationWebhookData | Unset):
    """

    type_: Literal[6]
    shop_id: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    tts_notification_id: str | Unset = UNSET
    data: SellerDeauthorizationWebhookData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        shop_id = self.shop_id

        timestamp = self.timestamp

        tts_notification_id = self.tts_notification_id

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if tts_notification_id is not UNSET:
            field_dict["tts_notification_id"] = tts_notification_id
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.seller_deauthorization_webhook_data import SellerDeauthorizationWebhookData  # noqa: PLC0415

        d = dict(src_dict)
        type_ = cast(Literal[6], d.pop("type"))
        if type_ != 6:
            raise ValueError(f"type must match const 6, got '{type_}'")

        shop_id = d.pop("shop_id", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        tts_notification_id = d.pop("tts_notification_id", UNSET)

        _data = d.pop("data", UNSET)
        data: SellerDeauthorizationWebhookData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SellerDeauthorizationWebhookData.from_dict(_data)

        seller_deauthorization_webhook = cls(
            type_=type_,
            shop_id=shop_id,
            timestamp=timestamp,
            tts_notification_id=tts_notification_id,
            data=data,
        )

        seller_deauthorization_webhook.additional_properties = d
        return seller_deauthorization_webhook

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
