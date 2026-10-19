from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalTraffic")


@_attrs_define
class GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalTraffic:
    """
    Attributes:
        views (int | Unset): Number of times the requested video was watched during the interval. Repeat views by the
            same user are counted separately.
        new_followers (int | Unset): The number of times a user followed you after watching a video
        shares (int | Unset): The cumulative number of times users shared the video
        comments (int | Unset): The cumulative number of times users left comments on the video
        likes (int | Unset): The cumulative number of times users liked the video
    """

    views: int | Unset = UNSET
    new_followers: int | Unset = UNSET
    shares: int | Unset = UNSET
    comments: int | Unset = UNSET
    likes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        views = self.views

        new_followers = self.new_followers

        shares = self.shares

        comments = self.comments

        likes = self.likes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if views is not UNSET:
            field_dict["views"] = views
        if new_followers is not UNSET:
            field_dict["new_followers"] = new_followers
        if shares is not UNSET:
            field_dict["shares"] = shares
        if comments is not UNSET:
            field_dict["comments"] = comments
        if likes is not UNSET:
            field_dict["likes"] = likes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        views = d.pop("views", UNSET)

        new_followers = d.pop("new_followers", UNSET)

        shares = d.pop("shares", UNSET)

        comments = d.pop("comments", UNSET)

        likes = d.pop("likes", UNSET)

        get_shop_video_performance_details_response_data_performance_interval_traffic = cls(
            views=views,
            new_followers=new_followers,
            shares=shares,
            comments=comments,
            likes=likes,
        )

        get_shop_video_performance_details_response_data_performance_interval_traffic.additional_properties = d
        return get_shop_video_performance_details_response_data_performance_interval_traffic

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
