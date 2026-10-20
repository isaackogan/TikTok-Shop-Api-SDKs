from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_transactions_by_order_response_data_sku_transaction_fee_tax_breakdown_fee import (
        GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownFee,
    )
    from ..models.get_transactions_by_order_response_data_sku_transaction_fee_tax_breakdown_tax import (
        GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownTax,
    )


T = TypeVar("T", bound="GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdown")


@_attrs_define
class GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdown:
    """
    Attributes:
        fee (GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownFee | Unset):
        tax (GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownTax | Unset):
    """

    fee: GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownFee | Unset = UNSET
    tax: GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownTax | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fee, Unset):
            fee = self.fee.to_dict()

        tax: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tax, Unset):
            tax = self.tax.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fee is not UNSET:
            field_dict["fee"] = fee
        if tax is not UNSET:
            field_dict["tax"] = tax

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_transactions_by_order_response_data_sku_transaction_fee_tax_breakdown_fee import (
            GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownFee,  # noqa: PLC0415
        )
        from ..models.get_transactions_by_order_response_data_sku_transaction_fee_tax_breakdown_tax import (
            GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownTax,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _fee = d.pop("fee", UNSET)
        fee: GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownFee | Unset
        if isinstance(_fee, Unset):
            fee = UNSET
        else:
            fee = GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownFee.from_dict(_fee)

        _tax = d.pop("tax", UNSET)
        tax: GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownTax | Unset
        if isinstance(_tax, Unset):
            tax = UNSET
        else:
            tax = GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownTax.from_dict(_tax)

        get_transactions_by_order_response_data_sku_transaction_fee_tax_breakdown = cls(
            fee=fee,
            tax=tax,
        )

        get_transactions_by_order_response_data_sku_transaction_fee_tax_breakdown.additional_properties = d
        return get_transactions_by_order_response_data_sku_transaction_fee_tax_breakdown

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
