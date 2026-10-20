from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shoppable_video_precheck_tasks_result_webhook_data_violation_check_result_issue import (
        ShoppableVideoPrecheckTasksResultWebhookDataViolationCheckResultIssue,
    )


T = TypeVar("T", bound="ShoppableVideoPrecheckTasksResultWebhookDataViolationCheckResult")


@_attrs_define
class ShoppableVideoPrecheckTasksResultWebhookDataViolationCheckResult:
    """
    Attributes:
        status (str | Unset): Possible enumerations:
             `SUCCESS`
             `FAIL`
             `PROCESSING`
        issues (list[ShoppableVideoPrecheckTasksResultWebhookDataViolationCheckResultIssue] | Unset):
    """

    status: str | Unset = UNSET
    issues: list[ShoppableVideoPrecheckTasksResultWebhookDataViolationCheckResultIssue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        issues: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = []
            for issues_item_data in self.issues:
                issues_item = issues_item_data.to_dict()
                issues.append(issues_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if issues is not UNSET:
            field_dict["issues"] = issues

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shoppable_video_precheck_tasks_result_webhook_data_violation_check_result_issue import (
            ShoppableVideoPrecheckTasksResultWebhookDataViolationCheckResultIssue,  # noqa: PLC0415
        )

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        _issues = d.pop("issues", UNSET)
        issues: list[ShoppableVideoPrecheckTasksResultWebhookDataViolationCheckResultIssue] | Unset = UNSET
        if _issues is not UNSET:
            issues = []
            for issues_item_data in _issues:
                issues_item = ShoppableVideoPrecheckTasksResultWebhookDataViolationCheckResultIssue.from_dict(
                    issues_item_data
                )

                issues.append(issues_item)

        shoppable_video_precheck_tasks_result_webhook_data_violation_check_result = cls(
            status=status,
            issues=issues,
        )

        shoppable_video_precheck_tasks_result_webhook_data_violation_check_result.additional_properties = d
        return shoppable_video_precheck_tasks_result_webhook_data_violation_check_result

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
