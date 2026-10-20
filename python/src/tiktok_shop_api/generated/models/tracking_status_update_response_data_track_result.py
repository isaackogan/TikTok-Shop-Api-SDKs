from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackingStatusUpdateResponseDataTrackResult")


@_attrs_define
class TrackingStatusUpdateResponseDataTrackResult:
    """
    Attributes:
        action_code (int | Unset): The standard trajectory node code must belong to the allowlist. See the below action
            code.
        occur_time (int | Unset): Actual Trajectory Occurrence Time. Unix timestamp GMT (UTC+00:00). The unit is
            milliseconds.
        description (str | Unset): The original trajectory description of the caller.
        code (int | Unset): The success or failure status of the trace corresponding to this action code, see the below
            error code
        message (str | Unset): The success or failure messages returned in the trace corresponding to this action code.
            Reasons of failure will be described in the message.
        tracking_no (str | Unset): The waybill number used when placing an order. If there is no tracking code, fill in
            the invoice id instead. And it may change in split shipment, it may change in different track in this scene.
    """

    action_code: int | Unset = UNSET
    occur_time: int | Unset = UNSET
    description: str | Unset = UNSET
    code: int | Unset = UNSET
    message: str | Unset = UNSET
    tracking_no: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_code = self.action_code

        occur_time = self.occur_time

        description = self.description

        code = self.code

        message = self.message

        tracking_no = self.tracking_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_code is not UNSET:
            field_dict["action_code"] = action_code
        if occur_time is not UNSET:
            field_dict["occur_time"] = occur_time
        if description is not UNSET:
            field_dict["description"] = description
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if tracking_no is not UNSET:
            field_dict["tracking_no"] = tracking_no

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_code = d.pop("action_code", UNSET)

        occur_time = d.pop("occur_time", UNSET)

        description = d.pop("description", UNSET)

        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        tracking_no = d.pop("tracking_no", UNSET)

        tracking_status_update_response_data_track_result = cls(
            action_code=action_code,
            occur_time=occur_time,
            description=description,
            code=code,
            message=message,
            tracking_no=tracking_no,
        )

        tracking_status_update_response_data_track_result.additional_properties = d
        return tracking_status_update_response_data_track_result

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
