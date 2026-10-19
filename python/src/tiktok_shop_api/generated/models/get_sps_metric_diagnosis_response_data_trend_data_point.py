from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSPSMetricDiagnosisResponseDataTrendDataPoint")


@_attrs_define
class GetSPSMetricDiagnosisResponseDataTrendDataPoint:
    """
    Attributes:
        record_date (str | Unset): Trend date in yyyyMMdd format.
        value (str | Unset): Metric value on the trend date, using the same unit as value_unit.
    """

    record_date: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        record_date = self.record_date

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if record_date is not UNSET:
            field_dict["record_date"] = record_date
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        record_date = d.pop("record_date", UNSET)

        value = d.pop("value", UNSET)

        get_sps_metric_diagnosis_response_data_trend_data_point = cls(
            record_date=record_date,
            value=value,
        )

        get_sps_metric_diagnosis_response_data_trend_data_point.additional_properties = d
        return get_sps_metric_diagnosis_response_data_trend_data_point

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
