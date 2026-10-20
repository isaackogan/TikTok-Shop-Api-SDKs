from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOpportunityDetailResponseDataOpportunityMarketData")


@_attrs_define
class GetOpportunityDetailResponseDataOpportunityMarketData:
    """
    Attributes:
        est_market_sales_volume (str | Unset): Estimated market sales volume for the last 30 days, returned as an
            approximate bucket: `<100`, a value rounded down to a hundreds bucket ending in `00+`, a `k+` or `M+` value, or
            `100M+`.
        est_market_gmv (str | Unset): Estimated market sales GMV in USD for the last 30 days, returned as an approximate
            bucket: `<100`, a value rounded down to a hundreds bucket ending in `00+`, a `k+` or `M+` value, or `100M+`.
        market_buzz (str | Unset): Popularity level of the product: HOT / HIGH / MEDIUM
        search_volume (str | Unset): TikTok Shop in-site search volume, rounded to the nearest whole number and returned
            as a decimal string.
        search_keyword (str | Unset): Comma-separated TikTok Shop in-site search keywords associated with the
            opportunity.
        competitor_product_count (str | Unset): Approximate number of competing products listed in the last 30 days,
            returned as one of `< 10`, `< 50`, `< 100`, or `100+`.
        competitor_seller_count (str | Unset): Number of competing sellers with the products currently listed.
    """

    est_market_sales_volume: str | Unset = UNSET
    est_market_gmv: str | Unset = UNSET
    market_buzz: str | Unset = UNSET
    search_volume: str | Unset = UNSET
    search_keyword: str | Unset = UNSET
    competitor_product_count: str | Unset = UNSET
    competitor_seller_count: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        est_market_sales_volume = self.est_market_sales_volume

        est_market_gmv = self.est_market_gmv

        market_buzz = self.market_buzz

        search_volume = self.search_volume

        search_keyword = self.search_keyword

        competitor_product_count = self.competitor_product_count

        competitor_seller_count = self.competitor_seller_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if est_market_sales_volume is not UNSET:
            field_dict["est_market_sales_volume"] = est_market_sales_volume
        if est_market_gmv is not UNSET:
            field_dict["est_market_gmv"] = est_market_gmv
        if market_buzz is not UNSET:
            field_dict["market_buzz"] = market_buzz
        if search_volume is not UNSET:
            field_dict["search_volume"] = search_volume
        if search_keyword is not UNSET:
            field_dict["search_keyword"] = search_keyword
        if competitor_product_count is not UNSET:
            field_dict["competitor_product_count"] = competitor_product_count
        if competitor_seller_count is not UNSET:
            field_dict["competitor_seller_count"] = competitor_seller_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        est_market_sales_volume = d.pop("est_market_sales_volume", UNSET)

        est_market_gmv = d.pop("est_market_gmv", UNSET)

        market_buzz = d.pop("market_buzz", UNSET)

        search_volume = d.pop("search_volume", UNSET)

        search_keyword = d.pop("search_keyword", UNSET)

        competitor_product_count = d.pop("competitor_product_count", UNSET)

        competitor_seller_count = d.pop("competitor_seller_count", UNSET)

        get_opportunity_detail_response_data_opportunity_market_data = cls(
            est_market_sales_volume=est_market_sales_volume,
            est_market_gmv=est_market_gmv,
            market_buzz=market_buzz,
            search_volume=search_volume,
            search_keyword=search_keyword,
            competitor_product_count=competitor_product_count,
            competitor_seller_count=competitor_seller_count,
        )

        get_opportunity_detail_response_data_opportunity_market_data.additional_properties = d
        return get_opportunity_detail_response_data_opportunity_market_data

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
