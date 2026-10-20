from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokopediaMirrorStatusChangeWebhookData")


@_attrs_define
class TokopediaMirrorStatusChangeWebhookData:
    """
    Attributes:
        tts_shop_id (str | Unset): The shop ID in TikTok Shop.
        update_time (int | Unset): The time when the change occurred. Unix timestamp.
        mirror_status (str | Unset): The shop mirroring status:
             - MIRRORED
             - ROLLED_BACK
             - CANCELED
    """

    tts_shop_id: str | Unset = UNSET
    update_time: int | Unset = UNSET
    mirror_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tts_shop_id = self.tts_shop_id

        update_time = self.update_time

        mirror_status = self.mirror_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tts_shop_id is not UNSET:
            field_dict["tts_shop_id"] = tts_shop_id
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if mirror_status is not UNSET:
            field_dict["mirror_status"] = mirror_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tts_shop_id = d.pop("tts_shop_id", UNSET)

        update_time = d.pop("update_time", UNSET)

        mirror_status = d.pop("mirror_status", UNSET)

        tokopedia_mirror_status_change_webhook_data = cls(
            tts_shop_id=tts_shop_id,
            update_time=update_time,
            mirror_status=mirror_status,
        )

        tokopedia_mirror_status_change_webhook_data.additional_properties = d
        return tokopedia_mirror_status_change_webhook_data

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
