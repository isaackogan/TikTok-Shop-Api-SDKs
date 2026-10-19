from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalInteraction")


@_attrs_define
class GetShopLIVEMinutePerformanceResponseDataPerformanceIntervalInteraction:
    """
    Attributes:
        new_followers (int | Unset): Number of viewers who followed creator from the LIVE video
        shares (int | Unset): Total number of shares of a LIVE.
        comments (int | Unset): Total number of comments for a LIVE.
        likes (int | Unset): The number of likes in the LIVE room.
        comment_rate (str | Unset): Total number of comments during the LIVE divided by the number of views.
        follow_rate (str | Unset): Number of users that followed the creator during the LIVE divided by the number of
            views.
        like_rate (str | Unset): Total number of likes during the LIVE divided by the number of views.
        share_rate (str | Unset): Total number of times the LIVE was shared divided by the total number of views.
    """

    new_followers: int | Unset = UNSET
    shares: int | Unset = UNSET
    comments: int | Unset = UNSET
    likes: int | Unset = UNSET
    comment_rate: str | Unset = UNSET
    follow_rate: str | Unset = UNSET
    like_rate: str | Unset = UNSET
    share_rate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_followers = self.new_followers

        shares = self.shares

        comments = self.comments

        likes = self.likes

        comment_rate = self.comment_rate

        follow_rate = self.follow_rate

        like_rate = self.like_rate

        share_rate = self.share_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_followers is not UNSET:
            field_dict["new_followers"] = new_followers
        if shares is not UNSET:
            field_dict["shares"] = shares
        if comments is not UNSET:
            field_dict["comments"] = comments
        if likes is not UNSET:
            field_dict["likes"] = likes
        if comment_rate is not UNSET:
            field_dict["comment_rate"] = comment_rate
        if follow_rate is not UNSET:
            field_dict["follow_rate"] = follow_rate
        if like_rate is not UNSET:
            field_dict["like_rate"] = like_rate
        if share_rate is not UNSET:
            field_dict["share_rate"] = share_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        new_followers = d.pop("new_followers", UNSET)

        shares = d.pop("shares", UNSET)

        comments = d.pop("comments", UNSET)

        likes = d.pop("likes", UNSET)

        comment_rate = d.pop("comment_rate", UNSET)

        follow_rate = d.pop("follow_rate", UNSET)

        like_rate = d.pop("like_rate", UNSET)

        share_rate = d.pop("share_rate", UNSET)

        get_shop_live_minute_performance_response_data_performance_interval_interaction = cls(
            new_followers=new_followers,
            shares=shares,
            comments=comments,
            likes=likes,
            comment_rate=comment_rate,
            follow_rate=follow_rate,
            like_rate=like_rate,
            share_rate=share_rate,
        )

        get_shop_live_minute_performance_response_data_performance_interval_interaction.additional_properties = d
        return get_shop_live_minute_performance_response_data_performance_interval_interaction

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
