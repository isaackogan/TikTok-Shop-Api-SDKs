from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_creator_performance_for_campaign_product_response_data_promotion_creator import (
        GetCreatorPerformanceForCampaignProductResponseDataPromotionCreator,
    )


T = TypeVar("T", bound="GetCreatorPerformanceForCampaignProductResponseData")


@_attrs_define
class GetCreatorPerformanceForCampaignProductResponseData:
    """
    Attributes:
        total_creator_count (int | Unset): The total number of creators associated with the specified product in the
            campaign across all pages.
        promotion_creators (list[GetCreatorPerformanceForCampaignProductResponseDataPromotionCreator] | Unset): A list
            of objects representing information about the Affiliate Creator associated with the product promotion.
        next_page_token (str | Unset): Opaque token for retrieving the next page. When this value is non-empty, pass it
            as the `page_token` query parameter in the next request and reuse the same `campaign_id`, `product_id`, and
            `page_size`. An empty token means there are no more results.
    """

    total_creator_count: int | Unset = UNSET
    promotion_creators: list[GetCreatorPerformanceForCampaignProductResponseDataPromotionCreator] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_creator_count = self.total_creator_count

        promotion_creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.promotion_creators, Unset):
            promotion_creators = []
            for promotion_creators_item_data in self.promotion_creators:
                promotion_creators_item = promotion_creators_item_data.to_dict()
                promotion_creators.append(promotion_creators_item)

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_creator_count is not UNSET:
            field_dict["total_creator_count"] = total_creator_count
        if promotion_creators is not UNSET:
            field_dict["promotion_creators"] = promotion_creators
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creator_performance_for_campaign_product_response_data_promotion_creator import (
            GetCreatorPerformanceForCampaignProductResponseDataPromotionCreator,  # noqa: PLC0415
        )

        d = dict(src_dict)
        total_creator_count = d.pop("total_creator_count", UNSET)

        _promotion_creators = d.pop("promotion_creators", UNSET)
        promotion_creators: list[GetCreatorPerformanceForCampaignProductResponseDataPromotionCreator] | Unset = UNSET
        if _promotion_creators is not UNSET:
            promotion_creators = []
            for promotion_creators_item_data in _promotion_creators:
                promotion_creators_item = GetCreatorPerformanceForCampaignProductResponseDataPromotionCreator.from_dict(
                    promotion_creators_item_data
                )

                promotion_creators.append(promotion_creators_item)

        next_page_token = d.pop("next_page_token", UNSET)

        get_creator_performance_for_campaign_product_response_data = cls(
            total_creator_count=total_creator_count,
            promotion_creators=promotion_creators,
            next_page_token=next_page_token,
        )

        get_creator_performance_for_campaign_product_response_data.additional_properties = d
        return get_creator_performance_for_campaign_product_response_data

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
