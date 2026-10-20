from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.appeal_completed_webhook_data import AppealCompletedWebhookData





T = TypeVar("T", bound="AppealCompletedWebhook")



@_attrs_define
class AppealCompletedWebhook:
    """ 
        Attributes:
            shop_id (str):
            type_ (Literal[66]): The ID of the webhook type.
            tts_notification_id (str):
            timestamp (int):
            data (AppealCompletedWebhookData):
     """

    shop_id: str
    type_: Literal[66]
    tts_notification_id: str
    timestamp: int
    data: AppealCompletedWebhookData
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.appeal_completed_webhook_data import AppealCompletedWebhookData # noqa: PLC0415
        shop_id = self.shop_id

        type_ = self.type_

        tts_notification_id = self.tts_notification_id

        timestamp = self.timestamp

        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "shop_id": shop_id,
            "type": type_,
            "tts_notification_id": tts_notification_id,
            "timestamp": timestamp,
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appeal_completed_webhook_data import AppealCompletedWebhookData # noqa: PLC0415
        d = dict(src_dict)
        shop_id = d.pop("shop_id")

        type_ = cast(Literal[66] , d.pop("type"))
        if type_ != 66:
            raise ValueError(f"type must match const 66, got '{type_}'")

        tts_notification_id = d.pop("tts_notification_id")

        timestamp = d.pop("timestamp")

        data = AppealCompletedWebhookData.from_dict(d.pop("data"))




        appeal_completed_webhook = cls(
            shop_id=shop_id,
            type_=type_,
            tts_notification_id=tts_notification_id,
            timestamp=timestamp,
            data=data,
        )


        appeal_completed_webhook.additional_properties = d
        return appeal_completed_webhook

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
