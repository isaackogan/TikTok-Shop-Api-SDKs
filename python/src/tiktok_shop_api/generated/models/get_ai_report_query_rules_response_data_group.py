from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_ai_report_query_rules_response_data_group_filter import GetAIReportQueryRulesResponseDataGroupFilter
  from ..models.get_ai_report_query_rules_response_data_group_metric_start_date import GetAIReportQueryRulesResponseDataGroupMetricStartDate





T = TypeVar("T", bound="GetAIReportQueryRulesResponseDataGroup")



@_attrs_define
class GetAIReportQueryRulesResponseDataGroup:
    """ 
        Attributes:
            detail_fields (list[str] | Unset): Detail field codes allowed in this group. Requested details must also satisfy
                detail_requirements.
            filters (list[GetAIReportQueryRulesResponseDataGroupFilter] | Unset): Dimensions allowed in filters for this
                group, with the maximum number of values allowed for each dimension.
            group_dimensions (list[str] | Unset): Dimension codes allowed in group_dimensions for this group. You can select
                a subset; the global exclusions still apply.
            id (str | Unset): Identifier of this rule group. Use it to distinguish groups when reading the rules; it is not
                a query parameter.
            max_days (int | Unset): Maximum number of calendar dates in one query, counting both start_date and end_date.
                This limits the length of a single query, not how far back it can start. For example, a limit of 7 allows
                October 25 through October 31. Omitted when this group has no configured limit.
            metric_codes (list[str] | Unset): Metric codes that this group can query together. Every code in the request
                metric_codes must appear in the same matching group.
            metric_start_dates (list[GetAIReportQueryRulesResponseDataGroupMetricStartDate] | Unset): Earliest supported
                query date for individual metrics. For each selected metric listed here, start_date must be on or after its
                specified date.
            required_any_filter_dimensions (list[str] | Unset): If this list is nonempty, at least one listed dimension must
                have a nonempty filter in the request. An empty list means this group does not require a filter.
            retention_days (int | Unset): Maximum lookback in calendar days, measured from the current date used by server
                validation. This limits how far back a query can start, independently of max_days. start_date must be on or
                after that date minus retention_days, and must also satisfy each selected metric's start_date in
                metric_start_dates.
     """

    detail_fields: list[str] | Unset = UNSET
    filters: list[GetAIReportQueryRulesResponseDataGroupFilter] | Unset = UNSET
    group_dimensions: list[str] | Unset = UNSET
    id: str | Unset = UNSET
    max_days: int | Unset = UNSET
    metric_codes: list[str] | Unset = UNSET
    metric_start_dates: list[GetAIReportQueryRulesResponseDataGroupMetricStartDate] | Unset = UNSET
    required_any_filter_dimensions: list[str] | Unset = UNSET
    retention_days: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_ai_report_query_rules_response_data_group_filter import GetAIReportQueryRulesResponseDataGroupFilter # noqa: PLC0415
        from ..models.get_ai_report_query_rules_response_data_group_metric_start_date import GetAIReportQueryRulesResponseDataGroupMetricStartDate # noqa: PLC0415
        detail_fields: list[str] | Unset = UNSET
        if not isinstance(self.detail_fields, Unset):
            detail_fields = self.detail_fields



        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)



        group_dimensions: list[str] | Unset = UNSET
        if not isinstance(self.group_dimensions, Unset):
            group_dimensions = self.group_dimensions



        id = self.id

        max_days = self.max_days

        metric_codes: list[str] | Unset = UNSET
        if not isinstance(self.metric_codes, Unset):
            metric_codes = self.metric_codes



        metric_start_dates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.metric_start_dates, Unset):
            metric_start_dates = []
            for metric_start_dates_item_data in self.metric_start_dates:
                metric_start_dates_item = metric_start_dates_item_data.to_dict()
                metric_start_dates.append(metric_start_dates_item)



        required_any_filter_dimensions: list[str] | Unset = UNSET
        if not isinstance(self.required_any_filter_dimensions, Unset):
            required_any_filter_dimensions = self.required_any_filter_dimensions



        retention_days = self.retention_days


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if detail_fields is not UNSET:
            field_dict["detail_fields"] = detail_fields
        if filters is not UNSET:
            field_dict["filters"] = filters
        if group_dimensions is not UNSET:
            field_dict["group_dimensions"] = group_dimensions
        if id is not UNSET:
            field_dict["id"] = id
        if max_days is not UNSET:
            field_dict["max_days"] = max_days
        if metric_codes is not UNSET:
            field_dict["metric_codes"] = metric_codes
        if metric_start_dates is not UNSET:
            field_dict["metric_start_dates"] = metric_start_dates
        if required_any_filter_dimensions is not UNSET:
            field_dict["required_any_filter_dimensions"] = required_any_filter_dimensions
        if retention_days is not UNSET:
            field_dict["retention_days"] = retention_days

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_ai_report_query_rules_response_data_group_filter import GetAIReportQueryRulesResponseDataGroupFilter # noqa: PLC0415
        from ..models.get_ai_report_query_rules_response_data_group_metric_start_date import GetAIReportQueryRulesResponseDataGroupMetricStartDate # noqa: PLC0415
        d = dict(src_dict)
        detail_fields = cast(list[str], d.pop("detail_fields", UNSET))


        _filters = d.pop("filters", UNSET)
        filters: list[GetAIReportQueryRulesResponseDataGroupFilter] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = GetAIReportQueryRulesResponseDataGroupFilter.from_dict(filters_item_data)



                filters.append(filters_item)


        group_dimensions = cast(list[str], d.pop("group_dimensions", UNSET))


        id = d.pop("id", UNSET)

        max_days = d.pop("max_days", UNSET)

        metric_codes = cast(list[str], d.pop("metric_codes", UNSET))


        _metric_start_dates = d.pop("metric_start_dates", UNSET)
        metric_start_dates: list[GetAIReportQueryRulesResponseDataGroupMetricStartDate] | Unset = UNSET
        if _metric_start_dates is not UNSET:
            metric_start_dates = []
            for metric_start_dates_item_data in _metric_start_dates:
                metric_start_dates_item = GetAIReportQueryRulesResponseDataGroupMetricStartDate.from_dict(metric_start_dates_item_data)



                metric_start_dates.append(metric_start_dates_item)


        required_any_filter_dimensions = cast(list[str], d.pop("required_any_filter_dimensions", UNSET))


        retention_days = d.pop("retention_days", UNSET)

        get_ai_report_query_rules_response_data_group = cls(
            detail_fields=detail_fields,
            filters=filters,
            group_dimensions=group_dimensions,
            id=id,
            max_days=max_days,
            metric_codes=metric_codes,
            metric_start_dates=metric_start_dates,
            required_any_filter_dimensions=required_any_filter_dimensions,
            retention_days=retention_days,
        )


        get_ai_report_query_rules_response_data_group.additional_properties = d
        return get_ai_report_query_rules_response_data_group

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
