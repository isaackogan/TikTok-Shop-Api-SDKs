from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EstimateArrivalTime")


@_attrs_define
class EstimateArrivalTime:
    """
    Attributes:
        start_timestamp (str): Start of the estimated arrival time window as a Unix timestamp in seconds. For example,
            `1774162800` corresponds to Sunday, 2026-03-22 at 00:00 PDT (`2026-03-22T07:00:00Z`). Use the exact
            `start_timestamp` returned in `available_time_window_list` by the `ListAvailableInboundMethod` API.
        end_timestamp (str): End of the estimated arrival time window as a Unix timestamp in seconds. For example,
            `1774767600` corresponds to Sunday, 2026-03-29 at 00:00 PDT (`2026-03-29T07:00:00Z`). Use the exact
            `end_timestamp` returned in `available_time_window_list` by the `ListAvailableInboundMethod` API.
    """

    start_timestamp: str
    end_timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_timestamp = self.start_timestamp

        end_timestamp = self.end_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_timestamp": start_timestamp,
                "end_timestamp": end_timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_timestamp = d.pop("start_timestamp")

        end_timestamp = d.pop("end_timestamp")

        estimate_arrival_time = cls(
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
        )

        estimate_arrival_time.additional_properties = d
        return estimate_arrival_time

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
