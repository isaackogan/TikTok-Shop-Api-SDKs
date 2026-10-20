from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_transactions_by_order_response_data_sku_transaction_shipping_cost_breakdown_supplementary_component import (
        GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdownSupplementaryComponent,
    )


T = TypeVar("T", bound="GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdown")


@_attrs_define
class GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdown:
    """
    Attributes:
        actual_shipping_fee_amount (str | Unset): The actual shipping fee calculated based on the weight/dimensions
            measured by the carrier. For details, check `shipping_cost_breakdown.supplementary_component`.
        international_leg_logistics_amount (str | Unset): The delivery fee charged to the seller for the international
            leg of a cross-border shipment
        shipping_fee_discount_amount (str | Unset): The shipping fee subsidies and incentives provided by the platform.
            This includes all subsidies regardless of fulfillment channels or policies. For details, check
            `shipping_cost_breakdown.supplementary_component`.
        customer_paid_shipping_fee_amount (str | Unset): The actual shipping fee borne by the customer, calculated based
            on the product weight uploaded by the seller. Negative numbers refer to the refunded amount of customer-paid
            shipping fees
        return_shipping_fee_amount (str | Unset): The shipping fee paid by the seller for the delivery of returns.
        replacement_shipping_fee_amount (str | Unset): The shipping fee paid by the seller for the delivery of goods
            replacement.
            Applicable only for Indonesia.
        exchange_shipping_fee_amount (str | Unset): The shipping fee paid by the seller for the delivery of goods
            exchange.
            Applicable only for Indonesia.
        signature_confirmation_fee_amount (str | Unset): The fee incurred for packages requiring signature confirmation
            services
        shipping_insurance_fee_amount (str | Unset): The shipping insurance fee incurred by the seller for purchasing
            additional TikTok shipping insurance services.
        fbt_fulfillment_fee_reimbursement_amount (str | Unset): A reimbursement from TikTok Shop for Fulfilled by TikTok
            (FBT) orders that don't qualify for free shipping.
            Applicable only for the US.
        return_shipping_label_fee_amount (str | Unset): The fee borne by the customer to cover the cost of return
            labels. This fee is collected on the seller's behalf and settled according to the agreed payment terms.
        seller_self_shipping_service_fee_amount (str | Unset): A service fee charged for orders shipped through your own
            logistics provider. Applies to packages that don't meet the exemption criteria.
        return_shipping_fee_paid_buyer_amount (str | Unset): Reimbursement for the shipping fees paid by customers to
            return packages
        failed_delivery_subsidy_amount (str | Unset): For shipping fee from failed deliveries, you pay up to a standard
            rate, and TikTok Shop covers the remaining amount.
        fbt_free_shipping_fee_amount (str | Unset): This is the fee that you cover when offering customers free shipping
            through FBT.
        free_return_subsidy_amount (str | Unset): Reimbursement for the platform-funded portion of return shipping fees,
            as part of the free returns offered to customers.
        distant_shipping_fee_amount (str | Unset): The distance fee for shipping paid by the customer. With your current
            settings for Horizon+ Program, this fee is included in product price for orders with shipping out of Java
            island.
        shipping_app_service_fee_amount (str | Unset): Shipping App Service Fee for using shipping fee to generate
            shipping labels
        logistics_service_fee (str | Unset): A fee charged to sellers throughout the order lifecycle for logistics-
            related services, including processing, coordination, handling of delivery-related matters, and basic shipping
            incentives. It is an amount per order, which is based on the parcel's weight tier and shipping route. It allows
            the platform to continuously enhance a high-quality, sustainable logistics network that serves both sellers and
            customers better over the long term, amidst changing global conditions.
        fbt_overall_merchant_subsidy (str | Unset): Subsidy applied to your orders and offered to all FBT (Fulfilled by
            TikTok) merchants for the statement period. The amount is calculated based on your qualifying FBT order volume
            during this period.
        fbt_key_merchant_subsidy (str | Unset): Subsidy applied to your orders based on eligibility for the key merchant
            program. The amount is calculated based on your qualifying FBT (Fulfilled by TikTok) order volume during the
            statement period.
        tiktok_shop_shipping_incentive_amount (str | Unset): The shipping fee incentive provided by TikTok Shop.
        supplementary_component
            (GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdownSupplementaryComponent | Unset):
        hazmat_noncompliance_fee (str | Unset): Fee charged when a parcel containing hazardous materials is shipped
            without the required declaration or compliant packaging, as assessed by the carrier. Charged when the parcel is
            delivered.
        hazmat_handling_fee (str | Unset): Fee charged for the additional handling required to ship a parcel containing
            hazardous materials. Charged when the parcel is delivered.
        non_standard_weight_fee (str | Unset): Fee charged when a parcel exceeds the standard weight range. The rate is
            set by TikTok Shop and charged when the parcel is delivered.
        non_standard_dimension_fee (str | Unset): Fee charged when a parcel exceeds the standard size range. The rate is
            set by TikTok Shop and charged when the parcel is delivered.
    """

    actual_shipping_fee_amount: str | Unset = UNSET
    international_leg_logistics_amount: str | Unset = UNSET
    shipping_fee_discount_amount: str | Unset = UNSET
    customer_paid_shipping_fee_amount: str | Unset = UNSET
    return_shipping_fee_amount: str | Unset = UNSET
    replacement_shipping_fee_amount: str | Unset = UNSET
    exchange_shipping_fee_amount: str | Unset = UNSET
    signature_confirmation_fee_amount: str | Unset = UNSET
    shipping_insurance_fee_amount: str | Unset = UNSET
    fbt_fulfillment_fee_reimbursement_amount: str | Unset = UNSET
    return_shipping_label_fee_amount: str | Unset = UNSET
    seller_self_shipping_service_fee_amount: str | Unset = UNSET
    return_shipping_fee_paid_buyer_amount: str | Unset = UNSET
    failed_delivery_subsidy_amount: str | Unset = UNSET
    fbt_free_shipping_fee_amount: str | Unset = UNSET
    free_return_subsidy_amount: str | Unset = UNSET
    distant_shipping_fee_amount: str | Unset = UNSET
    shipping_app_service_fee_amount: str | Unset = UNSET
    logistics_service_fee: str | Unset = UNSET
    fbt_overall_merchant_subsidy: str | Unset = UNSET
    fbt_key_merchant_subsidy: str | Unset = UNSET
    tiktok_shop_shipping_incentive_amount: str | Unset = UNSET
    supplementary_component: (
        GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdownSupplementaryComponent | Unset
    ) = UNSET
    hazmat_noncompliance_fee: str | Unset = UNSET
    hazmat_handling_fee: str | Unset = UNSET
    non_standard_weight_fee: str | Unset = UNSET
    non_standard_dimension_fee: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actual_shipping_fee_amount = self.actual_shipping_fee_amount

        international_leg_logistics_amount = self.international_leg_logistics_amount

        shipping_fee_discount_amount = self.shipping_fee_discount_amount

        customer_paid_shipping_fee_amount = self.customer_paid_shipping_fee_amount

        return_shipping_fee_amount = self.return_shipping_fee_amount

        replacement_shipping_fee_amount = self.replacement_shipping_fee_amount

        exchange_shipping_fee_amount = self.exchange_shipping_fee_amount

        signature_confirmation_fee_amount = self.signature_confirmation_fee_amount

        shipping_insurance_fee_amount = self.shipping_insurance_fee_amount

        fbt_fulfillment_fee_reimbursement_amount = self.fbt_fulfillment_fee_reimbursement_amount

        return_shipping_label_fee_amount = self.return_shipping_label_fee_amount

        seller_self_shipping_service_fee_amount = self.seller_self_shipping_service_fee_amount

        return_shipping_fee_paid_buyer_amount = self.return_shipping_fee_paid_buyer_amount

        failed_delivery_subsidy_amount = self.failed_delivery_subsidy_amount

        fbt_free_shipping_fee_amount = self.fbt_free_shipping_fee_amount

        free_return_subsidy_amount = self.free_return_subsidy_amount

        distant_shipping_fee_amount = self.distant_shipping_fee_amount

        shipping_app_service_fee_amount = self.shipping_app_service_fee_amount

        logistics_service_fee = self.logistics_service_fee

        fbt_overall_merchant_subsidy = self.fbt_overall_merchant_subsidy

        fbt_key_merchant_subsidy = self.fbt_key_merchant_subsidy

        tiktok_shop_shipping_incentive_amount = self.tiktok_shop_shipping_incentive_amount

        supplementary_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supplementary_component, Unset):
            supplementary_component = self.supplementary_component.to_dict()

        hazmat_noncompliance_fee = self.hazmat_noncompliance_fee

        hazmat_handling_fee = self.hazmat_handling_fee

        non_standard_weight_fee = self.non_standard_weight_fee

        non_standard_dimension_fee = self.non_standard_dimension_fee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if actual_shipping_fee_amount is not UNSET:
            field_dict["actual_shipping_fee_amount"] = actual_shipping_fee_amount
        if international_leg_logistics_amount is not UNSET:
            field_dict["international_leg_logistics_amount"] = international_leg_logistics_amount
        if shipping_fee_discount_amount is not UNSET:
            field_dict["shipping_fee_discount_amount"] = shipping_fee_discount_amount
        if customer_paid_shipping_fee_amount is not UNSET:
            field_dict["customer_paid_shipping_fee_amount"] = customer_paid_shipping_fee_amount
        if return_shipping_fee_amount is not UNSET:
            field_dict["return_shipping_fee_amount"] = return_shipping_fee_amount
        if replacement_shipping_fee_amount is not UNSET:
            field_dict["replacement_shipping_fee_amount"] = replacement_shipping_fee_amount
        if exchange_shipping_fee_amount is not UNSET:
            field_dict["exchange_shipping_fee_amount"] = exchange_shipping_fee_amount
        if signature_confirmation_fee_amount is not UNSET:
            field_dict["signature_confirmation_fee_amount"] = signature_confirmation_fee_amount
        if shipping_insurance_fee_amount is not UNSET:
            field_dict["shipping_insurance_fee_amount"] = shipping_insurance_fee_amount
        if fbt_fulfillment_fee_reimbursement_amount is not UNSET:
            field_dict["fbt_fulfillment_fee_reimbursement_amount"] = fbt_fulfillment_fee_reimbursement_amount
        if return_shipping_label_fee_amount is not UNSET:
            field_dict["return_shipping_label_fee_amount"] = return_shipping_label_fee_amount
        if seller_self_shipping_service_fee_amount is not UNSET:
            field_dict["seller_self_shipping_service_fee_amount"] = seller_self_shipping_service_fee_amount
        if return_shipping_fee_paid_buyer_amount is not UNSET:
            field_dict["return_shipping_fee_paid_buyer_amount"] = return_shipping_fee_paid_buyer_amount
        if failed_delivery_subsidy_amount is not UNSET:
            field_dict["failed_delivery_subsidy_amount"] = failed_delivery_subsidy_amount
        if fbt_free_shipping_fee_amount is not UNSET:
            field_dict["fbt_free_shipping_fee_amount"] = fbt_free_shipping_fee_amount
        if free_return_subsidy_amount is not UNSET:
            field_dict["free_return_subsidy_amount"] = free_return_subsidy_amount
        if distant_shipping_fee_amount is not UNSET:
            field_dict["distant_shipping_fee_amount"] = distant_shipping_fee_amount
        if shipping_app_service_fee_amount is not UNSET:
            field_dict["shipping_app_service_fee_amount"] = shipping_app_service_fee_amount
        if logistics_service_fee is not UNSET:
            field_dict["logistics_service_fee"] = logistics_service_fee
        if fbt_overall_merchant_subsidy is not UNSET:
            field_dict["fbt_overall_merchant_subsidy"] = fbt_overall_merchant_subsidy
        if fbt_key_merchant_subsidy is not UNSET:
            field_dict["fbt_key_merchant_subsidy"] = fbt_key_merchant_subsidy
        if tiktok_shop_shipping_incentive_amount is not UNSET:
            field_dict["tiktok_shop_shipping_incentive_amount"] = tiktok_shop_shipping_incentive_amount
        if supplementary_component is not UNSET:
            field_dict["supplementary_component"] = supplementary_component
        if hazmat_noncompliance_fee is not UNSET:
            field_dict["hazmat_noncompliance_fee"] = hazmat_noncompliance_fee
        if hazmat_handling_fee is not UNSET:
            field_dict["hazmat_handling_fee"] = hazmat_handling_fee
        if non_standard_weight_fee is not UNSET:
            field_dict["non_standard_weight_fee"] = non_standard_weight_fee
        if non_standard_dimension_fee is not UNSET:
            field_dict["non_standard_dimension_fee"] = non_standard_dimension_fee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_transactions_by_order_response_data_sku_transaction_shipping_cost_breakdown_supplementary_component import (
            GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdownSupplementaryComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        actual_shipping_fee_amount = d.pop("actual_shipping_fee_amount", UNSET)

        international_leg_logistics_amount = d.pop("international_leg_logistics_amount", UNSET)

        shipping_fee_discount_amount = d.pop("shipping_fee_discount_amount", UNSET)

        customer_paid_shipping_fee_amount = d.pop("customer_paid_shipping_fee_amount", UNSET)

        return_shipping_fee_amount = d.pop("return_shipping_fee_amount", UNSET)

        replacement_shipping_fee_amount = d.pop("replacement_shipping_fee_amount", UNSET)

        exchange_shipping_fee_amount = d.pop("exchange_shipping_fee_amount", UNSET)

        signature_confirmation_fee_amount = d.pop("signature_confirmation_fee_amount", UNSET)

        shipping_insurance_fee_amount = d.pop("shipping_insurance_fee_amount", UNSET)

        fbt_fulfillment_fee_reimbursement_amount = d.pop("fbt_fulfillment_fee_reimbursement_amount", UNSET)

        return_shipping_label_fee_amount = d.pop("return_shipping_label_fee_amount", UNSET)

        seller_self_shipping_service_fee_amount = d.pop("seller_self_shipping_service_fee_amount", UNSET)

        return_shipping_fee_paid_buyer_amount = d.pop("return_shipping_fee_paid_buyer_amount", UNSET)

        failed_delivery_subsidy_amount = d.pop("failed_delivery_subsidy_amount", UNSET)

        fbt_free_shipping_fee_amount = d.pop("fbt_free_shipping_fee_amount", UNSET)

        free_return_subsidy_amount = d.pop("free_return_subsidy_amount", UNSET)

        distant_shipping_fee_amount = d.pop("distant_shipping_fee_amount", UNSET)

        shipping_app_service_fee_amount = d.pop("shipping_app_service_fee_amount", UNSET)

        logistics_service_fee = d.pop("logistics_service_fee", UNSET)

        fbt_overall_merchant_subsidy = d.pop("fbt_overall_merchant_subsidy", UNSET)

        fbt_key_merchant_subsidy = d.pop("fbt_key_merchant_subsidy", UNSET)

        tiktok_shop_shipping_incentive_amount = d.pop("tiktok_shop_shipping_incentive_amount", UNSET)

        _supplementary_component = d.pop("supplementary_component", UNSET)
        supplementary_component: (
            GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdownSupplementaryComponent | Unset
        )
        if isinstance(_supplementary_component, Unset):
            supplementary_component = UNSET
        else:
            supplementary_component = (
                GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdownSupplementaryComponent.from_dict(
                    _supplementary_component
                )
            )

        hazmat_noncompliance_fee = d.pop("hazmat_noncompliance_fee", UNSET)

        hazmat_handling_fee = d.pop("hazmat_handling_fee", UNSET)

        non_standard_weight_fee = d.pop("non_standard_weight_fee", UNSET)

        non_standard_dimension_fee = d.pop("non_standard_dimension_fee", UNSET)

        get_transactions_by_order_response_data_sku_transaction_shipping_cost_breakdown = cls(
            actual_shipping_fee_amount=actual_shipping_fee_amount,
            international_leg_logistics_amount=international_leg_logistics_amount,
            shipping_fee_discount_amount=shipping_fee_discount_amount,
            customer_paid_shipping_fee_amount=customer_paid_shipping_fee_amount,
            return_shipping_fee_amount=return_shipping_fee_amount,
            replacement_shipping_fee_amount=replacement_shipping_fee_amount,
            exchange_shipping_fee_amount=exchange_shipping_fee_amount,
            signature_confirmation_fee_amount=signature_confirmation_fee_amount,
            shipping_insurance_fee_amount=shipping_insurance_fee_amount,
            fbt_fulfillment_fee_reimbursement_amount=fbt_fulfillment_fee_reimbursement_amount,
            return_shipping_label_fee_amount=return_shipping_label_fee_amount,
            seller_self_shipping_service_fee_amount=seller_self_shipping_service_fee_amount,
            return_shipping_fee_paid_buyer_amount=return_shipping_fee_paid_buyer_amount,
            failed_delivery_subsidy_amount=failed_delivery_subsidy_amount,
            fbt_free_shipping_fee_amount=fbt_free_shipping_fee_amount,
            free_return_subsidy_amount=free_return_subsidy_amount,
            distant_shipping_fee_amount=distant_shipping_fee_amount,
            shipping_app_service_fee_amount=shipping_app_service_fee_amount,
            logistics_service_fee=logistics_service_fee,
            fbt_overall_merchant_subsidy=fbt_overall_merchant_subsidy,
            fbt_key_merchant_subsidy=fbt_key_merchant_subsidy,
            tiktok_shop_shipping_incentive_amount=tiktok_shop_shipping_incentive_amount,
            supplementary_component=supplementary_component,
            hazmat_noncompliance_fee=hazmat_noncompliance_fee,
            hazmat_handling_fee=hazmat_handling_fee,
            non_standard_weight_fee=non_standard_weight_fee,
            non_standard_dimension_fee=non_standard_dimension_fee,
        )

        get_transactions_by_order_response_data_sku_transaction_shipping_cost_breakdown.additional_properties = d
        return get_transactions_by_order_response_data_sku_transaction_shipping_cost_breakdown

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
