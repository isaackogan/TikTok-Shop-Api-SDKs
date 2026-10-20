from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_unsettled_transactions_response_data_transaction_fee_tax_breakdown import (
        GetUnsettledTransactionsResponseDataTransactionFeeTaxBreakdown,
    )
    from ..models.get_unsettled_transactions_response_data_transaction_shipping_cost_breakdown import (
        GetUnsettledTransactionsResponseDataTransactionShippingCostBreakdown,
    )
    from ..models.revenue_breakdown import RevenueBreakdown


T = TypeVar("T", bound="GetUnsettledTransactionsResponseDataTransaction")


@_attrs_define
class GetUnsettledTransactionsResponseDataTransaction:
    """
    Attributes:
        type_ (str | Unset): The transaction type.
            Standard transactions
            - `ORDER`: A transaction related to an order settlement.
            - If the transaction is an adjustment, it returns one of the following values:
            Platform-related adjustments
            - `CHARGE_BACK`: Charges returned to a payment card after a customer has successfully disputed an item on their
            account statement or transactions report.
            - `CUSTOMER_SERVICE_COMPENSATION`: Extra compensation or compensation paid to a customer after the after-sales
            period by customer service.
            - `DEDUCTIONS_INCURRED_BY_SELLER`: Deduction arising from customer dissatisfaction as a result of the seller's
            responsibility. This includes issues such as fraud, empty packages, items that do not match the product display
            page, or items of lower value than advertised.
            - `GMV_PAYMENT_FOR_ADS`: Amount used to pay for your advertisement if you are enabled "auto pay ads with shop
            GMV", or to pay for Tiktok Promote ads orders.
            - `PLATFORM_COMMISSION_ADJUSTMENT`: Adjustment when there are differences in the platform commission paid by the
            seller.
            - `PLATFORM_COMMISSION_COMPENSATION`: Compensation paid to the seller when there are differences in the platform
            commission paid by the seller.
            - `PLATFORM_PENALTY`: Penalty imposed for a violation of TikTok Shop policies (the corresponding amount has been
            deducted from the seller's account). For details, please refer to the email notification sent to the seller.
            - `PROMOTION_ADJUSTMENT`: Adjustment when a seller takes part in a platform promotion and there are differences
            between the promotion price and the actual amount paid by the seller.
            - `REBATE`: A discount on referral fees offered by TikTok Shop to eligible sellers.
            - `PLATFORM_COMPENSATION`: Compensation paid to the seller after the seller successfully appealed for a customer
            dispute.
            - `PLATFORM_REIMBURSEMENT`: Reimbursement paid by TikTok Shop for an order refunded under TikTok's refund
            without return policy (the seller is not responsible).
            Logistics-related adjustments
            - `FBT_WAREHOUSE_SERVICE_FEE`: Amount charged by TikTok Fulfillment Portal (Pipak) for warehousing-related bills
            incurred by the seller under the Fulfilled by TikTok (FBT) service.
            - `LOGISTICS_REIMBURSEMENT`: Reimbursement paid by TikTok Shop for an order refunded due to logistics-related
            issues (e.g. lost or damaged order).
            - `SHIPPING_FEE_ADJUSTMENT`: Adjustment when there are differences or mistakes with the shipping fee paid by the
            seller.
            - `SHIPPING_FEE_COMPENSATION`: Compensation given to sellers due to differences between the actual shipping fee
            and the pre-paid shipping fee.
            - `SHIPPING_FEE_REBATE`: Shipping fee rebate provided to the seller as part of their participation in a platform
            campaign.
            - `SAMPLE_SHIPPING_FEE`: Fees charged for sending samples using the TikTok logistics provider.
            Miscellaneous adjustments
            `OTHER_ADJUSTMENT`: Adjustment for other reasons.
        id (str | Unset): The transaction ID.
        status (str | Unset): The transaction status. Only supports `UNSETTLED`.
        currency (str | Unset): The three-letter currency code in ISO 4217 format.
        estimated_settlement (str | Unset): Estimated settlement time for the transaction.
            Possible return values:
            - A relative settlement schedule, such as `Delivered + N days`, when the order has not been delivered and only
            an approximate settlement policy is available.
            - A Unix timestamp in seconds when the order has been delivered and the estimated settlement time is available.
        unsettled_reason (str | Unset): reason for why transaction is pending for settlement
        order_create_time (int | Unset): The time when the order was created, as a Unix timestamp in seconds.
        order_delivery_time (int | Unset): The time when the order was delivered, as a Unix timestamp in seconds. No
            delivery time is available if the order has not been delivered.
        order_id (str | Unset): The order ID.
            Each transaction can only be associated with an order ID or an adjustment ID.
        adjustment_id (str | Unset): The adjustment ID if the transaction is an adjustment.
            Each transaction can only be associated with an order ID or an adjustment ID.
        adjustment_order_id (str | Unset): The order ID associated with the adjustment, if any.
        est_adjustment_amount (str | Unset): The estimated adjustment amount based on TikTok Shop policy.
            Refer to `transactions.type` for the list of adjustment-related policies.
        est_settlement_amount (str | Unset): The estimated settlement amount for the order.
            Formula: revenue_amount - shipping_cost_amount - fee_tax_amount - adjustment_amount
        est_revenue_amount (str | Unset): The estimated revenue amount. This is equivalent to the sum of all amounts in
            `revenue_breakdown`.
        revenue_breakdown (RevenueBreakdown | Unset):
        est_shipping_cost_amount (str | Unset): The estimated shipping costs, please note that when order hasn't been
            delivered, no complete shipping cost can be provided. This is equivalent to the sum of all contributory amounts
            in `shipping_cost_breakdown`.
        shipping_cost_breakdown (GetUnsettledTransactionsResponseDataTransactionShippingCostBreakdown | Unset):
        est_fee_tax_amount (str | Unset): The estimated total fees and taxes charged by TikTok Shop. Shipping-related
            costs are excluded. This is equivalent to the sum of all contributory amounts in `fee_tax_breakdown`.
        fee_tax_breakdown (GetUnsettledTransactionsResponseDataTransactionFeeTaxBreakdown | Unset):
    """

    type_: str | Unset = UNSET
    id: str | Unset = UNSET
    status: str | Unset = UNSET
    currency: str | Unset = UNSET
    estimated_settlement: str | Unset = UNSET
    unsettled_reason: str | Unset = UNSET
    order_create_time: int | Unset = UNSET
    order_delivery_time: int | Unset = UNSET
    order_id: str | Unset = UNSET
    adjustment_id: str | Unset = UNSET
    adjustment_order_id: str | Unset = UNSET
    est_adjustment_amount: str | Unset = UNSET
    est_settlement_amount: str | Unset = UNSET
    est_revenue_amount: str | Unset = UNSET
    revenue_breakdown: RevenueBreakdown | Unset = UNSET
    est_shipping_cost_amount: str | Unset = UNSET
    shipping_cost_breakdown: GetUnsettledTransactionsResponseDataTransactionShippingCostBreakdown | Unset = UNSET
    est_fee_tax_amount: str | Unset = UNSET
    fee_tax_breakdown: GetUnsettledTransactionsResponseDataTransactionFeeTaxBreakdown | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        status = self.status

        currency = self.currency

        estimated_settlement = self.estimated_settlement

        unsettled_reason = self.unsettled_reason

        order_create_time = self.order_create_time

        order_delivery_time = self.order_delivery_time

        order_id = self.order_id

        adjustment_id = self.adjustment_id

        adjustment_order_id = self.adjustment_order_id

        est_adjustment_amount = self.est_adjustment_amount

        est_settlement_amount = self.est_settlement_amount

        est_revenue_amount = self.est_revenue_amount

        revenue_breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.revenue_breakdown, Unset):
            revenue_breakdown = self.revenue_breakdown.to_dict()

        est_shipping_cost_amount = self.est_shipping_cost_amount

        shipping_cost_breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shipping_cost_breakdown, Unset):
            shipping_cost_breakdown = self.shipping_cost_breakdown.to_dict()

        est_fee_tax_amount = self.est_fee_tax_amount

        fee_tax_breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fee_tax_breakdown, Unset):
            fee_tax_breakdown = self.fee_tax_breakdown.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if estimated_settlement is not UNSET:
            field_dict["estimated_settlement"] = estimated_settlement
        if unsettled_reason is not UNSET:
            field_dict["unsettled_reason"] = unsettled_reason
        if order_create_time is not UNSET:
            field_dict["order_create_time"] = order_create_time
        if order_delivery_time is not UNSET:
            field_dict["order_delivery_time"] = order_delivery_time
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if adjustment_id is not UNSET:
            field_dict["adjustment_id"] = adjustment_id
        if adjustment_order_id is not UNSET:
            field_dict["adjustment_order_id"] = adjustment_order_id
        if est_adjustment_amount is not UNSET:
            field_dict["est_adjustment_amount"] = est_adjustment_amount
        if est_settlement_amount is not UNSET:
            field_dict["est_settlement_amount"] = est_settlement_amount
        if est_revenue_amount is not UNSET:
            field_dict["est_revenue_amount"] = est_revenue_amount
        if revenue_breakdown is not UNSET:
            field_dict["revenue_breakdown"] = revenue_breakdown
        if est_shipping_cost_amount is not UNSET:
            field_dict["est_shipping_cost_amount"] = est_shipping_cost_amount
        if shipping_cost_breakdown is not UNSET:
            field_dict["shipping_cost_breakdown"] = shipping_cost_breakdown
        if est_fee_tax_amount is not UNSET:
            field_dict["est_fee_tax_amount"] = est_fee_tax_amount
        if fee_tax_breakdown is not UNSET:
            field_dict["fee_tax_breakdown"] = fee_tax_breakdown

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_unsettled_transactions_response_data_transaction_fee_tax_breakdown import (
            GetUnsettledTransactionsResponseDataTransactionFeeTaxBreakdown,  # noqa: PLC0415
        )
        from ..models.get_unsettled_transactions_response_data_transaction_shipping_cost_breakdown import (
            GetUnsettledTransactionsResponseDataTransactionShippingCostBreakdown,  # noqa: PLC0415
        )
        from ..models.revenue_breakdown import RevenueBreakdown  # noqa: PLC0415

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        currency = d.pop("currency", UNSET)

        estimated_settlement = d.pop("estimated_settlement", UNSET)

        unsettled_reason = d.pop("unsettled_reason", UNSET)

        order_create_time = d.pop("order_create_time", UNSET)

        order_delivery_time = d.pop("order_delivery_time", UNSET)

        order_id = d.pop("order_id", UNSET)

        adjustment_id = d.pop("adjustment_id", UNSET)

        adjustment_order_id = d.pop("adjustment_order_id", UNSET)

        est_adjustment_amount = d.pop("est_adjustment_amount", UNSET)

        est_settlement_amount = d.pop("est_settlement_amount", UNSET)

        est_revenue_amount = d.pop("est_revenue_amount", UNSET)

        _revenue_breakdown = d.pop("revenue_breakdown", UNSET)
        revenue_breakdown: RevenueBreakdown | Unset
        if isinstance(_revenue_breakdown, Unset):
            revenue_breakdown = UNSET
        else:
            revenue_breakdown = RevenueBreakdown.from_dict(_revenue_breakdown)

        est_shipping_cost_amount = d.pop("est_shipping_cost_amount", UNSET)

        _shipping_cost_breakdown = d.pop("shipping_cost_breakdown", UNSET)
        shipping_cost_breakdown: GetUnsettledTransactionsResponseDataTransactionShippingCostBreakdown | Unset
        if isinstance(_shipping_cost_breakdown, Unset):
            shipping_cost_breakdown = UNSET
        else:
            shipping_cost_breakdown = GetUnsettledTransactionsResponseDataTransactionShippingCostBreakdown.from_dict(
                _shipping_cost_breakdown
            )

        est_fee_tax_amount = d.pop("est_fee_tax_amount", UNSET)

        _fee_tax_breakdown = d.pop("fee_tax_breakdown", UNSET)
        fee_tax_breakdown: GetUnsettledTransactionsResponseDataTransactionFeeTaxBreakdown | Unset
        if isinstance(_fee_tax_breakdown, Unset):
            fee_tax_breakdown = UNSET
        else:
            fee_tax_breakdown = GetUnsettledTransactionsResponseDataTransactionFeeTaxBreakdown.from_dict(
                _fee_tax_breakdown
            )

        get_unsettled_transactions_response_data_transaction = cls(
            type_=type_,
            id=id,
            status=status,
            currency=currency,
            estimated_settlement=estimated_settlement,
            unsettled_reason=unsettled_reason,
            order_create_time=order_create_time,
            order_delivery_time=order_delivery_time,
            order_id=order_id,
            adjustment_id=adjustment_id,
            adjustment_order_id=adjustment_order_id,
            est_adjustment_amount=est_adjustment_amount,
            est_settlement_amount=est_settlement_amount,
            est_revenue_amount=est_revenue_amount,
            revenue_breakdown=revenue_breakdown,
            est_shipping_cost_amount=est_shipping_cost_amount,
            shipping_cost_breakdown=shipping_cost_breakdown,
            est_fee_tax_amount=est_fee_tax_amount,
            fee_tax_breakdown=fee_tax_breakdown,
        )

        get_unsettled_transactions_response_data_transaction.additional_properties = d
        return get_unsettled_transactions_response_data_transaction

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
