from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HandlingDuration")


@_attrs_define
class HandlingDuration:
    """
    Attributes:
        days (str | Unset): The number of days.
        type_ (str | Unset): Indicates if the duration is calculated in calendar days or business days.
            Possible values:
            - `CALENDAR_DAY`: Represents consecutive days, including weekends and holidays.
            - `BUSINESS_DAY`: Represents business days, excluding weekends and public holidays.
            Default: `BUSINESS_DAY`
    """

    days: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        days = self.days

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if days is not UNSET:
            field_dict["days"] = days
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        days = d.pop("days", UNSET)

        type_ = d.pop("type", UNSET)

        handling_duration = cls(
            days=days,
            type_=type_,
        )

        handling_duration.additional_properties = d
        return handling_duration

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
