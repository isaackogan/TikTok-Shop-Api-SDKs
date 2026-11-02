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
  from ..models.get_off_site_performance_overview_response_data_trend_interval_metric import GetOffSitePerformanceOverviewResponseDataTrendIntervalMetric





T = TypeVar("T", bound="GetOffSitePerformanceOverviewResponseDataTrendInterval")



@_attrs_define
class GetOffSitePerformanceOverviewResponseDataTrendInterval:
    """ 
        Attributes:
            end_date (datetime.date | Unset): End date of this weekly interval, exclusive, formatted as YYYY-MM-DD.
            metrics (GetOffSitePerformanceOverviewResponseDataTrendIntervalMetric | Unset):
            start_date (datetime.date | Unset): First date of this weekly interval, inclusive, formatted as YYYY-MM-DD.
     """

    end_date: datetime.date | Unset = UNSET
    metrics: GetOffSitePerformanceOverviewResponseDataTrendIntervalMetric | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_off_site_performance_overview_response_data_trend_interval_metric import GetOffSitePerformanceOverviewResponseDataTrendIntervalMetric # noqa: PLC0415
        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_off_site_performance_overview_response_data_trend_interval_metric import GetOffSitePerformanceOverviewResponseDataTrendIntervalMetric # noqa: PLC0415
        d = dict(src_dict)
        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        _metrics = d.pop("metrics", UNSET)
        metrics: GetOffSitePerformanceOverviewResponseDataTrendIntervalMetric | Unset
        if isinstance(_metrics,  Unset):
            metrics = UNSET
        else:
            metrics = GetOffSitePerformanceOverviewResponseDataTrendIntervalMetric.from_dict(_metrics)




        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        get_off_site_performance_overview_response_data_trend_interval = cls(
            end_date=end_date,
            metrics=metrics,
            start_date=start_date,
        )


        get_off_site_performance_overview_response_data_trend_interval.additional_properties = d
        return get_off_site_performance_overview_response_data_trend_interval

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
