from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_shop_video_performance_list_response_data_video import GetShopVideoPerformanceListResponseDataVideo





T = TypeVar("T", bound="GetShopVideoPerformanceListResponseData")



@_attrs_define
class GetShopVideoPerformanceListResponseData:
    """ 
        Attributes:
            latest_available_date (datetime.date | Unset): Latest date in local timezone where data is ready (ISO 8601
                format).
            next_page_token (str | Unset): Page token for the next page request. Pass a nonempty returned token as
                `page_token` in the next request and reuse the same `start_date_ge`, `end_date_lt`, `sort_field`, `sort_order`,
                `currency`, `account_type`, and `page_size` values. An empty value means there are no more pages.
            total_count (int | Unset): Total number of videos matching the request filters across all pages.
            videos (list[GetShopVideoPerformanceListResponseDataVideo] | Unset): List of video performance metrics.
     """

    latest_available_date: datetime.date | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    videos: list[GetShopVideoPerformanceListResponseDataVideo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_video_performance_list_response_data_video import GetShopVideoPerformanceListResponseDataVideo # noqa: PLC0415
        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()

        next_page_token = self.next_page_token

        total_count = self.total_count

        videos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.videos, Unset):
            videos = []
            for videos_item_data in self.videos:
                videos_item = videos_item_data.to_dict()
                videos.append(videos_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if videos is not UNSET:
            field_dict["videos"] = videos

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_video_performance_list_response_data_video import GetShopVideoPerformanceListResponseDataVideo # noqa: PLC0415
        d = dict(src_dict)
        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date,  Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)




        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        _videos = d.pop("videos", UNSET)
        videos: list[GetShopVideoPerformanceListResponseDataVideo] | Unset = UNSET
        if _videos is not UNSET:
            videos = []
            for videos_item_data in _videos:
                videos_item = GetShopVideoPerformanceListResponseDataVideo.from_dict(videos_item_data)



                videos.append(videos_item)


        get_shop_video_performance_list_response_data = cls(
            latest_available_date=latest_available_date,
            next_page_token=next_page_token,
            total_count=total_count,
            videos=videos,
        )


        get_shop_video_performance_list_response_data.additional_properties = d
        return get_shop_video_performance_list_response_data

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
