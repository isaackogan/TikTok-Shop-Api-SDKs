from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="VideoPrecheckResultWebhookDataIssue")



@_attrs_define
class VideoPrecheckResultWebhookDataIssue:
    """ 
        Attributes:
            risk (str | Unset): Risk type.
            suggestion (str | Unset): Suggestions on how to fix the risk.
     """

    risk: str | Unset = UNSET
    suggestion: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        risk = self.risk

        suggestion = self.suggestion


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if risk is not UNSET:
            field_dict["risk"] = risk
        if suggestion is not UNSET:
            field_dict["suggestion"] = suggestion

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        risk = d.pop("risk", UNSET)

        suggestion = d.pop("suggestion", UNSET)

        video_precheck_result_webhook_data_issue = cls(
            risk=risk,
            suggestion=suggestion,
        )


        video_precheck_result_webhook_data_issue.additional_properties = d
        return video_precheck_result_webhook_data_issue

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
