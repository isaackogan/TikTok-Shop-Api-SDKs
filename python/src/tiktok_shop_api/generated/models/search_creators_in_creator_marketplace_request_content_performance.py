from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchCreatorsInCreatorMarketplaceRequestContentPerformance")



@_attrs_define
class SearchCreatorsInCreatorMarketplaceRequestContentPerformance:
    """ 
        Attributes:
            avg_video_views (str | Unset): Average Video Views more than
                You can pass in average video views anywhere between 0 and 100k
                Pick any whole number between 0 and 100,000, and we will return all results with average video views greater
                than that number.
                You can only pass in Average Video Views OR Average Shoppable Video Views. Using both filters will cause the API
                call to fail.
            avg_shoppable_video_views (str | Unset): You can pass in average shoppable video views anywhere between 0 and
                100k
                Pick any whole number between 0 and 100,000, and we will return all results with average shoppable video views
                greater than that number.
                You can only pass in Average Video Views OR Average Shoppable Video Views. Using both filters will cause the API
                call to fail.
            avg_engagement_rate (str | Unset): Average engagement rate more than 0-20.
                You can only filter by increments of 1% point, up to 20%.
            avg_shopable_engagement_rate (str | Unset): Average shoppable engagement rate more than 0-20.
                You can only filter by increments of 1% point, up to 20%.
            avg_live_avg_viewers_ge (str | Unset): Filters creators whose average LIVE viewers are greater than or equal to
                the specified value.
                Enter a whole number from 0 to 100,000.
                You can only pass one of avg_live_avg_viewers_ge and avg_shoppable_live_avg_viewers_ge. Using both filters
                causes the API call to fail.
            avg_shoppable_live_avg_viewers_ge (str | Unset): Filters creators whose average shoppable LIVE viewers are
                greater than or equal to the specified value.
                Enter a whole number from 0 to 100,000.
                You can only pass one of avg_live_avg_viewers_ge and avg_shoppable_live_avg_viewers_ge. Using both filters
                causes the API call to fail.
     """

    avg_video_views: str | Unset = UNSET
    avg_shoppable_video_views: str | Unset = UNSET
    avg_engagement_rate: str | Unset = UNSET
    avg_shopable_engagement_rate: str | Unset = UNSET
    avg_live_avg_viewers_ge: str | Unset = UNSET
    avg_shoppable_live_avg_viewers_ge: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        avg_video_views = self.avg_video_views

        avg_shoppable_video_views = self.avg_shoppable_video_views

        avg_engagement_rate = self.avg_engagement_rate

        avg_shopable_engagement_rate = self.avg_shopable_engagement_rate

        avg_live_avg_viewers_ge = self.avg_live_avg_viewers_ge

        avg_shoppable_live_avg_viewers_ge = self.avg_shoppable_live_avg_viewers_ge


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if avg_video_views is not UNSET:
            field_dict["avg_video_views"] = avg_video_views
        if avg_shoppable_video_views is not UNSET:
            field_dict["avg_shoppable_video_views"] = avg_shoppable_video_views
        if avg_engagement_rate is not UNSET:
            field_dict["avg_engagement_rate"] = avg_engagement_rate
        if avg_shopable_engagement_rate is not UNSET:
            field_dict["avg_shopable_engagement_rate"] = avg_shopable_engagement_rate
        if avg_live_avg_viewers_ge is not UNSET:
            field_dict["avg_live_avg_viewers_ge"] = avg_live_avg_viewers_ge
        if avg_shoppable_live_avg_viewers_ge is not UNSET:
            field_dict["avg_shoppable_live_avg_viewers_ge"] = avg_shoppable_live_avg_viewers_ge

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_video_views = d.pop("avg_video_views", UNSET)

        avg_shoppable_video_views = d.pop("avg_shoppable_video_views", UNSET)

        avg_engagement_rate = d.pop("avg_engagement_rate", UNSET)

        avg_shopable_engagement_rate = d.pop("avg_shopable_engagement_rate", UNSET)

        avg_live_avg_viewers_ge = d.pop("avg_live_avg_viewers_ge", UNSET)

        avg_shoppable_live_avg_viewers_ge = d.pop("avg_shoppable_live_avg_viewers_ge", UNSET)

        search_creators_in_creator_marketplace_request_content_performance = cls(
            avg_video_views=avg_video_views,
            avg_shoppable_video_views=avg_shoppable_video_views,
            avg_engagement_rate=avg_engagement_rate,
            avg_shopable_engagement_rate=avg_shopable_engagement_rate,
            avg_live_avg_viewers_ge=avg_live_avg_viewers_ge,
            avg_shoppable_live_avg_viewers_ge=avg_shoppable_live_avg_viewers_ge,
        )


        search_creators_in_creator_marketplace_request_content_performance.additional_properties = d
        return search_creators_in_creator_marketplace_request_content_performance

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
