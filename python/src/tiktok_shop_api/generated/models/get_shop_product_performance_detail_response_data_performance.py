from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_product_performance_detail_response_data_performance_interval import (
        GetShopProductPerformanceDetailResponseDataPerformanceInterval,
    )
    from ..models.get_shop_product_performance_detail_response_data_performance_rating import (
        GetShopProductPerformanceDetailResponseDataPerformanceRating,
    )
    from ..models.get_shop_product_performance_detail_response_data_performance_top_content import (
        GetShopProductPerformanceDetailResponseDataPerformanceTopContent,
    )
    from ..models.get_shop_product_performance_detail_response_data_performance_top_creator import (
        GetShopProductPerformanceDetailResponseDataPerformanceTopCreator,
    )


T = TypeVar("T", bound="GetShopProductPerformanceDetailResponseDataPerformance")


@_attrs_define
class GetShopProductPerformanceDetailResponseDataPerformance:
    """
    Attributes:
        intervals (list[GetShopProductPerformanceDetailResponseDataPerformanceInterval] | Unset): Interval data for the
            requested time range. The time range of each interval is determined by the granularity.
        ratings (list[GetShopProductPerformanceDetailResponseDataPerformanceRating] | Unset): ratings within the choosen
            start_date_ge and end_date_ge
        top_contents (list[GetShopProductPerformanceDetailResponseDataPerformanceTopContent] | Unset): Product-related
            content for the period from `start_date_ge` (inclusive) to `end_date_lt` (exclusive).
            Sorted by GMV; returns only the top 100.
        top_creators (list[GetShopProductPerformanceDetailResponseDataPerformanceTopCreator] | Unset): Product-related
            creators for the period from `start_date_ge` (inclusive) to `end_date_lt` (exclusive).
            Sorted by GMV; returns only the top 100.
    """

    intervals: list[GetShopProductPerformanceDetailResponseDataPerformanceInterval] | Unset = UNSET
    ratings: list[GetShopProductPerformanceDetailResponseDataPerformanceRating] | Unset = UNSET
    top_contents: list[GetShopProductPerformanceDetailResponseDataPerformanceTopContent] | Unset = UNSET
    top_creators: list[GetShopProductPerformanceDetailResponseDataPerformanceTopCreator] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        intervals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.intervals, Unset):
            intervals = []
            for intervals_item_data in self.intervals:
                intervals_item = intervals_item_data.to_dict()
                intervals.append(intervals_item)

        ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ratings, Unset):
            ratings = []
            for ratings_item_data in self.ratings:
                ratings_item = ratings_item_data.to_dict()
                ratings.append(ratings_item)

        top_contents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_contents, Unset):
            top_contents = []
            for top_contents_item_data in self.top_contents:
                top_contents_item = top_contents_item_data.to_dict()
                top_contents.append(top_contents_item)

        top_creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_creators, Unset):
            top_creators = []
            for top_creators_item_data in self.top_creators:
                top_creators_item = top_creators_item_data.to_dict()
                top_creators.append(top_creators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if intervals is not UNSET:
            field_dict["intervals"] = intervals
        if ratings is not UNSET:
            field_dict["ratings"] = ratings
        if top_contents is not UNSET:
            field_dict["top_contents"] = top_contents
        if top_creators is not UNSET:
            field_dict["top_creators"] = top_creators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_product_performance_detail_response_data_performance_interval import (
            GetShopProductPerformanceDetailResponseDataPerformanceInterval,  # noqa: PLC0415
        )
        from ..models.get_shop_product_performance_detail_response_data_performance_rating import (
            GetShopProductPerformanceDetailResponseDataPerformanceRating,  # noqa: PLC0415
        )
        from ..models.get_shop_product_performance_detail_response_data_performance_top_content import (
            GetShopProductPerformanceDetailResponseDataPerformanceTopContent,  # noqa: PLC0415
        )
        from ..models.get_shop_product_performance_detail_response_data_performance_top_creator import (
            GetShopProductPerformanceDetailResponseDataPerformanceTopCreator,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _intervals = d.pop("intervals", UNSET)
        intervals: list[GetShopProductPerformanceDetailResponseDataPerformanceInterval] | Unset = UNSET
        if _intervals is not UNSET:
            intervals = []
            for intervals_item_data in _intervals:
                intervals_item = GetShopProductPerformanceDetailResponseDataPerformanceInterval.from_dict(
                    intervals_item_data
                )

                intervals.append(intervals_item)

        _ratings = d.pop("ratings", UNSET)
        ratings: list[GetShopProductPerformanceDetailResponseDataPerformanceRating] | Unset = UNSET
        if _ratings is not UNSET:
            ratings = []
            for ratings_item_data in _ratings:
                ratings_item = GetShopProductPerformanceDetailResponseDataPerformanceRating.from_dict(ratings_item_data)

                ratings.append(ratings_item)

        _top_contents = d.pop("top_contents", UNSET)
        top_contents: list[GetShopProductPerformanceDetailResponseDataPerformanceTopContent] | Unset = UNSET
        if _top_contents is not UNSET:
            top_contents = []
            for top_contents_item_data in _top_contents:
                top_contents_item = GetShopProductPerformanceDetailResponseDataPerformanceTopContent.from_dict(
                    top_contents_item_data
                )

                top_contents.append(top_contents_item)

        _top_creators = d.pop("top_creators", UNSET)
        top_creators: list[GetShopProductPerformanceDetailResponseDataPerformanceTopCreator] | Unset = UNSET
        if _top_creators is not UNSET:
            top_creators = []
            for top_creators_item_data in _top_creators:
                top_creators_item = GetShopProductPerformanceDetailResponseDataPerformanceTopCreator.from_dict(
                    top_creators_item_data
                )

                top_creators.append(top_creators_item)

        get_shop_product_performance_detail_response_data_performance = cls(
            intervals=intervals,
            ratings=ratings,
            top_contents=top_contents,
            top_creators=top_creators,
        )

        get_shop_product_performance_detail_response_data_performance.additional_properties = d
        return get_shop_product_performance_detail_response_data_performance

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
