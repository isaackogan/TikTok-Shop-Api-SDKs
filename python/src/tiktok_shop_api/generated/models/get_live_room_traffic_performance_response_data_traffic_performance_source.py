from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSource")


@_attrs_define
class GetLiveRoomTrafficPerformanceResponseDataTrafficPerformanceSource:
    """
    Attributes:
        name (str | Unset): The name of the live source
        watch_pv (int | Unset): The live room watch count attributed to the primary traffic source.
    """

    name: str | Unset = UNSET
    watch_pv: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        watch_pv = self.watch_pv

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if watch_pv is not UNSET:
            field_dict["watch_pv"] = watch_pv

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        watch_pv = d.pop("watch_pv", UNSET)

        get_live_room_traffic_performance_response_data_traffic_performance_source = cls(
            name=name,
            watch_pv=watch_pv,
        )

        get_live_room_traffic_performance_response_data_traffic_performance_source.additional_properties = d
        return get_live_room_traffic_performance_response_data_traffic_performance_source

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
