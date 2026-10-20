from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalTraffic")


@_attrs_define
class GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalTraffic:
    """
    Attributes:
        comments (int | Unset): The number of comments received by the video.
        likes (int | Unset): The number of likes received by the video.
        new_followers (int | Unset): The number of new followers attributed to the video.
        shares (int | Unset): The number of times the video was shared.
        views (int | Unset): The number of video views.
    """

    comments: int | Unset = UNSET
    likes: int | Unset = UNSET
    new_followers: int | Unset = UNSET
    shares: int | Unset = UNSET
    views: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comments = self.comments

        likes = self.likes

        new_followers = self.new_followers

        shares = self.shares

        views = self.views

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if likes is not UNSET:
            field_dict["likes"] = likes
        if new_followers is not UNSET:
            field_dict["new_followers"] = new_followers
        if shares is not UNSET:
            field_dict["shares"] = shares
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comments = d.pop("comments", UNSET)

        likes = d.pop("likes", UNSET)

        new_followers = d.pop("new_followers", UNSET)

        shares = d.pop("shares", UNSET)

        views = d.pop("views", UNSET)

        get_shop_videos_performance_details_response_data_video_performance_interval_traffic = cls(
            comments=comments,
            likes=likes,
            new_followers=new_followers,
            shares=shares,
            views=views,
        )

        get_shop_videos_performance_details_response_data_video_performance_interval_traffic.additional_properties = d
        return get_shop_videos_performance_details_response_data_video_performance_interval_traffic

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
