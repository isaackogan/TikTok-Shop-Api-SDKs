from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetShopVideosPerformanceDetailsResponseDataVideoVideo")



@_attrs_define
class GetShopVideosPerformanceDetailsResponseDataVideoVideo:
    """ 
        Attributes:
            duration (int | Unset): The video duration.
            id (str | Unset): The video ID.
            play_url (str | Unset): The video playback URL.
            thumbnail_url (str | Unset): The video thumbnail URL.
            title (str | Unset): The video title.
            username (str | Unset): The username of the video creator.
            video_post_time (str | Unset): The time when the video was posted.
     """

    duration: int | Unset = UNSET
    id: str | Unset = UNSET
    play_url: str | Unset = UNSET
    thumbnail_url: str | Unset = UNSET
    title: str | Unset = UNSET
    username: str | Unset = UNSET
    video_post_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        duration = self.duration

        id = self.id

        play_url = self.play_url

        thumbnail_url = self.thumbnail_url

        title = self.title

        username = self.username

        video_post_time = self.video_post_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if duration is not UNSET:
            field_dict["duration"] = duration
        if id is not UNSET:
            field_dict["id"] = id
        if play_url is not UNSET:
            field_dict["play_url"] = play_url
        if thumbnail_url is not UNSET:
            field_dict["thumbnail_url"] = thumbnail_url
        if title is not UNSET:
            field_dict["title"] = title
        if username is not UNSET:
            field_dict["username"] = username
        if video_post_time is not UNSET:
            field_dict["video_post_time"] = video_post_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration = d.pop("duration", UNSET)

        id = d.pop("id", UNSET)

        play_url = d.pop("play_url", UNSET)

        thumbnail_url = d.pop("thumbnail_url", UNSET)

        title = d.pop("title", UNSET)

        username = d.pop("username", UNSET)

        video_post_time = d.pop("video_post_time", UNSET)

        get_shop_videos_performance_details_response_data_video_video = cls(
            duration=duration,
            id=id,
            play_url=play_url,
            thumbnail_url=thumbnail_url,
            title=title,
            username=username,
            video_post_time=video_post_time,
        )


        get_shop_videos_performance_details_response_data_video_video.additional_properties = d
        return get_shop_videos_performance_details_response_data_video_video

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
