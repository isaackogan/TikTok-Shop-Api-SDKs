from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUnsettledTransactionsResponseDataTransactionFeeTaxBreakdownFee")


@_attrs_define
class GetUnsettledTransactionsResponseDataTransactionFeeTaxBreakdownFee:
    """
    Attributes:
        platform_commission_amount (str | Unset): The commission amount charged by the platform.
        referral_fee_amount (str | Unset): The referral fee charged for processing successful orders.
            Applicable only for the US.
        refund_administration_fee_amount (str | Unset): The 20% refund administration fee deducted from the total
            refunded referral fee amount.
        transaction_fee_amount (str | Unset): The transaction fee charged for processing successful orders.
        credit_card_handling_fee_amount (str | Unset): The handling fee charged when the buyer pays with a credit card.
        affiliate_commission_amount (str | Unset): The commission amount charged to the seller for payment to the
            creator.
        affiliate_commission_before_pit_amount (str | Unset): The affiliate ads commission paid to a creator before any
            personal income tax withholding.
            Applicable only for SEA markets.
        pit_withheld_from_ads_commission_amount (str | Unset): The creator's personal income tax withholding amount,
            deducted from the affiliate ads commission.
            Sellers are responsible for declaration and remittance to the tax authority, as well as providing finalized
            personal income tax documentation to creators.
            Applicable only for SEA markets.
        affiliate_partner_commission_amount (str | Unset): The commission amount for purchases through affiliate partner
            links.
        affiliate_ads_commission_amount (str | Unset): The commission for eligible orders from ads.
        sfp_service_fee_amount (str | Unset): The service fee charged for participation in the [Seller Free Shipping
            Programme].
        live_specials_fee_amount (str | Unset): The service fee charged for participation in the [LIVE Specials
            Programme].
        bonus_cashback_service_fee_amount (str | Unset): The service fee charged for participation in the bonus cashback
            program.
        mall_service_fee_amount (str | Unset): The service fee charged for using TikTok Shop Mall.
        retail_delivery_fee_amount (str | Unset): The final retail delivery fee for deliveries in Colorado, US. For more
            information, see [Colorado Retail Delivery Fee FAQ](https://seller-
            us.tiktok.com/university/essay?knowledge_id=2459780628350762&default_language=en&identity=1).

            Formula: retail_delivery_fee_payment_amount + retail_delivery_fee_refund_amount
        retail_delivery_fee_payment_amount (str | Unset): The retail delivery fee for deliveries in Colorado, US. For
            more information, see [Colorado Retail Delivery Fee FAQ](https://seller-
            us.tiktok.com/university/essay?knowledge_id=2459780628350762&default_language=en&identity=1).
        retail_delivery_fee_refund_amount (str | Unset): The retail delivery fee subsidy by the platform for losses due
            to returns, refunds, or other issues in Colorado, US.
        platform_special_service_fee_amount (str | Unset): The portion of the Distance Shipping Fee paid by the customer
            that exceeds the logistics service provider's charge, retained by TikTok Shop to support a secure fulfillment
            experience
        smart_promotion_fee_amount (str | Unset): This fee includes funds from TikTok Shop to help provide promotions to
            customers
        vn_fix_infrastructure_fee (str | Unset): Infrastructure fees are a fixed service fee that TikTok Shop charges
            for providing, maintaining, and developing infrastructure for delivery services. It applies to delivered orders
            on the main order level.
        dynamic_commission_amount (str | Unset): The dynamic commission fee is the amount that the platform charges to
            all sellers for every successfully delivered order.
            Applicable only for Indonesia.
        campaign_period_fee_cfp_amount (str | Unset): Fee charged during Co-funded Promotion campaigns.
        campaign_period_fee_sp_amount (str | Unset): Fee charged during Smart Promotion campaigns.
        campaign_period_fee_sp_tax_amount (str | Unset): Sales tax applied to the campaign period fee under Smart
            Promotion.
        campaign_period_fee_cfp_tax_amount (str | Unset): Sales tax applied to the campaign period fee under Co-funded
            Promotion.
        seller_growth_fee_amount (str | Unset): A fee charged on each successful order to provide Bonus Cashback and
            other growth benefits.
        failed_delivery_shipping_fee (str | Unset): Shipping fee for order that failed to be delivered to the customer.
            In some cases, the fee may be shared between seller and platform.
        buyer_fault_return_shipping_fee (str | Unset): Shipping fee for buyer-fault returns. In some cases, the fee may
            be shared between seller and platform.
        insurance_fee (str | Unset): Premium charged per order for insurance coverage
        cps_shop_ads_commission_tax_amount (str | Unset): Sales tax applied to GMV Max ad fee
        shipping_insurance_fee_tax_amount (str | Unset): Tax applied to the shipping protection fee.
        new_customer_growth_package_fee (str | Unset): Fee for using the New Customer Growth Package to offer discounts
            that attract new customers to your shop.
        target_product_gmv_growth_package_fee (str | Unset): Fee for using the Product GMV Growth Package to offer
            discounts on selected products and increase their sales.
        store_gmv_growth_package_fee (str | Unset): Fee for using the Shop GMV Growth Package to offer store-wide
            discounts and grow your overall sales.
        auto_post_shoppable_video_commission_fee (str | Unset): The commission fee charged to the seller for orders
            attributed to the AI-generated, auto-post shoppable videos.
        seller_funded_user_spoint_service_fee (str | Unset): Service fee charged for seller-funded user S-Points issued
            to shoppers. Calculated based on the order's actual payment amount and refunded if the order is later returned.
        flash_sales_service_fee_amount (str | Unset): The service fee charged for participation in flash sales.
    """

    platform_commission_amount: str | Unset = UNSET
    referral_fee_amount: str | Unset = UNSET
    refund_administration_fee_amount: str | Unset = UNSET
    transaction_fee_amount: str | Unset = UNSET
    credit_card_handling_fee_amount: str | Unset = UNSET
    affiliate_commission_amount: str | Unset = UNSET
    affiliate_commission_before_pit_amount: str | Unset = UNSET
    pit_withheld_from_ads_commission_amount: str | Unset = UNSET
    affiliate_partner_commission_amount: str | Unset = UNSET
    affiliate_ads_commission_amount: str | Unset = UNSET
    sfp_service_fee_amount: str | Unset = UNSET
    live_specials_fee_amount: str | Unset = UNSET
    bonus_cashback_service_fee_amount: str | Unset = UNSET
    mall_service_fee_amount: str | Unset = UNSET
    retail_delivery_fee_amount: str | Unset = UNSET
    retail_delivery_fee_payment_amount: str | Unset = UNSET
    retail_delivery_fee_refund_amount: str | Unset = UNSET
    platform_special_service_fee_amount: str | Unset = UNSET
    smart_promotion_fee_amount: str | Unset = UNSET
    vn_fix_infrastructure_fee: str | Unset = UNSET
    dynamic_commission_amount: str | Unset = UNSET
    campaign_period_fee_cfp_amount: str | Unset = UNSET
    campaign_period_fee_sp_amount: str | Unset = UNSET
    campaign_period_fee_sp_tax_amount: str | Unset = UNSET
    campaign_period_fee_cfp_tax_amount: str | Unset = UNSET
    seller_growth_fee_amount: str | Unset = UNSET
    failed_delivery_shipping_fee: str | Unset = UNSET
    buyer_fault_return_shipping_fee: str | Unset = UNSET
    insurance_fee: str | Unset = UNSET
    cps_shop_ads_commission_tax_amount: str | Unset = UNSET
    shipping_insurance_fee_tax_amount: str | Unset = UNSET
    new_customer_growth_package_fee: str | Unset = UNSET
    target_product_gmv_growth_package_fee: str | Unset = UNSET
    store_gmv_growth_package_fee: str | Unset = UNSET
    auto_post_shoppable_video_commission_fee: str | Unset = UNSET
    seller_funded_user_spoint_service_fee: str | Unset = UNSET
    flash_sales_service_fee_amount: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_commission_amount = self.platform_commission_amount

        referral_fee_amount = self.referral_fee_amount

        refund_administration_fee_amount = self.refund_administration_fee_amount

        transaction_fee_amount = self.transaction_fee_amount

        credit_card_handling_fee_amount = self.credit_card_handling_fee_amount

        affiliate_commission_amount = self.affiliate_commission_amount

        affiliate_commission_before_pit_amount = self.affiliate_commission_before_pit_amount

        pit_withheld_from_ads_commission_amount = self.pit_withheld_from_ads_commission_amount

        affiliate_partner_commission_amount = self.affiliate_partner_commission_amount

        affiliate_ads_commission_amount = self.affiliate_ads_commission_amount

        sfp_service_fee_amount = self.sfp_service_fee_amount

        live_specials_fee_amount = self.live_specials_fee_amount

        bonus_cashback_service_fee_amount = self.bonus_cashback_service_fee_amount

        mall_service_fee_amount = self.mall_service_fee_amount

        retail_delivery_fee_amount = self.retail_delivery_fee_amount

        retail_delivery_fee_payment_amount = self.retail_delivery_fee_payment_amount

        retail_delivery_fee_refund_amount = self.retail_delivery_fee_refund_amount

        platform_special_service_fee_amount = self.platform_special_service_fee_amount

        smart_promotion_fee_amount = self.smart_promotion_fee_amount

        vn_fix_infrastructure_fee = self.vn_fix_infrastructure_fee

        dynamic_commission_amount = self.dynamic_commission_amount

        campaign_period_fee_cfp_amount = self.campaign_period_fee_cfp_amount

        campaign_period_fee_sp_amount = self.campaign_period_fee_sp_amount

        campaign_period_fee_sp_tax_amount = self.campaign_period_fee_sp_tax_amount

        campaign_period_fee_cfp_tax_amount = self.campaign_period_fee_cfp_tax_amount

        seller_growth_fee_amount = self.seller_growth_fee_amount

        failed_delivery_shipping_fee = self.failed_delivery_shipping_fee

        buyer_fault_return_shipping_fee = self.buyer_fault_return_shipping_fee

        insurance_fee = self.insurance_fee

        cps_shop_ads_commission_tax_amount = self.cps_shop_ads_commission_tax_amount

        shipping_insurance_fee_tax_amount = self.shipping_insurance_fee_tax_amount

        new_customer_growth_package_fee = self.new_customer_growth_package_fee

        target_product_gmv_growth_package_fee = self.target_product_gmv_growth_package_fee

        store_gmv_growth_package_fee = self.store_gmv_growth_package_fee

        auto_post_shoppable_video_commission_fee = self.auto_post_shoppable_video_commission_fee

        seller_funded_user_spoint_service_fee = self.seller_funded_user_spoint_service_fee

        flash_sales_service_fee_amount = self.flash_sales_service_fee_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform_commission_amount is not UNSET:
            field_dict["platform_commission_amount"] = platform_commission_amount
        if referral_fee_amount is not UNSET:
            field_dict["referral_fee_amount"] = referral_fee_amount
        if refund_administration_fee_amount is not UNSET:
            field_dict["refund_administration_fee_amount"] = refund_administration_fee_amount
        if transaction_fee_amount is not UNSET:
            field_dict["transaction_fee_amount"] = transaction_fee_amount
        if credit_card_handling_fee_amount is not UNSET:
            field_dict["credit_card_handling_fee_amount"] = credit_card_handling_fee_amount
        if affiliate_commission_amount is not UNSET:
            field_dict["affiliate_commission_amount"] = affiliate_commission_amount
        if affiliate_commission_before_pit_amount is not UNSET:
            field_dict["affiliate_commission_before_pit_amount"] = affiliate_commission_before_pit_amount
        if pit_withheld_from_ads_commission_amount is not UNSET:
            field_dict["pit_withheld_from_ads_commission_amount"] = pit_withheld_from_ads_commission_amount
        if affiliate_partner_commission_amount is not UNSET:
            field_dict["affiliate_partner_commission_amount"] = affiliate_partner_commission_amount
        if affiliate_ads_commission_amount is not UNSET:
            field_dict["affiliate_ads_commission_amount"] = affiliate_ads_commission_amount
        if sfp_service_fee_amount is not UNSET:
            field_dict["sfp_service_fee_amount"] = sfp_service_fee_amount
        if live_specials_fee_amount is not UNSET:
            field_dict["live_specials_fee_amount"] = live_specials_fee_amount
        if bonus_cashback_service_fee_amount is not UNSET:
            field_dict["bonus_cashback_service_fee_amount"] = bonus_cashback_service_fee_amount
        if mall_service_fee_amount is not UNSET:
            field_dict["mall_service_fee_amount"] = mall_service_fee_amount
        if retail_delivery_fee_amount is not UNSET:
            field_dict["retail_delivery_fee_amount"] = retail_delivery_fee_amount
        if retail_delivery_fee_payment_amount is not UNSET:
            field_dict["retail_delivery_fee_payment_amount"] = retail_delivery_fee_payment_amount
        if retail_delivery_fee_refund_amount is not UNSET:
            field_dict["retail_delivery_fee_refund_amount"] = retail_delivery_fee_refund_amount
        if platform_special_service_fee_amount is not UNSET:
            field_dict["platform_special_service_fee_amount"] = platform_special_service_fee_amount
        if smart_promotion_fee_amount is not UNSET:
            field_dict["smart_promotion_fee_amount"] = smart_promotion_fee_amount
        if vn_fix_infrastructure_fee is not UNSET:
            field_dict["vn_fix_infrastructure_fee"] = vn_fix_infrastructure_fee
        if dynamic_commission_amount is not UNSET:
            field_dict["dynamic_commission_amount"] = dynamic_commission_amount
        if campaign_period_fee_cfp_amount is not UNSET:
            field_dict["campaign_period_fee_cfp_amount"] = campaign_period_fee_cfp_amount
        if campaign_period_fee_sp_amount is not UNSET:
            field_dict["campaign_period_fee_sp_amount"] = campaign_period_fee_sp_amount
        if campaign_period_fee_sp_tax_amount is not UNSET:
            field_dict["campaign_period_fee_sp_tax_amount"] = campaign_period_fee_sp_tax_amount
        if campaign_period_fee_cfp_tax_amount is not UNSET:
            field_dict["campaign_period_fee_cfp_tax_amount"] = campaign_period_fee_cfp_tax_amount
        if seller_growth_fee_amount is not UNSET:
            field_dict["seller_growth_fee_amount"] = seller_growth_fee_amount
        if failed_delivery_shipping_fee is not UNSET:
            field_dict["failed_delivery_shipping_fee"] = failed_delivery_shipping_fee
        if buyer_fault_return_shipping_fee is not UNSET:
            field_dict["buyer_fault_return_shipping_fee"] = buyer_fault_return_shipping_fee
        if insurance_fee is not UNSET:
            field_dict["insurance_fee"] = insurance_fee
        if cps_shop_ads_commission_tax_amount is not UNSET:
            field_dict["cps_shop_ads_commission_tax_amount"] = cps_shop_ads_commission_tax_amount
        if shipping_insurance_fee_tax_amount is not UNSET:
            field_dict["shipping_insurance_fee_tax_amount"] = shipping_insurance_fee_tax_amount
        if new_customer_growth_package_fee is not UNSET:
            field_dict["new_customer_growth_package_fee"] = new_customer_growth_package_fee
        if target_product_gmv_growth_package_fee is not UNSET:
            field_dict["target_product_gmv_growth_package_fee"] = target_product_gmv_growth_package_fee
        if store_gmv_growth_package_fee is not UNSET:
            field_dict["store_gmv_growth_package_fee"] = store_gmv_growth_package_fee
        if auto_post_shoppable_video_commission_fee is not UNSET:
            field_dict["auto_post_shoppable_video_commission_fee"] = auto_post_shoppable_video_commission_fee
        if seller_funded_user_spoint_service_fee is not UNSET:
            field_dict["seller_funded_user_spoint_service_fee"] = seller_funded_user_spoint_service_fee
        if flash_sales_service_fee_amount is not UNSET:
            field_dict["flash_sales_service_fee_amount"] = flash_sales_service_fee_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform_commission_amount = d.pop("platform_commission_amount", UNSET)

        referral_fee_amount = d.pop("referral_fee_amount", UNSET)

        refund_administration_fee_amount = d.pop("refund_administration_fee_amount", UNSET)

        transaction_fee_amount = d.pop("transaction_fee_amount", UNSET)

        credit_card_handling_fee_amount = d.pop("credit_card_handling_fee_amount", UNSET)

        affiliate_commission_amount = d.pop("affiliate_commission_amount", UNSET)

        affiliate_commission_before_pit_amount = d.pop("affiliate_commission_before_pit_amount", UNSET)

        pit_withheld_from_ads_commission_amount = d.pop("pit_withheld_from_ads_commission_amount", UNSET)

        affiliate_partner_commission_amount = d.pop("affiliate_partner_commission_amount", UNSET)

        affiliate_ads_commission_amount = d.pop("affiliate_ads_commission_amount", UNSET)

        sfp_service_fee_amount = d.pop("sfp_service_fee_amount", UNSET)

        live_specials_fee_amount = d.pop("live_specials_fee_amount", UNSET)

        bonus_cashback_service_fee_amount = d.pop("bonus_cashback_service_fee_amount", UNSET)

        mall_service_fee_amount = d.pop("mall_service_fee_amount", UNSET)

        retail_delivery_fee_amount = d.pop("retail_delivery_fee_amount", UNSET)

        retail_delivery_fee_payment_amount = d.pop("retail_delivery_fee_payment_amount", UNSET)

        retail_delivery_fee_refund_amount = d.pop("retail_delivery_fee_refund_amount", UNSET)

        platform_special_service_fee_amount = d.pop("platform_special_service_fee_amount", UNSET)

        smart_promotion_fee_amount = d.pop("smart_promotion_fee_amount", UNSET)

        vn_fix_infrastructure_fee = d.pop("vn_fix_infrastructure_fee", UNSET)

        dynamic_commission_amount = d.pop("dynamic_commission_amount", UNSET)

        campaign_period_fee_cfp_amount = d.pop("campaign_period_fee_cfp_amount", UNSET)

        campaign_period_fee_sp_amount = d.pop("campaign_period_fee_sp_amount", UNSET)

        campaign_period_fee_sp_tax_amount = d.pop("campaign_period_fee_sp_tax_amount", UNSET)

        campaign_period_fee_cfp_tax_amount = d.pop("campaign_period_fee_cfp_tax_amount", UNSET)

        seller_growth_fee_amount = d.pop("seller_growth_fee_amount", UNSET)

        failed_delivery_shipping_fee = d.pop("failed_delivery_shipping_fee", UNSET)

        buyer_fault_return_shipping_fee = d.pop("buyer_fault_return_shipping_fee", UNSET)

        insurance_fee = d.pop("insurance_fee", UNSET)

        cps_shop_ads_commission_tax_amount = d.pop("cps_shop_ads_commission_tax_amount", UNSET)

        shipping_insurance_fee_tax_amount = d.pop("shipping_insurance_fee_tax_amount", UNSET)

        new_customer_growth_package_fee = d.pop("new_customer_growth_package_fee", UNSET)

        target_product_gmv_growth_package_fee = d.pop("target_product_gmv_growth_package_fee", UNSET)

        store_gmv_growth_package_fee = d.pop("store_gmv_growth_package_fee", UNSET)

        auto_post_shoppable_video_commission_fee = d.pop("auto_post_shoppable_video_commission_fee", UNSET)

        seller_funded_user_spoint_service_fee = d.pop("seller_funded_user_spoint_service_fee", UNSET)

        flash_sales_service_fee_amount = d.pop("flash_sales_service_fee_amount", UNSET)

        get_unsettled_transactions_response_data_transaction_fee_tax_breakdown_fee = cls(
            platform_commission_amount=platform_commission_amount,
            referral_fee_amount=referral_fee_amount,
            refund_administration_fee_amount=refund_administration_fee_amount,
            transaction_fee_amount=transaction_fee_amount,
            credit_card_handling_fee_amount=credit_card_handling_fee_amount,
            affiliate_commission_amount=affiliate_commission_amount,
            affiliate_commission_before_pit_amount=affiliate_commission_before_pit_amount,
            pit_withheld_from_ads_commission_amount=pit_withheld_from_ads_commission_amount,
            affiliate_partner_commission_amount=affiliate_partner_commission_amount,
            affiliate_ads_commission_amount=affiliate_ads_commission_amount,
            sfp_service_fee_amount=sfp_service_fee_amount,
            live_specials_fee_amount=live_specials_fee_amount,
            bonus_cashback_service_fee_amount=bonus_cashback_service_fee_amount,
            mall_service_fee_amount=mall_service_fee_amount,
            retail_delivery_fee_amount=retail_delivery_fee_amount,
            retail_delivery_fee_payment_amount=retail_delivery_fee_payment_amount,
            retail_delivery_fee_refund_amount=retail_delivery_fee_refund_amount,
            platform_special_service_fee_amount=platform_special_service_fee_amount,
            smart_promotion_fee_amount=smart_promotion_fee_amount,
            vn_fix_infrastructure_fee=vn_fix_infrastructure_fee,
            dynamic_commission_amount=dynamic_commission_amount,
            campaign_period_fee_cfp_amount=campaign_period_fee_cfp_amount,
            campaign_period_fee_sp_amount=campaign_period_fee_sp_amount,
            campaign_period_fee_sp_tax_amount=campaign_period_fee_sp_tax_amount,
            campaign_period_fee_cfp_tax_amount=campaign_period_fee_cfp_tax_amount,
            seller_growth_fee_amount=seller_growth_fee_amount,
            failed_delivery_shipping_fee=failed_delivery_shipping_fee,
            buyer_fault_return_shipping_fee=buyer_fault_return_shipping_fee,
            insurance_fee=insurance_fee,
            cps_shop_ads_commission_tax_amount=cps_shop_ads_commission_tax_amount,
            shipping_insurance_fee_tax_amount=shipping_insurance_fee_tax_amount,
            new_customer_growth_package_fee=new_customer_growth_package_fee,
            target_product_gmv_growth_package_fee=target_product_gmv_growth_package_fee,
            store_gmv_growth_package_fee=store_gmv_growth_package_fee,
            auto_post_shoppable_video_commission_fee=auto_post_shoppable_video_commission_fee,
            seller_funded_user_spoint_service_fee=seller_funded_user_spoint_service_fee,
            flash_sales_service_fee_amount=flash_sales_service_fee_amount,
        )

        get_unsettled_transactions_response_data_transaction_fee_tax_breakdown_fee.additional_properties = d
        return get_unsettled_transactions_response_data_transaction_fee_tax_breakdown_fee

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
