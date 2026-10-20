from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_order_price_details_response_data_line_item_seller_funded_product_promotion import GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotion
  from ..models.get_order_price_details_response_data_line_item_seller_funded_shipping_promotion import GetOrderPriceDetailsResponseDataLineItemSellerFundedShippingPromotion





T = TypeVar("T", bound="GetOrderPriceDetailsResponseDataLineItem")



@_attrs_define
class GetOrderPriceDetailsResponseDataLineItem:
    """ 
        Attributes:
            id (str | Unset): corresponding line_item id
            currency (str | Unset): Currency Type. Three-letter code, see [ISO 4217](https://www.iso.org/iso-4217-currency-
                codes.html).
            total (str | Unset): Total original price of the line item. Calculation: `sku_list_price` +
                `shipping_list_price`
            payment (str | Unset): Amount paid by the buyer for the line item.
            sku_list_price (str | Unset): Total MSRP price of the products.
            sku_sale_price (str | Unset): Total promotional sale price of the products. Calculation: `sku_list_price` -
                `subtotal_deduction_seller` - `subtotal_deduction_platform`
            subtotal (str | Unset): Total promotional sale price for the line item, including tax.
            subtotal_deduction_seller (str | Unset): Seller provided price discount on the product
            subtotal_deduction_platform (str | Unset): Platform provided price discount on the product
            subtotal_tax_amount (str | Unset): Total tax amount on the product
            voucher_deduction_platform (str | Unset): Product-price deduction from platform-funded vouchers for the line
                item.
            voucher_deduction_seller (str | Unset): Product-price deduction from seller-funded vouchers for the line item.
            shipping_list_price (str | Unset): Original shipping price
            shipping_sale_price (str | Unset): Promotional shipping price. Calculation: `shipping_list_price` -
                `shipping_fee_deduction_seller` - `shipping_fee_deduction_platform`
            shipping_fee_deduction_seller (str | Unset): Shipping discount covered by the seller.
            shipping_fee_deduction_platform (str | Unset): Shipping discount covered by the platform
            shipping_fee_deduction_platform_voucher (str | Unset): Shipping-fee deduction from platform-funded vouchers for
                the line item.
            tax_amount (str | Unset): Total tax amount for the line item.
            tax_rate (str | Unset): Tax rate
            net_price_amount (str | Unset): Line item price excluding tax.
            cod_fee (str | Unset): COD fee charged by shipping aggregators. For regions outside of Saudi Arabia, the value
                is `0.00`.
            cod_fee_amount (str | Unset): COD fee charged by shipping aggregators including tax. For regions outside of
                Saudi Arabia, the value is `0.00`.
            sku_gift_original_price (str | Unset): Original sku list price of the gift product from the seller.
            sku_gift_net_price (str | Unset): Original sku list price of the gift product from the seller including tax.
            distance_shipping_fee (str | Unset): Distance shipping fee is fee that charged charged by our logistics partner
                and covers the separate distance-based cost for deliveries outside Java island as a part of Horizon+ Program.
                Only applicable in ID Market.
            distance_fee (str | Unset): Total distance fee for Horizon+ Program. Only applicable for ID market
            seller_funded_product_promotions (list[GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotion] |
                Unset): Seller-funded product promotions associated with the line item.
            seller_funded_shipping_promotions (list[GetOrderPriceDetailsResponseDataLineItemSellerFundedShippingPromotion] |
                Unset): Seller-funded shipping promotions associated with the line item.
     """

    id: str | Unset = UNSET
    currency: str | Unset = UNSET
    total: str | Unset = UNSET
    payment: str | Unset = UNSET
    sku_list_price: str | Unset = UNSET
    sku_sale_price: str | Unset = UNSET
    subtotal: str | Unset = UNSET
    subtotal_deduction_seller: str | Unset = UNSET
    subtotal_deduction_platform: str | Unset = UNSET
    subtotal_tax_amount: str | Unset = UNSET
    voucher_deduction_platform: str | Unset = UNSET
    voucher_deduction_seller: str | Unset = UNSET
    shipping_list_price: str | Unset = UNSET
    shipping_sale_price: str | Unset = UNSET
    shipping_fee_deduction_seller: str | Unset = UNSET
    shipping_fee_deduction_platform: str | Unset = UNSET
    shipping_fee_deduction_platform_voucher: str | Unset = UNSET
    tax_amount: str | Unset = UNSET
    tax_rate: str | Unset = UNSET
    net_price_amount: str | Unset = UNSET
    cod_fee: str | Unset = UNSET
    cod_fee_amount: str | Unset = UNSET
    sku_gift_original_price: str | Unset = UNSET
    sku_gift_net_price: str | Unset = UNSET
    distance_shipping_fee: str | Unset = UNSET
    distance_fee: str | Unset = UNSET
    seller_funded_product_promotions: list[GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotion] | Unset = UNSET
    seller_funded_shipping_promotions: list[GetOrderPriceDetailsResponseDataLineItemSellerFundedShippingPromotion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_order_price_details_response_data_line_item_seller_funded_product_promotion import GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotion # noqa: PLC0415
        from ..models.get_order_price_details_response_data_line_item_seller_funded_shipping_promotion import GetOrderPriceDetailsResponseDataLineItemSellerFundedShippingPromotion # noqa: PLC0415
        id = self.id

        currency = self.currency

        total = self.total

        payment = self.payment

        sku_list_price = self.sku_list_price

        sku_sale_price = self.sku_sale_price

        subtotal = self.subtotal

        subtotal_deduction_seller = self.subtotal_deduction_seller

        subtotal_deduction_platform = self.subtotal_deduction_platform

        subtotal_tax_amount = self.subtotal_tax_amount

        voucher_deduction_platform = self.voucher_deduction_platform

        voucher_deduction_seller = self.voucher_deduction_seller

        shipping_list_price = self.shipping_list_price

        shipping_sale_price = self.shipping_sale_price

        shipping_fee_deduction_seller = self.shipping_fee_deduction_seller

        shipping_fee_deduction_platform = self.shipping_fee_deduction_platform

        shipping_fee_deduction_platform_voucher = self.shipping_fee_deduction_platform_voucher

        tax_amount = self.tax_amount

        tax_rate = self.tax_rate

        net_price_amount = self.net_price_amount

        cod_fee = self.cod_fee

        cod_fee_amount = self.cod_fee_amount

        sku_gift_original_price = self.sku_gift_original_price

        sku_gift_net_price = self.sku_gift_net_price

        distance_shipping_fee = self.distance_shipping_fee

        distance_fee = self.distance_fee

        seller_funded_product_promotions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.seller_funded_product_promotions, Unset):
            seller_funded_product_promotions = []
            for seller_funded_product_promotions_item_data in self.seller_funded_product_promotions:
                seller_funded_product_promotions_item = seller_funded_product_promotions_item_data.to_dict()
                seller_funded_product_promotions.append(seller_funded_product_promotions_item)



        seller_funded_shipping_promotions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.seller_funded_shipping_promotions, Unset):
            seller_funded_shipping_promotions = []
            for seller_funded_shipping_promotions_item_data in self.seller_funded_shipping_promotions:
                seller_funded_shipping_promotions_item = seller_funded_shipping_promotions_item_data.to_dict()
                seller_funded_shipping_promotions.append(seller_funded_shipping_promotions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total is not UNSET:
            field_dict["total"] = total
        if payment is not UNSET:
            field_dict["payment"] = payment
        if sku_list_price is not UNSET:
            field_dict["sku_list_price"] = sku_list_price
        if sku_sale_price is not UNSET:
            field_dict["sku_sale_price"] = sku_sale_price
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if subtotal_deduction_seller is not UNSET:
            field_dict["subtotal_deduction_seller"] = subtotal_deduction_seller
        if subtotal_deduction_platform is not UNSET:
            field_dict["subtotal_deduction_platform"] = subtotal_deduction_platform
        if subtotal_tax_amount is not UNSET:
            field_dict["subtotal_tax_amount"] = subtotal_tax_amount
        if voucher_deduction_platform is not UNSET:
            field_dict["voucher_deduction_platform"] = voucher_deduction_platform
        if voucher_deduction_seller is not UNSET:
            field_dict["voucher_deduction_seller"] = voucher_deduction_seller
        if shipping_list_price is not UNSET:
            field_dict["shipping_list_price"] = shipping_list_price
        if shipping_sale_price is not UNSET:
            field_dict["shipping_sale_price"] = shipping_sale_price
        if shipping_fee_deduction_seller is not UNSET:
            field_dict["shipping_fee_deduction_seller"] = shipping_fee_deduction_seller
        if shipping_fee_deduction_platform is not UNSET:
            field_dict["shipping_fee_deduction_platform"] = shipping_fee_deduction_platform
        if shipping_fee_deduction_platform_voucher is not UNSET:
            field_dict["shipping_fee_deduction_platform_voucher"] = shipping_fee_deduction_platform_voucher
        if tax_amount is not UNSET:
            field_dict["tax_amount"] = tax_amount
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate
        if net_price_amount is not UNSET:
            field_dict["net_price_amount"] = net_price_amount
        if cod_fee is not UNSET:
            field_dict["cod_fee"] = cod_fee
        if cod_fee_amount is not UNSET:
            field_dict["cod_fee_amount"] = cod_fee_amount
        if sku_gift_original_price is not UNSET:
            field_dict["sku_gift_original_price"] = sku_gift_original_price
        if sku_gift_net_price is not UNSET:
            field_dict["sku_gift_net_price"] = sku_gift_net_price
        if distance_shipping_fee is not UNSET:
            field_dict["distance_shipping_fee"] = distance_shipping_fee
        if distance_fee is not UNSET:
            field_dict["distance_fee"] = distance_fee
        if seller_funded_product_promotions is not UNSET:
            field_dict["seller_funded_product_promotions"] = seller_funded_product_promotions
        if seller_funded_shipping_promotions is not UNSET:
            field_dict["seller_funded_shipping_promotions"] = seller_funded_shipping_promotions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_order_price_details_response_data_line_item_seller_funded_product_promotion import GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotion # noqa: PLC0415
        from ..models.get_order_price_details_response_data_line_item_seller_funded_shipping_promotion import GetOrderPriceDetailsResponseDataLineItemSellerFundedShippingPromotion # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        currency = d.pop("currency", UNSET)

        total = d.pop("total", UNSET)

        payment = d.pop("payment", UNSET)

        sku_list_price = d.pop("sku_list_price", UNSET)

        sku_sale_price = d.pop("sku_sale_price", UNSET)

        subtotal = d.pop("subtotal", UNSET)

        subtotal_deduction_seller = d.pop("subtotal_deduction_seller", UNSET)

        subtotal_deduction_platform = d.pop("subtotal_deduction_platform", UNSET)

        subtotal_tax_amount = d.pop("subtotal_tax_amount", UNSET)

        voucher_deduction_platform = d.pop("voucher_deduction_platform", UNSET)

        voucher_deduction_seller = d.pop("voucher_deduction_seller", UNSET)

        shipping_list_price = d.pop("shipping_list_price", UNSET)

        shipping_sale_price = d.pop("shipping_sale_price", UNSET)

        shipping_fee_deduction_seller = d.pop("shipping_fee_deduction_seller", UNSET)

        shipping_fee_deduction_platform = d.pop("shipping_fee_deduction_platform", UNSET)

        shipping_fee_deduction_platform_voucher = d.pop("shipping_fee_deduction_platform_voucher", UNSET)

        tax_amount = d.pop("tax_amount", UNSET)

        tax_rate = d.pop("tax_rate", UNSET)

        net_price_amount = d.pop("net_price_amount", UNSET)

        cod_fee = d.pop("cod_fee", UNSET)

        cod_fee_amount = d.pop("cod_fee_amount", UNSET)

        sku_gift_original_price = d.pop("sku_gift_original_price", UNSET)

        sku_gift_net_price = d.pop("sku_gift_net_price", UNSET)

        distance_shipping_fee = d.pop("distance_shipping_fee", UNSET)

        distance_fee = d.pop("distance_fee", UNSET)

        _seller_funded_product_promotions = d.pop("seller_funded_product_promotions", UNSET)
        seller_funded_product_promotions: list[GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotion] | Unset = UNSET
        if _seller_funded_product_promotions is not UNSET:
            seller_funded_product_promotions = []
            for seller_funded_product_promotions_item_data in _seller_funded_product_promotions:
                seller_funded_product_promotions_item = GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotion.from_dict(seller_funded_product_promotions_item_data)



                seller_funded_product_promotions.append(seller_funded_product_promotions_item)


        _seller_funded_shipping_promotions = d.pop("seller_funded_shipping_promotions", UNSET)
        seller_funded_shipping_promotions: list[GetOrderPriceDetailsResponseDataLineItemSellerFundedShippingPromotion] | Unset = UNSET
        if _seller_funded_shipping_promotions is not UNSET:
            seller_funded_shipping_promotions = []
            for seller_funded_shipping_promotions_item_data in _seller_funded_shipping_promotions:
                seller_funded_shipping_promotions_item = GetOrderPriceDetailsResponseDataLineItemSellerFundedShippingPromotion.from_dict(seller_funded_shipping_promotions_item_data)



                seller_funded_shipping_promotions.append(seller_funded_shipping_promotions_item)


        get_order_price_details_response_data_line_item = cls(
            id=id,
            currency=currency,
            total=total,
            payment=payment,
            sku_list_price=sku_list_price,
            sku_sale_price=sku_sale_price,
            subtotal=subtotal,
            subtotal_deduction_seller=subtotal_deduction_seller,
            subtotal_deduction_platform=subtotal_deduction_platform,
            subtotal_tax_amount=subtotal_tax_amount,
            voucher_deduction_platform=voucher_deduction_platform,
            voucher_deduction_seller=voucher_deduction_seller,
            shipping_list_price=shipping_list_price,
            shipping_sale_price=shipping_sale_price,
            shipping_fee_deduction_seller=shipping_fee_deduction_seller,
            shipping_fee_deduction_platform=shipping_fee_deduction_platform,
            shipping_fee_deduction_platform_voucher=shipping_fee_deduction_platform_voucher,
            tax_amount=tax_amount,
            tax_rate=tax_rate,
            net_price_amount=net_price_amount,
            cod_fee=cod_fee,
            cod_fee_amount=cod_fee_amount,
            sku_gift_original_price=sku_gift_original_price,
            sku_gift_net_price=sku_gift_net_price,
            distance_shipping_fee=distance_shipping_fee,
            distance_fee=distance_fee,
            seller_funded_product_promotions=seller_funded_product_promotions,
            seller_funded_shipping_promotions=seller_funded_shipping_promotions,
        )


        get_order_price_details_response_data_line_item.additional_properties = d
        return get_order_price_details_response_data_line_item

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
