from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdownSupplementaryComponent")



@_attrs_define
class GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdownSupplementaryComponent:
    """ 
        Attributes:
            fbt_fulfillment_fee_reimbursement_amount (str | Unset): (**Deprecated**: This field is deprecated and will
                return an empty string. Please refer to `shipping_cost_breakdown.fbt_fulfillment_fee_reimbursement_amount`
                instead for the relevant details.)
            platform_shipping_fee_discount_amount (str | Unset): The shipping fee discount provided in accordance with a
                campaign policy. This is part of `shipping_fee_discount_amount`.
            promo_shipping_incentive_amount (str | Unset): The additional shipping incentive that the seller will receive if
                the seller signed up for the Co-Funded Free Shipping Program. A negative amount indicates a reversal of
                incentives due to order refunds attributed to the seller's responsibility. This is part of
                `shipping_fee_discount_amount`.
            shipping_fee_subsidy_amount (str | Unset): The shipping fee subsidy funded by the platform for seller shipping.
                This is part of `shipping_fee_discount_amount`.
                - Positive amount represents a subsidy received by the seller.
                - Negative amount represents a subsidy that the seller must return to TikTok Shop.
            seller_shipping_fee_discount_amount (str | Unset): The shipping fee discount provided by sellers.
            fbt_shipping_cost_amount (str | Unset): The shipping fee incurred by the seller for orders fulfilled by TikTok
                (FBT). This is part of `actual_shipping_fee_amount`.
                Applicable only for EU and UK.
            customer_shipping_fee_offset_amount (str | Unset): The fee to offset TikTok Shop Shipping Incentive or customer-
                paid shipping fee, resulting in a net charge of $0 to the seller.
                Applicable only for the US.
            fbm_shipping_cost_amount (str | Unset): The shipping fee incurred by the seller for using TikTok Shipping. This
                is part of `actual_shipping_fee_amount`.
            fbt_fulfillment_fee_amount (str | Unset): The shipping and warehouse fulfillment fee incurred by the seller for
                orders fulfilled by TikTok (FBT). This is part of `actual_shipping_fee_amount`.
                Applicable only for the US.
            return_refund_subsidy_amount (str | Unset): For shipping fee from returns and refunds, you pay up to a standard
                rate, and TikTok Shop covers the remaining amount.This is part of `customer_paid_shipping_fee_amount`.
            refunded_customer_shipping_fee_amount (str | Unset): Shipping fee returned to customers due returns and
                refunds.Does not include subsidies.This is part of `customer_paid_shipping_fee_amount`.
            shipping_fee_guarantee_reimbursement (str | Unset): Reimbursement from the Shipping Fee Guarantee Program for
                failed deliveries or returns
     """

    fbt_fulfillment_fee_reimbursement_amount: str | Unset = UNSET
    platform_shipping_fee_discount_amount: str | Unset = UNSET
    promo_shipping_incentive_amount: str | Unset = UNSET
    shipping_fee_subsidy_amount: str | Unset = UNSET
    seller_shipping_fee_discount_amount: str | Unset = UNSET
    fbt_shipping_cost_amount: str | Unset = UNSET
    customer_shipping_fee_offset_amount: str | Unset = UNSET
    fbm_shipping_cost_amount: str | Unset = UNSET
    fbt_fulfillment_fee_amount: str | Unset = UNSET
    return_refund_subsidy_amount: str | Unset = UNSET
    refunded_customer_shipping_fee_amount: str | Unset = UNSET
    shipping_fee_guarantee_reimbursement: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        fbt_fulfillment_fee_reimbursement_amount = self.fbt_fulfillment_fee_reimbursement_amount

        platform_shipping_fee_discount_amount = self.platform_shipping_fee_discount_amount

        promo_shipping_incentive_amount = self.promo_shipping_incentive_amount

        shipping_fee_subsidy_amount = self.shipping_fee_subsidy_amount

        seller_shipping_fee_discount_amount = self.seller_shipping_fee_discount_amount

        fbt_shipping_cost_amount = self.fbt_shipping_cost_amount

        customer_shipping_fee_offset_amount = self.customer_shipping_fee_offset_amount

        fbm_shipping_cost_amount = self.fbm_shipping_cost_amount

        fbt_fulfillment_fee_amount = self.fbt_fulfillment_fee_amount

        return_refund_subsidy_amount = self.return_refund_subsidy_amount

        refunded_customer_shipping_fee_amount = self.refunded_customer_shipping_fee_amount

        shipping_fee_guarantee_reimbursement = self.shipping_fee_guarantee_reimbursement


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fbt_fulfillment_fee_reimbursement_amount is not UNSET:
            field_dict["fbt_fulfillment_fee_reimbursement_amount"] = fbt_fulfillment_fee_reimbursement_amount
        if platform_shipping_fee_discount_amount is not UNSET:
            field_dict["platform_shipping_fee_discount_amount"] = platform_shipping_fee_discount_amount
        if promo_shipping_incentive_amount is not UNSET:
            field_dict["promo_shipping_incentive_amount"] = promo_shipping_incentive_amount
        if shipping_fee_subsidy_amount is not UNSET:
            field_dict["shipping_fee_subsidy_amount"] = shipping_fee_subsidy_amount
        if seller_shipping_fee_discount_amount is not UNSET:
            field_dict["seller_shipping_fee_discount_amount"] = seller_shipping_fee_discount_amount
        if fbt_shipping_cost_amount is not UNSET:
            field_dict["fbt_shipping_cost_amount"] = fbt_shipping_cost_amount
        if customer_shipping_fee_offset_amount is not UNSET:
            field_dict["customer_shipping_fee_offset_amount"] = customer_shipping_fee_offset_amount
        if fbm_shipping_cost_amount is not UNSET:
            field_dict["fbm_shipping_cost_amount"] = fbm_shipping_cost_amount
        if fbt_fulfillment_fee_amount is not UNSET:
            field_dict["fbt_fulfillment_fee_amount"] = fbt_fulfillment_fee_amount
        if return_refund_subsidy_amount is not UNSET:
            field_dict["return_refund_subsidy_amount"] = return_refund_subsidy_amount
        if refunded_customer_shipping_fee_amount is not UNSET:
            field_dict["refunded_customer_shipping_fee_amount"] = refunded_customer_shipping_fee_amount
        if shipping_fee_guarantee_reimbursement is not UNSET:
            field_dict["shipping_fee_guarantee_reimbursement"] = shipping_fee_guarantee_reimbursement

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fbt_fulfillment_fee_reimbursement_amount = d.pop("fbt_fulfillment_fee_reimbursement_amount", UNSET)

        platform_shipping_fee_discount_amount = d.pop("platform_shipping_fee_discount_amount", UNSET)

        promo_shipping_incentive_amount = d.pop("promo_shipping_incentive_amount", UNSET)

        shipping_fee_subsidy_amount = d.pop("shipping_fee_subsidy_amount", UNSET)

        seller_shipping_fee_discount_amount = d.pop("seller_shipping_fee_discount_amount", UNSET)

        fbt_shipping_cost_amount = d.pop("fbt_shipping_cost_amount", UNSET)

        customer_shipping_fee_offset_amount = d.pop("customer_shipping_fee_offset_amount", UNSET)

        fbm_shipping_cost_amount = d.pop("fbm_shipping_cost_amount", UNSET)

        fbt_fulfillment_fee_amount = d.pop("fbt_fulfillment_fee_amount", UNSET)

        return_refund_subsidy_amount = d.pop("return_refund_subsidy_amount", UNSET)

        refunded_customer_shipping_fee_amount = d.pop("refunded_customer_shipping_fee_amount", UNSET)

        shipping_fee_guarantee_reimbursement = d.pop("shipping_fee_guarantee_reimbursement", UNSET)

        get_transactions_by_order_response_data_sku_transaction_shipping_cost_breakdown_supplementary_component = cls(
            fbt_fulfillment_fee_reimbursement_amount=fbt_fulfillment_fee_reimbursement_amount,
            platform_shipping_fee_discount_amount=platform_shipping_fee_discount_amount,
            promo_shipping_incentive_amount=promo_shipping_incentive_amount,
            shipping_fee_subsidy_amount=shipping_fee_subsidy_amount,
            seller_shipping_fee_discount_amount=seller_shipping_fee_discount_amount,
            fbt_shipping_cost_amount=fbt_shipping_cost_amount,
            customer_shipping_fee_offset_amount=customer_shipping_fee_offset_amount,
            fbm_shipping_cost_amount=fbm_shipping_cost_amount,
            fbt_fulfillment_fee_amount=fbt_fulfillment_fee_amount,
            return_refund_subsidy_amount=return_refund_subsidy_amount,
            refunded_customer_shipping_fee_amount=refunded_customer_shipping_fee_amount,
            shipping_fee_guarantee_reimbursement=shipping_fee_guarantee_reimbursement,
        )


        get_transactions_by_order_response_data_sku_transaction_shipping_cost_breakdown_supplementary_component.additional_properties = d
        return get_transactions_by_order_response_data_sku_transaction_shipping_cost_breakdown_supplementary_component

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
