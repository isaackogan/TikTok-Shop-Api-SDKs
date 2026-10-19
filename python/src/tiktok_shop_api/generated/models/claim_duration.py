from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClaimDuration")


@_attrs_define
class ClaimDuration:
    """
    Attributes:
        start_time (int | Unset): The UNIX timestamp, in seconds, from which a shopper can claim the coupon.
        end_time (int | Unset): The UNIX timestamp, in seconds, after which a shopper can no longer claim the coupon.
    """

    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        claim_duration = cls(
            start_time=start_time,
            end_time=end_time,
        )

        claim_duration.additional_properties = d
        return claim_duration

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
