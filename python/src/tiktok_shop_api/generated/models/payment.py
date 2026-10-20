from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="Payment")



@_attrs_define
class Payment:
    """ 
        Attributes:
            currency (str | Unset): Currency for payment.
            sub_total (str | Unset): Buyer paid subtotal of all the SKUs in the order. For the US market, this is pre-tax
                total amount.
                `sub_total` = `original_total_product_price` - `seller_discount` - `platform_discount`
            shipping_fee (str | Unset): Buyer paid shipping fee.
                `shipping_fee` = `original_shipping_fee` - `shipping_fee_seller_discount` - `shipping_fee_platform_discount`
                For the US market, this is pre-tax total amount.
            seller_discount (str | Unset): Product discount by seller.
            platform_discount (str | Unset): Product discount by platform.
            payment_platform_discount (str | Unset): Discount applied to the order funded by a payment platform
            payment_discount_service_fee (str | Unset): Service fee as paid by the buyer to apply payment platform discount
            total_amount (str | Unset): Buyer paid total amount.
                `total_amount` = `sub_total` + `shipping_fee` + `taxes` + `retail_delivery_fee`
            original_total_product_price (str | Unset): Total original price of products (VAT included for crossborder
                shop).
                For the US market, this is pre-tax total amount.
            original_shipping_fee (str | Unset): Shipping fee before discount
            shipping_fee_seller_discount (str | Unset): Shipping fee discount provided by seller for an order that will not
                qualify for co-funded reimbursement. **Note**: If an order meets the minimum order value for co-funded
                reimbursement, this will be 0. In this case, refer to `shipping_fee_cofunded_discount` for the shipping discount
                the buyer received.
            shipping_fee_platform_discount (str | Unset): Shipping fee discount by platform.
            shipping_fee_cofunded_discount (str | Unset): Shipping fee discount provided by seller, eligible for co-funded
                reimbursement upon order delivery, based on Co-Funded Free Shipping program terms. **Note**: This will be 0 for
                orders that did not meet minimum order value for co-funded reimbursement. In this case, refer to
                `shipping_fee_seller_discount` for the shipping discount the buyer received.
            tax (str | Unset): Buyer paid total taxes of the order. Applicable to crossborder shops and the US market.
            small_order_fee (str | Unset): Small order fee for TH.
                Small order fee is for Thailand only. small order fee means that the platform will set a minimum order spending
                amount, when the order amount is lower than the minimum order spending amount, the user needs to pay small order
                fee to meet the platform minimum spending amount.
                e.g. Minimum order spending amount is 100, order amount is 80. So the small order fee will be 20.
            shipping_fee_tax (str | Unset): The tax on the shipping price.
            product_tax (str | Unset): The tax on the total item price.
            retail_delivery_fee (str | Unset): RDF (retail delivery fee). Available only in the US market.
            buyer_service_fee (str | Unset): A service fee is charged on every transaction made. The charge is applied from
                the fifth order onwards and collected directly from customers during checkout. Only available in Indonesia
                market.
            handling_fee (str | Unset): A fee charged to buyers to cover the additional processing, handling, and/or
                installment costs associated with the chosen payment method.
            shipping_insurance_fee (str | Unset): The cost incurred by the buyers for coverage against loss or damage to
                goods during transit.
                **Note**: Available only in the Indonesia market.
            item_insurance_fee (str | Unset): The cost incurred by the buyers for coverage against defects or damage to the
                product after purchase.
                **Note**: Only available in the US and Indonesia markets.
            item_insurance_tax (str | Unset): The tax paid on the insurance purchased by buyers.

                Note: Only applicable in US market.
            distance_shipping_fee (str | Unset): Distance shipping fee is fee that charged charged by our logistics partner
                and covers the separate distance-based cost for deliveries outside Java island as a part of Horizon+ Program.
                Only applicable in ID Market.
            distance_fee (str | Unset): Total distance fee for Horizon+ Program. Only applicable for ID market
     """

    currency: str | Unset = UNSET
    sub_total: str | Unset = UNSET
    shipping_fee: str | Unset = UNSET
    seller_discount: str | Unset = UNSET
    platform_discount: str | Unset = UNSET
    payment_platform_discount: str | Unset = UNSET
    payment_discount_service_fee: str | Unset = UNSET
    total_amount: str | Unset = UNSET
    original_total_product_price: str | Unset = UNSET
    original_shipping_fee: str | Unset = UNSET
    shipping_fee_seller_discount: str | Unset = UNSET
    shipping_fee_platform_discount: str | Unset = UNSET
    shipping_fee_cofunded_discount: str | Unset = UNSET
    tax: str | Unset = UNSET
    small_order_fee: str | Unset = UNSET
    shipping_fee_tax: str | Unset = UNSET
    product_tax: str | Unset = UNSET
    retail_delivery_fee: str | Unset = UNSET
    buyer_service_fee: str | Unset = UNSET
    handling_fee: str | Unset = UNSET
    shipping_insurance_fee: str | Unset = UNSET
    item_insurance_fee: str | Unset = UNSET
    item_insurance_tax: str | Unset = UNSET
    distance_shipping_fee: str | Unset = UNSET
    distance_fee: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        sub_total = self.sub_total

        shipping_fee = self.shipping_fee

        seller_discount = self.seller_discount

        platform_discount = self.platform_discount

        payment_platform_discount = self.payment_platform_discount

        payment_discount_service_fee = self.payment_discount_service_fee

        total_amount = self.total_amount

        original_total_product_price = self.original_total_product_price

        original_shipping_fee = self.original_shipping_fee

        shipping_fee_seller_discount = self.shipping_fee_seller_discount

        shipping_fee_platform_discount = self.shipping_fee_platform_discount

        shipping_fee_cofunded_discount = self.shipping_fee_cofunded_discount

        tax = self.tax

        small_order_fee = self.small_order_fee

        shipping_fee_tax = self.shipping_fee_tax

        product_tax = self.product_tax

        retail_delivery_fee = self.retail_delivery_fee

        buyer_service_fee = self.buyer_service_fee

        handling_fee = self.handling_fee

        shipping_insurance_fee = self.shipping_insurance_fee

        item_insurance_fee = self.item_insurance_fee

        item_insurance_tax = self.item_insurance_tax

        distance_shipping_fee = self.distance_shipping_fee

        distance_fee = self.distance_fee


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if currency is not UNSET:
            field_dict["currency"] = currency
        if sub_total is not UNSET:
            field_dict["sub_total"] = sub_total
        if shipping_fee is not UNSET:
            field_dict["shipping_fee"] = shipping_fee
        if seller_discount is not UNSET:
            field_dict["seller_discount"] = seller_discount
        if platform_discount is not UNSET:
            field_dict["platform_discount"] = platform_discount
        if payment_platform_discount is not UNSET:
            field_dict["payment_platform_discount"] = payment_platform_discount
        if payment_discount_service_fee is not UNSET:
            field_dict["payment_discount_service_fee"] = payment_discount_service_fee
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount
        if original_total_product_price is not UNSET:
            field_dict["original_total_product_price"] = original_total_product_price
        if original_shipping_fee is not UNSET:
            field_dict["original_shipping_fee"] = original_shipping_fee
        if shipping_fee_seller_discount is not UNSET:
            field_dict["shipping_fee_seller_discount"] = shipping_fee_seller_discount
        if shipping_fee_platform_discount is not UNSET:
            field_dict["shipping_fee_platform_discount"] = shipping_fee_platform_discount
        if shipping_fee_cofunded_discount is not UNSET:
            field_dict["shipping_fee_cofunded_discount"] = shipping_fee_cofunded_discount
        if tax is not UNSET:
            field_dict["tax"] = tax
        if small_order_fee is not UNSET:
            field_dict["small_order_fee"] = small_order_fee
        if shipping_fee_tax is not UNSET:
            field_dict["shipping_fee_tax"] = shipping_fee_tax
        if product_tax is not UNSET:
            field_dict["product_tax"] = product_tax
        if retail_delivery_fee is not UNSET:
            field_dict["retail_delivery_fee"] = retail_delivery_fee
        if buyer_service_fee is not UNSET:
            field_dict["buyer_service_fee"] = buyer_service_fee
        if handling_fee is not UNSET:
            field_dict["handling_fee"] = handling_fee
        if shipping_insurance_fee is not UNSET:
            field_dict["shipping_insurance_fee"] = shipping_insurance_fee
        if item_insurance_fee is not UNSET:
            field_dict["item_insurance_fee"] = item_insurance_fee
        if item_insurance_tax is not UNSET:
            field_dict["item_insurance_tax"] = item_insurance_tax
        if distance_shipping_fee is not UNSET:
            field_dict["distance_shipping_fee"] = distance_shipping_fee
        if distance_fee is not UNSET:
            field_dict["distance_fee"] = distance_fee

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        sub_total = d.pop("sub_total", UNSET)

        shipping_fee = d.pop("shipping_fee", UNSET)

        seller_discount = d.pop("seller_discount", UNSET)

        platform_discount = d.pop("platform_discount", UNSET)

        payment_platform_discount = d.pop("payment_platform_discount", UNSET)

        payment_discount_service_fee = d.pop("payment_discount_service_fee", UNSET)

        total_amount = d.pop("total_amount", UNSET)

        original_total_product_price = d.pop("original_total_product_price", UNSET)

        original_shipping_fee = d.pop("original_shipping_fee", UNSET)

        shipping_fee_seller_discount = d.pop("shipping_fee_seller_discount", UNSET)

        shipping_fee_platform_discount = d.pop("shipping_fee_platform_discount", UNSET)

        shipping_fee_cofunded_discount = d.pop("shipping_fee_cofunded_discount", UNSET)

        tax = d.pop("tax", UNSET)

        small_order_fee = d.pop("small_order_fee", UNSET)

        shipping_fee_tax = d.pop("shipping_fee_tax", UNSET)

        product_tax = d.pop("product_tax", UNSET)

        retail_delivery_fee = d.pop("retail_delivery_fee", UNSET)

        buyer_service_fee = d.pop("buyer_service_fee", UNSET)

        handling_fee = d.pop("handling_fee", UNSET)

        shipping_insurance_fee = d.pop("shipping_insurance_fee", UNSET)

        item_insurance_fee = d.pop("item_insurance_fee", UNSET)

        item_insurance_tax = d.pop("item_insurance_tax", UNSET)

        distance_shipping_fee = d.pop("distance_shipping_fee", UNSET)

        distance_fee = d.pop("distance_fee", UNSET)

        payment = cls(
            currency=currency,
            sub_total=sub_total,
            shipping_fee=shipping_fee,
            seller_discount=seller_discount,
            platform_discount=platform_discount,
            payment_platform_discount=payment_platform_discount,
            payment_discount_service_fee=payment_discount_service_fee,
            total_amount=total_amount,
            original_total_product_price=original_total_product_price,
            original_shipping_fee=original_shipping_fee,
            shipping_fee_seller_discount=shipping_fee_seller_discount,
            shipping_fee_platform_discount=shipping_fee_platform_discount,
            shipping_fee_cofunded_discount=shipping_fee_cofunded_discount,
            tax=tax,
            small_order_fee=small_order_fee,
            shipping_fee_tax=shipping_fee_tax,
            product_tax=product_tax,
            retail_delivery_fee=retail_delivery_fee,
            buyer_service_fee=buyer_service_fee,
            handling_fee=handling_fee,
            shipping_insurance_fee=shipping_insurance_fee,
            item_insurance_fee=item_insurance_fee,
            item_insurance_tax=item_insurance_tax,
            distance_shipping_fee=distance_shipping_fee,
            distance_fee=distance_fee,
        )


        payment.additional_properties = d
        return payment

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
