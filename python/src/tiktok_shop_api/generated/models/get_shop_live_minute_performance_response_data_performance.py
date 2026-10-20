from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shop_live_minute_performance_response_data_performance_interval import GetShopLIVEMinutePerformanceResponseDataPerformanceInterval
  from ..models.get_shop_live_minute_performance_response_data_performance_overall import GetShopLIVEMinutePerformanceResponseDataPerformanceOverall





T = TypeVar("T", bound="GetShopLIVEMinutePerformanceResponseDataPerformance")



@_attrs_define
class GetShopLIVEMinutePerformanceResponseDataPerformance:
    """ 
        Attributes:
            overall (GetShopLIVEMinutePerformanceResponseDataPerformanceOverall | Unset):
            intervals (list[GetShopLIVEMinutePerformanceResponseDataPerformanceInterval] | Unset): Minute-level interval
                data for the LIVE session, including traffic, interactions, conversion, and sales fields. Each page contains up
                to 100 intervals.
     """

    overall: GetShopLIVEMinutePerformanceResponseDataPerformanceOverall | Unset = UNSET
    intervals: list[GetShopLIVEMinutePerformanceResponseDataPerformanceInterval] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_live_minute_performance_response_data_performance_interval import GetShopLIVEMinutePerformanceResponseDataPerformanceInterval # noqa: PLC0415
        from ..models.get_shop_live_minute_performance_response_data_performance_overall import GetShopLIVEMinutePerformanceResponseDataPerformanceOverall # noqa: PLC0415
        overall: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overall, Unset):
            overall = self.overall.to_dict()

        intervals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.intervals, Unset):
            intervals = []
            for intervals_item_data in self.intervals:
                intervals_item = intervals_item_data.to_dict()
                intervals.append(intervals_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if overall is not UNSET:
            field_dict["overall"] = overall
        if intervals is not UNSET:
            field_dict["intervals"] = intervals

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_live_minute_performance_response_data_performance_interval import GetShopLIVEMinutePerformanceResponseDataPerformanceInterval # noqa: PLC0415
        from ..models.get_shop_live_minute_performance_response_data_performance_overall import GetShopLIVEMinutePerformanceResponseDataPerformanceOverall # noqa: PLC0415
        d = dict(src_dict)
        _overall = d.pop("overall", UNSET)
        overall: GetShopLIVEMinutePerformanceResponseDataPerformanceOverall | Unset
        if isinstance(_overall,  Unset):
            overall = UNSET
        else:
            overall = GetShopLIVEMinutePerformanceResponseDataPerformanceOverall.from_dict(_overall)




        _intervals = d.pop("intervals", UNSET)
        intervals: list[GetShopLIVEMinutePerformanceResponseDataPerformanceInterval] | Unset = UNSET
        if _intervals is not UNSET:
            intervals = []
            for intervals_item_data in _intervals:
                intervals_item = GetShopLIVEMinutePerformanceResponseDataPerformanceInterval.from_dict(intervals_item_data)



                intervals.append(intervals_item)


        get_shop_live_minute_performance_response_data_performance = cls(
            overall=overall,
            intervals=intervals,
        )


        get_shop_live_minute_performance_response_data_performance.additional_properties = d
        return get_shop_live_minute_performance_response_data_performance

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
