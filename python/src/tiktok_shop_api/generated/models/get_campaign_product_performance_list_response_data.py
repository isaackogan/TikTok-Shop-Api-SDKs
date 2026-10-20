from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_campaign_product_performance_list_response_data_campaign_product_statistic import (
        GetCampaignProductPerformanceListResponseDataCampaignProductStatistic,
    )


T = TypeVar("T", bound="GetCampaignProductPerformanceListResponseData")


@_attrs_define
class GetCampaignProductPerformanceListResponseData:
    """
    Attributes:
        total_count (int | Unset): The total count of products included in the specified campaign.
        campaign_product_statistics (list[GetCampaignProductPerformanceListResponseDataCampaignProductStatistic] |
            Unset): A list of objects representing campaign product statistics.
        next_page_token (str | Unset): The token to use as `page_token` in the next request. Keep the same `campaign_id`
            and `page_size` on subsequent requests. An empty string indicates that there are no more results.
    """

    total_count: int | Unset = UNSET
    campaign_product_statistics: list[GetCampaignProductPerformanceListResponseDataCampaignProductStatistic] | Unset = (
        UNSET
    )
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        campaign_product_statistics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.campaign_product_statistics, Unset):
            campaign_product_statistics = []
            for campaign_product_statistics_item_data in self.campaign_product_statistics:
                campaign_product_statistics_item = campaign_product_statistics_item_data.to_dict()
                campaign_product_statistics.append(campaign_product_statistics_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if campaign_product_statistics is not UNSET:
            field_dict["campaign_product_statistics"] = campaign_product_statistics
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_campaign_product_performance_list_response_data_campaign_product_statistic import (
            GetCampaignProductPerformanceListResponseDataCampaignProductStatistic,  # noqa: PLC0415
        )

        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        _campaign_product_statistics = d.pop("campaign_product_statistics", UNSET)
        campaign_product_statistics: (
            list[GetCampaignProductPerformanceListResponseDataCampaignProductStatistic] | Unset
        ) = UNSET
        if _campaign_product_statistics is not UNSET:
            campaign_product_statistics = []
            for campaign_product_statistics_item_data in _campaign_product_statistics:
                campaign_product_statistics_item = (
                    GetCampaignProductPerformanceListResponseDataCampaignProductStatistic.from_dict(
                        campaign_product_statistics_item_data
                    )
                )

                campaign_product_statistics.append(campaign_product_statistics_item)

        next_page_token = d.pop("next_page_token", UNSET)

        get_campaign_product_performance_list_response_data = cls(
            total_count=total_count,
            campaign_product_statistics=campaign_product_statistics,
            next_page_token=next_page_token,
        )

        get_campaign_product_performance_list_response_data.additional_properties = d
        return get_campaign_product_performance_list_response_data

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
