from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point_gmv import GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv





T = TypeVar("T", bound="GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPoint")



@_attrs_define
class GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPoint:
    """ 
        Attributes:
            order_count (int | Unset): Number of created orders for this data point. Returned when `stats_type` is
                `TREND_CREATED_ORDER`.
            timestamp (int | Unset): timestamp
            gmv (GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv | Unset):
     """

    order_count: int | Unset = UNSET
    timestamp: int | Unset = UNSET
    gmv: GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point_gmv import GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv # noqa: PLC0415
        order_count = self.order_count

        timestamp = self.timestamp

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_count is not UNSET:
            field_dict["order_count"] = order_count
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if gmv is not UNSET:
            field_dict["gmv"] = gmv

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point_gmv import GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv # noqa: PLC0415
        d = dict(src_dict)
        order_count = d.pop("order_count", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        _gmv = d.pop("gmv", UNSET)
        gmv: GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv | Unset
        if isinstance(_gmv,  Unset):
            gmv = UNSET
        else:
            gmv = GetLiveRoomGMVAndOrderTrendsResponseDataGmvTrendPerformanceDataPointGmv.from_dict(_gmv)




        get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point = cls(
            order_count=order_count,
            timestamp=timestamp,
            gmv=gmv,
        )


        get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point.additional_properties = d
        return get_live_room_gmv_and_order_trends_response_data_gmv_trend_performance_data_point

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
