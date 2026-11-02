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
  from ..models.get_acc_audience_overview_response_data_key_metric import GetACCAudienceOverviewResponseDataKeyMetric
  from ..models.get_acc_audience_overview_response_data_trend import GetACCAudienceOverviewResponseDataTrend





T = TypeVar("T", bound="GetACCAudienceOverviewResponseData")



@_attrs_define
class GetACCAudienceOverviewResponseData:
    """ 
        Attributes:
            key_metrics (GetACCAudienceOverviewResponseDataKeyMetric | Unset):
            latest_available_date (datetime.date | Unset): Latest available date for the requested brand and industry, in
                `YYYY-MM-DD` format (UTC). This may differ from the requested `date`.
            trend (list[GetACCAudienceOverviewResponseDataTrend] | Unset): Time series for the six audience metrics. Each
                series contains up to 30 available daily data points in ascending UTC date order. Missing dates are not filled.
     """

    key_metrics: GetACCAudienceOverviewResponseDataKeyMetric | Unset = UNSET
    latest_available_date: datetime.date | Unset = UNSET
    trend: list[GetACCAudienceOverviewResponseDataTrend] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_audience_overview_response_data_key_metric import GetACCAudienceOverviewResponseDataKeyMetric # noqa: PLC0415
        from ..models.get_acc_audience_overview_response_data_trend import GetACCAudienceOverviewResponseDataTrend # noqa: PLC0415
        key_metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.key_metrics, Unset):
            key_metrics = self.key_metrics.to_dict()

        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()

        trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.trend, Unset):
            trend = []
            for trend_item_data in self.trend:
                trend_item = trend_item_data.to_dict()
                trend.append(trend_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if key_metrics is not UNSET:
            field_dict["key_metrics"] = key_metrics
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date
        if trend is not UNSET:
            field_dict["trend"] = trend

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_acc_audience_overview_response_data_key_metric import GetACCAudienceOverviewResponseDataKeyMetric # noqa: PLC0415
        from ..models.get_acc_audience_overview_response_data_trend import GetACCAudienceOverviewResponseDataTrend # noqa: PLC0415
        d = dict(src_dict)
        _key_metrics = d.pop("key_metrics", UNSET)
        key_metrics: GetACCAudienceOverviewResponseDataKeyMetric | Unset
        if isinstance(_key_metrics,  Unset):
            key_metrics = UNSET
        else:
            key_metrics = GetACCAudienceOverviewResponseDataKeyMetric.from_dict(_key_metrics)




        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date,  Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)




        _trend = d.pop("trend", UNSET)
        trend: list[GetACCAudienceOverviewResponseDataTrend] | Unset = UNSET
        if _trend is not UNSET:
            trend = []
            for trend_item_data in _trend:
                trend_item = GetACCAudienceOverviewResponseDataTrend.from_dict(trend_item_data)



                trend.append(trend_item)


        get_acc_audience_overview_response_data = cls(
            key_metrics=key_metrics,
            latest_available_date=latest_available_date,
            trend=trend,
        )


        get_acc_audience_overview_response_data.additional_properties = d
        return get_acc_audience_overview_response_data

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
