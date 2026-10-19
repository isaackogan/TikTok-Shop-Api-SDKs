from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepublishActivityRequest")


@_attrs_define
class RepublishActivityRequest:
    """
    Attributes:
        end_time (int | Unset): Activity end time as a Unix timestamp in seconds. It must be later than begin_time, and
            the effective period must be at least 10 minutes. The maximum period depends on the activity type and shop
            region; for FLASHSALE activities, it must not exceed 3 days.
        begin_time (int | Unset): Activity start time as a Unix timestamp in seconds. The value must be later than the
            current time.
    """

    end_time: int | Unset = UNSET
    begin_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_time = self.end_time

        begin_time = self.begin_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if begin_time is not UNSET:
            field_dict["begin_time"] = begin_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_time = d.pop("end_time", UNSET)

        begin_time = d.pop("begin_time", UNSET)

        republish_activity_request = cls(
            end_time=end_time,
            begin_time=begin_time,
        )

        republish_activity_request.additional_properties = d
        return republish_activity_request

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
