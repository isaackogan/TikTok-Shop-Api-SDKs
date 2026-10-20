from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLiveRoomUserPortraitsResponseDataAllFanIndicator")


@_attrs_define
class GetLiveRoomUserPortraitsResponseDataAllFanIndicator:
    """
    Attributes:
        type_ (str | Unset): The stats_type describes the type of value below.

            USER_PORTRAIT_FOLLOWER: The user portrait of the follower

            USER_PORTRAIT_NON_FOLLOWER: The user portrait of the non follower
        value (str | Unset): The count for the corresponding follower-status indicator.
    """

    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        get_live_room_user_portraits_response_data_all_fan_indicator = cls(
            type_=type_,
            value=value,
        )

        get_live_room_user_portraits_response_data_all_fan_indicator.additional_properties = d
        return get_live_room_user_portraits_response_data_all_fan_indicator

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
