from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetEngagementTaskPerformancesRequest")


@_attrs_define
class GetEngagementTaskPerformancesRequest:
    """
    Attributes:
        task_ids (list[str]): The customer engagement task IDs for which to retrieve performance data. Provide 1 to 50
            IDs; each ID must be a base-10 string that fits in a signed 64-bit integer.
    """

    task_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_ids = self.task_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_ids": task_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_ids = cast(list[str], d.pop("task_ids"))

        get_engagement_task_performances_request = cls(
            task_ids=task_ids,
        )

        get_engagement_task_performances_request.additional_properties = d
        return get_engagement_task_performances_request

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
