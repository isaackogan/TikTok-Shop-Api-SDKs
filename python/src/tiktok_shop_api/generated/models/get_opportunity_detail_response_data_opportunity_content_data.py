from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOpportunityDetailResponseDataOpportunityContentData")


@_attrs_define
class GetOpportunityDetailResponseDataOpportunityContentData:
    """
    Attributes:
        video_view_pv (str | Unset): The cumulative short video view count of all videos associated with this product
            opportunity.
        shoppable_video_search_pv (str | Unset): The search page-view count for shoppable short videos associated with
            this product opportunity over the previous 30 days, returned as an approximate bucket: `<100`, a rounded-down
            hundreds value such as `300+`, a rounded-down thousands value such as `12k+`, a rounded-down millions value such
            as `1M+`, or `100M+`.
        trending_hashtag (str | Unset): The top 1 video hashtag of the product-related videos, sorted by view count.
        top_shoppable_video_links (list[str] | Unset): Links to the top 10 shoppable short videos related to the
            product, sorted by view count.
    """

    video_view_pv: str | Unset = UNSET
    shoppable_video_search_pv: str | Unset = UNSET
    trending_hashtag: str | Unset = UNSET
    top_shoppable_video_links: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        video_view_pv = self.video_view_pv

        shoppable_video_search_pv = self.shoppable_video_search_pv

        trending_hashtag = self.trending_hashtag

        top_shoppable_video_links: list[str] | Unset = UNSET
        if not isinstance(self.top_shoppable_video_links, Unset):
            top_shoppable_video_links = self.top_shoppable_video_links

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if video_view_pv is not UNSET:
            field_dict["video_view_pv"] = video_view_pv
        if shoppable_video_search_pv is not UNSET:
            field_dict["shoppable_video_search_pv"] = shoppable_video_search_pv
        if trending_hashtag is not UNSET:
            field_dict["trending_hashtag"] = trending_hashtag
        if top_shoppable_video_links is not UNSET:
            field_dict["top_shoppable_video_links"] = top_shoppable_video_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        video_view_pv = d.pop("video_view_pv", UNSET)

        shoppable_video_search_pv = d.pop("shoppable_video_search_pv", UNSET)

        trending_hashtag = d.pop("trending_hashtag", UNSET)

        top_shoppable_video_links = cast(list[str], d.pop("top_shoppable_video_links", UNSET))

        get_opportunity_detail_response_data_opportunity_content_data = cls(
            video_view_pv=video_view_pv,
            shoppable_video_search_pv=shoppable_video_search_pv,
            trending_hashtag=trending_hashtag,
            top_shoppable_video_links=top_shoppable_video_links,
        )

        get_opportunity_detail_response_data_opportunity_content_data.additional_properties = d
        return get_opportunity_detail_response_data_opportunity_content_data

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
