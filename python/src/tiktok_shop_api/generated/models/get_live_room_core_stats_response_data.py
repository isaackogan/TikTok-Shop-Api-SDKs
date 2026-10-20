from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_live_room_core_stats_response_data_stat import GetLiveRoomCoreStatsResponseDataStat


T = TypeVar("T", bound="GetLiveRoomCoreStatsResponseData")


@_attrs_define
class GetLiveRoomCoreStatsResponseData:
    """
    Attributes:
        stats (GetLiveRoomCoreStatsResponseDataStat | Unset):
    """

    stats: GetLiveRoomCoreStatsResponseDataStat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_live_room_core_stats_response_data_stat import (
            GetLiveRoomCoreStatsResponseDataStat,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _stats = d.pop("stats", UNSET)
        stats: GetLiveRoomCoreStatsResponseDataStat | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = GetLiveRoomCoreStatsResponseDataStat.from_dict(_stats)

        get_live_room_core_stats_response_data = cls(
            stats=stats,
        )

        get_live_room_core_stats_response_data.additional_properties = d
        return get_live_room_core_stats_response_data

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
