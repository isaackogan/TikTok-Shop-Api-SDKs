from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_live_room_traffic_performance_response_data_traffic_performance import (
        GetLiveRoomTrafficPerformanceResponseDataTrafficPerformance,
    )


T = TypeVar("T", bound="GetLiveRoomTrafficPerformanceResponseData")


@_attrs_define
class GetLiveRoomTrafficPerformanceResponseData:
    """
    Attributes:
        traffic_performances (list[GetLiveRoomTrafficPerformanceResponseDataTrafficPerformance] | Unset): Traffic
            performance grouped by primary traffic source, including any available sub-source breakdowns.
    """

    traffic_performances: list[GetLiveRoomTrafficPerformanceResponseDataTrafficPerformance] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        traffic_performances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.traffic_performances, Unset):
            traffic_performances = []
            for traffic_performances_item_data in self.traffic_performances:
                traffic_performances_item = traffic_performances_item_data.to_dict()
                traffic_performances.append(traffic_performances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if traffic_performances is not UNSET:
            field_dict["traffic_performances"] = traffic_performances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_live_room_traffic_performance_response_data_traffic_performance import (
            GetLiveRoomTrafficPerformanceResponseDataTrafficPerformance,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _traffic_performances = d.pop("traffic_performances", UNSET)
        traffic_performances: list[GetLiveRoomTrafficPerformanceResponseDataTrafficPerformance] | Unset = UNSET
        if _traffic_performances is not UNSET:
            traffic_performances = []
            for traffic_performances_item_data in _traffic_performances:
                traffic_performances_item = GetLiveRoomTrafficPerformanceResponseDataTrafficPerformance.from_dict(
                    traffic_performances_item_data
                )

                traffic_performances.append(traffic_performances_item)

        get_live_room_traffic_performance_response_data = cls(
            traffic_performances=traffic_performances,
        )

        get_live_room_traffic_performance_response_data.additional_properties = d
        return get_live_room_traffic_performance_response_data

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
