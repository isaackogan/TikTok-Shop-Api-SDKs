from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PendingRegistrationStatistic")



@_attrs_define
class PendingRegistrationStatistic:
    """ 
        Attributes:
            has_pending_registrations (bool | Unset): Whether any registrations await seller confirmation. Omitted if no
                conclusion is available.
            processed_count (int | Unset): Nonnegative number of processed items in the same confirmation workflow. Omitted
                if unavailable. Does not count approved registrations or successful participation.
            total_count (int | Unset): Nonnegative total in the pending-confirmation workflow, including processed items.
                Omitted if unavailable. Not the number of remaining items.
     """

    has_pending_registrations: bool | Unset = UNSET
    processed_count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        has_pending_registrations = self.has_pending_registrations

        processed_count = self.processed_count

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if has_pending_registrations is not UNSET:
            field_dict["has_pending_registrations"] = has_pending_registrations
        if processed_count is not UNSET:
            field_dict["processed_count"] = processed_count
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_pending_registrations = d.pop("has_pending_registrations", UNSET)

        processed_count = d.pop("processed_count", UNSET)

        total_count = d.pop("total_count", UNSET)

        pending_registration_statistic = cls(
            has_pending_registrations=has_pending_registrations,
            processed_count=processed_count,
            total_count=total_count,
        )


        pending_registration_statistic.additional_properties = d
        return pending_registration_statistic

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
