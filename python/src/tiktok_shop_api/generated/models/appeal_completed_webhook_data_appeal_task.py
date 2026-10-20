from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.appeal_completed_webhook_data_appeal_task_appeal_audit_result import AppealCompletedWebhookDataAppealTaskAppealAuditResult





T = TypeVar("T", bound="AppealCompletedWebhookDataAppealTask")



@_attrs_define
class AppealCompletedWebhookDataAppealTask:
    """ 
        Attributes:
            appeal_audit_result (list[AppealCompletedWebhookDataAppealTaskAppealAuditResult]):
            size_chart_id (int | Unset):
            size_chart_image_uri (str | Unset):
     """

    appeal_audit_result: list[AppealCompletedWebhookDataAppealTaskAppealAuditResult]
    size_chart_id: int | Unset = UNSET
    size_chart_image_uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.appeal_completed_webhook_data_appeal_task_appeal_audit_result import AppealCompletedWebhookDataAppealTaskAppealAuditResult # noqa: PLC0415
        appeal_audit_result = []
        for appeal_audit_result_item_data in self.appeal_audit_result:
            appeal_audit_result_item = appeal_audit_result_item_data.to_dict()
            appeal_audit_result.append(appeal_audit_result_item)



        size_chart_id = self.size_chart_id

        size_chart_image_uri = self.size_chart_image_uri


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "appeal_audit_result": appeal_audit_result,
        })
        if size_chart_id is not UNSET:
            field_dict["size_chart_id"] = size_chart_id
        if size_chart_image_uri is not UNSET:
            field_dict["size_chart_image_uri"] = size_chart_image_uri

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.appeal_completed_webhook_data_appeal_task_appeal_audit_result import AppealCompletedWebhookDataAppealTaskAppealAuditResult # noqa: PLC0415
        d = dict(src_dict)
        appeal_audit_result = []
        _appeal_audit_result = d.pop("appeal_audit_result")
        for appeal_audit_result_item_data in (_appeal_audit_result):
            appeal_audit_result_item = AppealCompletedWebhookDataAppealTaskAppealAuditResult.from_dict(appeal_audit_result_item_data)



            appeal_audit_result.append(appeal_audit_result_item)


        size_chart_id = d.pop("size_chart_id", UNSET)

        size_chart_image_uri = d.pop("size_chart_image_uri", UNSET)

        appeal_completed_webhook_data_appeal_task = cls(
            appeal_audit_result=appeal_audit_result,
            size_chart_id=size_chart_id,
            size_chart_image_uri=size_chart_image_uri,
        )


        appeal_completed_webhook_data_appeal_task.additional_properties = d
        return appeal_completed_webhook_data_appeal_task

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
