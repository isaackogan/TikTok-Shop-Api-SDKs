from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_transactions_by_statement_response_data_total_settlement_breakdown import GetTransactionsByStatementResponseDataTotalSettlementBreakdown
  from ..models.get_transactions_by_statement_response_data_transaction import GetTransactionsByStatementResponseDataTransaction





T = TypeVar("T", bound="GetTransactionsByStatementResponseData")



@_attrs_define
class GetTransactionsByStatementResponseData:
    """ 
        Attributes:
            next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. If this
                value is present and non-empty, provide it in the `page_token` parameter of your next request. If this value is
                absent or empty, there are no more results to retrieve.
            id (str | Unset): The statement ID.
            create_time (int | Unset): The time when the statement was generated, as a Unix timestamp in seconds.
                Statements are generated daily at 00:00 UTC.
            status (str | Unset): The statement status. Only supports `SETTLED`.
            currency (str | Unset): The three-letter currency code in ISO 4217 format.
            payable_amount (str | Unset): The final amount paid out after accounting for reserve funds.
                Formula: total_settlement_amount + total_reserve_amount
            total_reserve_amount (str | Unset): The total amount withheld from settlement based on TikTok Shop Reserve
                Policy. Refer to TikTok Shop Academy for more information.
                - A positive amount indicates the funds that have been released.
                - A negative amount indicates the funds being withheld from the settlement.

                Applicable only for UK and US local sellers.
            total_settlement_amount (str | Unset): The total settlement amount.

                Formula: total_revenue_amount - total_shipping_cost_amount - total_fee_tax_amount - total_adjustment_amount
            total_settlement_breakdown (GetTransactionsByStatementResponseDataTotalSettlementBreakdown | Unset):
            total_count (int | Unset): The number of transaction records in the statement.
            transactions (list[GetTransactionsByStatementResponseDataTransaction] | Unset): The list of transaction records
                in the statement. Each transaction corresponds to an order, an adjustment, or a reserve-related transaction.
     """

    next_page_token: str | Unset = UNSET
    id: str | Unset = UNSET
    create_time: int | Unset = UNSET
    status: str | Unset = UNSET
    currency: str | Unset = UNSET
    payable_amount: str | Unset = UNSET
    total_reserve_amount: str | Unset = UNSET
    total_settlement_amount: str | Unset = UNSET
    total_settlement_breakdown: GetTransactionsByStatementResponseDataTotalSettlementBreakdown | Unset = UNSET
    total_count: int | Unset = UNSET
    transactions: list[GetTransactionsByStatementResponseDataTransaction] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_transactions_by_statement_response_data_total_settlement_breakdown import GetTransactionsByStatementResponseDataTotalSettlementBreakdown # noqa: PLC0415
        from ..models.get_transactions_by_statement_response_data_transaction import GetTransactionsByStatementResponseDataTransaction # noqa: PLC0415
        next_page_token = self.next_page_token

        id = self.id

        create_time = self.create_time

        status = self.status

        currency = self.currency

        payable_amount = self.payable_amount

        total_reserve_amount = self.total_reserve_amount

        total_settlement_amount = self.total_settlement_amount

        total_settlement_breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_settlement_breakdown, Unset):
            total_settlement_breakdown = self.total_settlement_breakdown.to_dict()

        total_count = self.total_count

        transactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.transactions, Unset):
            transactions = []
            for transactions_item_data in self.transactions:
                transactions_item = transactions_item_data.to_dict()
                transactions.append(transactions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if id is not UNSET:
            field_dict["id"] = id
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if status is not UNSET:
            field_dict["status"] = status
        if currency is not UNSET:
            field_dict["currency"] = currency
        if payable_amount is not UNSET:
            field_dict["payable_amount"] = payable_amount
        if total_reserve_amount is not UNSET:
            field_dict["total_reserve_amount"] = total_reserve_amount
        if total_settlement_amount is not UNSET:
            field_dict["total_settlement_amount"] = total_settlement_amount
        if total_settlement_breakdown is not UNSET:
            field_dict["total_settlement_breakdown"] = total_settlement_breakdown
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if transactions is not UNSET:
            field_dict["transactions"] = transactions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_transactions_by_statement_response_data_total_settlement_breakdown import GetTransactionsByStatementResponseDataTotalSettlementBreakdown # noqa: PLC0415
        from ..models.get_transactions_by_statement_response_data_transaction import GetTransactionsByStatementResponseDataTransaction # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        id = d.pop("id", UNSET)

        create_time = d.pop("create_time", UNSET)

        status = d.pop("status", UNSET)

        currency = d.pop("currency", UNSET)

        payable_amount = d.pop("payable_amount", UNSET)

        total_reserve_amount = d.pop("total_reserve_amount", UNSET)

        total_settlement_amount = d.pop("total_settlement_amount", UNSET)

        _total_settlement_breakdown = d.pop("total_settlement_breakdown", UNSET)
        total_settlement_breakdown: GetTransactionsByStatementResponseDataTotalSettlementBreakdown | Unset
        if isinstance(_total_settlement_breakdown,  Unset):
            total_settlement_breakdown = UNSET
        else:
            total_settlement_breakdown = GetTransactionsByStatementResponseDataTotalSettlementBreakdown.from_dict(_total_settlement_breakdown)




        total_count = d.pop("total_count", UNSET)

        _transactions = d.pop("transactions", UNSET)
        transactions: list[GetTransactionsByStatementResponseDataTransaction] | Unset = UNSET
        if _transactions is not UNSET:
            transactions = []
            for transactions_item_data in _transactions:
                transactions_item = GetTransactionsByStatementResponseDataTransaction.from_dict(transactions_item_data)



                transactions.append(transactions_item)


        get_transactions_by_statement_response_data = cls(
            next_page_token=next_page_token,
            id=id,
            create_time=create_time,
            status=status,
            currency=currency,
            payable_amount=payable_amount,
            total_reserve_amount=total_reserve_amount,
            total_settlement_amount=total_settlement_amount,
            total_settlement_breakdown=total_settlement_breakdown,
            total_count=total_count,
            transactions=transactions,
        )


        get_transactions_by_statement_response_data.additional_properties = d
        return get_transactions_by_statement_response_data

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
