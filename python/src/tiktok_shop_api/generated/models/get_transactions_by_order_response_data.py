from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_transactions_by_order_response_data_sku_transaction import GetTransactionsByOrderResponseDataSkuTransaction





T = TypeVar("T", bound="GetTransactionsByOrderResponseData")



@_attrs_define
class GetTransactionsByOrderResponseData:
    """ 
        Attributes:
            order_id (str | Unset): The order ID in TikTok Shop.
            order_create_time (int | Unset): The creation time of the order, as a Unix timestamp in seconds.
            currency (str | Unset): The three-letter currency code in ISO 4217 format.
            revenue_amount (str | Unset): The revenue amount for the order at the time of order settlement. This is
                equivalent to the net sales amount.
            fee_and_tax_amount (str | Unset): The fees and taxes charged by the platform for the order at the time of order
                settlement. Shipping-related costs are excluded.
            shipping_cost_amount (str | Unset): The shipping costs for the order at the time of order settlement.
            settlement_amount (str | Unset): The settlement amount for the order.

                Formula: revenue_amount - shipping_cost_amount - fee_tax_amount
            sku_transactions (list[GetTransactionsByOrderResponseDataSkuTransaction] | Unset): The list of SKU transaction
                records for the order.
            total_count (int | Unset): The number of transaction records
     """

    order_id: str | Unset = UNSET
    order_create_time: int | Unset = UNSET
    currency: str | Unset = UNSET
    revenue_amount: str | Unset = UNSET
    fee_and_tax_amount: str | Unset = UNSET
    shipping_cost_amount: str | Unset = UNSET
    settlement_amount: str | Unset = UNSET
    sku_transactions: list[GetTransactionsByOrderResponseDataSkuTransaction] | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_transactions_by_order_response_data_sku_transaction import GetTransactionsByOrderResponseDataSkuTransaction # noqa: PLC0415
        order_id = self.order_id

        order_create_time = self.order_create_time

        currency = self.currency

        revenue_amount = self.revenue_amount

        fee_and_tax_amount = self.fee_and_tax_amount

        shipping_cost_amount = self.shipping_cost_amount

        settlement_amount = self.settlement_amount

        sku_transactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sku_transactions, Unset):
            sku_transactions = []
            for sku_transactions_item_data in self.sku_transactions:
                sku_transactions_item = sku_transactions_item_data.to_dict()
                sku_transactions.append(sku_transactions_item)



        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if order_create_time is not UNSET:
            field_dict["order_create_time"] = order_create_time
        if currency is not UNSET:
            field_dict["currency"] = currency
        if revenue_amount is not UNSET:
            field_dict["revenue_amount"] = revenue_amount
        if fee_and_tax_amount is not UNSET:
            field_dict["fee_and_tax_amount"] = fee_and_tax_amount
        if shipping_cost_amount is not UNSET:
            field_dict["shipping_cost_amount"] = shipping_cost_amount
        if settlement_amount is not UNSET:
            field_dict["settlement_amount"] = settlement_amount
        if sku_transactions is not UNSET:
            field_dict["sku_transactions"] = sku_transactions
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_transactions_by_order_response_data_sku_transaction import GetTransactionsByOrderResponseDataSkuTransaction # noqa: PLC0415
        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        order_create_time = d.pop("order_create_time", UNSET)

        currency = d.pop("currency", UNSET)

        revenue_amount = d.pop("revenue_amount", UNSET)

        fee_and_tax_amount = d.pop("fee_and_tax_amount", UNSET)

        shipping_cost_amount = d.pop("shipping_cost_amount", UNSET)

        settlement_amount = d.pop("settlement_amount", UNSET)

        _sku_transactions = d.pop("sku_transactions", UNSET)
        sku_transactions: list[GetTransactionsByOrderResponseDataSkuTransaction] | Unset = UNSET
        if _sku_transactions is not UNSET:
            sku_transactions = []
            for sku_transactions_item_data in _sku_transactions:
                sku_transactions_item = GetTransactionsByOrderResponseDataSkuTransaction.from_dict(sku_transactions_item_data)



                sku_transactions.append(sku_transactions_item)


        total_count = d.pop("total_count", UNSET)

        get_transactions_by_order_response_data = cls(
            order_id=order_id,
            order_create_time=order_create_time,
            currency=currency,
            revenue_amount=revenue_amount,
            fee_and_tax_amount=fee_and_tax_amount,
            shipping_cost_amount=shipping_cost_amount,
            settlement_amount=settlement_amount,
            sku_transactions=sku_transactions,
            total_count=total_count,
        )


        get_transactions_by_order_response_data.additional_properties = d
        return get_transactions_by_order_response_data

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
