from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_live_room_interactive_trends_response_data_interactive_trend_performance import (
        GetLiveRoomInteractiveTrendsResponseDataInteractiveTrendPerformance,
    )


T = TypeVar("T", bound="GetLiveRoomInteractiveTrendsResponseData")


@_attrs_define
class GetLiveRoomInteractiveTrendsResponseData:
    """
    Attributes:
        interactive_trend_performances (list[GetLiveRoomInteractiveTrendsResponseDataInteractiveTrendPerformance] |
            Unset): The trend data of living room
    """

    interactive_trend_performances: (
        list[GetLiveRoomInteractiveTrendsResponseDataInteractiveTrendPerformance] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interactive_trend_performances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interactive_trend_performances, Unset):
            interactive_trend_performances = []
            for interactive_trend_performances_item_data in self.interactive_trend_performances:
                interactive_trend_performances_item = interactive_trend_performances_item_data.to_dict()
                interactive_trend_performances.append(interactive_trend_performances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interactive_trend_performances is not UNSET:
            field_dict["interactive_trend_performances"] = interactive_trend_performances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_live_room_interactive_trends_response_data_interactive_trend_performance import (
            GetLiveRoomInteractiveTrendsResponseDataInteractiveTrendPerformance,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _interactive_trend_performances = d.pop("interactive_trend_performances", UNSET)
        interactive_trend_performances: (
            list[GetLiveRoomInteractiveTrendsResponseDataInteractiveTrendPerformance] | Unset
        ) = UNSET
        if _interactive_trend_performances is not UNSET:
            interactive_trend_performances = []
            for interactive_trend_performances_item_data in _interactive_trend_performances:
                interactive_trend_performances_item = (
                    GetLiveRoomInteractiveTrendsResponseDataInteractiveTrendPerformance.from_dict(
                        interactive_trend_performances_item_data
                    )
                )

                interactive_trend_performances.append(interactive_trend_performances_item)

        get_live_room_interactive_trends_response_data = cls(
            interactive_trend_performances=interactive_trend_performances,
        )

        get_live_room_interactive_trends_response_data.additional_properties = d
        return get_live_room_interactive_trends_response_data

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
