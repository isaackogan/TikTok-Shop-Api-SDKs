from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCouponResponseDataCouponLiveTask")


@_attrs_define
class GetCouponResponseDataCouponLiveTask:
    """
    Attributes:
        type_ (str | Unset): Possible enumerations:
            - `NONE`: Any shopper in the LIVE room may claim the coupon.
            - `FOLLOW_HOST`: Shoppers must follow the LIVE host before being able to claim the coupon.
            - `WATCH_FOR_MIN_TIME`: Shoppers must watch the LIVE for the time specified by `min_watch_time` before being
            able to claim the coupon.
        min_watch_time (str | Unset): Number of seconds for which the shopper must watch the LIVE in order to claim the
            coupon.
    """

    type_: str | Unset = UNSET
    min_watch_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        min_watch_time = self.min_watch_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if min_watch_time is not UNSET:
            field_dict["min_watch_time"] = min_watch_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        min_watch_time = d.pop("min_watch_time", UNSET)

        get_coupon_response_data_coupon_live_task = cls(
            type_=type_,
            min_watch_time=min_watch_time,
        )

        get_coupon_response_data_coupon_live_task.additional_properties = d
        return get_coupon_response_data_coupon_live_task

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
