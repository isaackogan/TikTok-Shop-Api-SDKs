from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownFee")


@_attrs_define
class GetTransactionsByOrderResponseDataSkuTransactionFeeTaxBreakdownFee:
    """
    Attributes:
        platform_commission_amount (str | Unset): The commission amount charged by TikTok Shop.
        referral_fee_amount (str | Unset): The referral fee charged for processing successful orders.
            Applicable only for the US.
        refund_administration_fee_amount (str | Unset): The 20% refund administration fee deducted from the total
            refunded referral fee amount.
        transaction_fee_amount (str | Unset): The transaction fee charged for processing successful orders.
        credit_card_handling_fee_amount (str | Unset): The handling fee charged when the buyer pays with a credit card.
        affiliate_commission_amount (str | Unset): The commission amount charged to the seller for payment to the
            creator.
        affiliate_commission_amount_before_pit (str | Unset): The affiliate ads commission paid to a creator before any
            personal income tax withholding.
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
        voucher_xtra_service_fee_amount (str | Unset): The service fee charged for participation in the Voucher Xtra
            program.
        flash_sales_service_fee_amount (str | Unset): The service fee charged for participation in flash sales.
        cofunded_promotion_service_fee_amount (str | Unset): The service fee charged for co-funded promotions.
        pre_order_service_fee_amount (str | Unset): The service fee charged when seller joins Pre-order program.
        tsp_commission_amount (str | Unset): The commission amount charged by TikTok Shop Partners (TSP).
        dt_handling_fee_amount (str | Unset): The handling fee charged for orders that are fulfilled by Dilayani
            Tokopedia.
        epr_pob_service_fee_amount (str | Unset): The eco-contributions TikTok Shop pays on your behalf to the qualified
            producer responsibility organization (PRO).
        fee_per_item_sold_amount (str | Unset): The fee charged to sellers by the platform for each item sold.
            Applicable only for the Brazil market.
        seller_paylater_handling_fee_amount (str | Unset): The handling fee charged to the seller for participation in
            the PayLater program.
        cofunded_creator_bonus_amount (str | Unset): The portion of the creator bonus that you co-fund as part of the
            commission boost campaign.
        dynamic_commission_amount (str | Unset): The dynamic commission fee is the amount that the platform charges to
            all sellers for every successfully delivered order.
            Applicable only for Indonesia.
        external_affiliate_marketing_fee_amount (str | Unset): The service fee for participating in the External
            Affiliate Marketing Solution Program, as stated during registration.
        vn_fix_infrastructure_fee (str | Unset): Infrastructure fees are a fixed service fee that TikTok Shop charges
            for providing, maintaining, and developing infrastructure for delivery services. It applies to delivered orders
            on the main order level.
        affiliate_commission_deposit (str | Unset): The amount reserved for creator commissions after an order is paid.
            Applies only to commissions tied to order volume and is based on the highest earning rate.
        affiliate_commission_release (str | Unset): The commission deposit refunded to you after order settlement.
            Applies only to commissions tied to order volume.
        tap_shop_ads_commission (str | Unset): The advertising commission cost a merchant pays to TikTok Shop Affiliate
            Partner (TAP).
        shipping_fee_guarantee_service_fee (str | Unset): A flat service fee charged for each order under the Shipping
            Fee Guarantee Program
        installation_service_fee (str | Unset): The fee TikTok Shop charges you for using platform installation service
        campaign_resource_fee (str | Unset): Amount of campaign resource fee from program seller joining in
        platform_special_service_fee_amount (str | Unset): The portion of the Distance Shipping Fee paid by the customer
            that exceeds the logistics service provider's charge, retained by TikTok Shop to support a secure fulfillment
            experience
        smart_promotion_fee_amount (str | Unset): This fee includes funds from TikTok Shop to help provide promotions to
            customers
        gmv_max_ad_fee_amount (str | Unset): A percentage deducted from your net sales per order for GMV Max (net sales
            performance goal) advertising.
        platform_semi_managed_commission_fee (str | Unset): Calculated as a percentage of (original price − seller
            discount + customer-paid shipping fee).
        platform_semi_managed_commission_fee_tax (str | Unset): This amount is collected on behalf of the government.
        campaign_period_fee_cfp_amount (str | Unset): Fee charged during Co-funded Promotion campaigns.
        campaign_period_fee_sp_amount (str | Unset): Fee charged during Smart Promotion campaigns.
        campaign_period_fee_sp_tax_amount (str | Unset): Sales tax applied to the campaign period fee under Smart
            Promotion.
        campaign_period_fee_cfp_tax_amount (str | Unset): Sales tax applied to the campaign period fee under Co-funded
            Promotion.
        seller_growth_fee_amount (str | Unset): A fee charged on each successful order to provide Bonus Cashback and
            other growth benefits.
        category_led_campaign_fee_amount (str | Unset): Fee charged for participating in the Category-led campaign.
        category_led_campaign_fee_tax_amount (str | Unset): Sales tax charged for the fee.
        brand_amplification_program_commission (str | Unset): Commission fee charged for participating in the Brand
            Amplification Program.
        brand_amplification_program_fee_tax (str | Unset): Sales tax charged for the fee.
        brand_campaign_fee (str | Unset): Fee charged for participating in the Brand campaign.
        brand_campaign_fee_tax (str | Unset): Sales tax charged for the fee.
        failed_delivery_shipping_fee (str | Unset): Shipping fee for order that failed to be delivered to the customer.
            In some cases, the fee may be shared between seller and platform.
        buyer_fault_return_shipping_fee (str | Unset): Shipping fee for buyer-fault returns. In some cases, the fee may
            be shared between seller and platform.
        insurance_fee (str | Unset): Premium charged per order for insurance coverage
        gmv_max_coupon_fee (str | Unset): The cost of GMV Max coupons.
        cps_shop_ads_commission_tax_amount (str | Unset): Sales tax applied to GMV Max ad fee
        shipping_insurance_fee_tax_amount (str | Unset): The tax amount charged on the shipping insurance fee.
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
    """

    platform_commission_amount: str | Unset = UNSET
    referral_fee_amount: str | Unset = UNSET
    refund_administration_fee_amount: str | Unset = UNSET
    transaction_fee_amount: str | Unset = UNSET
    credit_card_handling_fee_amount: str | Unset = UNSET
    affiliate_commission_amount: str | Unset = UNSET
    affiliate_commission_amount_before_pit: str | Unset = UNSET
    affiliate_partner_commission_amount: str | Unset = UNSET
    affiliate_ads_commission_amount: str | Unset = UNSET
    sfp_service_fee_amount: str | Unset = UNSET
    live_specials_fee_amount: str | Unset = UNSET
    bonus_cashback_service_fee_amount: str | Unset = UNSET
    mall_service_fee_amount: str | Unset = UNSET
    voucher_xtra_service_fee_amount: str | Unset = UNSET
    flash_sales_service_fee_amount: str | Unset = UNSET
    cofunded_promotion_service_fee_amount: str | Unset = UNSET
    pre_order_service_fee_amount: str | Unset = UNSET
    tsp_commission_amount: str | Unset = UNSET
    dt_handling_fee_amount: str | Unset = UNSET
    epr_pob_service_fee_amount: str | Unset = UNSET
    fee_per_item_sold_amount: str | Unset = UNSET
    seller_paylater_handling_fee_amount: str | Unset = UNSET
    cofunded_creator_bonus_amount: str | Unset = UNSET
    dynamic_commission_amount: str | Unset = UNSET
    external_affiliate_marketing_fee_amount: str | Unset = UNSET
    vn_fix_infrastructure_fee: str | Unset = UNSET
    affiliate_commission_deposit: str | Unset = UNSET
    affiliate_commission_release: str | Unset = UNSET
    tap_shop_ads_commission: str | Unset = UNSET
    shipping_fee_guarantee_service_fee: str | Unset = UNSET
    installation_service_fee: str | Unset = UNSET
    campaign_resource_fee: str | Unset = UNSET
    platform_special_service_fee_amount: str | Unset = UNSET
    smart_promotion_fee_amount: str | Unset = UNSET
    gmv_max_ad_fee_amount: str | Unset = UNSET
    platform_semi_managed_commission_fee: str | Unset = UNSET
    platform_semi_managed_commission_fee_tax: str | Unset = UNSET
    campaign_period_fee_cfp_amount: str | Unset = UNSET
    campaign_period_fee_sp_amount: str | Unset = UNSET
    campaign_period_fee_sp_tax_amount: str | Unset = UNSET
    campaign_period_fee_cfp_tax_amount: str | Unset = UNSET
    seller_growth_fee_amount: str | Unset = UNSET
    category_led_campaign_fee_amount: str | Unset = UNSET
    category_led_campaign_fee_tax_amount: str | Unset = UNSET
    brand_amplification_program_commission: str | Unset = UNSET
    brand_amplification_program_fee_tax: str | Unset = UNSET
    brand_campaign_fee: str | Unset = UNSET
    brand_campaign_fee_tax: str | Unset = UNSET
    failed_delivery_shipping_fee: str | Unset = UNSET
    buyer_fault_return_shipping_fee: str | Unset = UNSET
    insurance_fee: str | Unset = UNSET
    gmv_max_coupon_fee: str | Unset = UNSET
    cps_shop_ads_commission_tax_amount: str | Unset = UNSET
    shipping_insurance_fee_tax_amount: str | Unset = UNSET
    new_customer_growth_package_fee: str | Unset = UNSET
    target_product_gmv_growth_package_fee: str | Unset = UNSET
    store_gmv_growth_package_fee: str | Unset = UNSET
    auto_post_shoppable_video_commission_fee: str | Unset = UNSET
    seller_funded_user_spoint_service_fee: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_commission_amount = self.platform_commission_amount

        referral_fee_amount = self.referral_fee_amount

        refund_administration_fee_amount = self.refund_administration_fee_amount

        transaction_fee_amount = self.transaction_fee_amount

        credit_card_handling_fee_amount = self.credit_card_handling_fee_amount

        affiliate_commission_amount = self.affiliate_commission_amount

        affiliate_commission_amount_before_pit = self.affiliate_commission_amount_before_pit

        affiliate_partner_commission_amount = self.affiliate_partner_commission_amount

        affiliate_ads_commission_amount = self.affiliate_ads_commission_amount

        sfp_service_fee_amount = self.sfp_service_fee_amount

        live_specials_fee_amount = self.live_specials_fee_amount

        bonus_cashback_service_fee_amount = self.bonus_cashback_service_fee_amount

        mall_service_fee_amount = self.mall_service_fee_amount

        voucher_xtra_service_fee_amount = self.voucher_xtra_service_fee_amount

        flash_sales_service_fee_amount = self.flash_sales_service_fee_amount

        cofunded_promotion_service_fee_amount = self.cofunded_promotion_service_fee_amount

        pre_order_service_fee_amount = self.pre_order_service_fee_amount

        tsp_commission_amount = self.tsp_commission_amount

        dt_handling_fee_amount = self.dt_handling_fee_amount

        epr_pob_service_fee_amount = self.epr_pob_service_fee_amount

        fee_per_item_sold_amount = self.fee_per_item_sold_amount

        seller_paylater_handling_fee_amount = self.seller_paylater_handling_fee_amount

        cofunded_creator_bonus_amount = self.cofunded_creator_bonus_amount

        dynamic_commission_amount = self.dynamic_commission_amount

        external_affiliate_marketing_fee_amount = self.external_affiliate_marketing_fee_amount

        vn_fix_infrastructure_fee = self.vn_fix_infrastructure_fee

        affiliate_commission_deposit = self.affiliate_commission_deposit

        affiliate_commission_release = self.affiliate_commission_release

        tap_shop_ads_commission = self.tap_shop_ads_commission

        shipping_fee_guarantee_service_fee = self.shipping_fee_guarantee_service_fee

        installation_service_fee = self.installation_service_fee

        campaign_resource_fee = self.campaign_resource_fee

        platform_special_service_fee_amount = self.platform_special_service_fee_amount

        smart_promotion_fee_amount = self.smart_promotion_fee_amount

        gmv_max_ad_fee_amount = self.gmv_max_ad_fee_amount

        platform_semi_managed_commission_fee = self.platform_semi_managed_commission_fee

        platform_semi_managed_commission_fee_tax = self.platform_semi_managed_commission_fee_tax

        campaign_period_fee_cfp_amount = self.campaign_period_fee_cfp_amount

        campaign_period_fee_sp_amount = self.campaign_period_fee_sp_amount

        campaign_period_fee_sp_tax_amount = self.campaign_period_fee_sp_tax_amount

        campaign_period_fee_cfp_tax_amount = self.campaign_period_fee_cfp_tax_amount

        seller_growth_fee_amount = self.seller_growth_fee_amount

        category_led_campaign_fee_amount = self.category_led_campaign_fee_amount

        category_led_campaign_fee_tax_amount = self.category_led_campaign_fee_tax_amount

        brand_amplification_program_commission = self.brand_amplification_program_commission

        brand_amplification_program_fee_tax = self.brand_amplification_program_fee_tax

        brand_campaign_fee = self.brand_campaign_fee

        brand_campaign_fee_tax = self.brand_campaign_fee_tax

        failed_delivery_shipping_fee = self.failed_delivery_shipping_fee

        buyer_fault_return_shipping_fee = self.buyer_fault_return_shipping_fee

        insurance_fee = self.insurance_fee

        gmv_max_coupon_fee = self.gmv_max_coupon_fee

        cps_shop_ads_commission_tax_amount = self.cps_shop_ads_commission_tax_amount

        shipping_insurance_fee_tax_amount = self.shipping_insurance_fee_tax_amount

        new_customer_growth_package_fee = self.new_customer_growth_package_fee

        target_product_gmv_growth_package_fee = self.target_product_gmv_growth_package_fee

        store_gmv_growth_package_fee = self.store_gmv_growth_package_fee

        auto_post_shoppable_video_commission_fee = self.auto_post_shoppable_video_commission_fee

        seller_funded_user_spoint_service_fee = self.seller_funded_user_spoint_service_fee

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
        if affiliate_commission_amount_before_pit is not UNSET:
            field_dict["affiliate_commission_amount_before_pit"] = affiliate_commission_amount_before_pit
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
        if voucher_xtra_service_fee_amount is not UNSET:
            field_dict["voucher_xtra_service_fee_amount"] = voucher_xtra_service_fee_amount
        if flash_sales_service_fee_amount is not UNSET:
            field_dict["flash_sales_service_fee_amount"] = flash_sales_service_fee_amount
        if cofunded_promotion_service_fee_amount is not UNSET:
            field_dict["cofunded_promotion_service_fee_amount"] = cofunded_promotion_service_fee_amount
        if pre_order_service_fee_amount is not UNSET:
            field_dict["pre_order_service_fee_amount"] = pre_order_service_fee_amount
        if tsp_commission_amount is not UNSET:
            field_dict["tsp_commission_amount"] = tsp_commission_amount
        if dt_handling_fee_amount is not UNSET:
            field_dict["dt_handling_fee_amount"] = dt_handling_fee_amount
        if epr_pob_service_fee_amount is not UNSET:
            field_dict["epr_pob_service_fee_amount"] = epr_pob_service_fee_amount
        if fee_per_item_sold_amount is not UNSET:
            field_dict["fee_per_item_sold_amount"] = fee_per_item_sold_amount
        if seller_paylater_handling_fee_amount is not UNSET:
            field_dict["seller_paylater_handling_fee_amount"] = seller_paylater_handling_fee_amount
        if cofunded_creator_bonus_amount is not UNSET:
            field_dict["cofunded_creator_bonus_amount"] = cofunded_creator_bonus_amount
        if dynamic_commission_amount is not UNSET:
            field_dict["dynamic_commission_amount"] = dynamic_commission_amount
        if external_affiliate_marketing_fee_amount is not UNSET:
            field_dict["external_affiliate_marketing_fee_amount"] = external_affiliate_marketing_fee_amount
        if vn_fix_infrastructure_fee is not UNSET:
            field_dict["vn_fix_infrastructure_fee"] = vn_fix_infrastructure_fee
        if affiliate_commission_deposit is not UNSET:
            field_dict["affiliate_commission_deposit"] = affiliate_commission_deposit
        if affiliate_commission_release is not UNSET:
            field_dict["affiliate_commission_release"] = affiliate_commission_release
        if tap_shop_ads_commission is not UNSET:
            field_dict["tap_shop_ads_commission"] = tap_shop_ads_commission
        if shipping_fee_guarantee_service_fee is not UNSET:
            field_dict["shipping_fee_guarantee_service_fee"] = shipping_fee_guarantee_service_fee
        if installation_service_fee is not UNSET:
            field_dict["installation_service_fee"] = installation_service_fee
        if campaign_resource_fee is not UNSET:
            field_dict["campaign_resource_fee"] = campaign_resource_fee
        if platform_special_service_fee_amount is not UNSET:
            field_dict["platform_special_service_fee_amount"] = platform_special_service_fee_amount
        if smart_promotion_fee_amount is not UNSET:
            field_dict["smart_promotion_fee_amount"] = smart_promotion_fee_amount
        if gmv_max_ad_fee_amount is not UNSET:
            field_dict["gmv_max_ad_fee_amount"] = gmv_max_ad_fee_amount
        if platform_semi_managed_commission_fee is not UNSET:
            field_dict["platform_semi_managed_commission_fee"] = platform_semi_managed_commission_fee
        if platform_semi_managed_commission_fee_tax is not UNSET:
            field_dict["platform_semi_managed_commission_fee_tax"] = platform_semi_managed_commission_fee_tax
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
        if category_led_campaign_fee_amount is not UNSET:
            field_dict["category_led_campaign_fee_amount"] = category_led_campaign_fee_amount
        if category_led_campaign_fee_tax_amount is not UNSET:
            field_dict["category_led_campaign_fee_tax_amount"] = category_led_campaign_fee_tax_amount
        if brand_amplification_program_commission is not UNSET:
            field_dict["brand_amplification_program_commission"] = brand_amplification_program_commission
        if brand_amplification_program_fee_tax is not UNSET:
            field_dict["brand_amplification_program_fee_tax"] = brand_amplification_program_fee_tax
        if brand_campaign_fee is not UNSET:
            field_dict["brand_campaign_fee"] = brand_campaign_fee
        if brand_campaign_fee_tax is not UNSET:
            field_dict["brand_campaign_fee_tax"] = brand_campaign_fee_tax
        if failed_delivery_shipping_fee is not UNSET:
            field_dict["failed_delivery_shipping_fee"] = failed_delivery_shipping_fee
        if buyer_fault_return_shipping_fee is not UNSET:
            field_dict["buyer_fault_return_shipping_fee"] = buyer_fault_return_shipping_fee
        if insurance_fee is not UNSET:
            field_dict["insurance_fee"] = insurance_fee
        if gmv_max_coupon_fee is not UNSET:
            field_dict["gmv_max_coupon_fee"] = gmv_max_coupon_fee
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

        affiliate_commission_amount_before_pit = d.pop("affiliate_commission_amount_before_pit", UNSET)

        affiliate_partner_commission_amount = d.pop("affiliate_partner_commission_amount", UNSET)

        affiliate_ads_commission_amount = d.pop("affiliate_ads_commission_amount", UNSET)

        sfp_service_fee_amount = d.pop("sfp_service_fee_amount", UNSET)

        live_specials_fee_amount = d.pop("live_specials_fee_amount", UNSET)

        bonus_cashback_service_fee_amount = d.pop("bonus_cashback_service_fee_amount", UNSET)

        mall_service_fee_amount = d.pop("mall_service_fee_amount", UNSET)

        voucher_xtra_service_fee_amount = d.pop("voucher_xtra_service_fee_amount", UNSET)

        flash_sales_service_fee_amount = d.pop("flash_sales_service_fee_amount", UNSET)

        cofunded_promotion_service_fee_amount = d.pop("cofunded_promotion_service_fee_amount", UNSET)

        pre_order_service_fee_amount = d.pop("pre_order_service_fee_amount", UNSET)

        tsp_commission_amount = d.pop("tsp_commission_amount", UNSET)

        dt_handling_fee_amount = d.pop("dt_handling_fee_amount", UNSET)

        epr_pob_service_fee_amount = d.pop("epr_pob_service_fee_amount", UNSET)

        fee_per_item_sold_amount = d.pop("fee_per_item_sold_amount", UNSET)

        seller_paylater_handling_fee_amount = d.pop("seller_paylater_handling_fee_amount", UNSET)

        cofunded_creator_bonus_amount = d.pop("cofunded_creator_bonus_amount", UNSET)

        dynamic_commission_amount = d.pop("dynamic_commission_amount", UNSET)

        external_affiliate_marketing_fee_amount = d.pop("external_affiliate_marketing_fee_amount", UNSET)

        vn_fix_infrastructure_fee = d.pop("vn_fix_infrastructure_fee", UNSET)

        affiliate_commission_deposit = d.pop("affiliate_commission_deposit", UNSET)

        affiliate_commission_release = d.pop("affiliate_commission_release", UNSET)

        tap_shop_ads_commission = d.pop("tap_shop_ads_commission", UNSET)

        shipping_fee_guarantee_service_fee = d.pop("shipping_fee_guarantee_service_fee", UNSET)

        installation_service_fee = d.pop("installation_service_fee", UNSET)

        campaign_resource_fee = d.pop("campaign_resource_fee", UNSET)

        platform_special_service_fee_amount = d.pop("platform_special_service_fee_amount", UNSET)

        smart_promotion_fee_amount = d.pop("smart_promotion_fee_amount", UNSET)

        gmv_max_ad_fee_amount = d.pop("gmv_max_ad_fee_amount", UNSET)

        platform_semi_managed_commission_fee = d.pop("platform_semi_managed_commission_fee", UNSET)

        platform_semi_managed_commission_fee_tax = d.pop("platform_semi_managed_commission_fee_tax", UNSET)

        campaign_period_fee_cfp_amount = d.pop("campaign_period_fee_cfp_amount", UNSET)

        campaign_period_fee_sp_amount = d.pop("campaign_period_fee_sp_amount", UNSET)

        campaign_period_fee_sp_tax_amount = d.pop("campaign_period_fee_sp_tax_amount", UNSET)

        campaign_period_fee_cfp_tax_amount = d.pop("campaign_period_fee_cfp_tax_amount", UNSET)

        seller_growth_fee_amount = d.pop("seller_growth_fee_amount", UNSET)

        category_led_campaign_fee_amount = d.pop("category_led_campaign_fee_amount", UNSET)

        category_led_campaign_fee_tax_amount = d.pop("category_led_campaign_fee_tax_amount", UNSET)

        brand_amplification_program_commission = d.pop("brand_amplification_program_commission", UNSET)

        brand_amplification_program_fee_tax = d.pop("brand_amplification_program_fee_tax", UNSET)

        brand_campaign_fee = d.pop("brand_campaign_fee", UNSET)

        brand_campaign_fee_tax = d.pop("brand_campaign_fee_tax", UNSET)

        failed_delivery_shipping_fee = d.pop("failed_delivery_shipping_fee", UNSET)

        buyer_fault_return_shipping_fee = d.pop("buyer_fault_return_shipping_fee", UNSET)

        insurance_fee = d.pop("insurance_fee", UNSET)

        gmv_max_coupon_fee = d.pop("gmv_max_coupon_fee", UNSET)

        cps_shop_ads_commission_tax_amount = d.pop("cps_shop_ads_commission_tax_amount", UNSET)

        shipping_insurance_fee_tax_amount = d.pop("shipping_insurance_fee_tax_amount", UNSET)

        new_customer_growth_package_fee = d.pop("new_customer_growth_package_fee", UNSET)

        target_product_gmv_growth_package_fee = d.pop("target_product_gmv_growth_package_fee", UNSET)

        store_gmv_growth_package_fee = d.pop("store_gmv_growth_package_fee", UNSET)

        auto_post_shoppable_video_commission_fee = d.pop("auto_post_shoppable_video_commission_fee", UNSET)

        seller_funded_user_spoint_service_fee = d.pop("seller_funded_user_spoint_service_fee", UNSET)

        get_transactions_by_order_response_data_sku_transaction_fee_tax_breakdown_fee = cls(
            platform_commission_amount=platform_commission_amount,
            referral_fee_amount=referral_fee_amount,
            refund_administration_fee_amount=refund_administration_fee_amount,
            transaction_fee_amount=transaction_fee_amount,
            credit_card_handling_fee_amount=credit_card_handling_fee_amount,
            affiliate_commission_amount=affiliate_commission_amount,
            affiliate_commission_amount_before_pit=affiliate_commission_amount_before_pit,
            affiliate_partner_commission_amount=affiliate_partner_commission_amount,
            affiliate_ads_commission_amount=affiliate_ads_commission_amount,
            sfp_service_fee_amount=sfp_service_fee_amount,
            live_specials_fee_amount=live_specials_fee_amount,
            bonus_cashback_service_fee_amount=bonus_cashback_service_fee_amount,
            mall_service_fee_amount=mall_service_fee_amount,
            voucher_xtra_service_fee_amount=voucher_xtra_service_fee_amount,
            flash_sales_service_fee_amount=flash_sales_service_fee_amount,
            cofunded_promotion_service_fee_amount=cofunded_promotion_service_fee_amount,
            pre_order_service_fee_amount=pre_order_service_fee_amount,
            tsp_commission_amount=tsp_commission_amount,
            dt_handling_fee_amount=dt_handling_fee_amount,
            epr_pob_service_fee_amount=epr_pob_service_fee_amount,
            fee_per_item_sold_amount=fee_per_item_sold_amount,
            seller_paylater_handling_fee_amount=seller_paylater_handling_fee_amount,
            cofunded_creator_bonus_amount=cofunded_creator_bonus_amount,
            dynamic_commission_amount=dynamic_commission_amount,
            external_affiliate_marketing_fee_amount=external_affiliate_marketing_fee_amount,
            vn_fix_infrastructure_fee=vn_fix_infrastructure_fee,
            affiliate_commission_deposit=affiliate_commission_deposit,
            affiliate_commission_release=affiliate_commission_release,
            tap_shop_ads_commission=tap_shop_ads_commission,
            shipping_fee_guarantee_service_fee=shipping_fee_guarantee_service_fee,
            installation_service_fee=installation_service_fee,
            campaign_resource_fee=campaign_resource_fee,
            platform_special_service_fee_amount=platform_special_service_fee_amount,
            smart_promotion_fee_amount=smart_promotion_fee_amount,
            gmv_max_ad_fee_amount=gmv_max_ad_fee_amount,
            platform_semi_managed_commission_fee=platform_semi_managed_commission_fee,
            platform_semi_managed_commission_fee_tax=platform_semi_managed_commission_fee_tax,
            campaign_period_fee_cfp_amount=campaign_period_fee_cfp_amount,
            campaign_period_fee_sp_amount=campaign_period_fee_sp_amount,
            campaign_period_fee_sp_tax_amount=campaign_period_fee_sp_tax_amount,
            campaign_period_fee_cfp_tax_amount=campaign_period_fee_cfp_tax_amount,
            seller_growth_fee_amount=seller_growth_fee_amount,
            category_led_campaign_fee_amount=category_led_campaign_fee_amount,
            category_led_campaign_fee_tax_amount=category_led_campaign_fee_tax_amount,
            brand_amplification_program_commission=brand_amplification_program_commission,
            brand_amplification_program_fee_tax=brand_amplification_program_fee_tax,
            brand_campaign_fee=brand_campaign_fee,
            brand_campaign_fee_tax=brand_campaign_fee_tax,
            failed_delivery_shipping_fee=failed_delivery_shipping_fee,
            buyer_fault_return_shipping_fee=buyer_fault_return_shipping_fee,
            insurance_fee=insurance_fee,
            gmv_max_coupon_fee=gmv_max_coupon_fee,
            cps_shop_ads_commission_tax_amount=cps_shop_ads_commission_tax_amount,
            shipping_insurance_fee_tax_amount=shipping_insurance_fee_tax_amount,
            new_customer_growth_package_fee=new_customer_growth_package_fee,
            target_product_gmv_growth_package_fee=target_product_gmv_growth_package_fee,
            store_gmv_growth_package_fee=store_gmv_growth_package_fee,
            auto_post_shoppable_video_commission_fee=auto_post_shoppable_video_commission_fee,
            seller_funded_user_spoint_service_fee=seller_funded_user_spoint_service_fee,
        )

        get_transactions_by_order_response_data_sku_transaction_fee_tax_breakdown_fee.additional_properties = d
        return get_transactions_by_order_response_data_sku_transaction_fee_tax_breakdown_fee

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
