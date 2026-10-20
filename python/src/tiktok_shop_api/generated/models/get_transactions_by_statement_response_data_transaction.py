from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_transactions_by_statement_response_data_transaction_fee_tax_breakdown import (
        GetTransactionsByStatementResponseDataTransactionFeeTaxBreakdown,
    )
    from ..models.get_transactions_by_statement_response_data_transaction_revenue_breakdown import (
        GetTransactionsByStatementResponseDataTransactionRevenueBreakdown,
    )
    from ..models.get_transactions_by_statement_response_data_transaction_shipping_cost_breakdown import (
        GetTransactionsByStatementResponseDataTransactionShippingCostBreakdown,
    )
    from ..models.get_transactions_by_statement_response_data_transaction_supplementary_component import (
        GetTransactionsByStatementResponseDataTransactionSupplementaryComponent,
    )


T = TypeVar("T", bound="GetTransactionsByStatementResponseDataTransaction")


@_attrs_define
class GetTransactionsByStatementResponseDataTransaction:
    """
    Attributes:
        id (str | Unset): The transaction ID.
        type_ (str | Unset): The transaction type.

            **Standard transactions**
            - `ORDER`: A transaction related to an order settlement.
            - `RESERVE`: A transaction involving collection or release of reserve funds.
            - If the transaction is an adjustment, it returns one of the following values:

            **Platform-related adjustments**
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
            - `COFUNDED_CREATOR_REWARDS`: Fees charged for joining the co-funded creator rewards program to reward creator
            activities.
            - `STAMP_DUTY`: To comply with Thailand's tax regulations, TikTok Shop withholds and remits the stamp duty
            levied on the withholding tax agent appointment letter. This document falls under Instrument No. 21 (Agency) and
            is subject to a THB 30 stamp duty.

            **Logistics-related adjustments**
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
            - `SELLER_MISSION_REWARD`: Platform provided cash reward for seller mission completion.
            - `Violation fee （settlement fee）`: The deduction to cover the cost of buyer's losses for the unpleasant
            experience of the buyer due to an issue that is the seller's responsibility.
            - `Violation fee （credit card）`: The amount owed to TikTok Shop from previous transactions, charged to your
            primary credit card.
            - `Bill payment （negative balance）`: The amount you owe TikTok Shop, charged to your primary credit card.
            -  `Sales proceed（negative balance） `:Sales proceed that is ready to pay for negeative balance.
            -  `Bill deduction for negative balance `:Deduction for the amount you owe TikTok Shop after all platform fees
            are deducted from your net earnings.

            **Miscellaneous adjustments**
            `OTHER_ADJUSTMENT`: Adjustment for other reasons.
        order_id (str | Unset): The order ID.
            Each transaction can only be associated with an order ID or an adjustment ID.
        order_create_time (int | Unset): The time when the order was created, as a Unix timestamp in seconds.
        adjustment_id (str | Unset): The adjustment ID if the transaction is an adjustment.
            Each transaction can only be associated with an order ID or an adjustment ID.
        adjustment_order_id (str | Unset): The order ID associated with the adjustment, if any.
        adjustment_amount (str | Unset): The adjustment amount based on TikTok Shop policy.
            Refer to `transactions.type` for the list of adjustment-related policies.
        settlement_amount (str | Unset): The settlement amount for the order.

            Formula: revenue_amount - shipping_cost_amount - fee_tax_amount - adjustment_amount
        revenue_amount (str | Unset): The revenue amount at the time of order settlement. This is equivalent to the sum
            of all amounts in `revenue_breakdown`.
        revenue_breakdown (GetTransactionsByStatementResponseDataTransactionRevenueBreakdown | Unset):
        shipping_cost_amount (str | Unset): The shipping costs at the time of order settlement. This is equivalent to
            the sum of all contributory amounts in `shipping_cost_breakdown`.
        shipping_cost_breakdown (GetTransactionsByStatementResponseDataTransactionShippingCostBreakdown | Unset):
        fee_tax_amount (str | Unset): The total fees and taxes charged by TikTok Shop at the time of order settlement.
            Shipping-related costs are excluded. This is equivalent to the sum of all contributory amounts in
            `fee_tax_breakdown`.
        fee_tax_breakdown (GetTransactionsByStatementResponseDataTransactionFeeTaxBreakdown | Unset):
        supplementary_component (GetTransactionsByStatementResponseDataTransactionSupplementaryComponent | Unset):
        reserve_id (str | Unset): The ID of a reserve transaction.
        reserve_amount (str | Unset): The amount withheld from settlement based on TikTok Shop Reserve Policy. Refer to
            TikTok Shop Academy for more information.
            - A positive amount indicates funds that have been released.
            - A negative amount indicates funds being withheld from the settlement.
        associated_order_id (str | Unset): The order ID associated with the reserve transaction.
        reserve_status (str | Unset): The status of the reserve funds.
            Possible values:
            - COLLECTED: A portion of the order's settlement amount has been withheld as reserve funds.
            - RELEASED: The previously reserved funds have been released and paid out to the seller.
        estimated_release_time (str | Unset): The estimated date when the reserve funds will be released and paid out to
            the seller. Unix timestamp.
            Returns an empty value if the reserve funds have already been released.
    """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    order_id: str | Unset = UNSET
    order_create_time: int | Unset = UNSET
    adjustment_id: str | Unset = UNSET
    adjustment_order_id: str | Unset = UNSET
    adjustment_amount: str | Unset = UNSET
    settlement_amount: str | Unset = UNSET
    revenue_amount: str | Unset = UNSET
    revenue_breakdown: GetTransactionsByStatementResponseDataTransactionRevenueBreakdown | Unset = UNSET
    shipping_cost_amount: str | Unset = UNSET
    shipping_cost_breakdown: GetTransactionsByStatementResponseDataTransactionShippingCostBreakdown | Unset = UNSET
    fee_tax_amount: str | Unset = UNSET
    fee_tax_breakdown: GetTransactionsByStatementResponseDataTransactionFeeTaxBreakdown | Unset = UNSET
    supplementary_component: GetTransactionsByStatementResponseDataTransactionSupplementaryComponent | Unset = UNSET
    reserve_id: str | Unset = UNSET
    reserve_amount: str | Unset = UNSET
    associated_order_id: str | Unset = UNSET
    reserve_status: str | Unset = UNSET
    estimated_release_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        order_id = self.order_id

        order_create_time = self.order_create_time

        adjustment_id = self.adjustment_id

        adjustment_order_id = self.adjustment_order_id

        adjustment_amount = self.adjustment_amount

        settlement_amount = self.settlement_amount

        revenue_amount = self.revenue_amount

        revenue_breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.revenue_breakdown, Unset):
            revenue_breakdown = self.revenue_breakdown.to_dict()

        shipping_cost_amount = self.shipping_cost_amount

        shipping_cost_breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shipping_cost_breakdown, Unset):
            shipping_cost_breakdown = self.shipping_cost_breakdown.to_dict()

        fee_tax_amount = self.fee_tax_amount

        fee_tax_breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fee_tax_breakdown, Unset):
            fee_tax_breakdown = self.fee_tax_breakdown.to_dict()

        supplementary_component: dict[str, Any] | Unset = UNSET
        if not isinstance(self.supplementary_component, Unset):
            supplementary_component = self.supplementary_component.to_dict()

        reserve_id = self.reserve_id

        reserve_amount = self.reserve_amount

        associated_order_id = self.associated_order_id

        reserve_status = self.reserve_status

        estimated_release_time = self.estimated_release_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if order_create_time is not UNSET:
            field_dict["order_create_time"] = order_create_time
        if adjustment_id is not UNSET:
            field_dict["adjustment_id"] = adjustment_id
        if adjustment_order_id is not UNSET:
            field_dict["adjustment_order_id"] = adjustment_order_id
        if adjustment_amount is not UNSET:
            field_dict["adjustment_amount"] = adjustment_amount
        if settlement_amount is not UNSET:
            field_dict["settlement_amount"] = settlement_amount
        if revenue_amount is not UNSET:
            field_dict["revenue_amount"] = revenue_amount
        if revenue_breakdown is not UNSET:
            field_dict["revenue_breakdown"] = revenue_breakdown
        if shipping_cost_amount is not UNSET:
            field_dict["shipping_cost_amount"] = shipping_cost_amount
        if shipping_cost_breakdown is not UNSET:
            field_dict["shipping_cost_breakdown"] = shipping_cost_breakdown
        if fee_tax_amount is not UNSET:
            field_dict["fee_tax_amount"] = fee_tax_amount
        if fee_tax_breakdown is not UNSET:
            field_dict["fee_tax_breakdown"] = fee_tax_breakdown
        if supplementary_component is not UNSET:
            field_dict["supplementary_component"] = supplementary_component
        if reserve_id is not UNSET:
            field_dict["reserve_id"] = reserve_id
        if reserve_amount is not UNSET:
            field_dict["reserve_amount"] = reserve_amount
        if associated_order_id is not UNSET:
            field_dict["associated_order_id"] = associated_order_id
        if reserve_status is not UNSET:
            field_dict["reserve_status"] = reserve_status
        if estimated_release_time is not UNSET:
            field_dict["estimated_release_time"] = estimated_release_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_transactions_by_statement_response_data_transaction_fee_tax_breakdown import (
            GetTransactionsByStatementResponseDataTransactionFeeTaxBreakdown,  # noqa: PLC0415
        )
        from ..models.get_transactions_by_statement_response_data_transaction_revenue_breakdown import (
            GetTransactionsByStatementResponseDataTransactionRevenueBreakdown,  # noqa: PLC0415
        )
        from ..models.get_transactions_by_statement_response_data_transaction_shipping_cost_breakdown import (
            GetTransactionsByStatementResponseDataTransactionShippingCostBreakdown,  # noqa: PLC0415
        )
        from ..models.get_transactions_by_statement_response_data_transaction_supplementary_component import (
            GetTransactionsByStatementResponseDataTransactionSupplementaryComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        order_id = d.pop("order_id", UNSET)

        order_create_time = d.pop("order_create_time", UNSET)

        adjustment_id = d.pop("adjustment_id", UNSET)

        adjustment_order_id = d.pop("adjustment_order_id", UNSET)

        adjustment_amount = d.pop("adjustment_amount", UNSET)

        settlement_amount = d.pop("settlement_amount", UNSET)

        revenue_amount = d.pop("revenue_amount", UNSET)

        _revenue_breakdown = d.pop("revenue_breakdown", UNSET)
        revenue_breakdown: GetTransactionsByStatementResponseDataTransactionRevenueBreakdown | Unset
        if isinstance(_revenue_breakdown, Unset):
            revenue_breakdown = UNSET
        else:
            revenue_breakdown = GetTransactionsByStatementResponseDataTransactionRevenueBreakdown.from_dict(
                _revenue_breakdown
            )

        shipping_cost_amount = d.pop("shipping_cost_amount", UNSET)

        _shipping_cost_breakdown = d.pop("shipping_cost_breakdown", UNSET)
        shipping_cost_breakdown: GetTransactionsByStatementResponseDataTransactionShippingCostBreakdown | Unset
        if isinstance(_shipping_cost_breakdown, Unset):
            shipping_cost_breakdown = UNSET
        else:
            shipping_cost_breakdown = GetTransactionsByStatementResponseDataTransactionShippingCostBreakdown.from_dict(
                _shipping_cost_breakdown
            )

        fee_tax_amount = d.pop("fee_tax_amount", UNSET)

        _fee_tax_breakdown = d.pop("fee_tax_breakdown", UNSET)
        fee_tax_breakdown: GetTransactionsByStatementResponseDataTransactionFeeTaxBreakdown | Unset
        if isinstance(_fee_tax_breakdown, Unset):
            fee_tax_breakdown = UNSET
        else:
            fee_tax_breakdown = GetTransactionsByStatementResponseDataTransactionFeeTaxBreakdown.from_dict(
                _fee_tax_breakdown
            )

        _supplementary_component = d.pop("supplementary_component", UNSET)
        supplementary_component: GetTransactionsByStatementResponseDataTransactionSupplementaryComponent | Unset
        if isinstance(_supplementary_component, Unset):
            supplementary_component = UNSET
        else:
            supplementary_component = GetTransactionsByStatementResponseDataTransactionSupplementaryComponent.from_dict(
                _supplementary_component
            )

        reserve_id = d.pop("reserve_id", UNSET)

        reserve_amount = d.pop("reserve_amount", UNSET)

        associated_order_id = d.pop("associated_order_id", UNSET)

        reserve_status = d.pop("reserve_status", UNSET)

        estimated_release_time = d.pop("estimated_release_time", UNSET)

        get_transactions_by_statement_response_data_transaction = cls(
            id=id,
            type_=type_,
            order_id=order_id,
            order_create_time=order_create_time,
            adjustment_id=adjustment_id,
            adjustment_order_id=adjustment_order_id,
            adjustment_amount=adjustment_amount,
            settlement_amount=settlement_amount,
            revenue_amount=revenue_amount,
            revenue_breakdown=revenue_breakdown,
            shipping_cost_amount=shipping_cost_amount,
            shipping_cost_breakdown=shipping_cost_breakdown,
            fee_tax_amount=fee_tax_amount,
            fee_tax_breakdown=fee_tax_breakdown,
            supplementary_component=supplementary_component,
            reserve_id=reserve_id,
            reserve_amount=reserve_amount,
            associated_order_id=associated_order_id,
            reserve_status=reserve_status,
            estimated_release_time=estimated_release_time,
        )

        get_transactions_by_statement_response_data_transaction.additional_properties = d
        return get_transactions_by_statement_response_data_transaction

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
