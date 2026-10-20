from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_sps_overview_response_data_top_issue_issue import GetSPSOverviewResponseDataTopIssueIssue


T = TypeVar("T", bound="GetSPSOverviewResponseDataTopIssue")


@_attrs_define
class GetSPSOverviewResponseDataTopIssue:
    """
    Attributes:
        issues (list[GetSPSOverviewResponseDataTopIssueIssue] | Unset): Ranked issue list.
        summary (str | Unset): Localized summary of the top issues.
    """

    issues: list[GetSPSOverviewResponseDataTopIssueIssue] | Unset = UNSET
    summary: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()
                issues.append(issues_item)

        summary = self.summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issues is not UNSET:
            field_dict["issues"] = issues
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sps_overview_response_data_top_issue_issue import (
            GetSPSOverviewResponseDataTopIssueIssue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _issues = d.pop("issues", UNSET)
        issues: list[GetSPSOverviewResponseDataTopIssueIssue] | Unset = UNSET
        if _issues is not UNSET:
            issues = []
            for issues_item_data in _issues:
                issues_item = GetSPSOverviewResponseDataTopIssueIssue.from_dict(issues_item_data)

                issues.append(issues_item)

        summary = d.pop("summary", UNSET)

        get_sps_overview_response_data_top_issue = cls(
            issues=issues,
            summary=summary,
        )

        get_sps_overview_response_data_top_issue.additional_properties = d
        return get_sps_overview_response_data_top_issue

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
