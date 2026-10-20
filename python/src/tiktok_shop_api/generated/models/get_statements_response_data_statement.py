from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetStatementsResponseDataStatement")



@_attrs_define
class GetStatementsResponseDataStatement:
    """ 
        Attributes:
            id (str | Unset): The statement ID.
            statement_time (int | Unset): The time when the statement was generated, expressed as a Unix timestamp in
                seconds.
                Statements are generated daily at 00:00 UTC and include all transactions from the previous day.
            settlement_amount (str | Unset): The settlement amount.
            currency (str | Unset): The currency code in ISO 4217 format.
            revenue_amount (str | Unset): The final revenue amount at the time of order settlement.
                Applicable for all regions except UK and US.
            fee_amount (str | Unset): The fees charged by TikTok Shop at the time of order settlement. An order is deemed
                settled a certain number of days after delivery (varies by region) if no returns or refunds are pending.

                **Note**: Shipping-related costs are excluded, except for local sellers in the SEA region, where they are
                included.
            adjustment_amount (str | Unset): The adjustment amount.
                For more details about the reason for adjustment, refer to the [Get Statement Transactions
                API](https://partner.tiktokshop.com/docv2/page/650a6749defece02be67da87).
            payment_status (str | Unset): The payment status, indicating whether payment has been transferred to the
                seller's bank account or settled to the seller's account.
                Possible values:
                - PAID: Payment has been transferred to the seller.
                - FAILED: Payment transfer failed.
                - PROCESSING: Payment is currently being processed.
                - SETTLED: Funds have been settled to the seller's account.
            payment_id (str | Unset): The payment ID.
            net_sales_amount (str | Unset): The final revenue amount after seller discounts are deducted.
                Applicable only for local sellers outside the SEA region.
            shipping_cost_amount (str | Unset): The shipping fees.
                Applicable only for local sellers outside the SEA region.
            payment_time (int | Unset): The Unix payment timestamp
     """

    id: str | Unset = UNSET
    statement_time: int | Unset = UNSET
    settlement_amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    revenue_amount: str | Unset = UNSET
    fee_amount: str | Unset = UNSET
    adjustment_amount: str | Unset = UNSET
    payment_status: str | Unset = UNSET
    payment_id: str | Unset = UNSET
    net_sales_amount: str | Unset = UNSET
    shipping_cost_amount: str | Unset = UNSET
    payment_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        statement_time = self.statement_time

        settlement_amount = self.settlement_amount

        currency = self.currency

        revenue_amount = self.revenue_amount

        fee_amount = self.fee_amount

        adjustment_amount = self.adjustment_amount

        payment_status = self.payment_status

        payment_id = self.payment_id

        net_sales_amount = self.net_sales_amount

        shipping_cost_amount = self.shipping_cost_amount

        payment_time = self.payment_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if statement_time is not UNSET:
            field_dict["statement_time"] = statement_time
        if settlement_amount is not UNSET:
            field_dict["settlement_amount"] = settlement_amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if revenue_amount is not UNSET:
            field_dict["revenue_amount"] = revenue_amount
        if fee_amount is not UNSET:
            field_dict["fee_amount"] = fee_amount
        if adjustment_amount is not UNSET:
            field_dict["adjustment_amount"] = adjustment_amount
        if payment_status is not UNSET:
            field_dict["payment_status"] = payment_status
        if payment_id is not UNSET:
            field_dict["payment_id"] = payment_id
        if net_sales_amount is not UNSET:
            field_dict["net_sales_amount"] = net_sales_amount
        if shipping_cost_amount is not UNSET:
            field_dict["shipping_cost_amount"] = shipping_cost_amount
        if payment_time is not UNSET:
            field_dict["payment_time"] = payment_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        statement_time = d.pop("statement_time", UNSET)

        settlement_amount = d.pop("settlement_amount", UNSET)

        currency = d.pop("currency", UNSET)

        revenue_amount = d.pop("revenue_amount", UNSET)

        fee_amount = d.pop("fee_amount", UNSET)

        adjustment_amount = d.pop("adjustment_amount", UNSET)

        payment_status = d.pop("payment_status", UNSET)

        payment_id = d.pop("payment_id", UNSET)

        net_sales_amount = d.pop("net_sales_amount", UNSET)

        shipping_cost_amount = d.pop("shipping_cost_amount", UNSET)

        payment_time = d.pop("payment_time", UNSET)

        get_statements_response_data_statement = cls(
            id=id,
            statement_time=statement_time,
            settlement_amount=settlement_amount,
            currency=currency,
            revenue_amount=revenue_amount,
            fee_amount=fee_amount,
            adjustment_amount=adjustment_amount,
            payment_status=payment_status,
            payment_id=payment_id,
            net_sales_amount=net_sales_amount,
            shipping_cost_amount=shipping_cost_amount,
            payment_time=payment_time,
        )


        get_statements_response_data_statement.additional_properties = d
        return get_statements_response_data_statement

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
