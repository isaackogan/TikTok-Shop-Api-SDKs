from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_transactions_by_order_response_data_sku_transaction_fee_tax_breakdown import (
        GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdown,
    )
    from ..models.get_transactions_by_order_response_data_sku_transaction_shipping_cost_breakdown import (
        GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdown,
    )
    from ..models.revenue_breakdown import RevenueBreakdown


T = TypeVar("T", bound="GetTransactionsByOrderResponseDataSkuTransaction")


@_attrs_define
class GetTransactionsByOrderResponseDataSkuTransaction:
    """
    Attributes:
        sku_id (str | Unset): The SKU ID in TikTok Shop.
        sku_name (str | Unset): The SKU name.
        statement_id (str | Unset): The statement ID.
        product_name (str | Unset): The product title.
        quantity (str | Unset): The SKU quantity included in the order settlement.
        settlement_amount (str | Unset): The settlement amount for the SKU.
        revenue_amount (str | Unset): The revenue amount at the time of order settlement. This is equivalent to the sum
            of all amounts in `revenue_breakdown`.
        revenue_breakdown (RevenueBreakdown | Unset):
        shipping_cost_amount (str | Unset): The shipping costs at the time of order settlement. This is equivalent to
            the sum of all contributory amounts in `shipping_cost_breakdown`.
        shipping_cost_breakdown (GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdown | Unset):
        fee_tax_amount (str | Unset): The total fees and taxes charged by TikTok Shop at the time of order settlement.
            Shipping-related costs are excluded. This is equivalent to the sum of all contributory amounts in
            `fee_tax_breakdown`.
        fee_tax_breakdown (GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdown | Unset):
    """

    sku_id: str | Unset = UNSET
    sku_name: str | Unset = UNSET
    statement_id: str | Unset = UNSET
    product_name: str | Unset = UNSET
    quantity: str | Unset = UNSET
    settlement_amount: str | Unset = UNSET
    revenue_amount: str | Unset = UNSET
    revenue_breakdown: RevenueBreakdown | Unset = UNSET
    shipping_cost_amount: str | Unset = UNSET
    shipping_cost_breakdown: GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdown | Unset = UNSET
    fee_tax_amount: str | Unset = UNSET
    fee_tax_breakdown: GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdown | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sku_id = self.sku_id

        sku_name = self.sku_name

        statement_id = self.statement_id

        product_name = self.product_name

        quantity = self.quantity

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if sku_name is not UNSET:
            field_dict["sku_name"] = sku_name
        if statement_id is not UNSET:
            field_dict["statement_id"] = statement_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_transactions_by_order_response_data_sku_transaction_fee_tax_breakdown import (
            GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdown,  # noqa: PLC0415
        )
        from ..models.get_transactions_by_order_response_data_sku_transaction_shipping_cost_breakdown import (
            GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdown,  # noqa: PLC0415
        )
        from ..models.revenue_breakdown import RevenueBreakdown  # noqa: PLC0415

        d = dict(src_dict)
        sku_id = d.pop("sku_id", UNSET)

        sku_name = d.pop("sku_name", UNSET)

        statement_id = d.pop("statement_id", UNSET)

        product_name = d.pop("product_name", UNSET)

        quantity = d.pop("quantity", UNSET)

        settlement_amount = d.pop("settlement_amount", UNSET)

        revenue_amount = d.pop("revenue_amount", UNSET)

        _revenue_breakdown = d.pop("revenue_breakdown", UNSET)
        revenue_breakdown: RevenueBreakdown | Unset
        if isinstance(_revenue_breakdown, Unset):
            revenue_breakdown = UNSET
        else:
            revenue_breakdown = RevenueBreakdown.from_dict(_revenue_breakdown)

        shipping_cost_amount = d.pop("shipping_cost_amount", UNSET)

        _shipping_cost_breakdown = d.pop("shipping_cost_breakdown", UNSET)
        shipping_cost_breakdown: GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdown | Unset
        if isinstance(_shipping_cost_breakdown, Unset):
            shipping_cost_breakdown = UNSET
        else:
            shipping_cost_breakdown = GetTransactionsByOrderResponseDataSkuTransactionShippingCostBreakdown.from_dict(
                _shipping_cost_breakdown
            )

        fee_tax_amount = d.pop("fee_tax_amount", UNSET)

        _fee_tax_breakdown = d.pop("fee_tax_breakdown", UNSET)
        fee_tax_breakdown: GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdown | Unset
        if isinstance(_fee_tax_breakdown, Unset):
            fee_tax_breakdown = UNSET
        else:
            fee_tax_breakdown = GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdown.from_dict(
                _fee_tax_breakdown
            )

        get_transactions_by_order_response_data_sku_transaction = cls(
            sku_id=sku_id,
            sku_name=sku_name,
            statement_id=statement_id,
            product_name=product_name,
            quantity=quantity,
            settlement_amount=settlement_amount,
            revenue_amount=revenue_amount,
            revenue_breakdown=revenue_breakdown,
            shipping_cost_amount=shipping_cost_amount,
            shipping_cost_breakdown=shipping_cost_breakdown,
            fee_tax_amount=fee_tax_amount,
            fee_tax_breakdown=fee_tax_breakdown,
        )

        get_transactions_by_order_response_data_sku_transaction.additional_properties = d
        return get_transactions_by_order_response_data_sku_transaction

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
