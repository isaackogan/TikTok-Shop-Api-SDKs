from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetPostViewSearchVideoKeywordsResponseData")



@_attrs_define
class GetPostViewSearchVideoKeywordsResponseData:
    """ 
        Attributes:
            keywords (list[str] | Unset): Current keywords; empty when none are configured.
            video_id (str | Unset): Unique video id.
     """

    keywords: list[str] | Unset = UNSET
    video_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        keywords: list[str] | Unset = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords



        video_id = self.video_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if video_id is not UNSET:
            field_dict["video_id"] = video_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keywords = cast(list[str], d.pop("keywords", UNSET))


        video_id = d.pop("video_id", UNSET)

        get_post_view_search_video_keywords_response_data = cls(
            keywords=keywords,
            video_id=video_id,
        )


        get_post_view_search_video_keywords_response_data.additional_properties = d
        return get_post_view_search_video_keywords_response_data

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
