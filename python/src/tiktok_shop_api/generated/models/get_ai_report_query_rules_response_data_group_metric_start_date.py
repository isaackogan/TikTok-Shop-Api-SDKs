from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="GetAIReportQueryRulesResponseDataGroupMetricStartDate")



@_attrs_define
class GetAIReportQueryRulesResponseDataGroupMetricStartDate:
    """ 
        Attributes:
            metric_code (str | Unset): Metric code whose earliest query start date is specified by this entry.
            start_date (datetime.date | Unset): Earliest query start_date allowed for this metric, in YYYY-MM-DD format.
     """

    metric_code: str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        metric_code = self.metric_code

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if metric_code is not UNSET:
            field_dict["metric_code"] = metric_code
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metric_code = d.pop("metric_code", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        get_ai_report_query_rules_response_data_group_metric_start_date = cls(
            metric_code=metric_code,
            start_date=start_date,
        )


        get_ai_report_query_rules_response_data_group_metric_start_date.additional_properties = d
        return get_ai_report_query_rules_response_data_group_metric_start_date

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
