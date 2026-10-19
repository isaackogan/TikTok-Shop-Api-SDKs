from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchOpenCollaborationsResponseDataOpenCollaborationCurrentCommission")


@_attrs_define
class SearchOpenCollaborationsResponseDataOpenCollaborationCurrentCommission:
    """
    Attributes:
        rate (int | Unset): The commission rate for this product is set by merchants for creators' public promotion.
            The range of this value is [100, 8000].
            This value is expressed in 1/10000 increments. For example: 3000 means the actual commission rate is 30.00%, and
            3555 means 35.55%
        start_time (int | Unset): The Unix timestamp, in seconds, when the commission rate becomes effective.
        end_time (int | Unset): The Unix timestamp, in seconds, when the commission rate stops being effective.
    """

    rate: int | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate = self.rate

        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate is not UNSET:
            field_dict["rate"] = rate
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate", UNSET)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        search_open_collaborations_response_data_open_collaboration_current_commission = cls(
            rate=rate,
            start_time=start_time,
            end_time=end_time,
        )

        search_open_collaborations_response_data_open_collaboration_current_commission.additional_properties = d
        return search_open_collaborations_response_data_open_collaboration_current_commission

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
