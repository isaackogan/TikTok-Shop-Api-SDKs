from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostShoppableVideoRequestVideoInfo")



@_attrs_define
class PostShoppableVideoRequestVideoInfo:
    """ 
        Attributes:
            file_id (str): The video file ID returned by Upload Shoppable Video File (`POST
                /affiliate_creator/202505/videos/video_files`).
            title (str): The video caption.
                The maximum length is 2200 in UTF-16 runes.
                If not specified, the ticket post will not have any captions.
            cover_uri (str | Unset): The video cover image URI returned by Upload Shoppable Photo File (`POST
                /affiliate_creator/202511/photos/photo_files`).
            cover_timestamp_ms (int | Unset): The input parameter is a timestamp, which specifies a particular moment in the
                video. The frame at that timestamp will be used as the video cover. If cover_uri and cover_timestamp_ms are both
                not provided, the cover will default to the first frame of the uploaded video. Only one of cover_uri or
                cover_timestamp_ms can be provided. If both parameters are passed, cover_uri will take precedence.
            music_id (str | Unset): The music ID for the video's background music. Obtain it from Search Music (`GET
                /affiliate_creator/202602/music/search`). If not provided, no music will be associated with the video.
     """

    file_id: str
    title: str
    cover_uri: str | Unset = UNSET
    cover_timestamp_ms: int | Unset = UNSET
    music_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        title = self.title

        cover_uri = self.cover_uri

        cover_timestamp_ms = self.cover_timestamp_ms

        music_id = self.music_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "file_id": file_id,
            "title": title,
        })
        if cover_uri is not UNSET:
            field_dict["cover_uri"] = cover_uri
        if cover_timestamp_ms is not UNSET:
            field_dict["cover_timestamp_ms"] = cover_timestamp_ms
        if music_id is not UNSET:
            field_dict["music_id"] = music_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("file_id")

        title = d.pop("title")

        cover_uri = d.pop("cover_uri", UNSET)

        cover_timestamp_ms = d.pop("cover_timestamp_ms", UNSET)

        music_id = d.pop("music_id", UNSET)

        post_shoppable_video_request_video_info = cls(
            file_id=file_id,
            title=title,
            cover_uri=cover_uri,
            cover_timestamp_ms=cover_timestamp_ms,
            music_id=music_id,
        )


        post_shoppable_video_request_video_info.additional_properties = d
        return post_shoppable_video_request_video_info

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
