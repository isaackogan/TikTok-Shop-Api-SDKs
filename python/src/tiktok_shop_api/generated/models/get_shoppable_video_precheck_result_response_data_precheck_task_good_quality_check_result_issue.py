from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetShoppableVideoPrecheckResultResponseDataPrecheckTaskGoodQualityCheckResultIssue")



@_attrs_define
class GetShoppableVideoPrecheckResultResponseDataPrecheckTaskGoodQualityCheckResultIssue:
    """ 
        Attributes:
            code (str | Unset): Quality finding
            suggestions (str | Unset): Recommended improvements based on the quality finding.
     """

    code: str | Unset = UNSET
    suggestions: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        suggestions = self.suggestions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        suggestions = d.pop("suggestions", UNSET)

        get_shoppable_video_precheck_result_response_data_precheck_task_good_quality_check_result_issue = cls(
            code=code,
            suggestions=suggestions,
        )


        get_shoppable_video_precheck_result_response_data_precheck_task_good_quality_check_result_issue.additional_properties = d
        return get_shoppable_video_precheck_result_response_data_precheck_task_good_quality_check_result_issue

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
