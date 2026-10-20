from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.creator_deauthorization_webhook_data import CreatorDeauthorizationWebhookData


T = TypeVar("T", bound="CreatorDeauthorizationWebhook")


@_attrs_define
class CreatorDeauthorizationWebhook:
    """
    Attributes:
        type_ (Literal[20]): The ID of the webhook type.
        tts_notification_id (str | Unset): The ID of the notification.
        creator_open_id (str | Unset): The open_id of the creator. To get the value, see [Authorization
            overview](authorization-overview-202407).
        timestamp (int | Unset): The UNIX timestamp when this webhook was triggered.
        data (CreatorDeauthorizationWebhookData | Unset):
    """

    type_: Literal[20]
    tts_notification_id: str | Unset = UNSET
    creator_open_id: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    data: CreatorDeauthorizationWebhookData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        tts_notification_id = self.tts_notification_id

        creator_open_id = self.creator_open_id

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
        if creator_open_id is not UNSET:
            field_dict["creator_open_id"] = creator_open_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator_deauthorization_webhook_data import CreatorDeauthorizationWebhookData  # noqa: PLC0415

        d = dict(src_dict)
        type_ = cast(Literal[20], d.pop("type"))
        if type_ != 20:
            raise ValueError(f"type must match const 20, got '{type_}'")

        tts_notification_id = d.pop("tts_notification_id", UNSET)

        creator_open_id = d.pop("creator_open_id", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        _data = d.pop("data", UNSET)
        data: CreatorDeauthorizationWebhookData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CreatorDeauthorizationWebhookData.from_dict(_data)

        creator_deauthorization_webhook = cls(
            type_=type_,
            tts_notification_id=tts_notification_id,
            creator_open_id=creator_open_id,
            timestamp=timestamp,
            data=data,
        )

        creator_deauthorization_webhook.additional_properties = d
        return creator_deauthorization_webhook

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
