from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_video_performances_response_data_video_performance_metric import GetVideoPerformancesResponseDataVideoPerformanceMetric
  from ..models.get_video_performances_response_data_video_performance_time_range import GetVideoPerformancesResponseDataVideoPerformanceTimeRange





T = TypeVar("T", bound="GetVideoPerformancesResponseDataVideoPerformance")



@_attrs_define
class GetVideoPerformancesResponseDataVideoPerformance:
    """ 
        Attributes:
            time_range (GetVideoPerformancesResponseDataVideoPerformanceTimeRange | Unset):
            metrics (GetVideoPerformancesResponseDataVideoPerformanceMetric | Unset):
     """

    time_range: GetVideoPerformancesResponseDataVideoPerformanceTimeRange | Unset = UNSET
    metrics: GetVideoPerformancesResponseDataVideoPerformanceMetric | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_video_performances_response_data_video_performance_metric import GetVideoPerformancesResponseDataVideoPerformanceMetric # noqa: PLC0415
        from ..models.get_video_performances_response_data_video_performance_time_range import GetVideoPerformancesResponseDataVideoPerformanceTimeRange # noqa: PLC0415
        time_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.to_dict()

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if time_range is not UNSET:
            field_dict["time_range"] = time_range
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_video_performances_response_data_video_performance_metric import GetVideoPerformancesResponseDataVideoPerformanceMetric # noqa: PLC0415
        from ..models.get_video_performances_response_data_video_performance_time_range import GetVideoPerformancesResponseDataVideoPerformanceTimeRange # noqa: PLC0415
        d = dict(src_dict)
        _time_range = d.pop("time_range", UNSET)
        time_range: GetVideoPerformancesResponseDataVideoPerformanceTimeRange | Unset
        if isinstance(_time_range,  Unset):
            time_range = UNSET
        else:
            time_range = GetVideoPerformancesResponseDataVideoPerformanceTimeRange.from_dict(_time_range)




        _metrics = d.pop("metrics", UNSET)
        metrics: GetVideoPerformancesResponseDataVideoPerformanceMetric | Unset
        if isinstance(_metrics,  Unset):
            metrics = UNSET
        else:
            metrics = GetVideoPerformancesResponseDataVideoPerformanceMetric.from_dict(_metrics)




        get_video_performances_response_data_video_performance = cls(
            time_range=time_range,
            metrics=metrics,
        )


        get_video_performances_response_data_video_performance.additional_properties = d
        return get_video_performances_response_data_video_performance

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
