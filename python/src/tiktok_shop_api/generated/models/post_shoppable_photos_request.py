from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_shoppable_photos_request_link_info import PostShoppablePhotosRequestLinkInfo
    from ..models.post_shoppable_photos_request_photos_info import PostShoppablePhotosRequestPhotosInfo


T = TypeVar("T", bound="PostShoppablePhotosRequest")


@_attrs_define
class PostShoppablePhotosRequest:
    """
    Attributes:
        photos_info (list[PostShoppablePhotosRequestPhotosInfo]): Photo Info Metadata
        music_id (str | Unset): Music ID
        title (str | Unset): Post title:The maximum length is 5000 in UTF-16 runes. If not specified, the ticket post
            will not have any captions.   - You can add relevant hashtags to increase discoverability. The format is simply
            # followed by the topic name. Multiple hashtags are supported,e.g.,#humor#BFCM
        link_info (PostShoppablePhotosRequestLinkInfo | Unset):
        is_ai_generated (bool | Unset): Field to indicate whether the content was AI generated. Marking this field as
            true will display a tag indicating this post as an AI generated post.
    """

    photos_info: list[PostShoppablePhotosRequestPhotosInfo]
    music_id: str | Unset = UNSET
    title: str | Unset = UNSET
    link_info: PostShoppablePhotosRequestLinkInfo | Unset = UNSET
    is_ai_generated: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        photos_info = []
        for photos_info_item_data in self.photos_info:
            photos_info_item = photos_info_item_data.to_dict()
            photos_info.append(photos_info_item)

        music_id = self.music_id

        title = self.title

        link_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link_info, Unset):
            link_info = self.link_info.to_dict()

        is_ai_generated = self.is_ai_generated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "photos_info": photos_info,
            }
        )
        if music_id is not UNSET:
            field_dict["music_id"] = music_id
        if title is not UNSET:
            field_dict["title"] = title
        if link_info is not UNSET:
            field_dict["link_info"] = link_info
        if is_ai_generated is not UNSET:
            field_dict["is_ai_generated"] = is_ai_generated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_shoppable_photos_request_link_info import PostShoppablePhotosRequestLinkInfo  # noqa: PLC0415
        from ..models.post_shoppable_photos_request_photos_info import (
            PostShoppablePhotosRequestPhotosInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        photos_info = []
        _photos_info = d.pop("photos_info")
        for photos_info_item_data in _photos_info:
            photos_info_item = PostShoppablePhotosRequestPhotosInfo.from_dict(photos_info_item_data)

            photos_info.append(photos_info_item)

        music_id = d.pop("music_id", UNSET)

        title = d.pop("title", UNSET)

        _link_info = d.pop("link_info", UNSET)
        link_info: PostShoppablePhotosRequestLinkInfo | Unset
        if isinstance(_link_info, Unset):
            link_info = UNSET
        else:
            link_info = PostShoppablePhotosRequestLinkInfo.from_dict(_link_info)

        is_ai_generated = d.pop("is_ai_generated", UNSET)

        post_shoppable_photos_request = cls(
            photos_info=photos_info,
            music_id=music_id,
            title=title,
            link_info=link_info,
            is_ai_generated=is_ai_generated,
        )

        post_shoppable_photos_request.additional_properties = d
        return post_shoppable_photos_request

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
