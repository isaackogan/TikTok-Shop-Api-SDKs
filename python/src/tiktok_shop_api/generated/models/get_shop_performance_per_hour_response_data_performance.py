from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shop_performance_per_hour_response_data_performance_interval import GetShopPerformancePerHourResponseDataPerformanceInterval
  from ..models.get_shop_performance_per_hour_response_data_performance_overall import GetShopPerformancePerHourResponseDataPerformanceOverall





T = TypeVar("T", bound="GetShopPerformancePerHourResponseDataPerformance")



@_attrs_define
class GetShopPerformancePerHourResponseDataPerformance:
    """ 
        Attributes:
            intervals (list[GetShopPerformancePerHourResponseDataPerformanceInterval] | Unset): Hourly interval data for the
                requested date, including hour index, GMV, customers, items sold, and visitors.
            latest_available_timestamp (int | Unset): The latest time when the data is ready, as a UNIX timestamp.
            overall (GetShopPerformancePerHourResponseDataPerformanceOverall | Unset):
     """

    intervals: list[GetShopPerformancePerHourResponseDataPerformanceInterval] | Unset = UNSET
    latest_available_timestamp: int | Unset = UNSET
    overall: GetShopPerformancePerHourResponseDataPerformanceOverall | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_performance_per_hour_response_data_performance_interval import GetShopPerformancePerHourResponseDataPerformanceInterval # noqa: PLC0415
        from ..models.get_shop_performance_per_hour_response_data_performance_overall import GetShopPerformancePerHourResponseDataPerformanceOverall # noqa: PLC0415
        intervals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.intervals, Unset):
            intervals = []
            for intervals_item_data in self.intervals:
                intervals_item = intervals_item_data.to_dict()
                intervals.append(intervals_item)



        latest_available_timestamp = self.latest_available_timestamp

        overall: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overall, Unset):
            overall = self.overall.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if intervals is not UNSET:
            field_dict["intervals"] = intervals
        if latest_available_timestamp is not UNSET:
            field_dict["latest_available_timestamp"] = latest_available_timestamp
        if overall is not UNSET:
            field_dict["overall"] = overall

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_performance_per_hour_response_data_performance_interval import GetShopPerformancePerHourResponseDataPerformanceInterval # noqa: PLC0415
        from ..models.get_shop_performance_per_hour_response_data_performance_overall import GetShopPerformancePerHourResponseDataPerformanceOverall # noqa: PLC0415
        d = dict(src_dict)
        _intervals = d.pop("intervals", UNSET)
        intervals: list[GetShopPerformancePerHourResponseDataPerformanceInterval] | Unset = UNSET
        if _intervals is not UNSET:
            intervals = []
            for intervals_item_data in _intervals:
                intervals_item = GetShopPerformancePerHourResponseDataPerformanceInterval.from_dict(intervals_item_data)



                intervals.append(intervals_item)


        latest_available_timestamp = d.pop("latest_available_timestamp", UNSET)

        _overall = d.pop("overall", UNSET)
        overall: GetShopPerformancePerHourResponseDataPerformanceOverall | Unset
        if isinstance(_overall,  Unset):
            overall = UNSET
        else:
            overall = GetShopPerformancePerHourResponseDataPerformanceOverall.from_dict(_overall)




        get_shop_performance_per_hour_response_data_performance = cls(
            intervals=intervals,
            latest_available_timestamp=latest_available_timestamp,
            overall=overall,
        )


        get_shop_performance_per_hour_response_data_performance.additional_properties = d
        return get_shop_performance_per_hour_response_data_performance

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
