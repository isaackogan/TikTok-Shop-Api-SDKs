from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchCreatorsInCreatorMarketplaceRequestAffiliateData")


@_attrs_define
class SearchCreatorsInCreatorMarketplaceRequestAffiliateData:
    """
    Attributes:
        avg_commission_rate (str | Unset): - ALL
            - LESS_THAN_20%
            - LESS_THAN_15%
            - LESS_THAN_10%
            - LESS_THAN_5%
            Creator's average commission rate range based on showcase products, sales, and promoted products in the last 30
            days.
            You can only pick one value.
        post_rate (str | Unset): These categories represent how often a creator posts a shoppable video or LIVE after
            receiving a sample.
            - ALL
            - OK
            - GOOD
            - BETTER
            Every country has its own benchmark based on what is a GOOD vs BETTER fulfillment rate. BETTER is always going
            to have the highest fulfillment rate, including 100% fulfillment rate.
        creator_agency_staus (str | Unset): - AGENCY_MANAGED
            - INDEPENDENT
        is_fast_growing (bool | Unset): Top 10% of creators with the greatest increase in transactions, revenue,
            shoppable videos, live views, or followers in the last 30 days
        not_invited_l90_days (bool | Unset): True/False
            Select this filter to see creators you haven't invited in the last 90 days
    """

    avg_commission_rate: str | Unset = UNSET
    post_rate: str | Unset = UNSET
    creator_agency_staus: str | Unset = UNSET
    is_fast_growing: bool | Unset = UNSET
    not_invited_l90_days: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_commission_rate = self.avg_commission_rate

        post_rate = self.post_rate

        creator_agency_staus = self.creator_agency_staus

        is_fast_growing = self.is_fast_growing

        not_invited_l90_days = self.not_invited_l90_days

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_commission_rate is not UNSET:
            field_dict["avg_commission_rate"] = avg_commission_rate
        if post_rate is not UNSET:
            field_dict["post_rate"] = post_rate
        if creator_agency_staus is not UNSET:
            field_dict["creator_agency_staus"] = creator_agency_staus
        if is_fast_growing is not UNSET:
            field_dict["is_fast_growing"] = is_fast_growing
        if not_invited_l90_days is not UNSET:
            field_dict["not_invited_l90_days"] = not_invited_l90_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avg_commission_rate = d.pop("avg_commission_rate", UNSET)

        post_rate = d.pop("post_rate", UNSET)

        creator_agency_staus = d.pop("creator_agency_staus", UNSET)

        is_fast_growing = d.pop("is_fast_growing", UNSET)

        not_invited_l90_days = d.pop("not_invited_l90_days", UNSET)

        search_creators_in_creator_marketplace_request_affiliate_data = cls(
            avg_commission_rate=avg_commission_rate,
            post_rate=post_rate,
            creator_agency_staus=creator_agency_staus,
            is_fast_growing=is_fast_growing,
            not_invited_l90_days=not_invited_l90_days,
        )

        search_creators_in_creator_marketplace_request_affiliate_data.additional_properties = d
        return search_creators_in_creator_marketplace_request_affiliate_data

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
