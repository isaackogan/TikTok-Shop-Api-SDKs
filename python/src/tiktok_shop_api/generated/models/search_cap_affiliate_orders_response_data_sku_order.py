from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actual_bonus_commission import ActualBonusCommission
    from ..models.actual_commission_base import ActualCommissionBase
    from ..models.actual_shop_ads_commission import ActualShopAdsCommission
    from ..models.actual_standard_commission import ActualStandardCommission
    from ..models.estimated_bonus_commission import EstimatedBonusCommission
    from ..models.estimated_commission_base import EstimatedCommissionBase
    from ..models.estimated_shop_ads_commission import EstimatedShopAdsCommission
    from ..models.estimated_standard_commission import EstimatedStandardCommission
    from ..models.price import Price
    from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_agency_isr import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderActualAgencyIsr,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_agency_iva import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderActualAgencyIva,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_creator_tax_isr import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxIsr,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_creator_tax_iva import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxIva,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_creator_tax_pit import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxPit,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_creator_total_earnings_after_tax import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTotalEarningsAfterTax,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_tap_bonus_commission import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderActualTapBonusCommission,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_total_agency_commission import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderActualTotalAgencyCommission,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_agency_isr import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedAgencyIsr,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_agency_iva import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedAgencyIva,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_creator_tax_isr import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxIsr,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_creator_tax_iva import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxIva,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_creator_tax_pit import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxPit,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_creator_total_earnings_after_tax import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTotalEarningsAfterTax,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_tap_bonus_commission import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedTapBonusCommission,
    )
    from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_total_agency_earning import (
        SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedTotalAgencyEarning,
    )


T = TypeVar("T", bound="SearchCAPAffiliateOrdersResponseDataSkuOrder")


