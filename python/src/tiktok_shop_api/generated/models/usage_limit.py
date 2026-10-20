from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageLimit")


@_attrs_define
class UsageLimit:
    """
    Attributes:
        single_buyer_claim_limit (int | Unset): The number of times a single buyer can claim the coupon.
        total_claim_limit (int | Unset): The total number of claims allowed for the coupon across all buyers.
        redemption_limit (int | Unset): The number of times that a claimed coupon can be redeemed across all buyers.
            (Only available in ID, MY, PH, TH, SG, VN regions.)
    """

    single_buyer_claim_limit: int | Unset = UNSET
    total_claim_limit: int | Unset = UNSET
    redemption_limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        single_buyer_claim_limit = self.single_buyer_claim_limit

        total_claim_limit = self.total_claim_limit

        redemption_limit = self.redemption_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if single_buyer_claim_limit is not UNSET:
            field_dict["single_buyer_claim_limit"] = single_buyer_claim_limit
        if total_claim_limit is not UNSET:
            field_dict["total_claim_limit"] = total_claim_limit
        if redemption_limit is not UNSET:
            field_dict["redemption_limit"] = redemption_limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        single_buyer_claim_limit = d.pop("single_buyer_claim_limit", UNSET)

        total_claim_limit = d.pop("total_claim_limit", UNSET)

        redemption_limit = d.pop("redemption_limit", UNSET)

        usage_limit = cls(
            single_buyer_claim_limit=single_buyer_claim_limit,
            total_claim_limit=total_claim_limit,
            redemption_limit=redemption_limit,
        )

        usage_limit.additional_properties = d
        return usage_limit

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
