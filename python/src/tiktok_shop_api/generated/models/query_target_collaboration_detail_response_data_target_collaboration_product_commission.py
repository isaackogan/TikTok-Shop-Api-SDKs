from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryTargetCollaborationDetailResponseDataTargetCollaborationProductCommission")


@_attrs_define
class QueryTargetCollaborationDetailResponseDataTargetCollaborationProductCommission:
    """
    Attributes:
        rate (int | Unset): The commission rate in hundredths of a percent. For example, 3587 is a commission rate of
            35.87%. This value must a minimum of 1000.  The range of this value is [100, 8000].
        effective_time (str | Unset): The time when the commission becomes effective, as a Unix timestamp in seconds
            represented as a string.
        currency (str | Unset): The currency code.
        minimum_amount (str | Unset): The minimum estimated commission amount for all SKUs of this product.
        maximum_amount (str | Unset): The maximum estimated commission amount for all SKUs of this product.
        shop_ads_commission_rate (int | Unset): The commission rate applies only to orders generated from ads. If a
            creator’s video is used as an ad without this rate being set, the resulting orders will instead earn either:
            - The Shop Ads commission you configured in open collaboration, or
            - The standard commission defined in this invitation.
            The commission rate is specified in increments of 1/10,000.
            For example, 1000 stands for 0.1 or 10%.
    """

    rate: int | Unset = UNSET
    effective_time: str | Unset = UNSET
    currency: str | Unset = UNSET
    minimum_amount: str | Unset = UNSET
    maximum_amount: str | Unset = UNSET
    shop_ads_commission_rate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate = self.rate

        effective_time = self.effective_time

        currency = self.currency

        minimum_amount = self.minimum_amount

        maximum_amount = self.maximum_amount

        shop_ads_commission_rate = self.shop_ads_commission_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate is not UNSET:
            field_dict["rate"] = rate
        if effective_time is not UNSET:
            field_dict["effective_time"] = effective_time
        if currency is not UNSET:
            field_dict["currency"] = currency
        if minimum_amount is not UNSET:
            field_dict["minimum_amount"] = minimum_amount
        if maximum_amount is not UNSET:
            field_dict["maximum_amount"] = maximum_amount
        if shop_ads_commission_rate is not UNSET:
            field_dict["shop_ads_commission_rate"] = shop_ads_commission_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate", UNSET)

        effective_time = d.pop("effective_time", UNSET)

        currency = d.pop("currency", UNSET)

        minimum_amount = d.pop("minimum_amount", UNSET)

        maximum_amount = d.pop("maximum_amount", UNSET)

        shop_ads_commission_rate = d.pop("shop_ads_commission_rate", UNSET)

        query_target_collaboration_detail_response_data_target_collaboration_product_commission = cls(
            rate=rate,
            effective_time=effective_time,
            currency=currency,
            minimum_amount=minimum_amount,
            maximum_amount=maximum_amount,
            shop_ads_commission_rate=shop_ads_commission_rate,
        )

        query_target_collaboration_detail_response_data_target_collaboration_product_commission.additional_properties = d
        return query_target_collaboration_detail_response_data_target_collaboration_product_commission

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
