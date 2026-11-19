from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.query_ai_report_data_response_data_row_detail_field import QueryAIReportDataResponseDataRowDetailField
  from ..models.query_ai_report_data_response_data_row_dimension import QueryAIReportDataResponseDataRowDimension
  from ..models.query_ai_report_data_response_data_row_metric import QueryAIReportDataResponseDataRowMetric





T = TypeVar("T", bound="QueryAIReportDataResponseDataRow")



@_attrs_define
class QueryAIReportDataResponseDataRow:
    """ 
        Attributes:
            detail_fields (list[QueryAIReportDataResponseDataRowDetailField] | Unset): Additional information requested in
                detail_fields for this row, such as payment time.
            dimensions (list[QueryAIReportDataResponseDataRowDimension] | Unset): Dimension values identifying this row,
                such as the product or content type.
            end_date (str | Unset): Last date covered by this result row, in the shop timezone.
            metrics (list[QueryAIReportDataResponseDataRowMetric] | Unset): Measured values for the metrics selected in
                metric_codes.
            start_date (str | Unset): First date covered by this result row, in the shop timezone.
     """

    detail_fields: list[QueryAIReportDataResponseDataRowDetailField] | Unset = UNSET
    dimensions: list[QueryAIReportDataResponseDataRowDimension] | Unset = UNSET
    end_date: str | Unset = UNSET
    metrics: list[QueryAIReportDataResponseDataRowMetric] | Unset = UNSET
    start_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.query_ai_report_data_response_data_row_detail_field import QueryAIReportDataResponseDataRowDetailField # noqa: PLC0415
        from ..models.query_ai_report_data_response_data_row_dimension import QueryAIReportDataResponseDataRowDimension # noqa: PLC0415
        from ..models.query_ai_report_data_response_data_row_metric import QueryAIReportDataResponseDataRowMetric # noqa: PLC0415
        detail_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.detail_fields, Unset):
            detail_fields = []
            for detail_fields_item_data in self.detail_fields:
                detail_fields_item = detail_fields_item_data.to_dict()
                detail_fields.append(detail_fields_item)



        dimensions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dimensions, Unset):
            dimensions = []
            for dimensions_item_data in self.dimensions:
                dimensions_item = dimensions_item_data.to_dict()
                dimensions.append(dimensions_item)



        end_date = self.end_date

        metrics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)



        start_date = self.start_date


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if detail_fields is not UNSET:
            field_dict["detail_fields"] = detail_fields
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_ai_report_data_response_data_row_detail_field import QueryAIReportDataResponseDataRowDetailField # noqa: PLC0415
        from ..models.query_ai_report_data_response_data_row_dimension import QueryAIReportDataResponseDataRowDimension # noqa: PLC0415
        from ..models.query_ai_report_data_response_data_row_metric import QueryAIReportDataResponseDataRowMetric # noqa: PLC0415
        d = dict(src_dict)
        _detail_fields = d.pop("detail_fields", UNSET)
        detail_fields: list[QueryAIReportDataResponseDataRowDetailField] | Unset = UNSET
        if _detail_fields is not UNSET:
            detail_fields = []
            for detail_fields_item_data in _detail_fields:
                detail_fields_item = QueryAIReportDataResponseDataRowDetailField.from_dict(detail_fields_item_data)



                detail_fields.append(detail_fields_item)


        _dimensions = d.pop("dimensions", UNSET)
        dimensions: list[QueryAIReportDataResponseDataRowDimension] | Unset = UNSET
        if _dimensions is not UNSET:
            dimensions = []
            for dimensions_item_data in _dimensions:
                dimensions_item = QueryAIReportDataResponseDataRowDimension.from_dict(dimensions_item_data)



                dimensions.append(dimensions_item)


        end_date = d.pop("end_date", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: list[QueryAIReportDataResponseDataRowMetric] | Unset = UNSET
        if _metrics is not UNSET:
            metrics = []
            for metrics_item_data in _metrics:
                metrics_item = QueryAIReportDataResponseDataRowMetric.from_dict(metrics_item_data)



                metrics.append(metrics_item)


        start_date = d.pop("start_date", UNSET)

        query_ai_report_data_response_data_row = cls(
            detail_fields=detail_fields,
            dimensions=dimensions,
            end_date=end_date,
            metrics=metrics,
            start_date=start_date,
        )


        query_ai_report_data_response_data_row.additional_properties = d
        return query_ai_report_data_response_data_row

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
