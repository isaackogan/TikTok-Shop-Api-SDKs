from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance import GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformance





T = TypeVar("T", bound="GetLiveRoomGMVAndOrderTrendsResponseData")



@_attrs_define
class GetLiveRoomGMVAndOrderTrendsResponseData:
    """ 
        Attributes:
            gmv_trend_performances (list[GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformance] | Unset): GMV and
                created-order trend series for the live room. Each item identifies one metric through `stats_type`.
     """

    gmv_trend_performances: list[GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformance] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance import GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformance # noqa: PLC0415
        gmv_trend_performances: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gmv_trend_performances, Unset):
            gmv_trend_performances = []
            for gmv_trend_performances_item_data in self.gmv_trend_performances:
                gmv_trend_performances_item = gmv_trend_performances_item_data.to_dict()
                gmv_trend_performances.append(gmv_trend_performances_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if gmv_trend_performances is not UNSET:
            field_dict["gmv_trend_performances"] = gmv_trend_performances

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance import GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformance # noqa: PLC0415
        d = dict(src_dict)
        _gmv_trend_performances = d.pop("gmv_trend_performances", UNSET)
        gmv_trend_performances: list[GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformance] | Unset = UNSET
        if _gmv_trend_performances is not UNSET:
            gmv_trend_performances = []
            for gmv_trend_performances_item_data in _gmv_trend_performances:
                gmv_trend_performances_item = GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformance.from_dict(gmv_trend_performances_item_data)



                gmv_trend_performances.append(gmv_trend_performances_item)


        get_live_room_gmv_and_order_trends_response_data = cls(
            gmv_trend_performances=gmv_trend_performances,
        )


        get_live_room_gmv_and_order_trends_response_data.additional_properties = d
        return get_live_room_gmv_and_order_trends_response_data

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
