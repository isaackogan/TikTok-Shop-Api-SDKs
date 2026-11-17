from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="UpdatePostViewSearchVideoKeywordsRequest")



@_attrs_define
class UpdatePostViewSearchVideoKeywordsRequest:
    """ 
        Attributes:
            keywords (list[str]): Complete keyword set. An empty array clears all configured keywords.
     """

    keywords: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        keywords = self.keywords




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "keywords": keywords,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keywords = cast(list[str], d.pop("keywords"))


        update_post_view_search_video_keywords_request = cls(
            keywords=keywords,
        )


        update_post_view_search_video_keywords_request.additional_properties = d
        return update_post_view_search_video_keywords_request

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
