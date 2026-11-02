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
  from ..models.get_off_site_performance_overview_response_data_key_metric import GetOffSitePerformanceOverviewResponseDataKeyMetric
  from ..models.get_off_site_performance_overview_response_data_trend import GetOffSitePerformanceOverviewResponseDataTrend





T = TypeVar("T", bound="GetOffSitePerformanceOverviewResponseData")



@_attrs_define
class GetOffSitePerformanceOverviewResponseData:
    """ 
        Attributes:
            end_date (datetime.date | Unset): Last date of the selected report week, inclusive, formatted as YYYY-MM-DD.
                This is a Saturday.
            key_metrics (GetOffSitePerformanceOverviewResponseDataKeyMetric | None | Unset): Performance metrics for the
                selected report week. Effect rates are decimal ratios, where 1.0000 means 100%, and can exceed 1. An unavailable
                rate may be null and must not be interpreted as zero; the response does not identify the cause of
                unavailability.
            latest_available_date (datetime.date | Unset): Latest available report date in the shop's reporting timezone,
                formatted as YYYY-MM-DD. The containing week is selected when date is omitted. Together with the preceding 11
                report weeks, it defines the supported query window; an available date does not guarantee data for every Pixel
                and attribution setting.
            start_date (datetime.date | Unset): First date of the selected report week, inclusive, formatted as YYYY-MM-DD.
                This is a Sunday.
            trend (GetOffSitePerformanceOverviewResponseDataTrend | Unset):
     """

    end_date: datetime.date | Unset = UNSET
    key_metrics: GetOffSitePerformanceOverviewResponseDataKeyMetric | None | Unset = UNSET
    latest_available_date: datetime.date | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    trend: GetOffSitePerformanceOverviewResponseDataTrend | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_off_site_performance_overview_response_data_key_metric import GetOffSitePerformanceOverviewResponseDataKeyMetric # noqa: PLC0415
        from ..models.get_off_site_performance_overview_response_data_trend import GetOffSitePerformanceOverviewResponseDataTrend # noqa: PLC0415
        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        key_metrics: dict[str, Any] | None | Unset
        if isinstance(self.key_metrics, Unset):
            key_metrics = UNSET
        elif isinstance(self.key_metrics, GetOffSitePerformanceOverviewResponseDataKeyMetric):
            key_metrics = self.key_metrics.to_dict()
        else:
            key_metrics = self.key_metrics

        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        trend: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trend, Unset):
            trend = self.trend.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if key_metrics is not UNSET:
            field_dict["key_metrics"] = key_metrics
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if trend is not UNSET:
            field_dict["trend"] = trend

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_off_site_performance_overview_response_data_key_metric import GetOffSitePerformanceOverviewResponseDataKeyMetric # noqa: PLC0415
        from ..models.get_off_site_performance_overview_response_data_trend import GetOffSitePerformanceOverviewResponseDataTrend # noqa: PLC0415
        d = dict(src_dict)
        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        def _parse_key_metrics(data: object) -> GetOffSitePerformanceOverviewResponseDataKeyMetric | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                key_metrics_type_0 = GetOffSitePerformanceOverviewResponseDataKeyMetric.from_dict(data)



                return key_metrics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetOffSitePerformanceOverviewResponseDataKeyMetric | None | Unset, data)

        key_metrics = _parse_key_metrics(d.pop("key_metrics", UNSET))


        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date,  Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)




        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        _trend = d.pop("trend", UNSET)
        trend: GetOffSitePerformanceOverviewResponseDataTrend | Unset
        if isinstance(_trend,  Unset):
            trend = UNSET
        else:
            trend = GetOffSitePerformanceOverviewResponseDataTrend.from_dict(_trend)




        get_off_site_performance_overview_response_data = cls(
            end_date=end_date,
            key_metrics=key_metrics,
            latest_available_date=latest_available_date,
            start_date=start_date,
            trend=trend,
        )


        get_off_site_performance_overview_response_data.additional_properties = d
        return get_off_site_performance_overview_response_data

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
