from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShopSKPPSummaryResponseDataShopSummary")


@_attrs_define
class GetShopSKPPSummaryResponseDataShopSummary:
    """
    Attributes:
        qualified_products_count (int | Unset): Number of products that are already SKPP.
        eligible_products_count (int | Unset): Number of products that are already SKPP, plus those that have not yet
            met the standard but can take SKPP tasks.
        earned_ad_credit (str | Unset): Total ad credit earned by the shop, currency-prefixed.
        increased_visibility_l30d (str | Unset): Incremental visibility gained from SKPP rewards in the last 30 days.
    """

    qualified_products_count: int | Unset = UNSET
    eligible_products_count: int | Unset = UNSET
    earned_ad_credit: str | Unset = UNSET
    increased_visibility_l30d: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        qualified_products_count = self.qualified_products_count

        eligible_products_count = self.eligible_products_count

        earned_ad_credit = self.earned_ad_credit

        increased_visibility_l30d = self.increased_visibility_l30d

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if qualified_products_count is not UNSET:
            field_dict["qualified_products_count"] = qualified_products_count
        if eligible_products_count is not UNSET:
            field_dict["eligible_products_count"] = eligible_products_count
        if earned_ad_credit is not UNSET:
            field_dict["earned_ad_credit"] = earned_ad_credit
        if increased_visibility_l30d is not UNSET:
            field_dict["increased_visibility_l30d"] = increased_visibility_l30d

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        qualified_products_count = d.pop("qualified_products_count", UNSET)

        eligible_products_count = d.pop("eligible_products_count", UNSET)

        earned_ad_credit = d.pop("earned_ad_credit", UNSET)

        increased_visibility_l30d = d.pop("increased_visibility_l30d", UNSET)

        get_shop_skpp_summary_response_data_shop_summary = cls(
            qualified_products_count=qualified_products_count,
            eligible_products_count=eligible_products_count,
            earned_ad_credit=earned_ad_credit,
            increased_visibility_l30d=increased_visibility_l30d,
        )

        get_shop_skpp_summary_response_data_shop_summary.additional_properties = d
        return get_shop_skpp_summary_response_data_shop_summary

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
