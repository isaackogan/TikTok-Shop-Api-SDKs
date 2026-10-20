from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetTransactionsByStatementResponseDataTransactionSupplementaryComponent")



@_attrs_define
class GetTransactionsByStatementResponseDataTransactionSupplementaryComponent:
    """ 
        Attributes:
            customer_payment_amount (str | Unset): The total amount paid by the customer.
            customer_refund_amount (str | Unset): The exact amount refunded to the customer.
            platform_discount_amount (str | Unset): The discounts funded by the platform, such as coupons and campaign
                discounts.
            platform_discount_refund_amount (str | Unset): The platform discounts to be reversed (and deducted from the
                final settlement) if the order was refunded as a result of the seller's responsibility.
            seller_cofunded_discount_amount (str | Unset): The seller's portion of a co-funded voucher discount in co-
                funding campaigns.
            seller_cofunded_discount_refund_amount (str | Unset): The seller's portion of a co-funded voucher discount in
                co-funding campaigns that was refunded to the seller.
            platform_cofunded_discount_amount (str | Unset): The platform's portion of a co-funded voucher discount in co-
                funding campaigns.
            platform_cofunded_discount_refund_amount (str | Unset): The platform's portion of a co-funded voucher discount
                in co-funding campaigns that was refunded to the platform.
            retail_delivery_fee_amount (str | Unset): The final retail delivery fee for deliveries in Colorado, US. For more
                information, see [Colorado Retail Delivery Fee FAQ](https://seller-
                us.tiktok.com/university/essay?knowledge_id=2459780628350762&default_language=en&identity=1).

                Formula: retail_delivery_fee_payment_amount + retail_delivery_fee_refund_amount
            retail_delivery_fee_payment_amount (str | Unset): The retail delivery fee for deliveries in Colorado, US. For
                more information, see [Colorado Retail Delivery Fee FAQ](https://seller-
                us.tiktok.com/university/essay?knowledge_id=2459780628350762&default_language=en&identity=1).
            retail_delivery_fee_refund_amount (str | Unset): The retail delivery fee subsidy by the platform for losses due
                to returns, refunds, or other issues in Colorado, US.
            sales_tax_amount (str | Unset): The final sales tax to be paid by the customer for the product and delivery.

                Formula: sales_tax_payment_amount - sales_tax_refund_amount
            sales_tax_payment_amount (str | Unset): The expected sales tax to be paid by the customer for the product and
                delivery.
            sales_tax_refund_amount (str | Unset): The sales tax amount returned to the customer in the event of a refund.
     """

    customer_payment_amount: str | Unset = UNSET
    customer_refund_amount: str | Unset = UNSET
    platform_discount_amount: str | Unset = UNSET
    platform_discount_refund_amount: str | Unset = UNSET
    seller_cofunded_discount_amount: str | Unset = UNSET
    seller_cofunded_discount_refund_amount: str | Unset = UNSET
    platform_cofunded_discount_amount: str | Unset = UNSET
    platform_cofunded_discount_refund_amount: str | Unset = UNSET
    retail_delivery_fee_amount: str | Unset = UNSET
    retail_delivery_fee_payment_amount: str | Unset = UNSET
    retail_delivery_fee_refund_amount: str | Unset = UNSET
    sales_tax_amount: str | Unset = UNSET
    sales_tax_payment_amount: str | Unset = UNSET
    sales_tax_refund_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        customer_payment_amount = self.customer_payment_amount

        customer_refund_amount = self.customer_refund_amount

        platform_discount_amount = self.platform_discount_amount

        platform_discount_refund_amount = self.platform_discount_refund_amount

        seller_cofunded_discount_amount = self.seller_cofunded_discount_amount

        seller_cofunded_discount_refund_amount = self.seller_cofunded_discount_refund_amount

        platform_cofunded_discount_amount = self.platform_cofunded_discount_amount

        platform_cofunded_discount_refund_amount = self.platform_cofunded_discount_refund_amount

        retail_delivery_fee_amount = self.retail_delivery_fee_amount

        retail_delivery_fee_payment_amount = self.retail_delivery_fee_payment_amount

        retail_delivery_fee_refund_amount = self.retail_delivery_fee_refund_amount

        sales_tax_amount = self.sales_tax_amount

        sales_tax_payment_amount = self.sales_tax_payment_amount

        sales_tax_refund_amount = self.sales_tax_refund_amount


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if customer_payment_amount is not UNSET:
            field_dict["customer_payment_amount"] = customer_payment_amount
        if customer_refund_amount is not UNSET:
            field_dict["customer_refund_amount"] = customer_refund_amount
        if platform_discount_amount is not UNSET:
            field_dict["platform_discount_amount"] = platform_discount_amount
        if platform_discount_refund_amount is not UNSET:
            field_dict["platform_discount_refund_amount"] = platform_discount_refund_amount
        if seller_cofunded_discount_amount is not UNSET:
            field_dict["seller_cofunded_discount_amount"] = seller_cofunded_discount_amount
        if seller_cofunded_discount_refund_amount is not UNSET:
            field_dict["seller_cofunded_discount_refund_amount"] = seller_cofunded_discount_refund_amount
        if platform_cofunded_discount_amount is not UNSET:
            field_dict["platform_cofunded_discount_amount"] = platform_cofunded_discount_amount
        if platform_cofunded_discount_refund_amount is not UNSET:
            field_dict["platform_cofunded_discount_refund_amount"] = platform_cofunded_discount_refund_amount
        if retail_delivery_fee_amount is not UNSET:
            field_dict["retail_delivery_fee_amount"] = retail_delivery_fee_amount
        if retail_delivery_fee_payment_amount is not UNSET:
            field_dict["retail_delivery_fee_payment_amount"] = retail_delivery_fee_payment_amount
        if retail_delivery_fee_refund_amount is not UNSET:
            field_dict["retail_delivery_fee_refund_amount"] = retail_delivery_fee_refund_amount
        if sales_tax_amount is not UNSET:
            field_dict["sales_tax_amount"] = sales_tax_amount
        if sales_tax_payment_amount is not UNSET:
            field_dict["sales_tax_payment_amount"] = sales_tax_payment_amount
        if sales_tax_refund_amount is not UNSET:
            field_dict["sales_tax_refund_amount"] = sales_tax_refund_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer_payment_amount = d.pop("customer_payment_amount", UNSET)

        customer_refund_amount = d.pop("customer_refund_amount", UNSET)

        platform_discount_amount = d.pop("platform_discount_amount", UNSET)

        platform_discount_refund_amount = d.pop("platform_discount_refund_amount", UNSET)

        seller_cofunded_discount_amount = d.pop("seller_cofunded_discount_amount", UNSET)

        seller_cofunded_discount_refund_amount = d.pop("seller_cofunded_discount_refund_amount", UNSET)

        platform_cofunded_discount_amount = d.pop("platform_cofunded_discount_amount", UNSET)

        platform_cofunded_discount_refund_amount = d.pop("platform_cofunded_discount_refund_amount", UNSET)

        retail_delivery_fee_amount = d.pop("retail_delivery_fee_amount", UNSET)

        retail_delivery_fee_payment_amount = d.pop("retail_delivery_fee_payment_amount", UNSET)

        retail_delivery_fee_refund_amount = d.pop("retail_delivery_fee_refund_amount", UNSET)

        sales_tax_amount = d.pop("sales_tax_amount", UNSET)

        sales_tax_payment_amount = d.pop("sales_tax_payment_amount", UNSET)

        sales_tax_refund_amount = d.pop("sales_tax_refund_amount", UNSET)

        get_transactions_by_statement_response_data_transaction_supplementary_component = cls(
            customer_payment_amount=customer_payment_amount,
            customer_refund_amount=customer_refund_amount,
            platform_discount_amount=platform_discount_amount,
            platform_discount_refund_amount=platform_discount_refund_amount,
            seller_cofunded_discount_amount=seller_cofunded_discount_amount,
            seller_cofunded_discount_refund_amount=seller_cofunded_discount_refund_amount,
            platform_cofunded_discount_amount=platform_cofunded_discount_amount,
            platform_cofunded_discount_refund_amount=platform_cofunded_discount_refund_amount,
            retail_delivery_fee_amount=retail_delivery_fee_amount,
            retail_delivery_fee_payment_amount=retail_delivery_fee_payment_amount,
            retail_delivery_fee_refund_amount=retail_delivery_fee_refund_amount,
            sales_tax_amount=sales_tax_amount,
            sales_tax_payment_amount=sales_tax_payment_amount,
            sales_tax_refund_amount=sales_tax_refund_amount,
        )


        get_transactions_by_statement_response_data_transaction_supplementary_component.additional_properties = d
        return get_transactions_by_statement_response_data_transaction_supplementary_component

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
