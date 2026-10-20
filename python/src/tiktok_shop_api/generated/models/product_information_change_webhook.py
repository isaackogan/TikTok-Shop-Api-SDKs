from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_information_change_webhook_data import ProductInformationChangeWebhookData


T = TypeVar("T", bound="ProductInformationChangeWebhook")


@_attrs_define
class ProductInformationChangeWebhook:
    """
    Attributes:
        type_ (Literal[15]): The ID of the webhook type.
        tts_notification_id (str | Unset): The ID of this webhook notification.
        shop_id (str | Unset): The shop ID.
        timestamp (int | Unset): The time when this webhook is triggered. Unix timestamp.
        data (ProductInformationChangeWebhookData | Unset):
    """

    type_: Literal[15]
    tts_notification_id: str | Unset = UNSET
    shop_id: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    data: ProductInformationChangeWebhookData | Unset = UNSET
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
        from ..models.product_information_change_webhook_data import (
            ProductInformationChangeWebhookData,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = cast(Literal[15], d.pop("type"))
        if type_ != 15:
            raise ValueError(f"type must match const 15, got '{type_}'")

        tts_notification_id = d.pop("tts_notification_id", UNSET)

        shop_id = d.pop("shop_id", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        _data = d.pop("data", UNSET)
        data: ProductInformationChangeWebhookData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ProductInformationChangeWebhookData.from_dict(_data)

        product_information_change_webhook = cls(
            type_=type_,
            tts_notification_id=tts_notification_id,
            shop_id=shop_id,
            timestamp=timestamp,
            data=data,
        )

        product_information_change_webhook.additional_properties = d
        return product_information_change_webhook

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
