from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gmv import Gmv





T = TypeVar("T", bound="GetShopLIVEMinutePerformanceResponseDataPerformanceOverall")



@_attrs_define
class GetShopLIVEMinutePerformanceResponseDataPerformanceOverall:
    """ 
        Attributes:
            live_title (str | Unset): LIVE session title
            start_time (int | Unset): Start time of the LIVE session as a Unix timestamp in seconds (UTC).
            end_time (int | Unset): End time of the LIVE session as a Unix timestamp in seconds (UTC).
            duration (int | Unset): LIVE session duration in seconds
            gmv (Gmv | Unset):
            items_sold (int | Unset): The number of items sold directly from the LIVE.
            unique_viewers (int | Unset): The number of unique viewers in the LIVE room.
            impressions (int | Unset): The total number of times the LIVE was displayed to viewers.
     """

    live_title: str | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    duration: int | Unset = UNSET
    gmv: Gmv | Unset = UNSET
    items_sold: int | Unset = UNSET
    unique_viewers: int | Unset = UNSET
    impressions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gmv import Gmv # noqa: PLC0415
        live_title = self.live_title

        start_time = self.start_time

        end_time = self.end_time

        duration = self.duration

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        items_sold = self.items_sold

        unique_viewers = self.unique_viewers

        impressions = self.impressions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if live_title is not UNSET:
            field_dict["live_title"] = live_title
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if duration is not UNSET:
            field_dict["duration"] = duration
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold
        if unique_viewers is not UNSET:
            field_dict["unique_viewers"] = unique_viewers
        if impressions is not UNSET:
            field_dict["impressions"] = impressions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gmv import Gmv # noqa: PLC0415
        d = dict(src_dict)
        live_title = d.pop("live_title", UNSET)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        duration = d.pop("duration", UNSET)

        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv,  Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)




        items_sold = d.pop("items_sold", UNSET)

        unique_viewers = d.pop("unique_viewers", UNSET)

        impressions = d.pop("impressions", UNSET)

        get_shop_live_minute_performance_response_data_performance_overall = cls(
            live_title=live_title,
            start_time=start_time,
            end_time=end_time,
            duration=duration,
            gmv=gmv,
            items_sold=items_sold,
            unique_viewers=unique_viewers,
            impressions=impressions,
        )


        get_shop_live_minute_performance_response_data_performance_overall.additional_properties = d
        return get_shop_live_minute_performance_response_data_performance_overall

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
