from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_creators_in_creator_marketplace_request_advanced_filter import (
        SearchCreatorsInCreatorMarketplaceRequestAdvancedFilter,
    )
    from ..models.search_creators_in_creator_marketplace_request_affiliate_data import (
        SearchCreatorsInCreatorMarketplaceRequestAffiliateData,
    )
    from ..models.search_creators_in_creator_marketplace_request_category import (
        SearchCreatorsInCreatorMarketplaceRequestCategory,
    )
    from ..models.search_creators_in_creator_marketplace_request_content_performance import (
        SearchCreatorsInCreatorMarketplaceRequestContentPerformance,
    )
    from ..models.search_creators_in_creator_marketplace_request_follower_demographic import (
        SearchCreatorsInCreatorMarketplaceRequestFollowerDemographic,
    )


T = TypeVar("T", bound="SearchCreatorsInCreatorMarketplaceRequest")


@_attrs_define
class SearchCreatorsInCreatorMarketplaceRequest:
    """
    Attributes:
        search_key (str | Unset): Caching search results improves api performance and ensures stable request results.
            You don't need to pass a value on the first call.
            For the second call, please pass the value returned in the response of the first call.
        keyword (str | Unset): Searching creators by keyword, matching based on TikTok Username and Nickname.
        follower_demographics (SearchCreatorsInCreatorMarketplaceRequestFollowerDemographic | Unset):
        gmv_ranges (list[str] | Unset): Filtering by GMV range intervals which include:
            GMV_RANGE_0_100: "0-100",
            GMV_RANGE_100_1000: "100-1000",
            GMV_RANGE_1000_10000: "1000-10000",
            GMV_RANGE_10000_AND_ABOVE: "10000+"
            For example:
            - If GMV_RANGE_0_100 is passed, it means filtering the creator data that is greater than or equal to 0 and less
            than or equal to 100.
            - If GMV_RANGE_0_100 and GMV_RANGE_100_1000 are passed, it means to filter the creator data that is greater than
            or equal to 0 and less than or equal to 1000.
        units_sold_ranges (list[str] | Unset): Filtering by sales volume range intervals which include:
            UNITS_SOLD_RANGE_0_10: "0-10",
            UNITS_SOLD_RANGE_10_100: "10-100",
            UNITS_SOLD_RANGE_100_1000: "100-1000",
            UNITS_SOLD_RANGE_1000_AND_ABOVE: "1000+"
            For example:
            - If UNITS_SOLD_RANGE_0_10 is passed, it means filtering the creator data that is greater than or equal to 0 and
            less than or equal to 10.
            - If UNITS_SOLD_RANGE_0_10 and UNITS_SOLD_RANGE_10_100 are passed, it means to filter the creator data that is
            greater than or equal to 0 and less than or equal to 100.
        category (list[SearchCreatorsInCreatorMarketplaceRequestCategory] | Unset): Array of category filter objects.
            Use [Get Categories](https://partner.tiktokshop.com/docv2/page/get-categories-202309) to retrieve category IDs.
        content_performance (SearchCreatorsInCreatorMarketplaceRequestContentPerformance | Unset):
        affiliate_data (SearchCreatorsInCreatorMarketplaceRequestAffiliateData | Unset):
        advanced_filters (SearchCreatorsInCreatorMarketplaceRequestAdvancedFilter | Unset):
        data_groups (list[str] | Unset): Creator's Data Group, get all group by default, which include:
            - BASIC_CREATOR_INFORMATION
            - CONTENT_PERFORMANCE
            - FOLLOWER_INFORMATION
            - COLLABORATION
            - SALES_AND_GMV
    """

    search_key: str | Unset = UNSET
    keyword: str | Unset = UNSET
    follower_demographics: SearchCreatorsInCreatorMarketplaceRequestFollowerDemographic | Unset = UNSET
    gmv_ranges: list[str] | Unset = UNSET
    units_sold_ranges: list[str] | Unset = UNSET
    category: list[SearchCreatorsInCreatorMarketplaceRequestCategory] | Unset = UNSET
    content_performance: SearchCreatorsInCreatorMarketplaceRequestContentPerformance | Unset = UNSET
    affiliate_data: SearchCreatorsInCreatorMarketplaceRequestAffiliateData | Unset = UNSET
    advanced_filters: SearchCreatorsInCreatorMarketplaceRequestAdvancedFilter | Unset = UNSET
    data_groups: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_key = self.search_key

        keyword = self.keyword

        follower_demographics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.follower_demographics, Unset):
            follower_demographics = self.follower_demographics.to_dict()

        gmv_ranges: list[str] | Unset = UNSET
        if not isinstance(self.gmv_ranges, Unset):
            gmv_ranges = self.gmv_ranges

        units_sold_ranges: list[str] | Unset = UNSET
        if not isinstance(self.units_sold_ranges, Unset):
            units_sold_ranges = self.units_sold_ranges

        category: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = []
            for category_item_data in self.category:
                category_item = category_item_data.to_dict()
                category.append(category_item)

        content_performance: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content_performance, Unset):
            content_performance = self.content_performance.to_dict()

        affiliate_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.affiliate_data, Unset):
            affiliate_data = self.affiliate_data.to_dict()

        advanced_filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.advanced_filters, Unset):
            advanced_filters = self.advanced_filters.to_dict()

        data_groups: list[str] | Unset = UNSET
        if not isinstance(self.data_groups, Unset):
            data_groups = self.data_groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_key is not UNSET:
            field_dict["search_key"] = search_key
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if follower_demographics is not UNSET:
            field_dict["follower_demographics"] = follower_demographics
        if gmv_ranges is not UNSET:
            field_dict["gmv_ranges"] = gmv_ranges
        if units_sold_ranges is not UNSET:
            field_dict["units_sold_ranges"] = units_sold_ranges
        if category is not UNSET:
            field_dict["category"] = category
        if content_performance is not UNSET:
            field_dict["content_performance"] = content_performance
        if affiliate_data is not UNSET:
            field_dict["affiliate_data"] = affiliate_data
        if advanced_filters is not UNSET:
            field_dict["advanced_filters"] = advanced_filters
        if data_groups is not UNSET:
            field_dict["data_groups"] = data_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_creators_in_creator_marketplace_request_advanced_filter import (
            SearchCreatorsInCreatorMarketplaceRequestAdvancedFilter,  # noqa: PLC0415
        )
        from ..models.search_creators_in_creator_marketplace_request_affiliate_data import (
            SearchCreatorsInCreatorMarketplaceRequestAffiliateData,  # noqa: PLC0415
        )
        from ..models.search_creators_in_creator_marketplace_request_category import (
            SearchCreatorsInCreatorMarketplaceRequestCategory,  # noqa: PLC0415
        )
        from ..models.search_creators_in_creator_marketplace_request_content_performance import (
            SearchCreatorsInCreatorMarketplaceRequestContentPerformance,  # noqa: PLC0415
        )
        from ..models.search_creators_in_creator_marketplace_request_follower_demographic import (
            SearchCreatorsInCreatorMarketplaceRequestFollowerDemographic,  # noqa: PLC0415
        )

        d = dict(src_dict)
        search_key = d.pop("search_key", UNSET)

        keyword = d.pop("keyword", UNSET)

        _follower_demographics = d.pop("follower_demographics", UNSET)
        follower_demographics: SearchCreatorsInCreatorMarketplaceRequestFollowerDemographic | Unset
        if isinstance(_follower_demographics, Unset):
            follower_demographics = UNSET
        else:
            follower_demographics = SearchCreatorsInCreatorMarketplaceRequestFollowerDemographic.from_dict(
                _follower_demographics
            )

        gmv_ranges = cast(list[str], d.pop("gmv_ranges", UNSET))

        units_sold_ranges = cast(list[str], d.pop("units_sold_ranges", UNSET))

        _category = d.pop("category", UNSET)
        category: list[SearchCreatorsInCreatorMarketplaceRequestCategory] | Unset = UNSET
        if _category is not UNSET:
            category = []
            for category_item_data in _category:
                category_item = SearchCreatorsInCreatorMarketplaceRequestCategory.from_dict(category_item_data)

                category.append(category_item)

        _content_performance = d.pop("content_performance", UNSET)
        content_performance: SearchCreatorsInCreatorMarketplaceRequestContentPerformance | Unset
        if isinstance(_content_performance, Unset):
            content_performance = UNSET
        else:
            content_performance = SearchCreatorsInCreatorMarketplaceRequestContentPerformance.from_dict(
                _content_performance
            )

        _affiliate_data = d.pop("affiliate_data", UNSET)
        affiliate_data: SearchCreatorsInCreatorMarketplaceRequestAffiliateData | Unset
        if isinstance(_affiliate_data, Unset):
            affiliate_data = UNSET
        else:
            affiliate_data = SearchCreatorsInCreatorMarketplaceRequestAffiliateData.from_dict(_affiliate_data)

        _advanced_filters = d.pop("advanced_filters", UNSET)
        advanced_filters: SearchCreatorsInCreatorMarketplaceRequestAdvancedFilter | Unset
        if isinstance(_advanced_filters, Unset):
            advanced_filters = UNSET
        else:
            advanced_filters = SearchCreatorsInCreatorMarketplaceRequestAdvancedFilter.from_dict(_advanced_filters)

        data_groups = cast(list[str], d.pop("data_groups", UNSET))

        search_creators_in_creator_marketplace_request = cls(
            search_key=search_key,
            keyword=keyword,
            follower_demographics=follower_demographics,
            gmv_ranges=gmv_ranges,
            units_sold_ranges=units_sold_ranges,
            category=category,
            content_performance=content_performance,
            affiliate_data=affiliate_data,
            advanced_filters=advanced_filters,
            data_groups=data_groups,
        )

        search_creators_in_creator_marketplace_request.additional_properties = d
        return search_creators_in_creator_marketplace_request

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
