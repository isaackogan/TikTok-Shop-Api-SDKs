from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetPostViewSearchVideoResponseDataComment")



@_attrs_define
class GetPostViewSearchVideoResponseDataComment:
    """ 
        Attributes:
            comment_id (str | Unset): Unique comment ID.
            content (str | Unset): Comment text.
            create_time (str | Unset): Creation time in UTC; omitted when unavailable.
     """

    comment_id: str | Unset = UNSET
    content: str | Unset = UNSET
    create_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        comment_id = self.comment_id

        content = self.content

        create_time = self.create_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if comment_id is not UNSET:
            field_dict["comment_id"] = comment_id
        if content is not UNSET:
            field_dict["content"] = content
        if create_time is not UNSET:
            field_dict["create_time"] = create_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_id = d.pop("comment_id", UNSET)

        content = d.pop("content", UNSET)

        create_time = d.pop("create_time", UNSET)

        get_post_view_search_video_response_data_comment = cls(
            comment_id=comment_id,
            content=content,
            create_time=create_time,
        )


        get_post_view_search_video_response_data_comment.additional_properties = d
        return get_post_view_search_video_response_data_comment

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
