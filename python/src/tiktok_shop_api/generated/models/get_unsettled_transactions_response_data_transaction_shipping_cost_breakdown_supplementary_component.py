from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUnsettledTransactionsResponseDataTransactionShippingCostBreakdownSupplementaryComponent")


@_attrs_define
class GetUnsettledTransactionsResponseDataTransactionShippingCostBreakdownSupplementaryComponent:
    """
    Attributes:
        customer_shipping_fee_offset_amount (str | Unset): The fee to offset TikTok Shop Shipping Incentive or customer-
            paid shipping fee, resulting in a net charge of $0 to the seller.
            Applicable only for the US.
        shipping_fee_subsidy_amount (str | Unset): The shipping fee subsidy funded by the platform for seller shipping.
            This is part of `shipping_fee_discount_amount`.
            - Positive amount represents a subsidy received by the seller.
            - Negative amount represents a subsidy that the seller must return to TikTok Shop.
        platform_shipping_fee_discount_amount (str | Unset): The shipping fee discount provided in accordance with a
            campaign policy.. This is part of `shipping_fee_discount_amount`.
        fbm_shipping_cost_amount (str | Unset): The shipping fee incurred by the seller for using TikTok Shipping. This
            is part of `actual_shipping_fee_amount`.
        fbt_shipping_cost_amount (str | Unset): The shipping fee incurred by the seller for orders fulfilled by TikTok
            (FBT). This is part of `actual_shipping_fee_amount`.
            Applicable for all regions except the US.
        promo_shipping_incentive_amount (str | Unset): The additional shipping incentive that the seller will receive if
            the seller signed up for the Co-Funded Free Shipping Program from 2024/08/26 to 2024/12/31. A negative amount
            indicates a reversal of incentives due to order refunds attributed to the seller's responsibility. This is part
            of `shipping_fee_discount_amount`.
        fbt_fulfillment_fee_amount (str | Unset): The shipping and warehouse fulfillment fee incurred by the seller for
            orders fulfilled by TikTok (FBT). This is part of `actual_shipping_fee_amount`.
            Applicable only for the US.
        seller_shipping_fee_discount_amount (str | Unset): The shipping fee discount provided by sellers.
    """

    customer_shipping_fee_offset_amount: str | Unset = UNSET
    shipping_fee_subsidy_amount: str | Unset = UNSET
    platform_shipping_fee_discount_amount: str | Unset = UNSET
    fbm_shipping_cost_amount: str | Unset = UNSET
    fbt_shipping_cost_amount: str | Unset = UNSET
    promo_shipping_incentive_amount: str | Unset = UNSET
    fbt_fulfillment_fee_amount: str | Unset = UNSET
    seller_shipping_fee_discount_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_shipping_fee_offset_amount = self.customer_shipping_fee_offset_amount

        shipping_fee_subsidy_amount = self.shipping_fee_subsidy_amount

        platform_shipping_fee_discount_amount = self.platform_shipping_fee_discount_amount

        fbm_shipping_cost_amount = self.fbm_shipping_cost_amount

        fbt_shipping_cost_amount = self.fbt_shipping_cost_amount

        promo_shipping_incentive_amount = self.promo_shipping_incentive_amount

        fbt_fulfillment_fee_amount = self.fbt_fulfillment_fee_amount

        seller_shipping_fee_discount_amount = self.seller_shipping_fee_discount_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_shipping_fee_offset_amount is not UNSET:
            field_dict["customer_shipping_fee_offset_amount"] = customer_shipping_fee_offset_amount
        if shipping_fee_subsidy_amount is not UNSET:
            field_dict["shipping_fee_subsidy_amount"] = shipping_fee_subsidy_amount
        if platform_shipping_fee_discount_amount is not UNSET:
            field_dict["platform_shipping_fee_discount_amount"] = platform_shipping_fee_discount_amount
        if fbm_shipping_cost_amount is not UNSET:
            field_dict["fbm_shipping_cost_amount"] = fbm_shipping_cost_amount
        if fbt_shipping_cost_amount is not UNSET:
            field_dict["fbt_shipping_cost_amount"] = fbt_shipping_cost_amount
        if promo_shipping_incentive_amount is not UNSET:
            field_dict["promo_shipping_incentive_amount"] = promo_shipping_incentive_amount
        if fbt_fulfillment_fee_amount is not UNSET:
            field_dict["fbt_fulfillment_fee_amount"] = fbt_fulfillment_fee_amount
        if seller_shipping_fee_discount_amount is not UNSET:
            field_dict["seller_shipping_fee_discount_amount"] = seller_shipping_fee_discount_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer_shipping_fee_offset_amount = d.pop("customer_shipping_fee_offset_amount", UNSET)

        shipping_fee_subsidy_amount = d.pop("shipping_fee_subsidy_amount", UNSET)

        platform_shipping_fee_discount_amount = d.pop("platform_shipping_fee_discount_amount", UNSET)

        fbm_shipping_cost_amount = d.pop("fbm_shipping_cost_amount", UNSET)

        fbt_shipping_cost_amount = d.pop("fbt_shipping_cost_amount", UNSET)

        promo_shipping_incentive_amount = d.pop("promo_shipping_incentive_amount", UNSET)

        fbt_fulfillment_fee_amount = d.pop("fbt_fulfillment_fee_amount", UNSET)

        seller_shipping_fee_discount_amount = d.pop("seller_shipping_fee_discount_amount", UNSET)

        get_unsettled_transactions_response_data_transaction_shipping_cost_breakdown_supplementary_component = cls(
            customer_shipping_fee_offset_amount=customer_shipping_fee_offset_amount,
            shipping_fee_subsidy_amount=shipping_fee_subsidy_amount,
            platform_shipping_fee_discount_amount=platform_shipping_fee_discount_amount,
            fbm_shipping_cost_amount=fbm_shipping_cost_amount,
            fbt_shipping_cost_amount=fbt_shipping_cost_amount,
            promo_shipping_incentive_amount=promo_shipping_incentive_amount,
            fbt_fulfillment_fee_amount=fbt_fulfillment_fee_amount,
            seller_shipping_fee_discount_amount=seller_shipping_fee_discount_amount,
        )

        get_unsettled_transactions_response_data_transaction_shipping_cost_breakdown_supplementary_component.additional_properties = d
        return get_unsettled_transactions_response_data_transaction_shipping_cost_breakdown_supplementary_component

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
