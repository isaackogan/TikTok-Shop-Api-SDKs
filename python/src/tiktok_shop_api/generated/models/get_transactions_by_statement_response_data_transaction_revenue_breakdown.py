from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTransactionsByStatementResponseDataTransactionRevenueBreakdown")


@_attrs_define
class GetTransactionsByStatementResponseDataTransactionRevenueBreakdown:
    """
    Attributes:
        subtotal_before_discount_amount (str | Unset): The total price of all order items before any seller discounts
            and platform discounts are deducted. This is equivalent to the shop's gross sales.
        refund_subtotal_before_discount_amount (str | Unset): The total price of all refunded items before any seller
            discounts. This is equivalent to the shop's gross sales refund.
        seller_discount_amount (str | Unset): The total amount of discounts funded by the seller, including:
            - Seller promotions (Product Discount, Flash Deal, Buy More Save More, Voucher and Bundle Deal)
            - Seller's portion of a co-funded voucher discount in co-funding campaigns
            - Seller discounts during a campaign
        seller_discount_refund_amount (str | Unset): Discounts returned to the sellers due to returns or refunds.
        cod_service_fee_amount (str | Unset): The cash on delivery service fees charged to buyers.
            Applicable only for Saudi Arabia.
        refund_cod_service_fee_amount (str | Unset): The refund for cash on delivery service fees.
            Applicable only for Saudi Arabia.
        distant_item_fee_amount (str | Unset): The distance fee for items paid by the customer. With your current
            settings for Horizon+ Program, this fee is included in product price for orders with shipping out of Java
            island.
    """

    subtotal_before_discount_amount: str | Unset = UNSET
    refund_subtotal_before_discount_amount: str | Unset = UNSET
    seller_discount_amount: str | Unset = UNSET
    seller_discount_refund_amount: str | Unset = UNSET
    cod_service_fee_amount: str | Unset = UNSET
    refund_cod_service_fee_amount: str | Unset = UNSET
    distant_item_fee_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subtotal_before_discount_amount = self.subtotal_before_discount_amount

        refund_subtotal_before_discount_amount = self.refund_subtotal_before_discount_amount

        seller_discount_amount = self.seller_discount_amount

        seller_discount_refund_amount = self.seller_discount_refund_amount

        cod_service_fee_amount = self.cod_service_fee_amount

        refund_cod_service_fee_amount = self.refund_cod_service_fee_amount

        distant_item_fee_amount = self.distant_item_fee_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subtotal_before_discount_amount is not UNSET:
            field_dict["subtotal_before_discount_amount"] = subtotal_before_discount_amount
        if refund_subtotal_before_discount_amount is not UNSET:
            field_dict["refund_subtotal_before_discount_amount"] = refund_subtotal_before_discount_amount
        if seller_discount_amount is not UNSET:
            field_dict["seller_discount_amount"] = seller_discount_amount
        if seller_discount_refund_amount is not UNSET:
            field_dict["seller_discount_refund_amount"] = seller_discount_refund_amount
        if cod_service_fee_amount is not UNSET:
            field_dict["cod_service_fee_amount"] = cod_service_fee_amount
        if refund_cod_service_fee_amount is not UNSET:
            field_dict["refund_cod_service_fee_amount"] = refund_cod_service_fee_amount
        if distant_item_fee_amount is not UNSET:
            field_dict["distant_item_fee_amount"] = distant_item_fee_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subtotal_before_discount_amount = d.pop("subtotal_before_discount_amount", UNSET)

        refund_subtotal_before_discount_amount = d.pop("refund_subtotal_before_discount_amount", UNSET)

        seller_discount_amount = d.pop("seller_discount_amount", UNSET)

        seller_discount_refund_amount = d.pop("seller_discount_refund_amount", UNSET)

        cod_service_fee_amount = d.pop("cod_service_fee_amount", UNSET)

        refund_cod_service_fee_amount = d.pop("refund_cod_service_fee_amount", UNSET)

        distant_item_fee_amount = d.pop("distant_item_fee_amount", UNSET)

        get_transactions_by_statement_response_data_transaction_revenue_breakdown = cls(
            subtotal_before_discount_amount=subtotal_before_discount_amount,
            refund_subtotal_before_discount_amount=refund_subtotal_before_discount_amount,
            seller_discount_amount=seller_discount_amount,
            seller_discount_refund_amount=seller_discount_refund_amount,
            cod_service_fee_amount=cod_service_fee_amount,
            refund_cod_service_fee_amount=refund_cod_service_fee_amount,
            distant_item_fee_amount=distant_item_fee_amount,
        )

        get_transactions_by_statement_response_data_transaction_revenue_breakdown.additional_properties = d
        return get_transactions_by_statement_response_data_transaction_revenue_breakdown

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
