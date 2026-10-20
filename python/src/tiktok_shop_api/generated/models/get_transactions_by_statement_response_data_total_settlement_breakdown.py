from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetTransactionsByStatementResponseDataTotalSettlementBreakdown")



@_attrs_define
class GetTransactionsByStatementResponseDataTotalSettlementBreakdown:
    """ 
        Attributes:
            total_revenue_amount (str | Unset): The total revenue amount at the time of order settlement. This is equivalent
                to the net sales amount.
            total_shipping_cost_amount (str | Unset): The total shipping costs at the time of order settlement.
            total_fee_tax_amount (str | Unset): The total fees and taxes charged by the platform at the time of order
                settlement. Shipping-related costs are excluded.
            total_adjustment_amount (str | Unset): The total adjustment amount based on TikTok Shop policy.
                Refer to `transactions.type` for the list of adjustment-related policies.
     """

    total_revenue_amount: str | Unset = UNSET
    total_shipping_cost_amount: str | Unset = UNSET
    total_fee_tax_amount: str | Unset = UNSET
    total_adjustment_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total_revenue_amount = self.total_revenue_amount

        total_shipping_cost_amount = self.total_shipping_cost_amount

        total_fee_tax_amount = self.total_fee_tax_amount

        total_adjustment_amount = self.total_adjustment_amount


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if total_revenue_amount is not UNSET:
            field_dict["total_revenue_amount"] = total_revenue_amount
        if total_shipping_cost_amount is not UNSET:
            field_dict["total_shipping_cost_amount"] = total_shipping_cost_amount
        if total_fee_tax_amount is not UNSET:
            field_dict["total_fee_tax_amount"] = total_fee_tax_amount
        if total_adjustment_amount is not UNSET:
            field_dict["total_adjustment_amount"] = total_adjustment_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_revenue_amount = d.pop("total_revenue_amount", UNSET)

        total_shipping_cost_amount = d.pop("total_shipping_cost_amount", UNSET)

        total_fee_tax_amount = d.pop("total_fee_tax_amount", UNSET)

        total_adjustment_amount = d.pop("total_adjustment_amount", UNSET)

        get_transactions_by_statement_response_data_total_settlement_breakdown = cls(
            total_revenue_amount=total_revenue_amount,
            total_shipping_cost_amount=total_shipping_cost_amount,
            total_fee_tax_amount=total_fee_tax_amount,
            total_adjustment_amount=total_adjustment_amount,
        )


        get_transactions_by_statement_response_data_total_settlement_breakdown.additional_properties = d
        return get_transactions_by_statement_response_data_total_settlement_breakdown

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
