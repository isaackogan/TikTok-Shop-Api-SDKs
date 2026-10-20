from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.benchmark import Benchmark


T = TypeVar("T", bound="GetSPSMetricsResponseDataMetric")


@_attrs_define
class GetSPSMetricsResponseDataMetric:
    """
    Attributes:
        benchmarks (Benchmark | Unset):
        dimension (str | Unset): SPS dimension that the metric belongs to.
        evaluate_duration_days (int | Unset): Number of days included in this metric's evaluation period.
        end_evaluation_time (int | Unset): Metric evaluation period end time. Unix timestamp in seconds.
        start_evaluation_time (int | Unset): Metric evaluation period start time. Unix timestamp in seconds.
        metric_code (str | Unset): Stable metric code. Possible values include NRR, NBFR, SFCR, OTDR, AHT, and IM_DSAT.
        metric_name (str | Unset): Localized metric display name.
        score (str | Unset): Metric score, from 0 to 5.
        status (str | Unset): Metric status. Possible values include EXCELLENT, GOOD, POOR, CRITICAL and NIL.
        status_text (str | Unset): Metric status text. Values like Excellent, Good, Normal, Attention.
        value (str | Unset): Metric value. Hours are represented as values; percentages are represented as values from 0
            to 100.
        value_unit (str | Unset): Unit of the metric value. Possible values include PERCENT and HOURS.
        top_reason_text (str | Unset): Indicates that this metric is a key contributor to SPS.
    """

    benchmarks: Benchmark | Unset = UNSET
    dimension: str | Unset = UNSET
    evaluate_duration_days: int | Unset = UNSET
    end_evaluation_time: int | Unset = UNSET
    start_evaluation_time: int | Unset = UNSET
    metric_code: str | Unset = UNSET
    metric_name: str | Unset = UNSET
    score: str | Unset = UNSET
    status: str | Unset = UNSET
    status_text: str | Unset = UNSET
    value: str | Unset = UNSET
    value_unit: str | Unset = UNSET
    top_reason_text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        benchmarks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.benchmarks, Unset):
            benchmarks = self.benchmarks.to_dict()

        dimension = self.dimension

        evaluate_duration_days = self.evaluate_duration_days

        end_evaluation_time = self.end_evaluation_time

        start_evaluation_time = self.start_evaluation_time

        metric_code = self.metric_code

        metric_name = self.metric_name

        score = self.score

        status = self.status

        status_text = self.status_text

        value = self.value

        value_unit = self.value_unit

        top_reason_text = self.top_reason_text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if benchmarks is not UNSET:
            field_dict["benchmarks"] = benchmarks
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if evaluate_duration_days is not UNSET:
            field_dict["evaluate_duration_days"] = evaluate_duration_days
        if end_evaluation_time is not UNSET:
            field_dict["end_evaluation_time"] = end_evaluation_time
        if start_evaluation_time is not UNSET:
            field_dict["start_evaluation_time"] = start_evaluation_time
        if metric_code is not UNSET:
            field_dict["metric_code"] = metric_code
        if metric_name is not UNSET:
            field_dict["metric_name"] = metric_name
        if score is not UNSET:
            field_dict["score"] = score
        if status is not UNSET:
            field_dict["status"] = status
        if status_text is not UNSET:
            field_dict["status_text"] = status_text
        if value is not UNSET:
            field_dict["value"] = value
        if value_unit is not UNSET:
            field_dict["value_unit"] = value_unit
        if top_reason_text is not UNSET:
            field_dict["top_reason_text"] = top_reason_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.benchmark import Benchmark  # noqa: PLC0415

        d = dict(src_dict)
        _benchmarks = d.pop("benchmarks", UNSET)
        benchmarks: Benchmark | Unset
        if isinstance(_benchmarks, Unset):
            benchmarks = UNSET
        else:
            benchmarks = Benchmark.from_dict(_benchmarks)

        dimension = d.pop("dimension", UNSET)

        evaluate_duration_days = d.pop("evaluate_duration_days", UNSET)

        end_evaluation_time = d.pop("end_evaluation_time", UNSET)

        start_evaluation_time = d.pop("start_evaluation_time", UNSET)

        metric_code = d.pop("metric_code", UNSET)

        metric_name = d.pop("metric_name", UNSET)

        score = d.pop("score", UNSET)

        status = d.pop("status", UNSET)

        status_text = d.pop("status_text", UNSET)

        value = d.pop("value", UNSET)

        value_unit = d.pop("value_unit", UNSET)

        top_reason_text = d.pop("top_reason_text", UNSET)

        get_sps_metrics_response_data_metric = cls(
            benchmarks=benchmarks,
            dimension=dimension,
            evaluate_duration_days=evaluate_duration_days,
            end_evaluation_time=end_evaluation_time,
            start_evaluation_time=start_evaluation_time,
            metric_code=metric_code,
            metric_name=metric_name,
            score=score,
            status=status,
            status_text=status_text,
            value=value,
            value_unit=value_unit,
            top_reason_text=top_reason_text,
        )

        get_sps_metrics_response_data_metric.additional_properties = d
        return get_sps_metrics_response_data_metric

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
