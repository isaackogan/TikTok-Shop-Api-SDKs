from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_engagement_task_performances_response_data_task_performance import (
        GetEngagementTaskPerformancesResponseDataTaskPerformance,
    )


T = TypeVar("T", bound="GetEngagementTaskPerformancesResponseData")


@_attrs_define
class GetEngagementTaskPerformancesResponseData:
    """
    Attributes:
        task_performances (list[GetEngagementTaskPerformancesResponseDataTaskPerformance] | Unset): The requested list
            of task performance.
    """

    task_performances: list[GetEngagementTaskPerformancesResponseDataTaskPerformance] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_performances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.task_performances, Unset):
            task_performances = []
            for task_performances_item_data in self.task_performances:
                task_performances_item = task_performances_item_data.to_dict()
                task_performances.append(task_performances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_performances is not UNSET:
            field_dict["task_performances"] = task_performances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_engagement_task_performances_response_data_task_performance import (
            GetEngagementTaskPerformancesResponseDataTaskPerformance,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _task_performances = d.pop("task_performances", UNSET)
        task_performances: list[GetEngagementTaskPerformancesResponseDataTaskPerformance] | Unset = UNSET
        if _task_performances is not UNSET:
            task_performances = []
            for task_performances_item_data in _task_performances:
                task_performances_item = GetEngagementTaskPerformancesResponseDataTaskPerformance.from_dict(
                    task_performances_item_data
                )

                task_performances.append(task_performances_item)

        get_engagement_task_performances_response_data = cls(
            task_performances=task_performances,
        )

        get_engagement_task_performances_response_data.additional_properties = d
        return get_engagement_task_performances_response_data

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
