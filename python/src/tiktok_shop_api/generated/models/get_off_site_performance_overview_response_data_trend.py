from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_off_site_performance_overview_response_data_trend_interval import GetOffSitePerformanceOverviewResponseDataTrendInterval





T = TypeVar("T", bound="GetOffSitePerformanceOverviewResponseDataTrend")



@_attrs_define
class GetOffSitePerformanceOverviewResponseDataTrend:
    """ 
        Attributes:
            actual_end_date (datetime.date | Unset): End date of the last returned trend interval, exclusive, formatted as
                YYYY-MM-DD.
            actual_start_date (datetime.date | Unset): Start date of the first returned trend interval, inclusive, formatted
                as YYYY-MM-DD.
            granularity (str | Unset): Time granularity of each trend interval. The value is 1W, representing one reporting
                week.
            interval_count (int | Unset): Number of weekly intervals returned in intervals, up to eight.
            intervals (list[GetOffSitePerformanceOverviewResponseDataTrendInterval] | Unset): Weekly intervals ordered by
                start_date from earliest to latest. Up to eight intervals are returned.
     """

    actual_end_date: datetime.date | Unset = UNSET
    actual_start_date: datetime.date | Unset = UNSET
    granularity: str | Unset = UNSET
    interval_count: int | Unset = UNSET
    intervals: list[GetOffSitePerformanceOverviewResponseDataTrendInterval] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_off_site_performance_overview_response_data_trend_interval import GetOffSitePerformanceOverviewResponseDataTrendInterval # noqa: PLC0415
        actual_end_date: str | Unset = UNSET
        if not isinstance(self.actual_end_date, Unset):
            actual_end_date = self.actual_end_date.isoformat()

        actual_start_date: str | Unset = UNSET
        if not isinstance(self.actual_start_date, Unset):
            actual_start_date = self.actual_start_date.isoformat()

        granularity = self.granularity

        interval_count = self.interval_count

        intervals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.intervals, Unset):
            intervals = []
            for intervals_item_data in self.intervals:
                intervals_item = intervals_item_data.to_dict()
                intervals.append(intervals_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if actual_end_date is not UNSET:
            field_dict["actual_end_date"] = actual_end_date
        if actual_start_date is not UNSET:
            field_dict["actual_start_date"] = actual_start_date
        if granularity is not UNSET:
            field_dict["granularity"] = granularity
        if interval_count is not UNSET:
            field_dict["interval_count"] = interval_count
        if intervals is not UNSET:
            field_dict["intervals"] = intervals

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_off_site_performance_overview_response_data_trend_interval import GetOffSitePerformanceOverviewResponseDataTrendInterval # noqa: PLC0415
        d = dict(src_dict)
        _actual_end_date = d.pop("actual_end_date", UNSET)
        actual_end_date: datetime.date | Unset
        if isinstance(_actual_end_date,  Unset):
            actual_end_date = UNSET
        else:
            actual_end_date = datetime.date.fromisoformat(_actual_end_date)




        _actual_start_date = d.pop("actual_start_date", UNSET)
        actual_start_date: datetime.date | Unset
        if isinstance(_actual_start_date,  Unset):
            actual_start_date = UNSET
        else:
            actual_start_date = datetime.date.fromisoformat(_actual_start_date)




        granularity = d.pop("granularity", UNSET)

        interval_count = d.pop("interval_count", UNSET)

        _intervals = d.pop("intervals", UNSET)
        intervals: list[GetOffSitePerformanceOverviewResponseDataTrendInterval] | Unset = UNSET
        if _intervals is not UNSET:
            intervals = []
            for intervals_item_data in _intervals:
                intervals_item = GetOffSitePerformanceOverviewResponseDataTrendInterval.from_dict(intervals_item_data)



                intervals.append(intervals_item)


        get_off_site_performance_overview_response_data_trend = cls(
            actual_end_date=actual_end_date,
            actual_start_date=actual_start_date,
            granularity=granularity,
            interval_count=interval_count,
            intervals=intervals,
        )


        get_off_site_performance_overview_response_data_trend.additional_properties = d
        return get_off_site_performance_overview_response_data_trend

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
