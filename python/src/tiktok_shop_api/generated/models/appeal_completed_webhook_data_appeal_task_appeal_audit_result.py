from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppealCompletedWebhookDataAppealTaskAppealAuditResult")


@_attrs_define
class AppealCompletedWebhookDataAppealTaskAppealAuditResult:
    """
    Attributes:
        indicator_type (str):
        status (str):
        reject_reason (str | Unset):
    """

    indicator_type: str
    status: str
    reject_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        indicator_type = self.indicator_type

        status = self.status

        reject_reason = self.reject_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "indicator_type": indicator_type,
                "status": status,
            }
        )
        if reject_reason is not UNSET:
            field_dict["reject_reason"] = reject_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        indicator_type = d.pop("indicator_type")

        status = d.pop("status")

        reject_reason = d.pop("reject_reason", UNSET)

        appeal_completed_webhook_data_appeal_task_appeal_audit_result = cls(
            indicator_type=indicator_type,
            status=status,
            reject_reason=reject_reason,
        )

        appeal_completed_webhook_data_appeal_task_appeal_audit_result.additional_properties = d
        return appeal_completed_webhook_data_appeal_task_appeal_audit_result

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
