from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_unsettled_transactions_response_data_transaction import GetUnsettledTransactionsResponseDataTransaction





T = TypeVar("T", bound="GetUnsettledTransactionsResponseData")



@_attrs_define
class GetUnsettledTransactionsResponseData:
    """ 
        Attributes:
            next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. If this
                value is present and non-empty, provide it in the `page_token` parameter of the next request and reuse the same
                shop context, explicit `search_time_ge`, `search_time_lt`, `sort_field`, and `sort_order` values. If this value
                is absent or empty, pagination is complete.
            total_count (int | Unset): The total number of matching unsettled transaction records across all pages.
            sum_est_settlement_amount (str | Unset): The sum of the estimated settlement amount.
            sum_est_revenue_amount (str | Unset): The sum of the estimated revenue amount.
            sum_est_adjustment_amount (str | Unset): The sum of the estimated adjustment amount.
            sum_est_fee_amount (str | Unset): The sum of the estimated fee amount.
            transactions (list[GetUnsettledTransactionsResponseDataTransaction] | Unset): The list of transaction records in
                the statement. Each transaction corresponds to an order, an adjustment, or a reserve-related transaction.
     """

    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    sum_est_settlement_amount: str | Unset = UNSET
    sum_est_revenue_amount: str | Unset = UNSET
    sum_est_adjustment_amount: str | Unset = UNSET
    sum_est_fee_amount: str | Unset = UNSET
    transactions: list[GetUnsettledTransactionsResponseDataTransaction] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_unsettled_transactions_response_data_transaction import GetUnsettledTransactionsResponseDataTransaction # noqa: PLC0415
        next_page_token = self.next_page_token

        total_count = self.total_count

        sum_est_settlement_amount = self.sum_est_settlement_amount

        sum_est_revenue_amount = self.sum_est_revenue_amount

        sum_est_adjustment_amount = self.sum_est_adjustment_amount

        sum_est_fee_amount = self.sum_est_fee_amount

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
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if sum_est_settlement_amount is not UNSET:
            field_dict["sum_est_settlement_amount"] = sum_est_settlement_amount
        if sum_est_revenue_amount is not UNSET:
            field_dict["sum_est_revenue_amount"] = sum_est_revenue_amount
        if sum_est_adjustment_amount is not UNSET:
            field_dict["sum_est_adjustment_amount"] = sum_est_adjustment_amount
        if sum_est_fee_amount is not UNSET:
            field_dict["sum_est_fee_amount"] = sum_est_fee_amount
        if transactions is not UNSET:
            field_dict["transactions"] = transactions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_unsettled_transactions_response_data_transaction import GetUnsettledTransactionsResponseDataTransaction # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        sum_est_settlement_amount = d.pop("sum_est_settlement_amount", UNSET)

        sum_est_revenue_amount = d.pop("sum_est_revenue_amount", UNSET)

        sum_est_adjustment_amount = d.pop("sum_est_adjustment_amount", UNSET)

        sum_est_fee_amount = d.pop("sum_est_fee_amount", UNSET)

        _transactions = d.pop("transactions", UNSET)
        transactions: list[GetUnsettledTransactionsResponseDataTransaction] | Unset = UNSET
        if _transactions is not UNSET:
            transactions = []
            for transactions_item_data in _transactions:
                transactions_item = GetUnsettledTransactionsResponseDataTransaction.from_dict(transactions_item_data)



                transactions.append(transactions_item)


        get_unsettled_transactions_response_data = cls(
            next_page_token=next_page_token,
            total_count=total_count,
            sum_est_settlement_amount=sum_est_settlement_amount,
            sum_est_revenue_amount=sum_est_revenue_amount,
            sum_est_adjustment_amount=sum_est_adjustment_amount,
            sum_est_fee_amount=sum_est_fee_amount,
            transactions=transactions,
        )


        get_unsettled_transactions_response_data.additional_properties = d
        return get_unsettled_transactions_response_data

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
