from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sps_metrics_response_data_metric import GetSPSMetricsResponseDataMetric


T = TypeVar("T", bound="GetSPSMetricsResponseData")


@_attrs_define
class GetSPSMetricsResponseData:
    """
    Attributes:
        metrics (list[GetSPSMetricsResponseDataMetric] | Unset): Fixed complete SPS metric set for the authorized shop.
    """

    metrics: list[GetSPSMetricsResponseDataMetric] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        metrics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sps_metrics_response_data_metric import GetSPSMetricsResponseDataMetric  # noqa: PLC0415

        d = dict(src_dict)
        _metrics = d.pop("metrics", UNSET)
        metrics: list[GetSPSMetricsResponseDataMetric] | Unset = UNSET
        if _metrics is not UNSET:
            metrics = []
            for metrics_item_data in _metrics:
                metrics_item = GetSPSMetricsResponseDataMetric.from_dict(metrics_item_data)

                metrics.append(metrics_item)

        get_sps_metrics_response_data = cls(
            metrics=metrics,
        )

        get_sps_metrics_response_data.additional_properties = d
        return get_sps_metrics_response_data

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
