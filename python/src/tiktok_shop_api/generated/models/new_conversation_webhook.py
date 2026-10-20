from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_conversation_webhook_data import NewConversationWebhookData


T = TypeVar("T", bound="NewConversationWebhook")


@_attrs_define
class NewConversationWebhook:
    """
    Attributes:
        type_ (Literal[13]): The ID of the webhook type.
        tts_notification_id (str | Unset): The ID of the notification.
        shop_id (str | Unset): The shop ID.
        timestamp (int | Unset): The Unix timestamp when the webhook was triggered.
        data (NewConversationWebhookData | Unset):
    """

    type_: Literal[13]
    tts_notification_id: str | Unset = UNSET
    shop_id: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    data: NewConversationWebhookData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        tts_notification_id = self.tts_notification_id

        shop_id = self.shop_id

        timestamp = self.timestamp

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
        if tts_notification_id is not UNSET:
            field_dict["tts_notification_id"] = tts_notification_id
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.new_conversation_webhook_data import NewConversationWebhookData  # noqa: PLC0415

        d = dict(src_dict)
        type_ = cast(Literal[13], d.pop("type"))
        if type_ != 13:
            raise ValueError(f"type must match const 13, got '{type_}'")

        tts_notification_id = d.pop("tts_notification_id", UNSET)

        shop_id = d.pop("shop_id", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        _data = d.pop("data", UNSET)
        data: NewConversationWebhookData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = NewConversationWebhookData.from_dict(_data)

        new_conversation_webhook = cls(
            type_=type_,
            tts_notification_id=tts_notification_id,
            shop_id=shop_id,
            timestamp=timestamp,
            data=data,
        )

        new_conversation_webhook.additional_properties = d
        return new_conversation_webhook

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
