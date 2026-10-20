from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.rma_status_update_webhook_data import RMAStatusUpdateWebhookData





T = TypeVar("T", bound="RMAStatusUpdateWebhook")



@_attrs_define
class RMAStatusUpdateWebhook:
    """ 
        Attributes:
            type_ (Literal[65]): The ID of the webhook type.
            shop_id (str | Unset): TikTok Shop identifier associated with the event.
            timestamp (int | Unset): The time when this webhook was triggered, represented by Unix timestamp.
            tts_notification_id (str | Unset): Unique notification identifier for deduplication and tracing.
            data (RMAStatusUpdateWebhookData | Unset):
     """

    type_: Literal[65]
    shop_id: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    tts_notification_id: str | Unset = UNSET
    data: RMAStatusUpdateWebhookData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rma_status_update_webhook_data import RMAStatusUpdateWebhookData # noqa: PLC0415
        type_ = self.type_

        shop_id = self.shop_id

        timestamp = self.timestamp

        tts_notification_id = self.tts_notification_id

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
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
        from ..models.rma_status_update_webhook_data import RMAStatusUpdateWebhookData # noqa: PLC0415
        d = dict(src_dict)
        type_ = cast(Literal[65] , d.pop("type"))
        if type_ != 65:
            raise ValueError(f"type must match const 65, got '{type_}'")

        shop_id = d.pop("shop_id", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        tts_notification_id = d.pop("tts_notification_id", UNSET)

        _data = d.pop("data", UNSET)
        data: RMAStatusUpdateWebhookData | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = RMAStatusUpdateWebhookData.from_dict(_data)




        rma_status_update_webhook = cls(
            type_=type_,
            shop_id=shop_id,
            timestamp=timestamp,
            tts_notification_id=tts_notification_id,
            data=data,
        )


        rma_status_update_webhook.additional_properties = d
        return rma_status_update_webhook

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
