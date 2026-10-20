from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RedemptionDuration")



@_attrs_define
class RedemptionDuration:
    """ 
        Attributes:
            type_ (str | Unset): Values:
                - `ABSOLUTE`: the redemption period starts from `start_time` and ends at `end_time`.
                - `RELATIVE`: the redemption period starts from the time the coupon is claimed and lasts for `relative_time`.
            start_time (int | Unset): The UNIX timestamp, in seconds, at which the redemption period starts, if `type ==
                'ABSOLUTE'`.
            end_time (int | Unset): The UNIX timestamp, in seconds, at which the redemption period ends, if `type ==
                'ABSOLUTE'`.
            relative_time (int | Unset): The number of days after coupon claim time for which a coupon is valid to be
                redeemed, `type = 'RELATIVE'`.
     """

    type_: str | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    relative_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        start_time = self.start_time

        end_time = self.end_time

        relative_time = self.relative_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if relative_time is not UNSET:
            field_dict["relative_time"] = relative_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        relative_time = d.pop("relative_time", UNSET)

        redemption_duration = cls(
            type_=type_,
            start_time=start_time,
            end_time=end_time,
            relative_time=relative_time,
        )


        redemption_duration.additional_properties = d
        return redemption_duration

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
