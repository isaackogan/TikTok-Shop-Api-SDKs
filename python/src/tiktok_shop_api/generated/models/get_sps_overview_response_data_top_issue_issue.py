from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetSPSOverviewResponseDataTopIssueIssue")



@_attrs_define
class GetSPSOverviewResponseDataTopIssueIssue:
    """ 
        Attributes:
            description (str | Unset): Localized issue description.
            evaluate_duration_days (int | Unset): Number of days included in this issue's evaluation period.
            end_evaluation_time (int | Unset): Issue evaluation period end time. Unix timestamp in seconds.
            start_evaluation_time (int | Unset): Issue evaluation period start time. Unix timestamp in seconds.
            metric_code (str | Unset): Related metric code. Possible values include NRR, NBFR, SFCR, OTDR, AHT, and IM_DSAT.
            metric_name (str | Unset): Localized metric display name.
            percentile (str | Unset): Metric percentile among peer shops, from 0 to 100.
            rank (int | Unset): Issue rank, where 1 is the top issue.
     """

    description: str | Unset = UNSET
    evaluate_duration_days: int | Unset = UNSET
    end_evaluation_time: int | Unset = UNSET
    start_evaluation_time: int | Unset = UNSET
    metric_code: str | Unset = UNSET
    metric_name: str | Unset = UNSET
    percentile: str | Unset = UNSET
    rank: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        evaluate_duration_days = self.evaluate_duration_days

        end_evaluation_time = self.end_evaluation_time

        start_evaluation_time = self.start_evaluation_time

        metric_code = self.metric_code

        metric_name = self.metric_name

        percentile = self.percentile

        rank = self.rank


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
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
        if percentile is not UNSET:
            field_dict["percentile"] = percentile
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        evaluate_duration_days = d.pop("evaluate_duration_days", UNSET)

        end_evaluation_time = d.pop("end_evaluation_time", UNSET)

        start_evaluation_time = d.pop("start_evaluation_time", UNSET)

        metric_code = d.pop("metric_code", UNSET)

        metric_name = d.pop("metric_name", UNSET)

        percentile = d.pop("percentile", UNSET)

        rank = d.pop("rank", UNSET)

        get_sps_overview_response_data_top_issue_issue = cls(
            description=description,
            evaluate_duration_days=evaluate_duration_days,
            end_evaluation_time=end_evaluation_time,
            start_evaluation_time=start_evaluation_time,
            metric_code=metric_code,
            metric_name=metric_name,
            percentile=percentile,
            rank=rank,
        )


        get_sps_overview_response_data_top_issue_issue.additional_properties = d
        return get_sps_overview_response_data_top_issue_issue

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
