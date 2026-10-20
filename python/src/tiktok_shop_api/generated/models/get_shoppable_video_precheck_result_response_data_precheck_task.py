from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shoppable_video_precheck_result_response_data_precheck_task_good_quality_check_result import (
        GetShoppableVideoPrecheckResultResponseDataPrecheckTaskGoodQualityCheckResult,
    )
    from ..models.get_shoppable_video_precheck_result_response_data_precheck_task_violation_check_result import (
        GetShoppableVideoPrecheckResultResponseDataPrecheckTaskViolationCheckResult,
    )


T = TypeVar("T", bound="GetShoppableVideoPrecheckResultResponseDataPrecheckTask")


@_attrs_define
class GetShoppableVideoPrecheckResultResponseDataPrecheckTask:
    """
    Attributes:
        id (str | Unset): The id of the video pre-check task.
        violation_check_result (GetShoppableVideoPrecheckResultResponseDataPrecheckTaskViolationCheckResult | Unset):
        good_quality_check_result (GetShoppableVideoPrecheckResultResponseDataPrecheckTaskGoodQualityCheckResult |
            Unset):
    """

    id: str | Unset = UNSET
    violation_check_result: GetShoppableVideoPrecheckResultResponseDataPrecheckTaskViolationCheckResult | Unset = UNSET
    good_quality_check_result: GetShoppableVideoPrecheckResultResponseDataPrecheckTaskGoodQualityCheckResult | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        violation_check_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.violation_check_result, Unset):
            violation_check_result = self.violation_check_result.to_dict()

        good_quality_check_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.good_quality_check_result, Unset):
            good_quality_check_result = self.good_quality_check_result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if violation_check_result is not UNSET:
            field_dict["violation_check_result"] = violation_check_result
        if good_quality_check_result is not UNSET:
            field_dict["good_quality_check_result"] = good_quality_check_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shoppable_video_precheck_result_response_data_precheck_task_good_quality_check_result import (
            GetShoppableVideoPrecheckResultResponseDataPrecheckTaskGoodQualityCheckResult,  # noqa: PLC0415
        )
        from ..models.get_shoppable_video_precheck_result_response_data_precheck_task_violation_check_result import (
            GetShoppableVideoPrecheckResultResponseDataPrecheckTaskViolationCheckResult,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _violation_check_result = d.pop("violation_check_result", UNSET)
        violation_check_result: GetShoppableVideoPrecheckResultResponseDataPrecheckTaskViolationCheckResult | Unset
        if isinstance(_violation_check_result, Unset):
            violation_check_result = UNSET
        else:
            violation_check_result = (
                GetShoppableVideoPrecheckResultResponseDataPrecheckTaskViolationCheckResult.from_dict(
                    _violation_check_result
                )
            )

        _good_quality_check_result = d.pop("good_quality_check_result", UNSET)
        good_quality_check_result: GetShoppableVideoPrecheckResultResponseDataPrecheckTaskGoodQualityCheckResult | Unset
        if isinstance(_good_quality_check_result, Unset):
            good_quality_check_result = UNSET
        else:
            good_quality_check_result = (
                GetShoppableVideoPrecheckResultResponseDataPrecheckTaskGoodQualityCheckResult.from_dict(
                    _good_quality_check_result
                )
            )

        get_shoppable_video_precheck_result_response_data_precheck_task = cls(
            id=id,
            violation_check_result=violation_check_result,
            good_quality_check_result=good_quality_check_result,
        )

        get_shoppable_video_precheck_result_response_data_precheck_task.additional_properties = d
        return get_shoppable_video_precheck_result_response_data_precheck_task

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
