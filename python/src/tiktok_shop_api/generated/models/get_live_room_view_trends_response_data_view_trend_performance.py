from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.data_point import DataPoint





T = TypeVar("T", bound="GetLiveRoomViewTrendsResponseDataViewTrendPerformance")



@_attrs_define
class GetLiveRoomViewTrendsResponseDataViewTrendPerformance:
    """ 
        Attributes:
            stats_type (str | Unset): The viewer trend category.
                TREND_ONLINE_VIEWER: Viewers who are watching the live streaming room.
                TREND_ENTER_VIEWER: Viewers who enter the live streaming room.
                TREND_LEFT_VIEWER: Viewers who left the live streaming room.
            data_points (list[DataPoint] | Unset): Viewer count data points for the corresponding trend category.
     """

    stats_type: str | Unset = UNSET
    data_points: list[DataPoint] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.data_point import DataPoint # noqa: PLC0415
        stats_type = self.stats_type

        data_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_points, Unset):
            data_points = []
            for data_points_item_data in self.data_points:
                data_points_item = data_points_item_data.to_dict()
                data_points.append(data_points_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if stats_type is not UNSET:
            field_dict["stats_type"] = stats_type
        if data_points is not UNSET:
            field_dict["data_points"] = data_points

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_point import DataPoint # noqa: PLC0415
        d = dict(src_dict)
        stats_type = d.pop("stats_type", UNSET)

        _data_points = d.pop("data_points", UNSET)
        data_points: list[DataPoint] | Unset = UNSET
        if _data_points is not UNSET:
            data_points = []
            for data_points_item_data in _data_points:
                data_points_item = DataPoint.from_dict(data_points_item_data)



                data_points.append(data_points_item)


        get_live_room_view_trends_response_data_view_trend_performance = cls(
            stats_type=stats_type,
            data_points=data_points,
        )


        get_live_room_view_trends_response_data_view_trend_performance.additional_properties = d
        return get_live_room_view_trends_response_data_view_trend_performance

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
