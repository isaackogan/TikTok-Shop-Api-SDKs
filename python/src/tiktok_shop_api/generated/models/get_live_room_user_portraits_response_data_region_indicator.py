from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLiveRoomUserPortraitsResponseDataRegionIndicator")


@_attrs_define
class GetLiveRoomUserPortraitsResponseDataRegionIndicator:
    """
    Attributes:
        value (str | Unset): The share for the corresponding indicator, scaled by 10,000. Divide by 10,000 to obtain the
            underlying proportion.
        type_ (str | Unset): The country of indicators
    """

    value: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value", UNSET)

        type_ = d.pop("type", UNSET)

        get_live_room_user_portraits_response_data_region_indicator = cls(
            value=value,
            type_=type_,
        )

        get_live_room_user_portraits_response_data_region_indicator.additional_properties = d
        return get_live_room_user_portraits_response_data_region_indicator

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
