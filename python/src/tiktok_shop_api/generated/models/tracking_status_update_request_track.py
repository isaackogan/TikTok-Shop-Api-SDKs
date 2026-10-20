from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracking_status_update_request_track_location import TrackingStatusUpdateRequestTrackLocation


T = TypeVar("T", bound="TrackingStatusUpdateRequestTrack")


@_attrs_define
class TrackingStatusUpdateRequestTrack:
    """
    Attributes:
        action_code (int): The standard trajectory node code must belong to the allowlist. See the below action code.
            The action code is limited, for the list of available enumerations, please refer to the documentation:
            https://partner.tiktokshop.com/docv2/page/1cjht3qx
        occur_time (int): Actual Trajectory Occurrence Time. Unix timestamp GMT (UTC+00:00). The unit is milliseconds.
        description (str): The original trajectory description of the caller.
        tracking_no (str): The waybill number used when placing an order. If there is no tracking code, fill in the
            invoice id instead. And it may change in split shipment, it may change in different track in this scene.
        failed_reason (str | Unset): Exception causes, details are listed below. See the below reason code. The reason
            code is limited, for the list of available enumerations, please refer to the documentation:
            https://partner.tiktokshop.com/docv2/page/1cjht3qx
        proof_url (str | Unset): Third-party tracking proof links or credentials.
        location (TrackingStatusUpdateRequestTrackLocation | Unset):
    """

    action_code: int
    occur_time: int
    description: str
    tracking_no: str
    failed_reason: str | Unset = UNSET
    proof_url: str | Unset = UNSET
    location: TrackingStatusUpdateRequestTrackLocation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_code = self.action_code

        occur_time = self.occur_time

        description = self.description

        tracking_no = self.tracking_no

        failed_reason = self.failed_reason

        proof_url = self.proof_url

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_code": action_code,
                "occur_time": occur_time,
                "description": description,
                "tracking_no": tracking_no,
            }
        )
        if failed_reason is not UNSET:
            field_dict["failed_reason"] = failed_reason
        if proof_url is not UNSET:
            field_dict["proof_url"] = proof_url
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tracking_status_update_request_track_location import (
            TrackingStatusUpdateRequestTrackLocation,  # noqa: PLC0415
        )

        d = dict(src_dict)
        action_code = d.pop("action_code")

        occur_time = d.pop("occur_time")

        description = d.pop("description")

        tracking_no = d.pop("tracking_no")

        failed_reason = d.pop("failed_reason", UNSET)

        proof_url = d.pop("proof_url", UNSET)

        _location = d.pop("location", UNSET)
        location: TrackingStatusUpdateRequestTrackLocation | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = TrackingStatusUpdateRequestTrackLocation.from_dict(_location)

        tracking_status_update_request_track = cls(
            action_code=action_code,
            occur_time=occur_time,
            description=description,
            tracking_no=tracking_no,
            failed_reason=failed_reason,
            proof_url=proof_url,
            location=location,
        )

        tracking_status_update_request_track.additional_properties = d
        return tracking_status_update_request_track

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
