from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_ai_report_catalog_response_data_detail_field import GetAIReportCatalogResponseDataDetailField
  from ..models.get_ai_report_catalog_response_data_dimension import GetAIReportCatalogResponseDataDimension
  from ..models.get_ai_report_catalog_response_data_metric import GetAIReportCatalogResponseDataMetric





T = TypeVar("T", bound="GetAIReportCatalogResponseData")



@_attrs_define
class GetAIReportCatalogResponseData:
    """ 
        Attributes:
            detail_fields (list[GetAIReportCatalogResponseDataDetailField] | Unset): Additional fields that can be returned
                on each result row, such as payment time. Select their codes in detail_fields and include any grouping
                dimensions required by the query rules.
            dimensions (list[GetAIReportCatalogResponseDataDimension] | Unset): Dimensions available for grouping or
                filtering. Use code in group_dimensions or filters[].code. The query rules specify which dimensions can be
                combined with your selected metrics.
            metrics (list[GetAIReportCatalogResponseDataMetric] | Unset): Metrics available for selection. Use each metric
                code in metric_codes when validating or querying data. This list describes metrics; it does not contain measured
                values.
            time_granularities (list[str] | Unset): Time unit used to split query results in the shop timezone. DAY:
                Calendar day. WEEK: Calendar week. MONTH: Calendar month. YEAR: Calendar year. Select a value returned by
                catalog.time_granularities for this shop. Only DAY, WEEK, MONTH and YEAR are supported.
     """

    detail_fields: list[GetAIReportCatalogResponseDataDetailField] | Unset = UNSET
    dimensions: list[GetAIReportCatalogResponseDataDimension] | Unset = UNSET
    metrics: list[GetAIReportCatalogResponseDataMetric] | Unset = UNSET
    time_granularities: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_ai_report_catalog_response_data_detail_field import GetAIReportCatalogResponseDataDetailField # noqa: PLC0415
        from ..models.get_ai_report_catalog_response_data_dimension import GetAIReportCatalogResponseDataDimension # noqa: PLC0415
        from ..models.get_ai_report_catalog_response_data_metric import GetAIReportCatalogResponseDataMetric # noqa: PLC0415
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



        metrics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)



        time_granularities: list[str] | Unset = UNSET
        if not isinstance(self.time_granularities, Unset):
            time_granularities = self.time_granularities




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if detail_fields is not UNSET:
            field_dict["detail_fields"] = detail_fields
        if dimensions is not UNSET:
            field_dict["dimensions"] = dimensions
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if time_granularities is not UNSET:
            field_dict["time_granularities"] = time_granularities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_ai_report_catalog_response_data_detail_field import GetAIReportCatalogResponseDataDetailField # noqa: PLC0415
        from ..models.get_ai_report_catalog_response_data_dimension import GetAIReportCatalogResponseDataDimension # noqa: PLC0415
        from ..models.get_ai_report_catalog_response_data_metric import GetAIReportCatalogResponseDataMetric # noqa: PLC0415
        d = dict(src_dict)
        _detail_fields = d.pop("detail_fields", UNSET)
        detail_fields: list[GetAIReportCatalogResponseDataDetailField] | Unset = UNSET
        if _detail_fields is not UNSET:
            detail_fields = []
            for detail_fields_item_data in _detail_fields:
                detail_fields_item = GetAIReportCatalogResponseDataDetailField.from_dict(detail_fields_item_data)



                detail_fields.append(detail_fields_item)


        _dimensions = d.pop("dimensions", UNSET)
        dimensions: list[GetAIReportCatalogResponseDataDimension] | Unset = UNSET
        if _dimensions is not UNSET:
            dimensions = []
            for dimensions_item_data in _dimensions:
                dimensions_item = GetAIReportCatalogResponseDataDimension.from_dict(dimensions_item_data)



                dimensions.append(dimensions_item)


        _metrics = d.pop("metrics", UNSET)
        metrics: list[GetAIReportCatalogResponseDataMetric] | Unset = UNSET
        if _metrics is not UNSET:
            metrics = []
            for metrics_item_data in _metrics:
                metrics_item = GetAIReportCatalogResponseDataMetric.from_dict(metrics_item_data)



                metrics.append(metrics_item)


        time_granularities = cast(list[str], d.pop("time_granularities", UNSET))


        get_ai_report_catalog_response_data = cls(
            detail_fields=detail_fields,
            dimensions=dimensions,
            metrics=metrics,
            time_granularities=time_granularities,
        )


        get_ai_report_catalog_response_data.additional_properties = d
        return get_ai_report_catalog_response_data

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
