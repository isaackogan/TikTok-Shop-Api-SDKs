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
  from ..models.get_acc_audience_overview_response_data_trend_interval import GetACCAudienceOverviewResponseDataTrendInterval





T = TypeVar("T", bound="GetACCAudienceOverviewResponseDataTrend")



@_attrs_define
class GetACCAudienceOverviewResponseDataTrend:
    """ 
        Attributes:
            actual_end_date (datetime.date | Unset): Latest UTC date included in `intervals`, in `YYYY-MM-DD` format.
                Unavailable when `intervals` is empty.
            actual_start_date (datetime.date | Unset): Earliest UTC date included in `intervals`, in `YYYY-MM-DD` format.
                Unavailable when `intervals` is empty.
            interval_count (int | Unset): Number of data points in `intervals` (0 to 30).
            intervals (list[GetACCAudienceOverviewResponseDataTrendInterval] | Unset): Daily data points for this metric, in
                ascending UTC date order. Counts and benchmarks are available only when greater than 1,000.
            metric (str | Unset): Audience metric represented by this series. Possible values: `ACC`, `AWARENESS`,
                `CONSIDERATION`, `CONVERSION`, `NEW_CONVERSION`, and `REPEAT_CONVERSION`. The six metric meanings match the
                corresponding fields in key_metrics.
     """

    actual_end_date: datetime.date | Unset = UNSET
    actual_start_date: datetime.date | Unset = UNSET
    interval_count: int | Unset = UNSET
    intervals: list[GetACCAudienceOverviewResponseDataTrendInterval] | Unset = UNSET
    metric: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_audience_overview_response_data_trend_interval import GetACCAudienceOverviewResponseDataTrendInterval # noqa: PLC0415
        actual_end_date: str | Unset = UNSET
        if not isinstance(self.actual_end_date, Unset):
            actual_end_date = self.actual_end_date.isoformat()

        actual_start_date: str | Unset = UNSET
        if not isinstance(self.actual_start_date, Unset):
            actual_start_date = self.actual_start_date.isoformat()

        interval_count = self.interval_count

        intervals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.intervals, Unset):
            intervals = []
            for intervals_item_data in self.intervals:
                intervals_item = intervals_item_data.to_dict()
                intervals.append(intervals_item)



        metric = self.metric


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if actual_end_date is not UNSET:
            field_dict["actual_end_date"] = actual_end_date
        if actual_start_date is not UNSET:
            field_dict["actual_start_date"] = actual_start_date
        if interval_count is not UNSET:
            field_dict["interval_count"] = interval_count
        if intervals is not UNSET:
            field_dict["intervals"] = intervals
        if metric is not UNSET:
            field_dict["metric"] = metric

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_acc_audience_overview_response_data_trend_interval import GetACCAudienceOverviewResponseDataTrendInterval # noqa: PLC0415
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




        interval_count = d.pop("interval_count", UNSET)

        _intervals = d.pop("intervals", UNSET)
        intervals: list[GetACCAudienceOverviewResponseDataTrendInterval] | Unset = UNSET
        if _intervals is not UNSET:
            intervals = []
            for intervals_item_data in _intervals:
                intervals_item = GetACCAudienceOverviewResponseDataTrendInterval.from_dict(intervals_item_data)



                intervals.append(intervals_item)


        metric = d.pop("metric", UNSET)

        get_acc_audience_overview_response_data_trend = cls(
            actual_end_date=actual_end_date,
            actual_start_date=actual_start_date,
            interval_count=interval_count,
            intervals=intervals,
            metric=metric,
        )


        get_acc_audience_overview_response_data_trend.additional_properties = d
        return get_acc_audience_overview_response_data_trend

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
