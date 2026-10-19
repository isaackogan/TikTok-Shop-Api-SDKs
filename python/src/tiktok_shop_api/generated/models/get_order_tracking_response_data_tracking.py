from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrderTrackingResponseDataTracking")


@_attrs_define
class GetOrderTrackingResponseDataTracking:
    """
    Attributes:
        description (str | Unset): Tracking status description.
        update_time_millis (int | Unset): Tracking status update time. Unix timestamp in milliseconds.
        action_code (int | Unset): Code that identifies the tracking event type. Use `description` for the human-
            readable event message.
    """

    description: str | Unset = UNSET
    update_time_millis: int | Unset = UNSET
    action_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        update_time_millis = self.update_time_millis

        action_code = self.action_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if update_time_millis is not UNSET:
            field_dict["update_time_millis"] = update_time_millis
        if action_code is not UNSET:
            field_dict["action_code"] = action_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        update_time_millis = d.pop("update_time_millis", UNSET)

        action_code = d.pop("action_code", UNSET)

        get_order_tracking_response_data_tracking = cls(
            description=description,
            update_time_millis=update_time_millis,
            action_code=action_code,
        )

        get_order_tracking_response_data_tracking.additional_properties = d
        return get_order_tracking_response_data_tracking

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