@_attrs_define
class SearchCAPAffiliateOrdersResponseDataSkuOrder:
    """
    Attributes:
        id (str | Unset): Transaction main order ID
        tags (str | Unset): The customizable ID for each order, used for tracking performance at difference front end
            modules.
        create_time (int | Unset): Unix timestamp in seconds when the order was created (UTC).
        delivery_time (int | Unset): Unix timestamp in seconds when the order was delivered (UTC). This field is omitted
            when no delivery timestamp is available.
        settle_status (str | Unset): Settlement Status of the order.
            Possible values:
            1. "CUSTOMER UNPAID",  customer hasn't paid for the orders.
            2. "PENDING", customers can still return or get a refund for this order. The earnings shown are estimates and
            waiting for settlement.
            3. "SETTLED", your earnings have already settled to your account
            4. "INELIGIBLE", The order has been returned/refunded/canceled by the buyer, and no commission will be settled.
            5. "FROZEN", Possible fraud has been detected regarding the order. The commission will be unfrozen after the
            fraud is resolved.
        sku_id (str | Unset): The SKU identifier.
        open_collaboration_id (str | Unset): The open collaboration identifier associated with the order.
        target_collaboration_id (str | Unset): The target collaboration identifier associated with the order.
        creator_username (str | Unset): Creator username
        product_name (str | Unset): The product name.
        product_id (str | Unset): Unique identifier for Product
        price (Price | Unset):
        quantity (int | Unset): Number of SKU items in the order, including refunded items.
        shop_name (str | Unset): Shop / Seller name
        content_type (str | Unset): The content format of the creator content through which the order was created.
            Possible values:
            - SHOP
            - VIDEO
            - LIVE
            - PRE_LIVE
            - PROMOTION_PAGE
            - LINKSHARE
        content_id (str | Unset): Unique identifier for content
        attribution_type (str | Unset): Attribution type for `LINKSHARE` content.
            Possible values:
            - `Direct`: same-shop attribution.
            - `Indirect`: non-same-shop attribution. The settlement commission rate is usually lower than the rate agreed in
            the Marketplace or target collaboration.

            For other content types, this field is an empty string.
        commission_model (str | Unset): Commission calculation model.
            Possible values:
            - `Fixed commission`
            - `Tiered commission`
        commission_tier_setting (str | Unset): Seller-configured commission rates for a tiered commission model,
            expressed as percentages and separated by ` OR `. Returns `-` for the fixed commission model.
        standard_commission_rate (int | Unset): Seller-to-creator standard commission rate. Returned as an integer in
            hundredths of a percent without a percent sign; for example, 3000 represents 30%.
        commission_bonus_rate (int | Unset): TTS-to-creator commission bonus rate. Returned as an integer in hundredths
            of a percent without a percent sign; for example, 3000 represents 30%.
        shop_ads_commission_rate (int | Unset): Shop Ads commission rate paid to the creator. Returned as an integer in
            hundredths of a percent without a percent sign; for example, 3000 represents 30%.
        tap_bonus_commission_rate (int | Unset): Commission bonus rate that the affiliate partner allocates to the
            creator. Returned as an integer in hundredths of a percent without a percent sign; for example, 3000 represents
            30%.
        revenue_sharing_portion_rate (int | Unset): Revenue-sharing portion between the creator and agency. Returned as
            an integer in hundredths of a percent without a percent sign; for example, 3000 represents 30%.
        estimated_commission_base (EstimatedCommissionBase | Unset):
        estimated_standard_commission (EstimatedStandardCommission | Unset):
        estimated_bonus_commission (EstimatedBonusCommission | Unset):
        estimated_shop_ads_commission (EstimatedShopAdsCommission | Unset):
        estimated_tap_bonus_commission (SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedTapBonusCommission |
            Unset):
        estimated_creator_tax_isr (SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxIsr | Unset):
        estimated_creator_tax_iva (SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxIva | Unset):
        estimated_creator_tax_pit (SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxPit | Unset):
        estimated_creator_total_earnings_after_tax
            (SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTotalEarningsAfterTax | Unset):
        estimated_total_agency_earnings (SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedTotalAgencyEarning |
            Unset):
        estimated_agency_isr (SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedAgencyIsr | Unset):
        estimated_agency_iva (SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedAgencyIva | Unset):
        actual_commission_base (ActualCommissionBase | Unset):
        actual_standard_commission (ActualStandardCommission | Unset):
        actual_bonus_commission (ActualBonusCommission | Unset):
        actual_shop_ads_commission (ActualShopAdsCommission | Unset):
        actual_tap_bonus_commission (SearchCAPAffiliateOrdersResponseDataSkuOrderActualTapBonusCommission | Unset):
        actual_creator_tax_isr (SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxIsr | Unset):
        actual_creator_tax_iva (SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxIva | Unset):
        actual_creator_tax_pit (SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxPit | Unset):
        actual_creator_total_earnings_after_tax
            (SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTotalEarningsAfterTax | Unset):
        actual_total_agency_commission (SearchCAPAffiliateOrdersResponseDataSkuOrderActualTotalAgencyCommission |
            Unset):
        actual_agency_isr (SearchCAPAffiliateOrdersResponseDataSkuOrderActualAgencyIsr | Unset):
        actual_agency_iva (SearchCAPAffiliateOrdersResponseDataSkuOrderActualAgencyIva | Unset):
        fully_return (str | Unset): Whether this SKU order was fully returned or refunded.
            Possible values:
            - `Yes`: this SKU order was fully returned or refunded, and no commission is paid.
            - `No`: this SKU order was not fully returned or refunded.
        settlement_time (int | Unset): Unix timestamp in seconds when the order commission was settled (UTC). This field
            is omitted when no settlement timestamp is available.
        last_update_time (int | Unset): Unix timestamp in seconds when the record was last updated (UTC).
        is_carousel (bool | Unset): Carousel content may involve a commission rate discount. Returns true when the SKU
            order is attributed to carousel content.
    """

    id: str | Unset = UNSET
    tags: str | Unset = UNSET
    create_time: int | Unset = UNSET
    delivery_time: int | Unset = UNSET
    settle_status: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    open_collaboration_id: str | Unset = UNSET
    target_collaboration_id: str | Unset = UNSET
    creator_username: str | Unset = UNSET
    product_name: str | Unset = UNSET
    product_id: str | Unset = UNSET
    price: Price | Unset = UNSET
    quantity: int | Unset = UNSET
    shop_name: str | Unset = UNSET
    content_type: str | Unset = UNSET
    content_id: str | Unset = UNSET
    attribution_type: str | Unset = UNSET
    commission_model: str | Unset = UNSET
    commission_tier_setting: str | Unset = UNSET
    standard_commission_rate: int | Unset = UNSET
    commission_bonus_rate: int | Unset = UNSET
    shop_ads_commission_rate: int | Unset = UNSET
    tap_bonus_commission_rate: int | Unset = UNSET
    revenue_sharing_portion_rate: int | Unset = UNSET
    estimated_commission_base: EstimatedCommissionBase | Unset = UNSET
    estimated_standard_commission: EstimatedStandardCommission | Unset = UNSET
    estimated_bonus_commission: EstimatedBonusCommission | Unset = UNSET
    estimated_shop_ads_commission: EstimatedShopAdsCommission | Unset = UNSET
    estimated_tap_bonus_commission: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedTapBonusCommission | Unset = (
        UNSET
    )
    estimated_creator_tax_isr: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxIsr | Unset = UNSET
    estimated_creator_tax_iva: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxIva | Unset = UNSET
    estimated_creator_tax_pit: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxPit | Unset = UNSET
    estimated_creator_total_earnings_after_tax: (
        SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTotalEarningsAfterTax | Unset
    ) = UNSET
    estimated_total_agency_earnings: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedTotalAgencyEarning | Unset = (
        UNSET
    )
    estimated_agency_isr: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedAgencyIsr | Unset = UNSET
    estimated_agency_iva: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedAgencyIva | Unset = UNSET
    actual_commission_base: ActualCommissionBase | Unset = UNSET
    actual_standard_commission: ActualStandardCommission | Unset = UNSET
    actual_bonus_commission: ActualBonusCommission | Unset = UNSET
    actual_shop_ads_commission: ActualShopAdsCommission | Unset = UNSET
    actual_tap_bonus_commission: SearchCAPAffiliateOrdersResponseDataSkuOrderActualTapBonusCommission | Unset = UNSET
    actual_creator_tax_isr: SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxIsr | Unset = UNSET
    actual_creator_tax_iva: SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxIva | Unset = UNSET
    actual_creator_tax_pit: SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxPit | Unset = UNSET
    actual_creator_total_earnings_after_tax: (
        SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTotalEarningsAfterTax | Unset
    ) = UNSET
    actual_total_agency_commission: SearchCAPAffiliateOrdersResponseDataSkuOrderActualTotalAgencyCommission | Unset = (
        UNSET
    )
    actual_agency_isr: SearchCAPAffiliateOrdersResponseDataSkuOrderActualAgencyIsr | Unset = UNSET
    actual_agency_iva: SearchCAPAffiliateOrdersResponseDataSkuOrderActualAgencyIva | Unset = UNSET
    fully_return: str | Unset = UNSET
    settlement_time: int | Unset = UNSET
    last_update_time: int | Unset = UNSET
    is_carousel: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        tags = self.tags

        create_time = self.create_time

        delivery_time = self.delivery_time

        settle_status = self.settle_status

        sku_id = self.sku_id

        open_collaboration_id = self.open_collaboration_id

        target_collaboration_id = self.target_collaboration_id

        creator_username = self.creator_username

        product_name = self.product_name

        product_id = self.product_id

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        quantity = self.quantity

        shop_name = self.shop_name

        content_type = self.content_type

        content_id = self.content_id

        attribution_type = self.attribution_type

        commission_model = self.commission_model

        commission_tier_setting = self.commission_tier_setting

        standard_commission_rate = self.standard_commission_rate

        commission_bonus_rate = self.commission_bonus_rate

        shop_ads_commission_rate = self.shop_ads_commission_rate

        tap_bonus_commission_rate = self.tap_bonus_commission_rate

        revenue_sharing_portion_rate = self.revenue_sharing_portion_rate

        estimated_commission_base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_commission_base, Unset):
            estimated_commission_base = self.estimated_commission_base.to_dict()

        estimated_standard_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_standard_commission, Unset):
            estimated_standard_commission = self.estimated_standard_commission.to_dict()

        estimated_bonus_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_bonus_commission, Unset):
            estimated_bonus_commission = self.estimated_bonus_commission.to_dict()

        estimated_shop_ads_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_shop_ads_commission, Unset):
            estimated_shop_ads_commission = self.estimated_shop_ads_commission.to_dict()

        estimated_tap_bonus_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_tap_bonus_commission, Unset):
            estimated_tap_bonus_commission = self.estimated_tap_bonus_commission.to_dict()

        estimated_creator_tax_isr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_creator_tax_isr, Unset):
            estimated_creator_tax_isr = self.estimated_creator_tax_isr.to_dict()

        estimated_creator_tax_iva: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_creator_tax_iva, Unset):
            estimated_creator_tax_iva = self.estimated_creator_tax_iva.to_dict()

        estimated_creator_tax_pit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_creator_tax_pit, Unset):
            estimated_creator_tax_pit = self.estimated_creator_tax_pit.to_dict()

        estimated_creator_total_earnings_after_tax: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_creator_total_earnings_after_tax, Unset):
            estimated_creator_total_earnings_after_tax = self.estimated_creator_total_earnings_after_tax.to_dict()

        estimated_total_agency_earnings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_total_agency_earnings, Unset):
            estimated_total_agency_earnings = self.estimated_total_agency_earnings.to_dict()

        estimated_agency_isr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_agency_isr, Unset):
            estimated_agency_isr = self.estimated_agency_isr.to_dict()

        estimated_agency_iva: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_agency_iva, Unset):
            estimated_agency_iva = self.estimated_agency_iva.to_dict()

        actual_commission_base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_commission_base, Unset):
            actual_commission_base = self.actual_commission_base.to_dict()

        actual_standard_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_standard_commission, Unset):
            actual_standard_commission = self.actual_standard_commission.to_dict()

        actual_bonus_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_bonus_commission, Unset):
            actual_bonus_commission = self.actual_bonus_commission.to_dict()

        actual_shop_ads_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_shop_ads_commission, Unset):
            actual_shop_ads_commission = self.actual_shop_ads_commission.to_dict()

        actual_tap_bonus_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_tap_bonus_commission, Unset):
            actual_tap_bonus_commission = self.actual_tap_bonus_commission.to_dict()

        actual_creator_tax_isr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_creator_tax_isr, Unset):
            actual_creator_tax_isr = self.actual_creator_tax_isr.to_dict()

        actual_creator_tax_iva: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_creator_tax_iva, Unset):
            actual_creator_tax_iva = self.actual_creator_tax_iva.to_dict()

        actual_creator_tax_pit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_creator_tax_pit, Unset):
            actual_creator_tax_pit = self.actual_creator_tax_pit.to_dict()

        actual_creator_total_earnings_after_tax: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_creator_total_earnings_after_tax, Unset):
            actual_creator_total_earnings_after_tax = self.actual_creator_total_earnings_after_tax.to_dict()

        actual_total_agency_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_total_agency_commission, Unset):
            actual_total_agency_commission = self.actual_total_agency_commission.to_dict()

        actual_agency_isr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_agency_isr, Unset):
            actual_agency_isr = self.actual_agency_isr.to_dict()

        actual_agency_iva: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_agency_iva, Unset):
            actual_agency_iva = self.actual_agency_iva.to_dict()

        fully_return = self.fully_return

        settlement_time = self.settlement_time

        last_update_time = self.last_update_time

        is_carousel = self.is_carousel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if delivery_time is not UNSET:
            field_dict["delivery_time"] = delivery_time
        if settle_status is not UNSET:
            field_dict["settle_status"] = settle_status
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if open_collaboration_id is not UNSET:
            field_dict["open_collaboration_id"] = open_collaboration_id
        if target_collaboration_id is not UNSET:
            field_dict["target_collaboration_id"] = target_collaboration_id
        if creator_username is not UNSET:
            field_dict["creator_username"] = creator_username
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if price is not UNSET:
            field_dict["price"] = price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if shop_name is not UNSET:
            field_dict["shop_name"] = shop_name
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if content_id is not UNSET:
            field_dict["content_id"] = content_id
        if attribution_type is not UNSET:
            field_dict["attribution_type"] = attribution_type
        if commission_model is not UNSET:
            field_dict["commission_model"] = commission_model
        if commission_tier_setting is not UNSET:
            field_dict["commission_tier_setting"] = commission_tier_setting
        if standard_commission_rate is not UNSET:
            field_dict["standard_commission_rate"] = standard_commission_rate
        if commission_bonus_rate is not UNSET:
            field_dict["commission_bonus_rate"] = commission_bonus_rate
        if shop_ads_commission_rate is not UNSET:
            field_dict["shop_ads_commission_rate"] = shop_ads_commission_rate
        if tap_bonus_commission_rate is not UNSET:
            field_dict["tap_bonus_commission_rate"] = tap_bonus_commission_rate
        if revenue_sharing_portion_rate is not UNSET:
            field_dict["revenue_sharing_portion_rate"] = revenue_sharing_portion_rate
        if estimated_commission_base is not UNSET:
            field_dict["estimated_commission_base"] = estimated_commission_base
        if estimated_standard_commission is not UNSET:
            field_dict["estimated_standard_commission"] = estimated_standard_commission
        if estimated_bonus_commission is not UNSET:
            field_dict["estimated_bonus_commission"] = estimated_bonus_commission
        if estimated_shop_ads_commission is not UNSET:
            field_dict["estimated_shop_ads_commission"] = estimated_shop_ads_commission
        if estimated_tap_bonus_commission is not UNSET:
            field_dict["estimated_tap_bonus_commission"] = estimated_tap_bonus_commission
        if estimated_creator_tax_isr is not UNSET:
            field_dict["estimated_creator_tax_isr"] = estimated_creator_tax_isr
        if estimated_creator_tax_iva is not UNSET:
            field_dict["estimated_creator_tax_iva"] = estimated_creator_tax_iva
        if estimated_creator_tax_pit is not UNSET:
            field_dict["estimated_creator_tax_pit"] = estimated_creator_tax_pit
        if estimated_creator_total_earnings_after_tax is not UNSET:
            field_dict["estimated_creator_total_earnings_after_tax"] = estimated_creator_total_earnings_after_tax
        if estimated_total_agency_earnings is not UNSET:
            field_dict["estimated_total_agency_earnings"] = estimated_total_agency_earnings
        if estimated_agency_isr is not UNSET:
            field_dict["estimated_agency_isr"] = estimated_agency_isr
        if estimated_agency_iva is not UNSET:
            field_dict["estimated_agency_iva"] = estimated_agency_iva
        if actual_commission_base is not UNSET:
            field_dict["actual_commission_base"] = actual_commission_base
        if actual_standard_commission is not UNSET:
            field_dict["actual_standard_commission"] = actual_standard_commission
        if actual_bonus_commission is not UNSET:
            field_dict["actual_bonus_commission"] = actual_bonus_commission
        if actual_shop_ads_commission is not UNSET:
            field_dict["actual_shop_ads_commission"] = actual_shop_ads_commission
        if actual_tap_bonus_commission is not UNSET:
            field_dict["actual_tap_bonus_commission"] = actual_tap_bonus_commission
        if actual_creator_tax_isr is not UNSET:
            field_dict["actual_creator_tax_isr"] = actual_creator_tax_isr
        if actual_creator_tax_iva is not UNSET:
            field_dict["actual_creator_tax_iva"] = actual_creator_tax_iva
        if actual_creator_tax_pit is not UNSET:
            field_dict["actual_creator_tax_pit"] = actual_creator_tax_pit
        if actual_creator_total_earnings_after_tax is not UNSET:
            field_dict["actual_creator_total_earnings_after_tax"] = actual_creator_total_earnings_after_tax
        if actual_total_agency_commission is not UNSET:
            field_dict["actual_total_agency_commission"] = actual_total_agency_commission
        if actual_agency_isr is not UNSET:
            field_dict["actual_agency_isr"] = actual_agency_isr
        if actual_agency_iva is not UNSET:
            field_dict["actual_agency_iva"] = actual_agency_iva
        if fully_return is not UNSET:
            field_dict["fully_return"] = fully_return
        if settlement_time is not UNSET:
            field_dict["settlement_time"] = settlement_time
        if last_update_time is not UNSET:
            field_dict["last_update_time"] = last_update_time
        if is_carousel is not UNSET:
            field_dict["is_carousel"] = is_carousel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.actual_bonus_commission import ActualBonusCommission  # noqa: PLC0415
        from ..models.actual_commission_base import ActualCommissionBase  # noqa: PLC0415
        from ..models.actual_shop_ads_commission import ActualShopAdsCommission  # noqa: PLC0415
        from ..models.actual_standard_commission import ActualStandardCommission  # noqa: PLC0415
        from ..models.estimated_bonus_commission import EstimatedBonusCommission  # noqa: PLC0415
        from ..models.estimated_commission_base import EstimatedCommissionBase  # noqa: PLC0415
        from ..models.estimated_shop_ads_commission import EstimatedShopAdsCommission  # noqa: PLC0415
        from ..models.estimated_standard_commission import EstimatedStandardCommission  # noqa: PLC0415
        from ..models.price import Price  # noqa: PLC0415
        from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_agency_isr import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderActualAgencyIsr,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_agency_iva import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderActualAgencyIva,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_creator_tax_isr import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxIsr,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_creator_tax_iva import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxIva,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_creator_tax_pit import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxPit,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_creator_total_earnings_after_tax import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTotalEarningsAfterTax,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_tap_bonus_commission import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderActualTapBonusCommission,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_actual_total_agency_commission import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderActualTotalAgencyCommission,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_agency_isr import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedAgencyIsr,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_agency_iva import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedAgencyIva,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_creator_tax_isr import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxIsr,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_creator_tax_iva import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxIva,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_creator_tax_pit import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxPit,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_creator_total_earnings_after_tax import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTotalEarningsAfterTax,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_tap_bonus_commission import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedTapBonusCommission,  # noqa: PLC0415
        )
        from ..models.search_cap_affiliate_orders_response_data_sku_order_estimated_total_agency_earning import (
            SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedTotalAgencyEarning,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        tags = d.pop("tags", UNSET)

        create_time = d.pop("create_time", UNSET)

        delivery_time = d.pop("delivery_time", UNSET)

        settle_status = d.pop("settle_status", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        open_collaboration_id = d.pop("open_collaboration_id", UNSET)

        target_collaboration_id = d.pop("target_collaboration_id", UNSET)

        creator_username = d.pop("creator_username", UNSET)

        product_name = d.pop("product_name", UNSET)

        product_id = d.pop("product_id", UNSET)

        _price = d.pop("price", UNSET)
        price: Price | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = Price.from_dict(_price)

        quantity = d.pop("quantity", UNSET)

        shop_name = d.pop("shop_name", UNSET)

        content_type = d.pop("content_type", UNSET)

        content_id = d.pop("content_id", UNSET)

        attribution_type = d.pop("attribution_type", UNSET)

        commission_model = d.pop("commission_model", UNSET)

        commission_tier_setting = d.pop("commission_tier_setting", UNSET)

        standard_commission_rate = d.pop("standard_commission_rate", UNSET)

        commission_bonus_rate = d.pop("commission_bonus_rate", UNSET)

        shop_ads_commission_rate = d.pop("shop_ads_commission_rate", UNSET)

        tap_bonus_commission_rate = d.pop("tap_bonus_commission_rate", UNSET)

        revenue_sharing_portion_rate = d.pop("revenue_sharing_portion_rate", UNSET)

        _estimated_commission_base = d.pop("estimated_commission_base", UNSET)
        estimated_commission_base: EstimatedCommissionBase | Unset
        if isinstance(_estimated_commission_base, Unset):
            estimated_commission_base = UNSET
        else:
            estimated_commission_base = EstimatedCommissionBase.from_dict(_estimated_commission_base)

        _estimated_standard_commission = d.pop("estimated_standard_commission", UNSET)
        estimated_standard_commission: EstimatedStandardCommission | Unset
        if isinstance(_estimated_standard_commission, Unset):
            estimated_standard_commission = UNSET
        else:
            estimated_standard_commission = EstimatedStandardCommission.from_dict(_estimated_standard_commission)

        _estimated_bonus_commission = d.pop("estimated_bonus_commission", UNSET)
        estimated_bonus_commission: EstimatedBonusCommission | Unset
        if isinstance(_estimated_bonus_commission, Unset):
            estimated_bonus_commission = UNSET
        else:
            estimated_bonus_commission = EstimatedBonusCommission.from_dict(_estimated_bonus_commission)

        _estimated_shop_ads_commission = d.pop("estimated_shop_ads_commission", UNSET)
        estimated_shop_ads_commission: EstimatedShopAdsCommission | Unset
        if isinstance(_estimated_shop_ads_commission, Unset):
            estimated_shop_ads_commission = UNSET
        else:
            estimated_shop_ads_commission = EstimatedShopAdsCommission.from_dict(_estimated_shop_ads_commission)

        _estimated_tap_bonus_commission = d.pop("estimated_tap_bonus_commission", UNSET)
        estimated_tap_bonus_commission: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedTapBonusCommission | Unset
        if isinstance(_estimated_tap_bonus_commission, Unset):
            estimated_tap_bonus_commission = UNSET
        else:
            estimated_tap_bonus_commission = (
                SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedTapBonusCommission.from_dict(
                    _estimated_tap_bonus_commission
                )
            )

        _estimated_creator_tax_isr = d.pop("estimated_creator_tax_isr", UNSET)
        estimated_creator_tax_isr: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxIsr | Unset
        if isinstance(_estimated_creator_tax_isr, Unset):
            estimated_creator_tax_isr = UNSET
        else:
            estimated_creator_tax_isr = SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxIsr.from_dict(
                _estimated_creator_tax_isr
            )

        _estimated_creator_tax_iva = d.pop("estimated_creator_tax_iva", UNSET)
        estimated_creator_tax_iva: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxIva | Unset
        if isinstance(_estimated_creator_tax_iva, Unset):
            estimated_creator_tax_iva = UNSET
        else:
            estimated_creator_tax_iva = SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxIva.from_dict(
                _estimated_creator_tax_iva
            )

        _estimated_creator_tax_pit = d.pop("estimated_creator_tax_pit", UNSET)
        estimated_creator_tax_pit: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxPit | Unset
        if isinstance(_estimated_creator_tax_pit, Unset):
            estimated_creator_tax_pit = UNSET
        else:
            estimated_creator_tax_pit = SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTaxPit.from_dict(
                _estimated_creator_tax_pit
            )

        _estimated_creator_total_earnings_after_tax = d.pop("estimated_creator_total_earnings_after_tax", UNSET)
        estimated_creator_total_earnings_after_tax: (
            SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTotalEarningsAfterTax | Unset
        )
        if isinstance(_estimated_creator_total_earnings_after_tax, Unset):
            estimated_creator_total_earnings_after_tax = UNSET
        else:
            estimated_creator_total_earnings_after_tax = (
                SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTotalEarningsAfterTax.from_dict(
                    _estimated_creator_total_earnings_after_tax
                )
            )

        _estimated_total_agency_earnings = d.pop("estimated_total_agency_earnings", UNSET)
        estimated_total_agency_earnings: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedTotalAgencyEarning | Unset
        if isinstance(_estimated_total_agency_earnings, Unset):
            estimated_total_agency_earnings = UNSET
        else:
            estimated_total_agency_earnings = (
                SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedTotalAgencyEarning.from_dict(
                    _estimated_total_agency_earnings
                )
            )

        _estimated_agency_isr = d.pop("estimated_agency_isr", UNSET)
        estimated_agency_isr: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedAgencyIsr | Unset
        if isinstance(_estimated_agency_isr, Unset):
            estimated_agency_isr = UNSET
        else:
            estimated_agency_isr = SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedAgencyIsr.from_dict(
                _estimated_agency_isr
            )

        _estimated_agency_iva = d.pop("estimated_agency_iva", UNSET)
        estimated_agency_iva: SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedAgencyIva | Unset
        if isinstance(_estimated_agency_iva, Unset):
            estimated_agency_iva = UNSET
        else:
            estimated_agency_iva = SearchCAPAffiliateOrdersResponseDataSkuOrderEstimatedAgencyIva.from_dict(
                _estimated_agency_iva
            )

        _actual_commission_base = d.pop("actual_commission_base", UNSET)
        actual_commission_base: ActualCommissionBase | Unset
        if isinstance(_actual_commission_base, Unset):
            actual_commission_base = UNSET
        else:
            actual_commission_base = ActualCommissionBase.from_dict(_actual_commission_base)

        _actual_standard_commission = d.pop("actual_standard_commission", UNSET)
        actual_standard_commission: ActualStandardCommission | Unset
        if isinstance(_actual_standard_commission, Unset):
            actual_standard_commission = UNSET
        else:
            actual_standard_commission = ActualStandardCommission.from_dict(_actual_standard_commission)

        _actual_bonus_commission = d.pop("actual_bonus_commission", UNSET)
        actual_bonus_commission: ActualBonusCommission | Unset
        if isinstance(_actual_bonus_commission, Unset):
            actual_bonus_commission = UNSET
        else:
            actual_bonus_commission = ActualBonusCommission.from_dict(_actual_bonus_commission)

        _actual_shop_ads_commission = d.pop("actual_shop_ads_commission", UNSET)
        actual_shop_ads_commission: ActualShopAdsCommission | Unset
        if isinstance(_actual_shop_ads_commission, Unset):
            actual_shop_ads_commission = UNSET
        else:
            actual_shop_ads_commission = ActualShopAdsCommission.from_dict(_actual_shop_ads_commission)

        _actual_tap_bonus_commission = d.pop("actual_tap_bonus_commission", UNSET)
        actual_tap_bonus_commission: SearchCAPAffiliateOrdersResponseDataSkuOrderActualTapBonusCommission | Unset
        if isinstance(_actual_tap_bonus_commission, Unset):
            actual_tap_bonus_commission = UNSET
        else:
            actual_tap_bonus_commission = (
                SearchCAPAffiliateOrdersResponseDataSkuOrderActualTapBonusCommission.from_dict(
                    _actual_tap_bonus_commission
                )
            )

        _actual_creator_tax_isr = d.pop("actual_creator_tax_isr", UNSET)
        actual_creator_tax_isr: SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxIsr | Unset
        if isinstance(_actual_creator_tax_isr, Unset):
            actual_creator_tax_isr = UNSET
        else:
            actual_creator_tax_isr = SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxIsr.from_dict(
                _actual_creator_tax_isr
            )

        _actual_creator_tax_iva = d.pop("actual_creator_tax_iva", UNSET)
        actual_creator_tax_iva: SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxIva | Unset
        if isinstance(_actual_creator_tax_iva, Unset):
            actual_creator_tax_iva = UNSET
        else:
            actual_creator_tax_iva = SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxIva.from_dict(
                _actual_creator_tax_iva
            )

        _actual_creator_tax_pit = d.pop("actual_creator_tax_pit", UNSET)
        actual_creator_tax_pit: SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxPit | Unset
        if isinstance(_actual_creator_tax_pit, Unset):
            actual_creator_tax_pit = UNSET
        else:
            actual_creator_tax_pit = SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTaxPit.from_dict(
                _actual_creator_tax_pit
            )

        _actual_creator_total_earnings_after_tax = d.pop("actual_creator_total_earnings_after_tax", UNSET)
        actual_creator_total_earnings_after_tax: (
            SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTotalEarningsAfterTax | Unset
        )
        if isinstance(_actual_creator_total_earnings_after_tax, Unset):
            actual_creator_total_earnings_after_tax = UNSET
        else:
            actual_creator_total_earnings_after_tax = (
                SearchCAPAffiliateOrdersResponseDataSkuOrderActualCreatorTotalEarningsAfterTax.from_dict(
                    _actual_creator_total_earnings_after_tax
                )
            )

        _actual_total_agency_commission = d.pop("actual_total_agency_commission", UNSET)
        actual_total_agency_commission: SearchCAPAffiliateOrdersResponseDataSkuOrderActualTotalAgencyCommission | Unset
        if isinstance(_actual_total_agency_commission, Unset):
            actual_total_agency_commission = UNSET
        else:
            actual_total_agency_commission = (
                SearchCAPAffiliateOrdersResponseDataSkuOrderActualTotalAgencyCommission.from_dict(
                    _actual_total_agency_commission
                )
            )

        _actual_agency_isr = d.pop("actual_agency_isr", UNSET)
        actual_agency_isr: SearchCAPAffiliateOrdersResponseDataSkuOrderActualAgencyIsr | Unset
        if isinstance(_actual_agency_isr, Unset):
            actual_agency_isr = UNSET
        else:
            actual_agency_isr = SearchCAPAffiliateOrdersResponseDataSkuOrderActualAgencyIsr.from_dict(
                _actual_agency_isr
            )

        _actual_agency_iva = d.pop("actual_agency_iva", UNSET)
        actual_agency_iva: SearchCAPAffiliateOrdersResponseDataSkuOrderActualAgencyIva | Unset
        if isinstance(_actual_agency_iva, Unset):
            actual_agency_iva = UNSET
        else:
            actual_agency_iva = SearchCAPAffiliateOrdersResponseDataSkuOrderActualAgencyIva.from_dict(
                _actual_agency_iva
            )

        fully_return = d.pop("fully_return", UNSET)

        settlement_time = d.pop("settlement_time", UNSET)

        last_update_time = d.pop("last_update_time", UNSET)

        is_carousel = d.pop("is_carousel", UNSET)

        search_cap_affiliate_orders_response_data_sku_order = cls(
            id=id,
            tags=tags,
            create_time=create_time,
            delivery_time=delivery_time,
            settle_status=settle_status,
            sku_id=sku_id,
            open_collaboration_id=open_collaboration_id,
            target_collaboration_id=target_collaboration_id,
            creator_username=creator_username,
            product_name=product_name,
            product_id=product_id,
            price=price,
            quantity=quantity,
            shop_name=shop_name,
            content_type=content_type,
            content_id=content_id,
            attribution_type=attribution_type,
            commission_model=commission_model,
            commission_tier_setting=commission_tier_setting,
            standard_commission_rate=standard_commission_rate,
            commission_bonus_rate=commission_bonus_rate,
            shop_ads_commission_rate=shop_ads_commission_rate,
            tap_bonus_commission_rate=tap_bonus_commission_rate,
            revenue_sharing_portion_rate=revenue_sharing_portion_rate,
            estimated_commission_base=estimated_commission_base,
            estimated_standard_commission=estimated_standard_commission,
            estimated_bonus_commission=estimated_bonus_commission,
            estimated_shop_ads_commission=estimated_shop_ads_commission,
            estimated_tap_bonus_commission=estimated_tap_bonus_commission,
            estimated_creator_tax_isr=estimated_creator_tax_isr,
            estimated_creator_tax_iva=estimated_creator_tax_iva,
            estimated_creator_tax_pit=estimated_creator_tax_pit,
            estimated_creator_total_earnings_after_tax=estimated_creator_total_earnings_after_tax,
            estimated_total_agency_earnings=estimated_total_agency_earnings,
            estimated_agency_isr=estimated_agency_isr,
            estimated_agency_iva=estimated_agency_iva,
            actual_commission_base=actual_commission_base,
            actual_standard_commission=actual_standard_commission,
            actual_bonus_commission=actual_bonus_commission,
            actual_shop_ads_commission=actual_shop_ads_commission,
            actual_tap_bonus_commission=actual_tap_bonus_commission,
            actual_creator_tax_isr=actual_creator_tax_isr,
            actual_creator_tax_iva=actual_creator_tax_iva,
            actual_creator_tax_pit=actual_creator_tax_pit,
            actual_creator_total_earnings_after_tax=actual_creator_total_earnings_after_tax,
            actual_total_agency_commission=actual_total_agency_commission,
            actual_agency_isr=actual_agency_isr,
            actual_agency_iva=actual_agency_iva,
            fully_return=fully_return,
            settlement_time=settlement_time,
            last_update_time=last_update_time,
            is_carousel=is_carousel,
        )

        search_cap_affiliate_orders_response_data_sku_order.additional_properties = d
        return search_cap_affiliate_orders_response_data_sku_order

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
