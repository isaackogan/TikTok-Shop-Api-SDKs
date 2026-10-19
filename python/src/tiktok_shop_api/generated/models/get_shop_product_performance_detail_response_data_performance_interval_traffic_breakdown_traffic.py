from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownTraffic")


@_attrs_define
class GetShopProductPerformanceDetailResponseDataPerformanceIntervalTrafficBreakdownTraffic:
    """
    Attributes:
        impressions (int | Unset): Each time a link to your listing appears in the shop tab, it's counted as one
            impression. Users can tap links to visit your listings page directly.
        page_views (int | Unset): Total number of product details page views during the selected period, including
            multiple views from unique users.
        avg_unique_page_views (int | Unset): Daily average unique views visitors to your product details pages.
        ctr (str | Unset): The percentage of viewers who clicked on product links after seeing them in the Shop tab.
            Number of clicks divided by the number of views.
        avg_conversion_rate (str | Unset): Average percentage of unique page views that result in sales.
    """

    impressions: int | Unset = UNSET
    page_views: int | Unset = UNSET
    avg_unique_page_views: int | Unset = UNSET
    ctr: str | Unset = UNSET
    avg_conversion_rate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        impressions = self.impressions

        page_views = self.page_views

        avg_unique_page_views = self.avg_unique_page_views

        ctr = self.ctr

        avg_conversion_rate = self.avg_conversion_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if impressions is not UNSET:
            field_dict["impressions"] = impressions
        if page_views is not UNSET:
            field_dict["page_views"] = page_views
        if avg_unique_page_views is not UNSET:
            field_dict["avg_unique_page_views"] = avg_unique_page_views
        if ctr is not UNSET:
            field_dict["ctr"] = ctr
        if avg_conversion_rate is not UNSET:
            field_dict["avg_conversion_rate"] = avg_conversion_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        impressions = d.pop("impressions", UNSET)

        page_views = d.pop("page_views", UNSET)

        avg_unique_page_views = d.pop("avg_unique_page_views", UNSET)

        ctr = d.pop("ctr", UNSET)

        avg_conversion_rate = d.pop("avg_conversion_rate", UNSET)

        get_shop_product_performance_detail_response_data_performance_interval_traffic_breakdown_traffic = cls(
            impressions=impressions,
            page_views=page_views,
            avg_unique_page_views=avg_unique_page_views,
            ctr=ctr,
            avg_conversion_rate=avg_conversion_rate,
        )

        get_shop_product_performance_detail_response_data_performance_interval_traffic_breakdown_traffic.additional_properties = d
        return get_shop_product_performance_detail_response_data_performance_interval_traffic_breakdown_traffic

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
