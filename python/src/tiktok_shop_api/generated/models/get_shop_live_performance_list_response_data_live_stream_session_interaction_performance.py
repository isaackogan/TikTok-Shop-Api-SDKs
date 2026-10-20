from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetShopLIVEPerformanceListResponseDataLiveStreamSessionInteractionPerformance")



@_attrs_define
class GetShopLIVEPerformanceListResponseDataLiveStreamSessionInteractionPerformance:
    """ 
        Attributes:
            comment_rate (str | Unset): Ratio of comments to views. Expressed as a raw decimal string.
            comments (int | Unset): Number of comments on the LIVE video posted during the selected period.
            follow_rate (str | Unset): Ratio of new followers to viewers. Expressed as a raw decimal string.
            like_rate (str | Unset): Ratio of likes to views. Expressed as a raw decimal string.
            likes (int | Unset): The number of likes a LIVE video received during the selected time period.
            new_followers (int | Unset): The number of viewers who followed creators from the video during the selected
                period.
            share_rate (str | Unset): Ratio of shares to views. Expressed as a raw decimal string.
            shares (int | Unset): Number of times the LIVE video posted during the selected period were shared.
     """

    comment_rate: str | Unset = UNSET
    comments: int | Unset = UNSET
    follow_rate: str | Unset = UNSET
    like_rate: str | Unset = UNSET
    likes: int | Unset = UNSET
    new_followers: int | Unset = UNSET
    share_rate: str | Unset = UNSET
    shares: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        comment_rate = self.comment_rate

        comments = self.comments

        follow_rate = self.follow_rate

        like_rate = self.like_rate

        likes = self.likes

        new_followers = self.new_followers

        share_rate = self.share_rate

        shares = self.shares


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if comment_rate is not UNSET:
            field_dict["comment_rate"] = comment_rate
        if comments is not UNSET:
            field_dict["comments"] = comments
        if follow_rate is not UNSET:
            field_dict["follow_rate"] = follow_rate
        if like_rate is not UNSET:
            field_dict["like_rate"] = like_rate
        if likes is not UNSET:
            field_dict["likes"] = likes
        if new_followers is not UNSET:
            field_dict["new_followers"] = new_followers
        if share_rate is not UNSET:
            field_dict["share_rate"] = share_rate
        if shares is not UNSET:
            field_dict["shares"] = shares

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_rate = d.pop("comment_rate", UNSET)

        comments = d.pop("comments", UNSET)

        follow_rate = d.pop("follow_rate", UNSET)

        like_rate = d.pop("like_rate", UNSET)

        likes = d.pop("likes", UNSET)

        new_followers = d.pop("new_followers", UNSET)

        share_rate = d.pop("share_rate", UNSET)

        shares = d.pop("shares", UNSET)

        get_shop_live_performance_list_response_data_live_stream_session_interaction_performance = cls(
            comment_rate=comment_rate,
            comments=comments,
            follow_rate=follow_rate,
            like_rate=like_rate,
            likes=likes,
            new_followers=new_followers,
            share_rate=share_rate,
            shares=shares,
        )


        get_shop_live_performance_list_response_data_live_stream_session_interaction_performance.additional_properties = d
        return get_shop_live_performance_list_response_data_live_stream_session_interaction_performance

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
