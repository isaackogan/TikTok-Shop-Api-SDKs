from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_live_room_view_trends_response_data_view_trend_performance import GetLiveRoomViewTrendsResponseDataViewTrendPerformance





T = TypeVar("T", bound="GetLiveRoomViewTrendsResponseData")



@_attrs_define
class GetLiveRoomViewTrendsResponseData:
    """ 
        Attributes:
            view_trend_performances (list[GetLiveRoomViewTrendsResponseDataViewTrendPerformance] | Unset): Viewer count
                trends of the live streaming room
     """

    view_trend_performances: list[GetLiveRoomViewTrendsResponseDataViewTrendPerformance] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_live_room_view_trends_response_data_view_trend_performance import GetLiveRoomViewTrendsResponseDataViewTrendPerformance # noqa: PLC0415
        view_trend_performances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.view_trend_performances, Unset):
            view_trend_performances = []
            for view_trend_performances_item_data in self.view_trend_performances:
                view_trend_performances_item = view_trend_performances_item_data.to_dict()
                view_trend_performances.append(view_trend_performances_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if view_trend_performances is not UNSET:
            field_dict["view_trend_performances"] = view_trend_performances

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_live_room_view_trends_response_data_view_trend_performance import GetLiveRoomViewTrendsResponseDataViewTrendPerformance # noqa: PLC0415
        d = dict(src_dict)
        _view_trend_performances = d.pop("view_trend_performances", UNSET)
        view_trend_performances: list[GetLiveRoomViewTrendsResponseDataViewTrendPerformance] | Unset = UNSET
        if _view_trend_performances is not UNSET:
            view_trend_performances = []
            for view_trend_performances_item_data in _view_trend_performances:
                view_trend_performances_item = GetLiveRoomViewTrendsResponseDataViewTrendPerformance.from_dict(view_trend_performances_item_data)



                view_trend_performances.append(view_trend_performances_item)


        get_live_room_view_trends_response_data = cls(
            view_trend_performances=view_trend_performances,
        )


        get_live_room_view_trends_response_data.additional_properties = d
        return get_live_room_view_trends_response_data

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
