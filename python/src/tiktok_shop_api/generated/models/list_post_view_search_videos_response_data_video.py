from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_post_view_search_video_response_data_video_metric import GetPostViewSearchVideoResponseDataVideoMetric





T = TypeVar("T", bound="ListPostViewSearchVideosResponseDataVideo")



@_attrs_define
class ListPostViewSearchVideosResponseDataVideo:
    """ 
        Attributes:
            author_type (str): SELF: posted by the shop; CREATOR: posted by a creator.
            metrics (GetPostViewSearchVideoResponseDataVideoMetric):
            video_id (str): Unique video ID.
            cover_url (str | Unset): Video cover URL; omitted when unavailable.
            has_optimization_inputs (bool | Unset): Whether an operation record exists for this video and shop. Does not
                indicate current configuration, keyword approval or effectiveness.
            title (str | Unset): Video caption; omitted when video metadata is unavailable.
            top_keywords (list[str] | Unset): Up to two popular search keywords from warehouse data, in the returned order;
                empty when none are available. These are not shop-configured keywords.
     """

    author_type: str
    metrics: GetPostViewSearchVideoResponseDataVideoMetric
    video_id: str
    cover_url: str | Unset = UNSET
    has_optimization_inputs: bool | Unset = UNSET
    title: str | Unset = UNSET
    top_keywords: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_post_view_search_video_response_data_video_metric import GetPostViewSearchVideoResponseDataVideoMetric # noqa: PLC0415
        author_type = self.author_type

        metrics = self.metrics.to_dict()

        video_id = self.video_id

        cover_url = self.cover_url

        has_optimization_inputs = self.has_optimization_inputs

        title = self.title

        top_keywords: list[str] | Unset = UNSET
        if not isinstance(self.top_keywords, Unset):
            top_keywords = self.top_keywords




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "author_type": author_type,
            "metrics": metrics,
            "video_id": video_id,
        })
        if cover_url is not UNSET:
            field_dict["cover_url"] = cover_url
        if has_optimization_inputs is not UNSET:
            field_dict["has_optimization_inputs"] = has_optimization_inputs
        if title is not UNSET:
            field_dict["title"] = title
        if top_keywords is not UNSET:
            field_dict["top_keywords"] = top_keywords

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_post_view_search_video_response_data_video_metric import GetPostViewSearchVideoResponseDataVideoMetric # noqa: PLC0415
        d = dict(src_dict)
        author_type = d.pop("author_type")

        metrics = GetPostViewSearchVideoResponseDataVideoMetric.from_dict(d.pop("metrics"))




        video_id = d.pop("video_id")

        cover_url = d.pop("cover_url", UNSET)

        has_optimization_inputs = d.pop("has_optimization_inputs", UNSET)

        title = d.pop("title", UNSET)

        top_keywords = cast(list[str], d.pop("top_keywords", UNSET))


        list_post_view_search_videos_response_data_video = cls(
            author_type=author_type,
            metrics=metrics,
            video_id=video_id,
            cover_url=cover_url,
            has_optimization_inputs=has_optimization_inputs,
            title=title,
            top_keywords=top_keywords,
        )


        list_post_view_search_videos_response_data_video.additional_properties = d
        return list_post_view_search_videos_response_data_video

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
