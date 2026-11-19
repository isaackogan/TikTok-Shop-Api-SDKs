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
  from ..models.filter_ import Filter
  from ..models.sort_rule import SortRule





T = TypeVar("T", bound="QueryAIReportDataRequest")



@_attrs_define
class QueryAIReportDataRequest:
    """ 
        Attributes:
            end_date (datetime.date): Last date to query, in YYYY-MM-DD format and the shop timezone. Data for this date is
                included.
            metric_codes (list[str]): Metrics to calculate, such as pay_amt for GMV. Select at least one metric code from
                the catalog. All selected metrics must be supported together by the query rules.
            start_date (datetime.date): First date to query, in YYYY-MM-DD format and the shop timezone. Data for this date
                is included.
            time_granularity (str): Time unit used to split query results in the shop timezone. DAY: Calendar day. WEEK:
                Calendar week. MONTH: Calendar month. YEAR: Calendar year. Select a value returned by catalog.time_granularities
                for this shop. Only DAY, WEEK, MONTH and YEAR are supported.
            detail_fields (list[str] | Unset): Additional fields to return for each row, such as payment time. Select codes
                from the catalog and include the grouping dimensions required by the query rules.
            filters (list[Filter] | Unset): Conditions that restrict which data is included. Values within one dimension are
                combined with IN; different dimensions are combined with AND.
            group_dimensions (list[str] | Unset): Dimensions that split metric values into separate rows. For example,
                product_id returns separate values for each product. Select dimension codes supported with your metrics by the
                query rules.
            sort_rules (list[SortRule] | Unset): Sort rules in order of priority. If omitted or empty, sort by the first
                selected metric in descending order. When time_granularity splits results into time buckets and no time sort is
                specified, append time ascending after the selected sort rules. Any remaining grouping keys are then appended in
                ascending order. An explicit time sort keeps its position and direction.
     """

    end_date: datetime.date
    metric_codes: list[str]
    start_date: datetime.date
    time_granularity: str
    detail_fields: list[str] | Unset = UNSET
    filters: list[Filter] | Unset = UNSET
    group_dimensions: list[str] | Unset = UNSET
    sort_rules: list[SortRule] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_ import Filter # noqa: PLC0415
        from ..models.sort_rule import SortRule # noqa: PLC0415
        end_date = self.end_date.isoformat()

        metric_codes = self.metric_codes



        start_date = self.start_date.isoformat()

        time_granularity = self.time_granularity

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



        sort_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sort_rules, Unset):
            sort_rules = []
            for sort_rules_item_data in self.sort_rules:
                sort_rules_item = sort_rules_item_data.to_dict()
                sort_rules.append(sort_rules_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "end_date": end_date,
            "metric_codes": metric_codes,
            "start_date": start_date,
            "time_granularity": time_granularity,
        })
        if detail_fields is not UNSET:
            field_dict["detail_fields"] = detail_fields
        if filters is not UNSET:
            field_dict["filters"] = filters
        if group_dimensions is not UNSET:
            field_dict["group_dimensions"] = group_dimensions
        if sort_rules is not UNSET:
            field_dict["sort_rules"] = sort_rules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_ import Filter # noqa: PLC0415
        from ..models.sort_rule import SortRule # noqa: PLC0415
        d = dict(src_dict)
        end_date = datetime.date.fromisoformat(d.pop("end_date"))




        metric_codes = cast(list[str], d.pop("metric_codes"))


        start_date = datetime.date.fromisoformat(d.pop("start_date"))




        time_granularity = d.pop("time_granularity")

        detail_fields = cast(list[str], d.pop("detail_fields", UNSET))


        _filters = d.pop("filters", UNSET)
        filters: list[Filter] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = Filter.from_dict(filters_item_data)



                filters.append(filters_item)


        group_dimensions = cast(list[str], d.pop("group_dimensions", UNSET))


        _sort_rules = d.pop("sort_rules", UNSET)
        sort_rules: list[SortRule] | Unset = UNSET
        if _sort_rules is not UNSET:
            sort_rules = []
            for sort_rules_item_data in _sort_rules:
                sort_rules_item = SortRule.from_dict(sort_rules_item_data)



                sort_rules.append(sort_rules_item)


        query_ai_report_data_request = cls(
            end_date=end_date,
            metric_codes=metric_codes,
            start_date=start_date,
            time_granularity=time_granularity,
            detail_fields=detail_fields,
            filters=filters,
            group_dimensions=group_dimensions,
            sort_rules=sort_rules,
        )


        query_ai_report_data_request.additional_properties = d
        return query_ai_report_data_request

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
