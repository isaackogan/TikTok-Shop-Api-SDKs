from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShoppableVideoPrecheckResultResponseDataPrecheckTaskViolationCheckResultIssue")


@_attrs_define
class GetShoppableVideoPrecheckResultResponseDataPrecheckTaskViolationCheckResultIssue:
    """
    Attributes:
        risk (str | Unset): Policy violation
        suggestions (str | Unset): Detailed guidance to resolve the detected violation.
    """

    risk: str | Unset = UNSET
    suggestions: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        risk = self.risk

        suggestions = self.suggestions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if risk is not UNSET:
            field_dict["risk"] = risk
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        risk = d.pop("risk", UNSET)

        suggestions = d.pop("suggestions", UNSET)

        get_shoppable_video_precheck_result_response_data_precheck_task_violation_check_result_issue = cls(
            risk=risk,
            suggestions=suggestions,
        )

        get_shoppable_video_precheck_result_response_data_precheck_task_violation_check_result_issue.additional_properties = d
        return get_shoppable_video_precheck_result_response_data_precheck_task_violation_check_result_issue

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
