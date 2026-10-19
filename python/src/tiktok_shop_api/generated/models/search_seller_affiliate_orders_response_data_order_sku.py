from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_seller_affiliate_orders_response_data_order_sku_content_type import (
    SearchSellerAffiliateOrdersResponseDataOrderSkuContentType,
)
from ..models.search_seller_affiliate_orders_response_data_order_sku_fully_return import (
    SearchSellerAffiliateOrdersResponseDataOrderSkuFullyReturn,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actual_commission_base import ActualCommissionBase
    from ..models.estimated_commission_base import EstimatedCommissionBase
    from ..models.price import Price
    from ..models.search_seller_affiliate_orders_response_data_order_sku_actual_cofunded_creator_bonus_amount import (
        SearchSellerAffiliateOrdersResponseDataOrderSkuActualCofundedCreatorBonusAmount,
    )
    from ..models.search_seller_affiliate_orders_response_data_order_sku_actual_paid_commission import (
        SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidCommission,
    )
    from ..models.search_seller_affiliate_orders_response_data_order_sku_actual_paid_partner_commission import (
        SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidPartnerCommission,
    )
    from ..models.search_seller_affiliate_orders_response_data_order_sku_actual_paid_shop_ads_commission import (
        SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidShopAdsCommission,
    )
    from ..models.search_seller_affiliate_orders_response_data_order_sku_estimated_cofunded_creator_bonus_amount import (
        SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedCofundedCreatorBonusAmount,
    )
    from ..models.search_seller_affiliate_orders_response_data_order_sku_estimated_paid_commission import (
        SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidCommission,
    )
    from ..models.search_seller_affiliate_orders_response_data_order_sku_estimated_paid_partner_commission import (
        SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidPartnerCommission,
    )
    from ..models.search_seller_affiliate_orders_response_data_order_sku_estimated_paid_shop_ads_commission import (
        SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidShopAdsCommission,
    )


T = TypeVar("T", bound="SearchSellerAffiliateOrdersResponseDataOrderSku")


@_attrs_define
class SearchSellerAffiliateOrdersResponseDataOrderSku:
    """
    Attributes:
        sku_id (str | Unset): The ID of your SKU
        settlement_status (str | Unset): The current settlement status of the sku order. Possible options are:
            - Unknown: The status of the order is undefined. It might be updated later.
            - AWAITING PAYMENT：The order hasn't been paid by customer yet, only estimated commission is available
            - To-SETTLE：The order is waiting for settlement, only estimated commission is available
            - SETTLED: The commission of the order is already settled.
            - INELIGIBLE: The order has been returned/refunded/canceled by the buyer, and no commission will be settled.
        open_collaboration_id (str | Unset): The ID of the open collaboration in which the product is enrolled.
        target_collaboration_id (str | Unset): The ID of the target collaboration in which the product is enrolled.
        campaign_id (str | Unset): The ID of the TAP campaign in which the product is enrolled.
        creator_username (str | Unset): The username of the creator attributed to the SKU order. This field is returned
            as an empty string for affiliate partner campaign orders.
        price (Price | Unset):
        quantity (int | Unset): The number of units of the SKU in the order, including units that were later refunded.
        content_type (SearchSellerAffiliateOrdersResponseDataOrderSkuContentType | Unset): The content format of the
            creator content through which the order was created.
            Possible values:
            - SHOP
            - VIDEO
            - LIVE
            - PRE_LIVE
            - PROMOTION_PAGE
            - LINKSHARE
        content_id (str | Unset): The content identifier.
        product_id (str | Unset): The product  ID in TikTok Shop.
        commission_model (str | Unset): The commission model selected for the SKU order.
            Possible values:
            - `Fixed commission`: The fixed commission model is selected.
            - `Tiered commission`: The tiered commission model is selected; see `commission_tier_setting` for any available
            tier settings.
        commission_tier_setting (str | Unset): For `Tiered commission`, the creator commission rates configured by the
            seller, expressed as percentages in ascending threshold order and separated by ` OR `. Returns `-` when tiered
            commission does not apply or no tier is configured.
        commission_rate (str | Unset): The commission rate established by the seller for creators involved in the
            collaboration, expressed in hundredths of a percent. For example, 1550 represents a commission rate of 15.50%.
            This value is returned only when the order is generated directly by the seller's creator. For affiliate partner
            campaign orders, see `partner_commission_rate`.
        partner_commission_rate (str | Unset): The commission rate established by the seller to be paid to affiliate
            partner involved in the collaboration, expressed in hundredths of a percent. For example, 1550 represents a
            commission rate of 15.50%.
        shop_ads_commission_rate (str | Unset): The commission rate for orders generated through Shop Ads, expressed in
            hundredths of a percent. For example, 5000 represents 50.00%.
        estimated_commission_base (EstimatedCommissionBase | Unset):
        estimated_paid_shop_ads_commission
            (SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidShopAdsCommission | Unset):
        estimated_paid_commission (SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidCommission | Unset):
        estimated_paid_partner_commission (SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidPartnerCommission
            | Unset):
        actual_commission_base (ActualCommissionBase | Unset):
        actual_paid_commission (SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidCommission | Unset):
        actual_paid_partner_commission (SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidPartnerCommission |
            Unset):
        actual_paid_shop_ads_commission (SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidShopAdsCommission |
            Unset):
        estimated_cofunded_creator_bonus_amount
            (SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedCofundedCreatorBonusAmount | Unset):
        actual_cofunded_creator_bonus_amount
            (SearchSellerAffiliateOrdersResponseDataOrderSkuActualCofundedCreatorBonusAmount | Unset):
        refunded_quantity (int | Unset): Deprecated. This field is not returned. Use `fully_return` to determine whether
            the SKU order was fully returned or refunded.
        returned_quantity (int | Unset): Deprecated. This field is not returned. Use `fully_return` to determine whether
            the SKU order was fully returned or refunded.
        fully_return (SearchSellerAffiliateOrdersResponseDataOrderSkuFullyReturn | Unset): Indicates whether the entire
            SKU order was returned or refunded. Possible values:
            - `Yes`: The full quantity was returned or refunded, so no commission is paid.
            - `No`: The full quantity was not returned or refunded.
        is_carousel (bool | Unset): Indicates whether the SKU order is attributed to carousel content. Carousel content
            may involve a commission rate discount. Returns `true` for a carousel-attributed SKU order and `false`
            otherwise.
    """

    sku_id: str | Unset = UNSET
    settlement_status: str | Unset = UNSET
    open_collaboration_id: str | Unset = UNSET
    target_collaboration_id: str | Unset = UNSET
    campaign_id: str | Unset = UNSET
    creator_username: str | Unset = UNSET
    price: Price | Unset = UNSET
    quantity: int | Unset = UNSET
    content_type: SearchSellerAffiliateOrdersResponseDataOrderSkuContentType | Unset = UNSET
    content_id: str | Unset = UNSET
    product_id: str | Unset = UNSET
    commission_model: str | Unset = UNSET
    commission_tier_setting: str | Unset = UNSET
    commission_rate: str | Unset = UNSET
    partner_commission_rate: str | Unset = UNSET
    shop_ads_commission_rate: str | Unset = UNSET
    estimated_commission_base: EstimatedCommissionBase | Unset = UNSET
    estimated_paid_shop_ads_commission: (
        SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidShopAdsCommission | Unset
    ) = UNSET
    estimated_paid_commission: SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidCommission | Unset = UNSET
    estimated_paid_partner_commission: (
        SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidPartnerCommission | Unset
    ) = UNSET
    actual_commission_base: ActualCommissionBase | Unset = UNSET
    actual_paid_commission: SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidCommission | Unset = UNSET
    actual_paid_partner_commission: (
        SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidPartnerCommission | Unset
    ) = UNSET
    actual_paid_shop_ads_commission: (
        SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidShopAdsCommission | Unset
    ) = UNSET
    estimated_cofunded_creator_bonus_amount: (
        SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedCofundedCreatorBonusAmount | Unset
    ) = UNSET
    actual_cofunded_creator_bonus_amount: (
        SearchSellerAffiliateOrdersResponseDataOrderSkuActualCofundedCreatorBonusAmount | Unset
    ) = UNSET
    refunded_quantity: int | Unset = UNSET
    returned_quantity: int | Unset = UNSET
    fully_return: SearchSellerAffiliateOrdersResponseDataOrderSkuFullyReturn | Unset = UNSET
    is_carousel: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sku_id = self.sku_id

        settlement_status = self.settlement_status

        open_collaboration_id = self.open_collaboration_id

        target_collaboration_id = self.target_collaboration_id

        campaign_id = self.campaign_id

        creator_username = self.creator_username

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        quantity = self.quantity

        content_type: str | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value

        content_id = self.content_id

        product_id = self.product_id

        commission_model = self.commission_model

        commission_tier_setting = self.commission_tier_setting

        commission_rate = self.commission_rate

        partner_commission_rate = self.partner_commission_rate

        shop_ads_commission_rate = self.shop_ads_commission_rate

        estimated_commission_base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_commission_base, Unset):
            estimated_commission_base = self.estimated_commission_base.to_dict()

        estimated_paid_shop_ads_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_paid_shop_ads_commission, Unset):
            estimated_paid_shop_ads_commission = self.estimated_paid_shop_ads_commission.to_dict()

        estimated_paid_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_paid_commission, Unset):
            estimated_paid_commission = self.estimated_paid_commission.to_dict()

        estimated_paid_partner_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_paid_partner_commission, Unset):
            estimated_paid_partner_commission = self.estimated_paid_partner_commission.to_dict()

        actual_commission_base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_commission_base, Unset):
            actual_commission_base = self.actual_commission_base.to_dict()

        actual_paid_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_paid_commission, Unset):
            actual_paid_commission = self.actual_paid_commission.to_dict()

        actual_paid_partner_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_paid_partner_commission, Unset):
            actual_paid_partner_commission = self.actual_paid_partner_commission.to_dict()

        actual_paid_shop_ads_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_paid_shop_ads_commission, Unset):
            actual_paid_shop_ads_commission = self.actual_paid_shop_ads_commission.to_dict()

        estimated_cofunded_creator_bonus_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_cofunded_creator_bonus_amount, Unset):
            estimated_cofunded_creator_bonus_amount = self.estimated_cofunded_creator_bonus_amount.to_dict()

        actual_cofunded_creator_bonus_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_cofunded_creator_bonus_amount, Unset):
            actual_cofunded_creator_bonus_amount = self.actual_cofunded_creator_bonus_amount.to_dict()

        refunded_quantity = self.refunded_quantity

        returned_quantity = self.returned_quantity

        fully_return: str | Unset = UNSET
        if not isinstance(self.fully_return, Unset):
            fully_return = self.fully_return.value

        is_carousel = self.is_carousel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if settlement_status is not UNSET:
            field_dict["settlement_status"] = settlement_status
        if open_collaboration_id is not UNSET:
            field_dict["open_collaboration_id"] = open_collaboration_id
        if target_collaboration_id is not UNSET:
            field_dict["target_collaboration_id"] = target_collaboration_id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if creator_username is not UNSET:
            field_dict["creator_username"] = creator_username
        if price is not UNSET:
            field_dict["price"] = price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if content_id is not UNSET:
            field_dict["content_id"] = content_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if commission_model is not UNSET:
            field_dict["commission_model"] = commission_model
        if commission_tier_setting is not UNSET:
            field_dict["commission_tier_setting"] = commission_tier_setting
        if commission_rate is not UNSET:
            field_dict["commission_rate"] = commission_rate
        if partner_commission_rate is not UNSET:
            field_dict["partner_commission_rate"] = partner_commission_rate
        if shop_ads_commission_rate is not UNSET:
            field_dict["shop_ads_commission_rate"] = shop_ads_commission_rate
        if estimated_commission_base is not UNSET:
            field_dict["estimated_commission_base"] = estimated_commission_base
        if estimated_paid_shop_ads_commission is not UNSET:
            field_dict["estimated_paid_shop_ads_commission"] = estimated_paid_shop_ads_commission
        if estimated_paid_commission is not UNSET:
            field_dict["estimated_paid_commission"] = estimated_paid_commission
        if estimated_paid_partner_commission is not UNSET:
            field_dict["estimated_paid_partner_commission"] = estimated_paid_partner_commission
        if actual_commission_base is not UNSET:
            field_dict["actual_commission_base"] = actual_commission_base
        if actual_paid_commission is not UNSET:
            field_dict["actual_paid_commission"] = actual_paid_commission
        if actual_paid_partner_commission is not UNSET:
            field_dict["actual_paid_partner_commission"] = actual_paid_partner_commission
        if actual_paid_shop_ads_commission is not UNSET:
            field_dict["actual_paid_shop_ads_commission"] = actual_paid_shop_ads_commission
        if estimated_cofunded_creator_bonus_amount is not UNSET:
            field_dict["estimated_cofunded_creator_bonus_amount"] = estimated_cofunded_creator_bonus_amount
        if actual_cofunded_creator_bonus_amount is not UNSET:
            field_dict["actual_cofunded_creator_bonus_amount"] = actual_cofunded_creator_bonus_amount
        if refunded_quantity is not UNSET:
            field_dict["refunded_quantity"] = refunded_quantity
        if returned_quantity is not UNSET:
            field_dict["returned_quantity"] = returned_quantity
        if fully_return is not UNSET:
            field_dict["fully_return"] = fully_return
        if is_carousel is not UNSET:
            field_dict["is_carousel"] = is_carousel

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.actual_commission_base import ActualCommissionBase  # noqa: PLC0415
        from ..models.estimated_commission_base import EstimatedCommissionBase  # noqa: PLC0415
        from ..models.price import Price  # noqa: PLC0415
        from ..models.search_seller_affiliate_orders_response_data_order_sku_actual_cofunded_creator_bonus_amount import (
            SearchSellerAffiliateOrdersResponseDataOrderSkuActualCofundedCreatorBonusAmount,  # noqa: PLC0415
        )
        from ..models.search_seller_affiliate_orders_response_data_order_sku_actual_paid_commission import (
            SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidCommission,  # noqa: PLC0415
        )
        from ..models.search_seller_affiliate_orders_response_data_order_sku_actual_paid_partner_commission import (
            SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidPartnerCommission,  # noqa: PLC0415
        )
        from ..models.search_seller_affiliate_orders_response_data_order_sku_actual_paid_shop_ads_commission import (
            SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidShopAdsCommission,  # noqa: PLC0415
        )
        from ..models.search_seller_affiliate_orders_response_data_order_sku_estimated_cofunded_creator_bonus_amount import (
            SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedCofundedCreatorBonusAmount,  # noqa: PLC0415
        )
        from ..models.search_seller_affiliate_orders_response_data_order_sku_estimated_paid_commission import (
            SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidCommission,  # noqa: PLC0415
        )
        from ..models.search_seller_affiliate_orders_response_data_order_sku_estimated_paid_partner_commission import (
            SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidPartnerCommission,  # noqa: PLC0415
        )
        from ..models.search_seller_affiliate_orders_response_data_order_sku_estimated_paid_shop_ads_commission import (
            SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidShopAdsCommission,  # noqa: PLC0415
        )

        d = dict(src_dict)
        sku_id = d.pop("sku_id", UNSET)

        settlement_status = d.pop("settlement_status", UNSET)

        open_collaboration_id = d.pop("open_collaboration_id", UNSET)

        target_collaboration_id = d.pop("target_collaboration_id", UNSET)

        campaign_id = d.pop("campaign_id", UNSET)

        creator_username = d.pop("creator_username", UNSET)

        _price = d.pop("price", UNSET)
        price: Price | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = Price.from_dict(_price)

        quantity = d.pop("quantity", UNSET)

        _content_type = d.pop("content_type", UNSET)
        content_type: SearchSellerAffiliateOrdersResponseDataOrderSkuContentType | Unset
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = SearchSellerAffiliateOrdersResponseDataOrderSkuContentType(_content_type)

        content_id = d.pop("content_id", UNSET)

        product_id = d.pop("product_id", UNSET)

        commission_model = d.pop("commission_model", UNSET)

        commission_tier_setting = d.pop("commission_tier_setting", UNSET)

        commission_rate = d.pop("commission_rate", UNSET)

        partner_commission_rate = d.pop("partner_commission_rate", UNSET)

        shop_ads_commission_rate = d.pop("shop_ads_commission_rate", UNSET)

        _estimated_commission_base = d.pop("estimated_commission_base", UNSET)
        estimated_commission_base: EstimatedCommissionBase | Unset
        if isinstance(_estimated_commission_base, Unset):
            estimated_commission_base = UNSET
        else:
            estimated_commission_base = EstimatedCommissionBase.from_dict(_estimated_commission_base)

        _estimated_paid_shop_ads_commission = d.pop("estimated_paid_shop_ads_commission", UNSET)
        estimated_paid_shop_ads_commission: (
            SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidShopAdsCommission | Unset
        )
        if isinstance(_estimated_paid_shop_ads_commission, Unset):
            estimated_paid_shop_ads_commission = UNSET
        else:
            estimated_paid_shop_ads_commission = (
                SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidShopAdsCommission.from_dict(
                    _estimated_paid_shop_ads_commission
                )
            )

        _estimated_paid_commission = d.pop("estimated_paid_commission", UNSET)
        estimated_paid_commission: SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidCommission | Unset
        if isinstance(_estimated_paid_commission, Unset):
            estimated_paid_commission = UNSET
        else:
            estimated_paid_commission = (
                SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidCommission.from_dict(
                    _estimated_paid_commission
                )
            )

        _estimated_paid_partner_commission = d.pop("estimated_paid_partner_commission", UNSET)
        estimated_paid_partner_commission: (
            SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidPartnerCommission | Unset
        )
        if isinstance(_estimated_paid_partner_commission, Unset):
            estimated_paid_partner_commission = UNSET
        else:
            estimated_paid_partner_commission = (
                SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedPaidPartnerCommission.from_dict(
                    _estimated_paid_partner_commission
                )
            )

        _actual_commission_base = d.pop("actual_commission_base", UNSET)
        actual_commission_base: ActualCommissionBase | Unset
        if isinstance(_actual_commission_base, Unset):
            actual_commission_base = UNSET
        else:
            actual_commission_base = ActualCommissionBase.from_dict(_actual_commission_base)

        _actual_paid_commission = d.pop("actual_paid_commission", UNSET)
        actual_paid_commission: SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidCommission | Unset
        if isinstance(_actual_paid_commission, Unset):
            actual_paid_commission = UNSET
        else:
            actual_paid_commission = SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidCommission.from_dict(
                _actual_paid_commission
            )

        _actual_paid_partner_commission = d.pop("actual_paid_partner_commission", UNSET)
        actual_paid_partner_commission: (
            SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidPartnerCommission | Unset
        )
        if isinstance(_actual_paid_partner_commission, Unset):
            actual_paid_partner_commission = UNSET
        else:
            actual_paid_partner_commission = (
                SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidPartnerCommission.from_dict(
                    _actual_paid_partner_commission
                )
            )

        _actual_paid_shop_ads_commission = d.pop("actual_paid_shop_ads_commission", UNSET)
        actual_paid_shop_ads_commission: (
            SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidShopAdsCommission | Unset
        )
        if isinstance(_actual_paid_shop_ads_commission, Unset):
            actual_paid_shop_ads_commission = UNSET
        else:
            actual_paid_shop_ads_commission = (
                SearchSellerAffiliateOrdersResponseDataOrderSkuActualPaidShopAdsCommission.from_dict(
                    _actual_paid_shop_ads_commission
                )
            )

        _estimated_cofunded_creator_bonus_amount = d.pop("estimated_cofunded_creator_bonus_amount", UNSET)
        estimated_cofunded_creator_bonus_amount: (
            SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedCofundedCreatorBonusAmount | Unset
        )
        if isinstance(_estimated_cofunded_creator_bonus_amount, Unset):
            estimated_cofunded_creator_bonus_amount = UNSET
        else:
            estimated_cofunded_creator_bonus_amount = (
                SearchSellerAffiliateOrdersResponseDataOrderSkuEstimatedCofundedCreatorBonusAmount.from_dict(
                    _estimated_cofunded_creator_bonus_amount
                )
            )

        _actual_cofunded_creator_bonus_amount = d.pop("actual_cofunded_creator_bonus_amount", UNSET)
        actual_cofunded_creator_bonus_amount: (
            SearchSellerAffiliateOrdersResponseDataOrderSkuActualCofundedCreatorBonusAmount | Unset
        )
        if isinstance(_actual_cofunded_creator_bonus_amount, Unset):
            actual_cofunded_creator_bonus_amount = UNSET
        else:
            actual_cofunded_creator_bonus_amount = (
                SearchSellerAffiliateOrdersResponseDataOrderSkuActualCofundedCreatorBonusAmount.from_dict(
                    _actual_cofunded_creator_bonus_amount
                )
            )

        refunded_quantity = d.pop("refunded_quantity", UNSET)

        returned_quantity = d.pop("returned_quantity", UNSET)

        _fully_return = d.pop("fully_return", UNSET)
        fully_return: SearchSellerAffiliateOrdersResponseDataOrderSkuFullyReturn | Unset
        if isinstance(_fully_return, Unset):
            fully_return = UNSET
        else:
            fully_return = SearchSellerAffiliateOrdersResponseDataOrderSkuFullyReturn(_fully_return)

        is_carousel = d.pop("is_carousel", UNSET)

        search_seller_affiliate_orders_response_data_order_sku = cls(
            sku_id=sku_id,
            settlement_status=settlement_status,
            open_collaboration_id=open_collaboration_id,
            target_collaboration_id=target_collaboration_id,
            campaign_id=campaign_id,
            creator_username=creator_username,
            price=price,
            quantity=quantity,
            content_type=content_type,
            content_id=content_id,
            product_id=product_id,
            commission_model=commission_model,
            commission_tier_setting=commission_tier_setting,
            commission_rate=commission_rate,
            partner_commission_rate=partner_commission_rate,
            shop_ads_commission_rate=shop_ads_commission_rate,
            estimated_commission_base=estimated_commission_base,
            estimated_paid_shop_ads_commission=estimated_paid_shop_ads_commission,
            estimated_paid_commission=estimated_paid_commission,
            estimated_paid_partner_commission=estimated_paid_partner_commission,
            actual_commission_base=actual_commission_base,
            actual_paid_commission=actual_paid_commission,
            actual_paid_partner_commission=actual_paid_partner_commission,
            actual_paid_shop_ads_commission=actual_paid_shop_ads_commission,
            estimated_cofunded_creator_bonus_amount=estimated_cofunded_creator_bonus_amount,
            actual_cofunded_creator_bonus_amount=actual_cofunded_creator_bonus_amount,
            refunded_quantity=refunded_quantity,
            returned_quantity=returned_quantity,
            fully_return=fully_return,
            is_carousel=is_carousel,
        )

        search_seller_affiliate_orders_response_data_order_sku.additional_properties = d
        return search_seller_affiliate_orders_response_data_order_sku

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
