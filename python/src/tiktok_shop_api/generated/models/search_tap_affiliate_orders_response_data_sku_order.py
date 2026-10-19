from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_tap_affiliate_orders_response_data_sku_order_content_type import (
    SearchTAPAffiliateOrdersResponseDataSkuOrderContentType,
)
from ..models.search_tap_affiliate_orders_response_data_sku_order_fully_return import (
    SearchTAPAffiliateOrdersResponseDataSkuOrderFullyReturn,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actual_commission_base import ActualCommissionBase
    from ..models.estimated_commission_base import EstimatedCommissionBase
    from ..models.price import Price
    from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_creator_shop_ads_commission import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorShopAdsCommission,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_creator_standard_commission import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorStandardCommission,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_creator_tap_bonus_commission import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorTapBonusCommission,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_partner_isr import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIsr,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_partner_iva import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIva,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_partner_shop_ads_commission import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerShopAdsCommission,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_partner_standard_commission import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerStandardCommission,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_partner_tap_bonus_commission import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerTapBonusCommission,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_creator_shop_ads_commission import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorShopAdsCommission,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_creator_standard_commission import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorStandardCommission,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_creator_tap_bonus_commission import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTapBonusCommission,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_partner_isr import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerIsr,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_partner_iva import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerIva,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_partner_shop_ads_commission import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerShopAdsCommission,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_partner_standard_commission import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerStandardCommission,
    )
    from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_partner_tap_bonus_commission import (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerTapBonusCommission,
    )


T = TypeVar("T", bound="SearchTAPAffiliateOrdersResponseDataSkuOrder")


