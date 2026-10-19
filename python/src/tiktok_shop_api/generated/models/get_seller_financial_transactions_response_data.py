from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_seller_financial_transactions_response_data_withdrawal import (
        GetSellerFinancialTransactionsResponseDataWithdrawal,
    )


T = TypeVar("T", bound="GetSellerFinancialTransactionsResponseData")


@_attrs_define
class GetSellerFinancialTransactionsResponseData:
    """
    Attributes:
        next_page_token (str | Unset): Cursor used for searching for more information
        total_count (int | Unset): The total num of the withdraws
        withdrawals (list[GetSellerFinancialTransactionsResponseDataWithdrawal] | Unset): The list of transaction
            records matching the request filters.
    """

    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    withdrawals: list[GetSellerFinancialTransactionsResponseDataWithdrawal] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_page_token = self.next_page_token

        total_count = self.total_count

        withdrawals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.withdrawals, Unset):
            withdrawals = []
            for withdrawals_item_data in self.withdrawals:
                withdrawals_item = withdrawals_item_data.to_dict()
                withdrawals.append(withdrawals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if withdrawals is not UNSET:
            field_dict["withdrawals"] = withdrawals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_seller_financial_transactions_response_data_withdrawal import (
            GetSellerFinancialTransactionsResponseDataWithdrawal,  # noqa: PLC0415
        )

        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        _withdrawals = d.pop("withdrawals", UNSET)
        withdrawals: list[GetSellerFinancialTransactionsResponseDataWithdrawal] | Unset = UNSET
        if _withdrawals is not UNSET:
            withdrawals = []
            for withdrawals_item_data in _withdrawals:
                withdrawals_item = GetSellerFinancialTransactionsResponseDataWithdrawal.from_dict(withdrawals_item_data)

                withdrawals.append(withdrawals_item)

        get_seller_financial_transactions_response_data = cls(
            next_page_token=next_page_token,
            total_count=total_count,
            withdrawals=withdrawals,
        )

        get_seller_financial_transactions_response_data.additional_properties = d
        return get_seller_financial_transactions_response_data

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
