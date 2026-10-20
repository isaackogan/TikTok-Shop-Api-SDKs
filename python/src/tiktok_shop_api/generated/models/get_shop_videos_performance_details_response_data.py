from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_videos_performance_details_response_data_video import (
        GetShopVideosPerformanceDetailsResponseDataVideo,
    )


T = TypeVar("T", bound="GetShopVideosPerformanceDetailsResponseData")


@_attrs_define
class GetShopVideosPerformanceDetailsResponseData:
    """
    Attributes:
        latest_available_date (datetime.date | Unset): Latest date in local timezone where data is ready (ISO 8601
            format).
        videos (list[GetShopVideosPerformanceDetailsResponseDataVideo] | Unset): Performance details for the requested
            videos.
    """

    latest_available_date: datetime.date | Unset = UNSET
    videos: list[GetShopVideosPerformanceDetailsResponseDataVideo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()

        videos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.videos, Unset):
            videos = []
            for videos_item_data in self.videos:
                videos_item = videos_item_data.to_dict()
                videos.append(videos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date
        if videos is not UNSET:
            field_dict["videos"] = videos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_videos_performance_details_response_data_video import (
            GetShopVideosPerformanceDetailsResponseDataVideo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date, Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)

        _videos = d.pop("videos", UNSET)
        videos: list[GetShopVideosPerformanceDetailsResponseDataVideo] | Unset = UNSET
        if _videos is not UNSET:
            videos = []
            for videos_item_data in _videos:
                videos_item = GetShopVideosPerformanceDetailsResponseDataVideo.from_dict(videos_item_data)

                videos.append(videos_item)

        get_shop_videos_performance_details_response_data = cls(
            latest_available_date=latest_available_date,
            videos=videos,
        )

        get_shop_videos_performance_details_response_data.additional_properties = d
        return get_shop_videos_performance_details_response_data

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
