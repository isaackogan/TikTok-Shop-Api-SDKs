from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.benchmark import Benchmark
    from ..models.get_sps_metric_diagnosis_response_data_analysis import GetSPSMetricDiagnosisResponseDataAnalysis
    from ..models.get_sps_metric_diagnosis_response_data_calculation_rule import (
        GetSPSMetricDiagnosisResponseDataCalculationRule,
    )
    from ..models.get_sps_metric_diagnosis_response_data_distribution_detail import (
        GetSPSMetricDiagnosisResponseDataDistributionDetail,
    )
    from ..models.get_sps_metric_diagnosis_response_data_trend import GetSPSMetricDiagnosisResponseDataTrend


T = TypeVar("T", bound="GetSPSMetricDiagnosisResponseData")


@_attrs_define
class GetSPSMetricDiagnosisResponseData:
    """
    Attributes:
        benchmarks (Benchmark | Unset):
        calculation_rule (GetSPSMetricDiagnosisResponseDataCalculationRule | Unset):
        dimension (str | Unset): SPS dimension that the metric belongs to.
        distribution_details (list[GetSPSMetricDiagnosisResponseDataDistributionDetail] | Unset): Additional
            distribution details for the metric.
        evaluate_duration_days (int | Unset): Number of days included in the metric evaluation period.
        end_evaluation_time (int | Unset): Metric evaluation period end time. Unix timestamp in seconds.
        start_evaluation_time (int | Unset): Metric evaluation period start time. Unix timestamp in seconds.
        metric_code (str | Unset): Stable metric code. Possible values: NRR, NBFR, SFCR, OTDR, AHT, and IM_DSAT.
        score (str | Unset): Metric score, from 0 to 5.
        status (str | Unset): Metric status. Possible values include EXCELLENT, GOOD, POOR, CRITICAL and NIL.
        status_text (str | Unset): Metric status text. Values like Excellent, Good, Normal, Attention.
        trend (GetSPSMetricDiagnosisResponseDataTrend | Unset):
        value (str | Unset): Metric value. Ratios are represented as values from 0 to 1; percentages are represented as
            values from 0 to 100.
        value_unit (str | Unset): Unit of the metric value. Possible values include PERCENT and HOURS.
        analyses (list[GetSPSMetricDiagnosisResponseDataAnalysis] | Unset): Diagnostic insights for the selected metric.
    """

    benchmarks: Benchmark | Unset = UNSET
    calculation_rule: GetSPSMetricDiagnosisResponseDataCalculationRule | Unset = UNSET
    dimension: str | Unset = UNSET
    distribution_details: list[GetSPSMetricDiagnosisResponseDataDistributionDetail] | Unset = UNSET
    evaluate_duration_days: int | Unset = UNSET
    end_evaluation_time: int | Unset = UNSET
    start_evaluation_time: int | Unset = UNSET
    metric_code: str | Unset = UNSET
    score: str | Unset = UNSET
    status: str | Unset = UNSET
    status_text: str | Unset = UNSET
    trend: GetSPSMetricDiagnosisResponseDataTrend | Unset = UNSET
    value: str | Unset = UNSET
    value_unit: str | Unset = UNSET
    analyses: list[GetSPSMetricDiagnosisResponseDataAnalysis] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        benchmarks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.benchmarks, Unset):
            benchmarks = self.benchmarks.to_dict()

        calculation_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.calculation_rule, Unset):
            calculation_rule = self.calculation_rule.to_dict()

        dimension = self.dimension

        distribution_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.distribution_details, Unset):
            distribution_details = []
            for distribution_details_item_data in self.distribution_details:
                distribution_details_item = distribution_details_item_data.to_dict()
                distribution_details.append(distribution_details_item)

        evaluate_duration_days = self.evaluate_duration_days

        end_evaluation_time = self.end_evaluation_time

        start_evaluation_time = self.start_evaluation_time

        metric_code = self.metric_code

        score = self.score

        status = self.status

        status_text = self.status_text

        trend: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trend, Unset):
            trend = self.trend.to_dict()

        value = self.value

        value_unit = self.value_unit

        analyses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.analyses, Unset):
            analyses = []
            for analyses_item_data in self.analyses:
                analyses_item = analyses_item_data.to_dict()
                analyses.append(analyses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if benchmarks is not UNSET:
            field_dict["benchmarks"] = benchmarks
        if calculation_rule is not UNSET:
            field_dict["calculation_rule"] = calculation_rule
        if dimension is not UNSET:
            field_dict["dimension"] = dimension
        if distribution_details is not UNSET:
            field_dict["distribution_details"] = distribution_details
        if evaluate_duration_days is not UNSET:
            field_dict["evaluate_duration_days"] = evaluate_duration_days
        if end_evaluation_time is not UNSET:
            field_dict["end_evaluation_time"] = end_evaluation_time
        if start_evaluation_time is not UNSET:
            field_dict["start_evaluation_time"] = start_evaluation_time
        if metric_code is not UNSET:
            field_dict["metric_code"] = metric_code
        if score is not UNSET:
            field_dict["score"] = score
        if status is not UNSET:
            field_dict["status"] = status
        if status_text is not UNSET:
            field_dict["status_text"] = status_text
        if trend is not UNSET:
            field_dict["trend"] = trend
        if value is not UNSET:
            field_dict["value"] = value
        if value_unit is not UNSET:
            field_dict["value_unit"] = value_unit
        if analyses is not UNSET:
            field_dict["analyses"] = analyses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.benchmark import Benchmark  # noqa: PLC0415
        from ..models.get_sps_metric_diagnosis_response_data_analysis import (
            GetSPSMetricDiagnosisResponseDataAnalysis,  # noqa: PLC0415
        )
        from ..models.get_sps_metric_diagnosis_response_data_calculation_rule import (
            GetSPSMetricDiagnosisResponseDataCalculationRule,  # noqa: PLC0415
        )
        from ..models.get_sps_metric_diagnosis_response_data_distribution_detail import (
            GetSPSMetricDiagnosisResponseDataDistributionDetail,  # noqa: PLC0415
        )
        from ..models.get_sps_metric_diagnosis_response_data_trend import (
            GetSPSMetricDiagnosisResponseDataTrend,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _benchmarks = d.pop("benchmarks", UNSET)
        benchmarks: Benchmark | Unset
        if isinstance(_benchmarks, Unset):
            benchmarks = UNSET
        else:
            benchmarks = Benchmark.from_dict(_benchmarks)

        _calculation_rule = d.pop("calculation_rule", UNSET)
        calculation_rule: GetSPSMetricDiagnosisResponseDataCalculationRule | Unset
        if isinstance(_calculation_rule, Unset):
            calculation_rule = UNSET
        else:
            calculation_rule = GetSPSMetricDiagnosisResponseDataCalculationRule.from_dict(_calculation_rule)

        dimension = d.pop("dimension", UNSET)

        _distribution_details = d.pop("distribution_details", UNSET)
        distribution_details: list[GetSPSMetricDiagnosisResponseDataDistributionDetail] | Unset = UNSET
        if _distribution_details is not UNSET:
            distribution_details = []
            for distribution_details_item_data in _distribution_details:
                distribution_details_item = GetSPSMetricDiagnosisResponseDataDistributionDetail.from_dict(
                    distribution_details_item_data
                )

                distribution_details.append(distribution_details_item)

        evaluate_duration_days = d.pop("evaluate_duration_days", UNSET)

        end_evaluation_time = d.pop("end_evaluation_time", UNSET)

        start_evaluation_time = d.pop("start_evaluation_time", UNSET)

        metric_code = d.pop("metric_code", UNSET)

        score = d.pop("score", UNSET)

        status = d.pop("status", UNSET)

        status_text = d.pop("status_text", UNSET)

        _trend = d.pop("trend", UNSET)
        trend: GetSPSMetricDiagnosisResponseDataTrend | Unset
        if isinstance(_trend, Unset):
            trend = UNSET
        else:
            trend = GetSPSMetricDiagnosisResponseDataTrend.from_dict(_trend)

        value = d.pop("value", UNSET)

        value_unit = d.pop("value_unit", UNSET)

        _analyses = d.pop("analyses", UNSET)
        analyses: list[GetSPSMetricDiagnosisResponseDataAnalysis] | Unset = UNSET
        if _analyses is not UNSET:
            analyses = []
            for analyses_item_data in _analyses:
                analyses_item = GetSPSMetricDiagnosisResponseDataAnalysis.from_dict(analyses_item_data)

                analyses.append(analyses_item)

        get_sps_metric_diagnosis_response_data = cls(
            benchmarks=benchmarks,
            calculation_rule=calculation_rule,
            dimension=dimension,
            distribution_details=distribution_details,
            evaluate_duration_days=evaluate_duration_days,
            end_evaluation_time=end_evaluation_time,
            start_evaluation_time=start_evaluation_time,
            metric_code=metric_code,
            score=score,
            status=status,
            status_text=status_text,
            trend=trend,
            value=value,
            value_unit=value_unit,
            analyses=analyses,
        )

        get_sps_metric_diagnosis_response_data.additional_properties = d
        return get_sps_metric_diagnosis_response_data

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
