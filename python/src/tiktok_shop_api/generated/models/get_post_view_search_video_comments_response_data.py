from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_post_view_search_video_comments_response_data_comment import GetPostViewSearchVideoCommentsResponseDataComment





T = TypeVar("T", bound="GetPostViewSearchVideoCommentsResponseData")



@_attrs_define
class GetPostViewSearchVideoCommentsResponseData:
    """ 
        Attributes:
            comments (list[GetPostViewSearchVideoCommentsResponseDataComment] | Unset): Business access is limited to the
                latest 50 matching comments per video, newest first. Earlier comments cannot be retrieved through this API.
                Duplicate comment IDs are removed.
            video_id (str | Unset): Unique video id.
     """

    comments: list[GetPostViewSearchVideoCommentsResponseDataComment] | Unset = UNSET
    video_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_post_view_search_video_comments_response_data_comment import GetPostViewSearchVideoCommentsResponseDataComment # noqa: PLC0415
        comments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()
                comments.append(comments_item)



        video_id = self.video_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if comments is not UNSET:
            field_dict["comments"] = comments
        if video_id is not UNSET:
            field_dict["video_id"] = video_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_post_view_search_video_comments_response_data_comment import GetPostViewSearchVideoCommentsResponseDataComment # noqa: PLC0415
        d = dict(src_dict)
        _comments = d.pop("comments", UNSET)
        comments: list[GetPostViewSearchVideoCommentsResponseDataComment] | Unset = UNSET
        if _comments is not UNSET:
            comments = []
            for comments_item_data in _comments:
                comments_item = GetPostViewSearchVideoCommentsResponseDataComment.from_dict(comments_item_data)



                comments.append(comments_item)


        video_id = d.pop("video_id", UNSET)

        get_post_view_search_video_comments_response_data = cls(
            comments=comments,
            video_id=video_id,
        )


        get_post_view_search_video_comments_response_data.additional_properties = d
        return get_post_view_search_video_comments_response_data

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
