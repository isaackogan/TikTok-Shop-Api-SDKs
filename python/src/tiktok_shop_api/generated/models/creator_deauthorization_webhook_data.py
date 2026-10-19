from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatorDeauthorizationWebhookData")


@_attrs_define
class CreatorDeauthorizationWebhookData:
    """
    Attributes:
        cancel_time (str | Unset): The UNIX timestamp when this event happened.
    """

    cancel_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancel_time = self.cancel_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancel_time is not UNSET:
            field_dict["cancel_time"] = cancel_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cancel_time = d.pop("cancel_time", UNSET)

        creator_deauthorization_webhook_data = cls(
            cancel_time=cancel_time,
        )

        creator_deauthorization_webhook_data.additional_properties = d
        return creator_deauthorization_webhook_data

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
