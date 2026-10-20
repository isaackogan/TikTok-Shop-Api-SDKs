from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetShopPerformanceResponseDataPerformanceIntervalTraffic")



@_attrs_define
class GetShopPerformanceResponseDataPerformanceIntervalTraffic:
    """ 
        Attributes:
            avg_conversation_rate (str | Unset): The daily average percentage of unique users who paid for orders after
                viewing product detail pages during the selected period.
            avg_page_views (int | Unset): Daily average number of page views for all of your product detail pages during the
                selected period.
            avg_visitors (int | Unset): Daily average number of unique users who visited your product detail pages during
                the selected period
            product_clicks (int | Unset): Total number of product clicks during the selected period.
            product_impressions (int | Unset): Total number of product impressions during the selected period.
            unique_clicks (int | Unset): Total number of unique clicks during the selected period.
            unique_product_impressions (int | Unset): Total number of unique product impressions during the selected period.
     """

    avg_conversation_rate: str | Unset = UNSET
    avg_page_views: int | Unset = UNSET
    avg_visitors: int | Unset = UNSET
    product_clicks: int | Unset = UNSET
    product_impressions: int | Unset = UNSET
    unique_clicks: int | Unset = UNSET
    unique_product_impressions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        avg_conversation_rate = self.avg_conversation_rate

        avg_page_views = self.avg_page_views

        avg_visitors = self.avg_visitors

        product_clicks = self.product_clicks

        product_impressions = self.product_impressions

        unique_clicks = self.unique_clicks

        unique_product_impressions = self.unique_product_impressions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if avg_conversation_rate is not UNSET:
            field_dict["avg_conversation_rate"] = avg_conversation_rate
        if avg_page_views is not UNSET:
            field_dict["avg_page_views"] = avg_page_views
        if avg_visitors is not UNSET:
            field_dict["avg_visitors"] = avg_visitors
        if product_clicks is not UNSET:
            field_dict["product_clicks"] = product_clicks
        if product_impressions is not UNSET:
            field_dict["product_impressions"] = product_impressions
        if unique_clicks is not UNSET:
            field_dict["unique_clicks"] = unique_clicks
        if unique_product_impressions is not UNSET:
            field_dict["unique_product_impressions"] = unique_product_impressions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_conversation_rate = d.pop("avg_conversation_rate", UNSET)

        avg_page_views = d.pop("avg_page_views", UNSET)

        avg_visitors = d.pop("avg_visitors", UNSET)

        product_clicks = d.pop("product_clicks", UNSET)

        product_impressions = d.pop("product_impressions", UNSET)

        unique_clicks = d.pop("unique_clicks", UNSET)

        unique_product_impressions = d.pop("unique_product_impressions", UNSET)

        get_shop_performance_response_data_performance_interval_traffic = cls(
            avg_conversation_rate=avg_conversation_rate,
            avg_page_views=avg_page_views,
            avg_visitors=avg_visitors,
            product_clicks=product_clicks,
            product_impressions=product_impressions,
            unique_clicks=unique_clicks,
            unique_product_impressions=unique_product_impressions,
        )


        get_shop_performance_response_data_performance_interval_traffic.additional_properties = d
        return get_shop_performance_response_data_performance_interval_traffic

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
