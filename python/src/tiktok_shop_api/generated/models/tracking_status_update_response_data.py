from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tracking_status_update_response_data_track_result import TrackingStatusUpdateResponseDataTrackResult


T = TypeVar("T", bound="TrackingStatusUpdateResponseData")


@_attrs_define
class TrackingStatusUpdateResponseData:
    """
    Attributes:
        track_results (list[TrackingStatusUpdateResponseDataTrackResult] | Unset): The trajectory node array, where the
            field in each element of the array indicates which trajectory it is. The `code` and `message` fields describe
            whether the trajectory has been received; if not, they represent the corresponding error code and error
            description.
    """

    track_results: list[TrackingStatusUpdateResponseDataTrackResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        track_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.track_results, Unset):
            track_results = []
            for track_results_item_data in self.track_results:
                track_results_item = track_results_item_data.to_dict()
                track_results.append(track_results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if track_results is not UNSET:
            field_dict["track_results"] = track_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tracking_status_update_response_data_track_result import (
            TrackingStatusUpdateResponseDataTrackResult,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _track_results = d.pop("track_results", UNSET)
        track_results: list[TrackingStatusUpdateResponseDataTrackResult] | Unset = UNSET
        if _track_results is not UNSET:
            track_results = []
            for track_results_item_data in _track_results:
                track_results_item = TrackingStatusUpdateResponseDataTrackResult.from_dict(track_results_item_data)

                track_results.append(track_results_item)

        tracking_status_update_response_data = cls(
            track_results=track_results,
        )

        tracking_status_update_response_data.additional_properties = d
        return tracking_status_update_response_data

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