@_attrs_define
class SearchTAPAffiliateOrdersResponseDataSkuOrder:
    """
    Attributes:
        id (str | Unset): Transaction main order ID
        create_time (int | Unset): The order creation time as a Unix timestamp in seconds (UTC).
        delivery_time (int | Unset): The order delivery time as a Unix timestamp in seconds (UTC).
        settle_status (str | Unset): Settlement Status of the order.
            Possible values:
            1. "CUSTOMER UNPAID",  customer hasn't paid for the orders.
            2. "PENDING", customers can still return or get a refund for this order. The earnings shown are estimates and
            waiting for settlement.
            3. "SETTLED", your earnings have already settled to your account
            4. "INELIGIBLE", The order has been returned/refunded/canceled by the buyer, and no commission will be settled.
            5. "FROZEN", Possible fraud has been detected regarding the order. The commission will be unfrozen after the
            fraud is resolved.
        sku_id (str | Unset): sku ID
        campaign_id (str | Unset): The identifier of the TAP campaign associated with the order.
        creator_username (str | Unset): Creator username
        product_name (str | Unset): The product name.
        product_id (str | Unset): Unique identifier for Product
        price (Price | Unset):
        quantity (int | Unset): Number of SKU items in the order, including refunded items.
        content_type (SearchTAPAffiliateOrdersResponseDataSkuOrderContentType | Unset): The content format of the
            creator content through which the order was created.
            Possible values:
            - SHOP
            - VIDEO
            - LIVE
            - PRE_LIVE
            - PROMOTION_PAGE
            - LINKSHARE
        content_id (str | Unset): Unique identifier for content
        creator_standard_commission_rate (int | Unset): The creator standard commission rate, scaled by 10,000. For
            example, `3000` represents 30%.
        partner_standard_commission_rate (int | Unset): The affiliate partner's standard commission rate, scaled by
            10,000. For example, `4000` represents 40%.
        creator_shop_ads_commission_rate (int | Unset): The creator Shop Ads commission rate, scaled by 10,000. For
            example, `3000` represents 30%.
        partner_shop_ads_commission_rate (int | Unset): The affiliate partner's Shop Ads commission rate, scaled by
            10,000. For example, `4000` represents 40%.
        partner_tap_bonus_commission_rate (int | Unset): The additional commission rate TikTok Shop offers to affiliate
            partners for driving product sales in specific campaigns, scaled by 10,000. For example, `1000` represents 10%.
        creator_tap_bonus_commission_rate (int | Unset): The commission reward rate allocated by the affiliate partner
            to the creator, scaled by 10,000. For example, `2000` represents 20%.
        estimated_commission_base (EstimatedCommissionBase | Unset):
        estimated_creator_standard_commission
            (SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorStandardCommission | Unset):
        estimated_partner_standard_commission
            (SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerStandardCommission | Unset):
        estimated_creator_shop_ads_commission
            (SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorShopAdsCommission | Unset):
        estimated_partner_shop_ads_commission
            (SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerShopAdsCommission | Unset):
        estimated_partner_tap_bonus_commission
            (SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerTapBonusCommission | Unset):
        estimated_creator_tap_bonus_commission
            (SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTapBonusCommission | Unset):
        estimated_partner_isr (SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerIsr | Unset):
        estimated_partner_iva (SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerIva | Unset):
        actual_commission_base (ActualCommissionBase | Unset):
        actual_creator_standard_commission (SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorStandardCommission
            | Unset):
        actual_partner_standard_commission (SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerStandardCommission
            | Unset):
        actual_creator_shop_ads_commission (SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorShopAdsCommission |
            Unset):
        actual_partner_shop_ads_commission (SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerShopAdsCommission |
            Unset):
        actual_partner_isr (SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIsr | Unset):
        actual_partner_iva (SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIva | Unset):
        actual_partner_tap_bonus_commission (SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerTapBonusCommission
            | Unset):
        actual_creator_tap_bonus_commission (SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorTapBonusCommission
            | Unset):
        fully_return (SearchTAPAffiliateOrdersResponseDataSkuOrderFullyReturn | Unset): Whether the SKU was fully
            returned or refunded.
            Possible values:
            - `Yes`: The SKU was fully returned or refunded, and no commission is paid.
            - `No`: The SKU was not fully returned or refunded.
        settlement_time (int | Unset): The time when the order commission was settled, as a Unix timestamp in seconds
            (UTC).
        last_update_time (int | Unset): The time when the record was last updated, as a Unix timestamp in seconds (UTC).
        is_carousel (bool | Unset): Carousel content may involve a commission rate discount. Returns true when the order
            is attributed to carousel content.
    """

    id: str | Unset = UNSET
    create_time: int | Unset = UNSET
    delivery_time: int | Unset = UNSET
    settle_status: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    campaign_id: str | Unset = UNSET
    creator_username: str | Unset = UNSET
    product_name: str | Unset = UNSET
    product_id: str | Unset = UNSET
    price: Price | Unset = UNSET
    quantity: int | Unset = UNSET
    content_type: SearchTAPAffiliateOrdersResponseDataSkuOrderContentType | Unset = UNSET
    content_id: str | Unset = UNSET
    creator_standard_commission_rate: int | Unset = UNSET
    partner_standard_commission_rate: int | Unset = UNSET
    creator_shop_ads_commission_rate: int | Unset = UNSET
    partner_shop_ads_commission_rate: int | Unset = UNSET
    partner_tap_bonus_commission_rate: int | Unset = UNSET
    creator_tap_bonus_commission_rate: int | Unset = UNSET
    estimated_commission_base: EstimatedCommissionBase | Unset = UNSET
    estimated_creator_standard_commission: (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorStandardCommission | Unset
    ) = UNSET
    estimated_partner_standard_commission: (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerStandardCommission | Unset
    ) = UNSET
    estimated_creator_shop_ads_commission: (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorShopAdsCommission | Unset
    ) = UNSET
    estimated_partner_shop_ads_commission: (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerShopAdsCommission | Unset
    ) = UNSET
    estimated_partner_tap_bonus_commission: (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerTapBonusCommission | Unset
    ) = UNSET
    estimated_creator_tap_bonus_commission: (
        SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTapBonusCommission | Unset
    ) = UNSET
    estimated_partner_isr: SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerIsr | Unset = UNSET
    estimated_partner_iva: SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerIva | Unset = UNSET
    actual_commission_base: ActualCommissionBase | Unset = UNSET
    actual_creator_standard_commission: (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorStandardCommission | Unset
    ) = UNSET
    actual_partner_standard_commission: (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerStandardCommission | Unset
    ) = UNSET
    actual_creator_shop_ads_commission: (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorShopAdsCommission | Unset
    ) = UNSET
    actual_partner_shop_ads_commission: (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerShopAdsCommission | Unset
    ) = UNSET
    actual_partner_isr: SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIsr | Unset = UNSET
    actual_partner_iva: SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIva | Unset = UNSET
    actual_partner_tap_bonus_commission: (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerTapBonusCommission | Unset
    ) = UNSET
    actual_creator_tap_bonus_commission: (
        SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorTapBonusCommission | Unset
    ) = UNSET
    fully_return: SearchTAPAffiliateOrdersResponseDataSkuOrderFullyReturn | Unset = UNSET
    settlement_time: int | Unset = UNSET
    last_update_time: int | Unset = UNSET
    is_carousel: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        create_time = self.create_time

        delivery_time = self.delivery_time

        settle_status = self.settle_status

        sku_id = self.sku_id

        campaign_id = self.campaign_id

        creator_username = self.creator_username

        product_name = self.product_name

        product_id = self.product_id

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        quantity = self.quantity

        content_type: str | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value

        content_id = self.content_id

        creator_standard_commission_rate = self.creator_standard_commission_rate

        partner_standard_commission_rate = self.partner_standard_commission_rate

        creator_shop_ads_commission_rate = self.creator_shop_ads_commission_rate

        partner_shop_ads_commission_rate = self.partner_shop_ads_commission_rate

        partner_tap_bonus_commission_rate = self.partner_tap_bonus_commission_rate

        creator_tap_bonus_commission_rate = self.creator_tap_bonus_commission_rate

        estimated_commission_base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_commission_base, Unset):
            estimated_commission_base = self.estimated_commission_base.to_dict()

        estimated_creator_standard_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_creator_standard_commission, Unset):
            estimated_creator_standard_commission = self.estimated_creator_standard_commission.to_dict()

        estimated_partner_standard_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_partner_standard_commission, Unset):
            estimated_partner_standard_commission = self.estimated_partner_standard_commission.to_dict()

        estimated_creator_shop_ads_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_creator_shop_ads_commission, Unset):
            estimated_creator_shop_ads_commission = self.estimated_creator_shop_ads_commission.to_dict()

        estimated_partner_shop_ads_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_partner_shop_ads_commission, Unset):
            estimated_partner_shop_ads_commission = self.estimated_partner_shop_ads_commission.to_dict()

        estimated_partner_tap_bonus_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_partner_tap_bonus_commission, Unset):
            estimated_partner_tap_bonus_commission = self.estimated_partner_tap_bonus_commission.to_dict()

        estimated_creator_tap_bonus_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_creator_tap_bonus_commission, Unset):
            estimated_creator_tap_bonus_commission = self.estimated_creator_tap_bonus_commission.to_dict()

        estimated_partner_isr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_partner_isr, Unset):
            estimated_partner_isr = self.estimated_partner_isr.to_dict()

        estimated_partner_iva: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_partner_iva, Unset):
            estimated_partner_iva = self.estimated_partner_iva.to_dict()

        actual_commission_base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_commission_base, Unset):
            actual_commission_base = self.actual_commission_base.to_dict()

        actual_creator_standard_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_creator_standard_commission, Unset):
            actual_creator_standard_commission = self.actual_creator_standard_commission.to_dict()

        actual_partner_standard_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_partner_standard_commission, Unset):
            actual_partner_standard_commission = self.actual_partner_standard_commission.to_dict()

        actual_creator_shop_ads_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_creator_shop_ads_commission, Unset):
            actual_creator_shop_ads_commission = self.actual_creator_shop_ads_commission.to_dict()

        actual_partner_shop_ads_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_partner_shop_ads_commission, Unset):
            actual_partner_shop_ads_commission = self.actual_partner_shop_ads_commission.to_dict()

        actual_partner_isr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_partner_isr, Unset):
            actual_partner_isr = self.actual_partner_isr.to_dict()

        actual_partner_iva: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_partner_iva, Unset):
            actual_partner_iva = self.actual_partner_iva.to_dict()

        actual_partner_tap_bonus_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_partner_tap_bonus_commission, Unset):
            actual_partner_tap_bonus_commission = self.actual_partner_tap_bonus_commission.to_dict()

        actual_creator_tap_bonus_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_creator_tap_bonus_commission, Unset):
            actual_creator_tap_bonus_commission = self.actual_creator_tap_bonus_commission.to_dict()

        fully_return: str | Unset = UNSET
        if not isinstance(self.fully_return, Unset):
            fully_return = self.fully_return.value

        settlement_time = self.settlement_time

        last_update_time = self.last_update_time

        is_carousel = self.is_carousel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if delivery_time is not UNSET:
            field_dict["delivery_time"] = delivery_time
        if settle_status is not UNSET:
            field_dict["settle_status"] = settle_status
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
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
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if content_id is not UNSET:
            field_dict["content_id"] = content_id
        if creator_standard_commission_rate is not UNSET:
            field_dict["creator_standard_commission_rate"] = creator_standard_commission_rate
        if partner_standard_commission_rate is not UNSET:
            field_dict["partner_standard_commission_rate"] = partner_standard_commission_rate
        if creator_shop_ads_commission_rate is not UNSET:
            field_dict["creator_shop_ads_commission_rate"] = creator_shop_ads_commission_rate
        if partner_shop_ads_commission_rate is not UNSET:
            field_dict["partner_shop_ads_commission_rate"] = partner_shop_ads_commission_rate
        if partner_tap_bonus_commission_rate is not UNSET:
            field_dict["partner_tap_bonus_commission_rate"] = partner_tap_bonus_commission_rate
        if creator_tap_bonus_commission_rate is not UNSET:
            field_dict["creator_tap_bonus_commission_rate"] = creator_tap_bonus_commission_rate
        if estimated_commission_base is not UNSET:
            field_dict["estimated_commission_base"] = estimated_commission_base
        if estimated_creator_standard_commission is not UNSET:
            field_dict["estimated_creator_standard_commission"] = estimated_creator_standard_commission
        if estimated_partner_standard_commission is not UNSET:
            field_dict["estimated_partner_standard_commission"] = estimated_partner_standard_commission
        if estimated_creator_shop_ads_commission is not UNSET:
            field_dict["estimated_creator_shop_ads_commission"] = estimated_creator_shop_ads_commission
        if estimated_partner_shop_ads_commission is not UNSET:
            field_dict["estimated_partner_shop_ads_commission"] = estimated_partner_shop_ads_commission
        if estimated_partner_tap_bonus_commission is not UNSET:
            field_dict["estimated_partner_tap_bonus_commission"] = estimated_partner_tap_bonus_commission
        if estimated_creator_tap_bonus_commission is not UNSET:
            field_dict["estimated_creator_tap_bonus_commission"] = estimated_creator_tap_bonus_commission
        if estimated_partner_isr is not UNSET:
            field_dict["estimated_partner_isr"] = estimated_partner_isr
        if estimated_partner_iva is not UNSET:
            field_dict["estimated_partner_iva"] = estimated_partner_iva
        if actual_commission_base is not UNSET:
            field_dict["actual_commission_base"] = actual_commission_base
        if actual_creator_standard_commission is not UNSET:
            field_dict["actual_creator_standard_commission"] = actual_creator_standard_commission
        if actual_partner_standard_commission is not UNSET:
            field_dict["actual_partner_standard_commission"] = actual_partner_standard_commission
        if actual_creator_shop_ads_commission is not UNSET:
            field_dict["actual_creator_shop_ads_commission"] = actual_creator_shop_ads_commission
        if actual_partner_shop_ads_commission is not UNSET:
            field_dict["actual_partner_shop_ads_commission"] = actual_partner_shop_ads_commission
        if actual_partner_isr is not UNSET:
            field_dict["actual_partner_isr"] = actual_partner_isr
        if actual_partner_iva is not UNSET:
            field_dict["actual_partner_iva"] = actual_partner_iva
        if actual_partner_tap_bonus_commission is not UNSET:
            field_dict["actual_partner_tap_bonus_commission"] = actual_partner_tap_bonus_commission
        if actual_creator_tap_bonus_commission is not UNSET:
            field_dict["actual_creator_tap_bonus_commission"] = actual_creator_tap_bonus_commission
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
        from ..models.actual_commission_base import ActualCommissionBase  # noqa: PLC0415
        from ..models.estimated_commission_base import EstimatedCommissionBase  # noqa: PLC0415
        from ..models.price import Price  # noqa: PLC0415
        from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_creator_shop_ads_commission import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorShopAdsCommission,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_creator_standard_commission import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorStandardCommission,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_creator_tap_bonus_commission import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorTapBonusCommission,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_partner_isr import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIsr,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_partner_iva import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIva,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_partner_shop_ads_commission import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerShopAdsCommission,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_partner_standard_commission import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerStandardCommission,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_actual_partner_tap_bonus_commission import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerTapBonusCommission,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_creator_shop_ads_commission import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorShopAdsCommission,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_creator_standard_commission import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorStandardCommission,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_creator_tap_bonus_commission import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTapBonusCommission,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_partner_isr import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerIsr,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_partner_iva import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerIva,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_partner_shop_ads_commission import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerShopAdsCommission,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_partner_standard_commission import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerStandardCommission,  # noqa: PLC0415
        )
        from ..models.search_tap_affiliate_orders_response_data_sku_order_estimated_partner_tap_bonus_commission import (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerTapBonusCommission,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        create_time = d.pop("create_time", UNSET)

        delivery_time = d.pop("delivery_time", UNSET)

        settle_status = d.pop("settle_status", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        campaign_id = d.pop("campaign_id", UNSET)

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

        _content_type = d.pop("content_type", UNSET)
        content_type: SearchTAPAffiliateOrdersResponseDataSkuOrderContentType | Unset
        if isinstance(_content_type, Unset):
            content_type = UNSET
        else:
            content_type = SearchTAPAffiliateOrdersResponseDataSkuOrderContentType(_content_type)

        content_id = d.pop("content_id", UNSET)

        creator_standard_commission_rate = d.pop("creator_standard_commission_rate", UNSET)

        partner_standard_commission_rate = d.pop("partner_standard_commission_rate", UNSET)

        creator_shop_ads_commission_rate = d.pop("creator_shop_ads_commission_rate", UNSET)

        partner_shop_ads_commission_rate = d.pop("partner_shop_ads_commission_rate", UNSET)

        partner_tap_bonus_commission_rate = d.pop("partner_tap_bonus_commission_rate", UNSET)

        creator_tap_bonus_commission_rate = d.pop("creator_tap_bonus_commission_rate", UNSET)

        _estimated_commission_base = d.pop("estimated_commission_base", UNSET)
        estimated_commission_base: EstimatedCommissionBase | Unset
        if isinstance(_estimated_commission_base, Unset):
            estimated_commission_base = UNSET
        else:
            estimated_commission_base = EstimatedCommissionBase.from_dict(_estimated_commission_base)

        _estimated_creator_standard_commission = d.pop("estimated_creator_standard_commission", UNSET)
        estimated_creator_standard_commission: (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorStandardCommission | Unset
        )
        if isinstance(_estimated_creator_standard_commission, Unset):
            estimated_creator_standard_commission = UNSET
        else:
            estimated_creator_standard_commission = (
                SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorStandardCommission.from_dict(
                    _estimated_creator_standard_commission
                )
            )

        _estimated_partner_standard_commission = d.pop("estimated_partner_standard_commission", UNSET)
        estimated_partner_standard_commission: (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerStandardCommission | Unset
        )
        if isinstance(_estimated_partner_standard_commission, Unset):
            estimated_partner_standard_commission = UNSET
        else:
            estimated_partner_standard_commission = (
                SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerStandardCommission.from_dict(
                    _estimated_partner_standard_commission
                )
            )

        _estimated_creator_shop_ads_commission = d.pop("estimated_creator_shop_ads_commission", UNSET)
        estimated_creator_shop_ads_commission: (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorShopAdsCommission | Unset
        )
        if isinstance(_estimated_creator_shop_ads_commission, Unset):
            estimated_creator_shop_ads_commission = UNSET
        else:
            estimated_creator_shop_ads_commission = (
                SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorShopAdsCommission.from_dict(
                    _estimated_creator_shop_ads_commission
                )
            )

        _estimated_partner_shop_ads_commission = d.pop("estimated_partner_shop_ads_commission", UNSET)
        estimated_partner_shop_ads_commission: (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerShopAdsCommission | Unset
        )
        if isinstance(_estimated_partner_shop_ads_commission, Unset):
            estimated_partner_shop_ads_commission = UNSET
        else:
            estimated_partner_shop_ads_commission = (
                SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerShopAdsCommission.from_dict(
                    _estimated_partner_shop_ads_commission
                )
            )

        _estimated_partner_tap_bonus_commission = d.pop("estimated_partner_tap_bonus_commission", UNSET)
        estimated_partner_tap_bonus_commission: (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerTapBonusCommission | Unset
        )
        if isinstance(_estimated_partner_tap_bonus_commission, Unset):
            estimated_partner_tap_bonus_commission = UNSET
        else:
            estimated_partner_tap_bonus_commission = (
                SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerTapBonusCommission.from_dict(
                    _estimated_partner_tap_bonus_commission
                )
            )

        _estimated_creator_tap_bonus_commission = d.pop("estimated_creator_tap_bonus_commission", UNSET)
        estimated_creator_tap_bonus_commission: (
            SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTapBonusCommission | Unset
        )
        if isinstance(_estimated_creator_tap_bonus_commission, Unset):
            estimated_creator_tap_bonus_commission = UNSET
        else:
            estimated_creator_tap_bonus_commission = (
                SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedCreatorTapBonusCommission.from_dict(
                    _estimated_creator_tap_bonus_commission
                )
            )

        _estimated_partner_isr = d.pop("estimated_partner_isr", UNSET)
        estimated_partner_isr: SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerIsr | Unset
        if isinstance(_estimated_partner_isr, Unset):
            estimated_partner_isr = UNSET
        else:
            estimated_partner_isr = SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerIsr.from_dict(
                _estimated_partner_isr
            )

        _estimated_partner_iva = d.pop("estimated_partner_iva", UNSET)
        estimated_partner_iva: SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerIva | Unset
        if isinstance(_estimated_partner_iva, Unset):
            estimated_partner_iva = UNSET
        else:
            estimated_partner_iva = SearchTAPAffiliateOrdersResponseDataSkuOrderEstimatedPartnerIva.from_dict(
                _estimated_partner_iva
            )

        _actual_commission_base = d.pop("actual_commission_base", UNSET)
        actual_commission_base: ActualCommissionBase | Unset
        if isinstance(_actual_commission_base, Unset):
            actual_commission_base = UNSET
        else:
            actual_commission_base = ActualCommissionBase.from_dict(_actual_commission_base)

        _actual_creator_standard_commission = d.pop("actual_creator_standard_commission", UNSET)
        actual_creator_standard_commission: (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorStandardCommission | Unset
        )
        if isinstance(_actual_creator_standard_commission, Unset):
            actual_creator_standard_commission = UNSET
        else:
            actual_creator_standard_commission = (
                SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorStandardCommission.from_dict(
                    _actual_creator_standard_commission
                )
            )

        _actual_partner_standard_commission = d.pop("actual_partner_standard_commission", UNSET)
        actual_partner_standard_commission: (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerStandardCommission | Unset
        )
        if isinstance(_actual_partner_standard_commission, Unset):
            actual_partner_standard_commission = UNSET
        else:
            actual_partner_standard_commission = (
                SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerStandardCommission.from_dict(
                    _actual_partner_standard_commission
                )
            )

        _actual_creator_shop_ads_commission = d.pop("actual_creator_shop_ads_commission", UNSET)
        actual_creator_shop_ads_commission: (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorShopAdsCommission | Unset
        )
        if isinstance(_actual_creator_shop_ads_commission, Unset):
            actual_creator_shop_ads_commission = UNSET
        else:
            actual_creator_shop_ads_commission = (
                SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorShopAdsCommission.from_dict(
                    _actual_creator_shop_ads_commission
                )
            )

        _actual_partner_shop_ads_commission = d.pop("actual_partner_shop_ads_commission", UNSET)
        actual_partner_shop_ads_commission: (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerShopAdsCommission | Unset
        )
        if isinstance(_actual_partner_shop_ads_commission, Unset):
            actual_partner_shop_ads_commission = UNSET
        else:
            actual_partner_shop_ads_commission = (
                SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerShopAdsCommission.from_dict(
                    _actual_partner_shop_ads_commission
                )
            )

        _actual_partner_isr = d.pop("actual_partner_isr", UNSET)
        actual_partner_isr: SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIsr | Unset
        if isinstance(_actual_partner_isr, Unset):
            actual_partner_isr = UNSET
        else:
            actual_partner_isr = SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIsr.from_dict(
                _actual_partner_isr
            )

        _actual_partner_iva = d.pop("actual_partner_iva", UNSET)
        actual_partner_iva: SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIva | Unset
        if isinstance(_actual_partner_iva, Unset):
            actual_partner_iva = UNSET
        else:
            actual_partner_iva = SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerIva.from_dict(
                _actual_partner_iva
            )

        _actual_partner_tap_bonus_commission = d.pop("actual_partner_tap_bonus_commission", UNSET)
        actual_partner_tap_bonus_commission: (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerTapBonusCommission | Unset
        )
        if isinstance(_actual_partner_tap_bonus_commission, Unset):
            actual_partner_tap_bonus_commission = UNSET
        else:
            actual_partner_tap_bonus_commission = (
                SearchTAPAffiliateOrdersResponseDataSkuOrderActualPartnerTapBonusCommission.from_dict(
                    _actual_partner_tap_bonus_commission
                )
            )

        _actual_creator_tap_bonus_commission = d.pop("actual_creator_tap_bonus_commission", UNSET)
        actual_creator_tap_bonus_commission: (
            SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorTapBonusCommission | Unset
        )
        if isinstance(_actual_creator_tap_bonus_commission, Unset):
            actual_creator_tap_bonus_commission = UNSET
        else:
            actual_creator_tap_bonus_commission = (
                SearchTAPAffiliateOrdersResponseDataSkuOrderActualCreatorTapBonusCommission.from_dict(
                    _actual_creator_tap_bonus_commission
                )
            )

        _fully_return = d.pop("fully_return", UNSET)
        fully_return: SearchTAPAffiliateOrdersResponseDataSkuOrderFullyReturn | Unset
        if isinstance(_fully_return, Unset):
            fully_return = UNSET
        else:
            fully_return = SearchTAPAffiliateOrdersResponseDataSkuOrderFullyReturn(_fully_return)

        settlement_time = d.pop("settlement_time", UNSET)

        last_update_time = d.pop("last_update_time", UNSET)

        is_carousel = d.pop("is_carousel", UNSET)

        search_tap_affiliate_orders_response_data_sku_order = cls(
            id=id,
            create_time=create_time,
            delivery_time=delivery_time,
            settle_status=settle_status,
            sku_id=sku_id,
            campaign_id=campaign_id,
            creator_username=creator_username,
            product_name=product_name,
            product_id=product_id,
            price=price,
            quantity=quantity,
            content_type=content_type,
            content_id=content_id,
            creator_standard_commission_rate=creator_standard_commission_rate,
            partner_standard_commission_rate=partner_standard_commission_rate,
            creator_shop_ads_commission_rate=creator_shop_ads_commission_rate,
            partner_shop_ads_commission_rate=partner_shop_ads_commission_rate,
            partner_tap_bonus_commission_rate=partner_tap_bonus_commission_rate,
            creator_tap_bonus_commission_rate=creator_tap_bonus_commission_rate,
            estimated_commission_base=estimated_commission_base,
            estimated_creator_standard_commission=estimated_creator_standard_commission,
            estimated_partner_standard_commission=estimated_partner_standard_commission,
            estimated_creator_shop_ads_commission=estimated_creator_shop_ads_commission,
            estimated_partner_shop_ads_commission=estimated_partner_shop_ads_commission,
            estimated_partner_tap_bonus_commission=estimated_partner_tap_bonus_commission,
            estimated_creator_tap_bonus_commission=estimated_creator_tap_bonus_commission,
            estimated_partner_isr=estimated_partner_isr,
            estimated_partner_iva=estimated_partner_iva,
            actual_commission_base=actual_commission_base,
            actual_creator_standard_commission=actual_creator_standard_commission,
            actual_partner_standard_commission=actual_partner_standard_commission,
            actual_creator_shop_ads_commission=actual_creator_shop_ads_commission,
            actual_partner_shop_ads_commission=actual_partner_shop_ads_commission,
            actual_partner_isr=actual_partner_isr,
            actual_partner_iva=actual_partner_iva,
            actual_partner_tap_bonus_commission=actual_partner_tap_bonus_commission,
            actual_creator_tap_bonus_commission=actual_creator_tap_bonus_commission,
            fully_return=fully_return,
            settlement_time=settlement_time,
            last_update_time=last_update_time,
            is_carousel=is_carousel,
        )

        search_tap_affiliate_orders_response_data_sku_order.additional_properties = d
        return search_tap_affiliate_orders_response_data_sku_order

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
