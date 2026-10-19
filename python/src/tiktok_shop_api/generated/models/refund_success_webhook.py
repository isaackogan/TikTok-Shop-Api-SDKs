from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.refund_success_webhook_data import RefundSuccessWebhookData


T = TypeVar("T", bound="RefundSuccessWebhook")


@_attrs_define
class RefundSuccessWebhook:
    """
    Attributes:
        type_ (Literal[67]): The ID of the webhook type.
        shop_id (str | Unset): TikTok Shop identifier associated with the event.
        timestamp (int | Unset): The time when this webhook was triggered, represented by Unix timestamp.
        tts_notification_id (str | Unset): Unique notification identifier for deduplication and tracing.
        data (RefundSuccessWebhookData | Unset):
    """

    type_: Literal[67]
    shop_id: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    tts_notification_id: str | Unset = UNSET
    data: RefundSuccessWebhookData | Unset = UNSET
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
        from ..models.refund_success_webhook_data import RefundSuccessWebhookData  # noqa: PLC0415

        d = dict(src_dict)
        type_ = cast(Literal[67], d.pop("type"))
        if type_ != 67:
            raise ValueError(f"type must match const 67, got '{type_}'")

        shop_id = d.pop("shop_id", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        tts_notification_id = d.pop("tts_notification_id", UNSET)

        _data = d.pop("data", UNSET)
        data: RefundSuccessWebhookData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RefundSuccessWebhookData.from_dict(_data)

        refund_success_webhook = cls(
            type_=type_,
            shop_id=shop_id,
            timestamp=timestamp,
            tts_notification_id=tts_notification_id,
            data=data,
        )

        refund_success_webhook.additional_properties = d
        return refund_success_webhook

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
