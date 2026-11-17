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
            file_id (str): Video file_id from [Upload Shoppable Video File]
            title (str): The video caption.
                The maximum length is 4000 in UTF-16 runes.
                If not specified, the ticket post will not have any captions.
            cover_uri (str | Unset): Video cover image URI, which is returned after uploading the image via the Upload
                Shoppable Photo File API.
            cover_timestamp_ms (int | Unset): The input parameter is a timestamp, which specifies a particular moment in the
                video. The frame at that timestamp will be used as the video cover. If cover_uri and cover_timestamp_ms are both
                not provided, the cover will default to the first frame of the uploaded video. Only one of cover_uri or
                cover_timestamp_ms can be provided. If both parameters are passed, cover_uri will take precedence.
            music_id (str | Unset): The music ID for the video BGM. If not provided, no music will be associated with the
                video. The music ID must be obtained via Search Music Library.
            is_ai_generated (bool | Unset): Field to indicate whether the content was AI generated. Marking this field as
                true will display a tag indicating this post as an AI generated post.
     """

    file_id: str
    title: str
    cover_uri: str | Unset = UNSET
    cover_timestamp_ms: int | Unset = UNSET
    music_id: str | Unset = UNSET
    is_ai_generated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file_id = self.file_id

        title = self.title

        cover_uri = self.cover_uri

        cover_timestamp_ms = self.cover_timestamp_ms

        music_id = self.music_id

        is_ai_generated = self.is_ai_generated


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
        if is_ai_generated is not UNSET:
            field_dict["is_ai_generated"] = is_ai_generated

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = d.pop("file_id")

        title = d.pop("title")

        cover_uri = d.pop("cover_uri", UNSET)

        cover_timestamp_ms = d.pop("cover_timestamp_ms", UNSET)

        music_id = d.pop("music_id", UNSET)

        is_ai_generated = d.pop("is_ai_generated", UNSET)

        post_shoppable_video_request_video_info = cls(
            file_id=file_id,
            title=title,
            cover_uri=cover_uri,
            cover_timestamp_ms=cover_timestamp_ms,
            music_id=music_id,
            is_ai_generated=is_ai_generated,
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
