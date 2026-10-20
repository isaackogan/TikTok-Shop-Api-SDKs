from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.actual_bonus_commission import ActualBonusCommission
  from ..models.actual_commission import ActualCommission
  from ..models.actual_commission_base import ActualCommissionBase
  from ..models.actual_creator_commission_reward_fee import ActualCreatorCommissionRewardFee
  from ..models.actual_shop_ads_commission import ActualShopAdsCommission
  from ..models.actual_standard_commission import ActualStandardCommission
  from ..models.estimated_bonus_commission import EstimatedBonusCommission
  from ..models.estimated_commission import EstimatedCommission
  from ..models.estimated_commission_base import EstimatedCommissionBase
  from ..models.estimated_creator_commission_reward_fee import EstimatedCreatorCommissionRewardFee
  from ..models.estimated_shop_ads_commission import EstimatedShopAdsCommission
  from ..models.estimated_standard_commission import EstimatedStandardCommission
  from ..models.price import Price
  from ..models.search_creator_affiliate_orders_response_data_order_sku_isr import SearchCreatorAffiliateOrdersResponseDataOrderSkuIsr
  from ..models.search_creator_affiliate_orders_response_data_order_sku_iva import SearchCreatorAffiliateOrdersResponseDataOrderSkuIva
  from ..models.search_creator_affiliate_orders_response_data_order_sku_pit import SearchCreatorAffiliateOrdersResponseDataOrderSkuPit
  from ..models.search_creator_affiliate_orders_response_data_order_sku_shared_with_partner import SearchCreatorAffiliateOrdersResponseDataOrderSkuSharedWithPartner
  from ..models.search_creator_affiliate_orders_response_data_order_sku_trace_info import SearchCreatorAffiliateOrdersResponseDataOrderSkuTraceInfo





T = TypeVar("T", bound="SearchCreatorAffiliateOrdersResponseDataOrderSku")



@_attrs_define
class SearchCreatorAffiliateOrdersResponseDataOrderSku:
    """ 
        Attributes:
            id (str | Unset): The SKU identifier.
            campaign_id (str | Unset): The campaign identifier associated with the order.
            open_collaboration_id (str | Unset): The open collaboration identifier associated with the order.
            target_collaboration_id (str | Unset): The target collaboration identifier associated with the order.
            product_name (str | Unset): The product name in the TikTok Shop.
            product_id (str | Unset): The product identifier.
            price (Price | Unset):
            shop_name (str | Unset): The name of the TIkTok Shop in which the product is offered for sale.
            content_type (str | Unset): The content format of the creator content through which the order was created.
                Possible values:
                - SHOP
                - VIDEO
                - LIVE
                - PRE_LIVE
                - PROMOTION_PAGE
                - LINKSHARE
            content_id (str | Unset): The content identifier for the creator content through which the order was created.
            quantity (int | Unset): The quantity of this SKU in the order, including refunded units.
            commission_rate (int | Unset): The total commission rate for this SKU, equal to the sum of the standard
                commission rate, shop ads commission rate, bonus rate, and reward rate. It is expressed in hundredths of a
                percent; the percent sign (`%`) is not included. For example, `3000` represents a 30% commission.
            commission_tier_setting (str | Unset): Between Seller & Creator percentagecommission. When tiering commission
                model applied, will return each tier's commission rate seller set.
            commission_model (str | Unset): The commission model used for the order.
                Possible values:
                - Fixed commission
                - Tiered commission
            commission_bonus_rate (int | Unset): The commission bonus rate associated with the collaboration. It is
                expressed in hundredths of a percent; the percent sign (`%`) is not included. For example, `3000` represents a
                30% commission.
            estimated_commission_base (EstimatedCommissionBase | Unset):
            standard_commission_rate (int | Unset): The standard affiliate commission rate associated with the
                collaboration. It is expressed in hundredths of a percent; the percent sign (`%`) is not included. For example,
                `3000` represents a 30% commission.
            shop_ads_commission_rate (int | Unset): The commission rate received by a creator for a sale associated with a
                specific piece of content. It is expressed in hundredths of a percent; the percent sign (`%`) is not included.
                For example, `3000` represents a 30% commission.
            estimated_bonus_commission (EstimatedBonusCommission | Unset):
            estimated_standard_commission (EstimatedStandardCommission | Unset):
            estimated_shop_ads_commission (EstimatedShopAdsCommission | Unset):
            estimated_commission (EstimatedCommission | Unset):
            actual_commission (ActualCommission | Unset):
            actual_bonus_commission (ActualBonusCommission | Unset):
            actual_commission_base (ActualCommissionBase | Unset):
            actual_standard_commission (ActualStandardCommission | Unset):
            actual_shop_ads_commission (ActualShopAdsCommission | Unset):
            returned_quantity (int | Unset): The returned quantity for this SKU in the order.
            refunded_quantity (int | Unset): The refunded quantity for this SKU in the order.
            tag (str | Unset): A field for storing user-defined metadata for tracking purposes.
            creator_commission_reward_rate (int | Unset): The commission reward rate that an affiliate partner allocates to
                the creator. It is expressed in hundredths of a percent; the percent sign (`%`) is not included. For example,
                `1000` represents 10%.
            estimated_creator_commission_reward_fee (EstimatedCreatorCommissionRewardFee | Unset):
            actual_creator_commission_reward_fee (ActualCreatorCommissionRewardFee | Unset):
            isr (SearchCreatorAffiliateOrdersResponseDataOrderSkuIsr | Unset):
            iva (SearchCreatorAffiliateOrdersResponseDataOrderSkuIva | Unset):
            pit (SearchCreatorAffiliateOrdersResponseDataOrderSkuPit | Unset):
            shared_with_partner (SearchCreatorAffiliateOrdersResponseDataOrderSkuSharedWithPartner | Unset):
            trace_info (SearchCreatorAffiliateOrdersResponseDataOrderSkuTraceInfo | Unset):
            last_update_time (int | Unset): The time when the record was last updated, as a Unix timestamp in seconds (UTC).
            is_carousel (bool | Unset): Carousel content may involve a commission rate discount. Returns true when the order
                is attributed to carousel content.
     """

    id: str | Unset = UNSET
    campaign_id: str | Unset = UNSET
    open_collaboration_id: str | Unset = UNSET
    target_collaboration_id: str | Unset = UNSET
    product_name: str | Unset = UNSET
    product_id: str | Unset = UNSET
    price: Price | Unset = UNSET
    shop_name: str | Unset = UNSET
    content_type: str | Unset = UNSET
    content_id: str | Unset = UNSET
    quantity: int | Unset = UNSET
    commission_rate: int | Unset = UNSET
    commission_tier_setting: str | Unset = UNSET
    commission_model: str | Unset = UNSET
    commission_bonus_rate: int | Unset = UNSET
    estimated_commission_base: EstimatedCommissionBase | Unset = UNSET
    standard_commission_rate: int | Unset = UNSET
    shop_ads_commission_rate: int | Unset = UNSET
    estimated_bonus_commission: EstimatedBonusCommission | Unset = UNSET
    estimated_standard_commission: EstimatedStandardCommission | Unset = UNSET
    estimated_shop_ads_commission: EstimatedShopAdsCommission | Unset = UNSET
    estimated_commission: EstimatedCommission | Unset = UNSET
    actual_commission: ActualCommission | Unset = UNSET
    actual_bonus_commission: ActualBonusCommission | Unset = UNSET
    actual_commission_base: ActualCommissionBase | Unset = UNSET
    actual_standard_commission: ActualStandardCommission | Unset = UNSET
    actual_shop_ads_commission: ActualShopAdsCommission | Unset = UNSET
    returned_quantity: int | Unset = UNSET
    refunded_quantity: int | Unset = UNSET
    tag: str | Unset = UNSET
    creator_commission_reward_rate: int | Unset = UNSET
    estimated_creator_commission_reward_fee: EstimatedCreatorCommissionRewardFee | Unset = UNSET
    actual_creator_commission_reward_fee: ActualCreatorCommissionRewardFee | Unset = UNSET
    isr: SearchCreatorAffiliateOrdersResponseDataOrderSkuIsr | Unset = UNSET
    iva: SearchCreatorAffiliateOrdersResponseDataOrderSkuIva | Unset = UNSET
    pit: SearchCreatorAffiliateOrdersResponseDataOrderSkuPit | Unset = UNSET
    shared_with_partner: SearchCreatorAffiliateOrdersResponseDataOrderSkuSharedWithPartner | Unset = UNSET
    trace_info: SearchCreatorAffiliateOrdersResponseDataOrderSkuTraceInfo | Unset = UNSET
    last_update_time: int | Unset = UNSET
    is_carousel: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.actual_bonus_commission import ActualBonusCommission # noqa: PLC0415
        from ..models.actual_commission import ActualCommission # noqa: PLC0415
        from ..models.actual_commission_base import ActualCommissionBase # noqa: PLC0415
        from ..models.actual_creator_commission_reward_fee import ActualCreatorCommissionRewardFee # noqa: PLC0415
        from ..models.actual_shop_ads_commission import ActualShopAdsCommission # noqa: PLC0415
        from ..models.actual_standard_commission import ActualStandardCommission # noqa: PLC0415
        from ..models.estimated_bonus_commission import EstimatedBonusCommission # noqa: PLC0415
        from ..models.estimated_commission import EstimatedCommission # noqa: PLC0415
        from ..models.estimated_commission_base import EstimatedCommissionBase # noqa: PLC0415
        from ..models.estimated_creator_commission_reward_fee import EstimatedCreatorCommissionRewardFee # noqa: PLC0415
        from ..models.estimated_shop_ads_commission import EstimatedShopAdsCommission # noqa: PLC0415
        from ..models.estimated_standard_commission import EstimatedStandardCommission # noqa: PLC0415
        from ..models.price import Price # noqa: PLC0415
        from ..models.search_creator_affiliate_orders_response_data_order_sku_isr import SearchCreatorAffiliateOrdersResponseDataOrderSkuIsr # noqa: PLC0415
        from ..models.search_creator_affiliate_orders_response_data_order_sku_iva import SearchCreatorAffiliateOrdersResponseDataOrderSkuIva # noqa: PLC0415
        from ..models.search_creator_affiliate_orders_response_data_order_sku_pit import SearchCreatorAffiliateOrdersResponseDataOrderSkuPit # noqa: PLC0415
        from ..models.search_creator_affiliate_orders_response_data_order_sku_shared_with_partner import SearchCreatorAffiliateOrdersResponseDataOrderSkuSharedWithPartner # noqa: PLC0415
        from ..models.search_creator_affiliate_orders_response_data_order_sku_trace_info import SearchCreatorAffiliateOrdersResponseDataOrderSkuTraceInfo # noqa: PLC0415
        id = self.id

        campaign_id = self.campaign_id

        open_collaboration_id = self.open_collaboration_id

        target_collaboration_id = self.target_collaboration_id

        product_name = self.product_name

        product_id = self.product_id

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        shop_name = self.shop_name

        content_type = self.content_type

        content_id = self.content_id

        quantity = self.quantity

        commission_rate = self.commission_rate

        commission_tier_setting = self.commission_tier_setting

        commission_model = self.commission_model

        commission_bonus_rate = self.commission_bonus_rate

        estimated_commission_base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_commission_base, Unset):
            estimated_commission_base = self.estimated_commission_base.to_dict()

        standard_commission_rate = self.standard_commission_rate

        shop_ads_commission_rate = self.shop_ads_commission_rate

        estimated_bonus_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_bonus_commission, Unset):
            estimated_bonus_commission = self.estimated_bonus_commission.to_dict()

        estimated_standard_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_standard_commission, Unset):
            estimated_standard_commission = self.estimated_standard_commission.to_dict()

        estimated_shop_ads_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_shop_ads_commission, Unset):
            estimated_shop_ads_commission = self.estimated_shop_ads_commission.to_dict()

        estimated_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_commission, Unset):
            estimated_commission = self.estimated_commission.to_dict()

        actual_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_commission, Unset):
            actual_commission = self.actual_commission.to_dict()

        actual_bonus_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_bonus_commission, Unset):
            actual_bonus_commission = self.actual_bonus_commission.to_dict()

        actual_commission_base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_commission_base, Unset):
            actual_commission_base = self.actual_commission_base.to_dict()

        actual_standard_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_standard_commission, Unset):
            actual_standard_commission = self.actual_standard_commission.to_dict()

        actual_shop_ads_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_shop_ads_commission, Unset):
            actual_shop_ads_commission = self.actual_shop_ads_commission.to_dict()

        returned_quantity = self.returned_quantity

        refunded_quantity = self.refunded_quantity

        tag = self.tag

        creator_commission_reward_rate = self.creator_commission_reward_rate

        estimated_creator_commission_reward_fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_creator_commission_reward_fee, Unset):
            estimated_creator_commission_reward_fee = self.estimated_creator_commission_reward_fee.to_dict()

        actual_creator_commission_reward_fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_creator_commission_reward_fee, Unset):
            actual_creator_commission_reward_fee = self.actual_creator_commission_reward_fee.to_dict()

        isr: dict[str, Any] | Unset = UNSET
        if not isinstance(self.isr, Unset):
            isr = self.isr.to_dict()

        iva: dict[str, Any] | Unset = UNSET
        if not isinstance(self.iva, Unset):
            iva = self.iva.to_dict()

        pit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pit, Unset):
            pit = self.pit.to_dict()

        shared_with_partner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shared_with_partner, Unset):
            shared_with_partner = self.shared_with_partner.to_dict()

        trace_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trace_info, Unset):
            trace_info = self.trace_info.to_dict()

        last_update_time = self.last_update_time

        is_carousel = self.is_carousel


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if open_collaboration_id is not UNSET:
            field_dict["open_collaboration_id"] = open_collaboration_id
        if target_collaboration_id is not UNSET:
            field_dict["target_collaboration_id"] = target_collaboration_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if price is not UNSET:
            field_dict["price"] = price
        if shop_name is not UNSET:
            field_dict["shop_name"] = shop_name
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if content_id is not UNSET:
            field_dict["content_id"] = content_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if commission_rate is not UNSET:
            field_dict["commission_rate"] = commission_rate
        if commission_tier_setting is not UNSET:
            field_dict["commission_tier_setting"] = commission_tier_setting
        if commission_model is not UNSET:
            field_dict["commission_model"] = commission_model
        if commission_bonus_rate is not UNSET:
            field_dict["commission_bonus_rate"] = commission_bonus_rate
        if estimated_commission_base is not UNSET:
            field_dict["estimated_commission_base"] = estimated_commission_base
        if standard_commission_rate is not UNSET:
            field_dict["standard_commission_rate"] = standard_commission_rate
        if shop_ads_commission_rate is not UNSET:
            field_dict["shop_ads_commission_rate"] = shop_ads_commission_rate
        if estimated_bonus_commission is not UNSET:
            field_dict["estimated_bonus_commission"] = estimated_bonus_commission
        if estimated_standard_commission is not UNSET:
            field_dict["estimated_standard_commission"] = estimated_standard_commission
        if estimated_shop_ads_commission is not UNSET:
            field_dict["estimated_shop_ads_commission"] = estimated_shop_ads_commission
        if estimated_commission is not UNSET:
            field_dict["estimated_commission"] = estimated_commission
        if actual_commission is not UNSET:
            field_dict["actual_commission"] = actual_commission
        if actual_bonus_commission is not UNSET:
            field_dict["actual_bonus_commission"] = actual_bonus_commission
        if actual_commission_base is not UNSET:
            field_dict["actual_commission_base"] = actual_commission_base
        if actual_standard_commission is not UNSET:
            field_dict["actual_standard_commission"] = actual_standard_commission
        if actual_shop_ads_commission is not UNSET:
            field_dict["actual_shop_ads_commission"] = actual_shop_ads_commission
        if returned_quantity is not UNSET:
            field_dict["returned_quantity"] = returned_quantity
        if refunded_quantity is not UNSET:
            field_dict["refunded_quantity"] = refunded_quantity
        if tag is not UNSET:
            field_dict["tag"] = tag
        if creator_commission_reward_rate is not UNSET:
            field_dict["creator_commission_reward_rate"] = creator_commission_reward_rate
        if estimated_creator_commission_reward_fee is not UNSET:
            field_dict["estimated_creator_commission_reward_fee"] = estimated_creator_commission_reward_fee
        if actual_creator_commission_reward_fee is not UNSET:
            field_dict["actual_creator_commission_reward_fee"] = actual_creator_commission_reward_fee
        if isr is not UNSET:
            field_dict["isr"] = isr
        if iva is not UNSET:
            field_dict["iva"] = iva
        if pit is not UNSET:
            field_dict["pit"] = pit
        if shared_with_partner is not UNSET:
            field_dict["shared_with_partner"] = shared_with_partner
        if trace_info is not UNSET:
            field_dict["trace_info"] = trace_info
        if last_update_time is not UNSET:
            field_dict["last_update_time"] = last_update_time
        if is_carousel is not UNSET:
            field_dict["is_carousel"] = is_carousel

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.actual_bonus_commission import ActualBonusCommission # noqa: PLC0415
        from ..models.actual_commission import ActualCommission # noqa: PLC0415
        from ..models.actual_commission_base import ActualCommissionBase # noqa: PLC0415
        from ..models.actual_creator_commission_reward_fee import ActualCreatorCommissionRewardFee # noqa: PLC0415
        from ..models.actual_shop_ads_commission import ActualShopAdsCommission # noqa: PLC0415
        from ..models.actual_standard_commission import ActualStandardCommission # noqa: PLC0415
        from ..models.estimated_bonus_commission import EstimatedBonusCommission # noqa: PLC0415
        from ..models.estimated_commission import EstimatedCommission # noqa: PLC0415
        from ..models.estimated_commission_base import EstimatedCommissionBase # noqa: PLC0415
        from ..models.estimated_creator_commission_reward_fee import EstimatedCreatorCommissionRewardFee # noqa: PLC0415
        from ..models.estimated_shop_ads_commission import EstimatedShopAdsCommission # noqa: PLC0415
        from ..models.estimated_standard_commission import EstimatedStandardCommission # noqa: PLC0415
        from ..models.price import Price # noqa: PLC0415
        from ..models.search_creator_affiliate_orders_response_data_order_sku_isr import SearchCreatorAffiliateOrdersResponseDataOrderSkuIsr # noqa: PLC0415
        from ..models.search_creator_affiliate_orders_response_data_order_sku_iva import SearchCreatorAffiliateOrdersResponseDataOrderSkuIva # noqa: PLC0415
        from ..models.search_creator_affiliate_orders_response_data_order_sku_pit import SearchCreatorAffiliateOrdersResponseDataOrderSkuPit # noqa: PLC0415
        from ..models.search_creator_affiliate_orders_response_data_order_sku_shared_with_partner import SearchCreatorAffiliateOrdersResponseDataOrderSkuSharedWithPartner # noqa: PLC0415
        from ..models.search_creator_affiliate_orders_response_data_order_sku_trace_info import SearchCreatorAffiliateOrdersResponseDataOrderSkuTraceInfo # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        campaign_id = d.pop("campaign_id", UNSET)

        open_collaboration_id = d.pop("open_collaboration_id", UNSET)

        target_collaboration_id = d.pop("target_collaboration_id", UNSET)

        product_name = d.pop("product_name", UNSET)

        product_id = d.pop("product_id", UNSET)

        _price = d.pop("price", UNSET)
        price: Price | Unset
        if isinstance(_price,  Unset):
            price = UNSET
        else:
            price = Price.from_dict(_price)




        shop_name = d.pop("shop_name", UNSET)

        content_type = d.pop("content_type", UNSET)

        content_id = d.pop("content_id", UNSET)

        quantity = d.pop("quantity", UNSET)

        commission_rate = d.pop("commission_rate", UNSET)

        commission_tier_setting = d.pop("commission_tier_setting", UNSET)

        commission_model = d.pop("commission_model", UNSET)

        commission_bonus_rate = d.pop("commission_bonus_rate", UNSET)

        _estimated_commission_base = d.pop("estimated_commission_base", UNSET)
        estimated_commission_base: EstimatedCommissionBase | Unset
        if isinstance(_estimated_commission_base,  Unset):
            estimated_commission_base = UNSET
        else:
            estimated_commission_base = EstimatedCommissionBase.from_dict(_estimated_commission_base)




        standard_commission_rate = d.pop("standard_commission_rate", UNSET)

        shop_ads_commission_rate = d.pop("shop_ads_commission_rate", UNSET)

        _estimated_bonus_commission = d.pop("estimated_bonus_commission", UNSET)
        estimated_bonus_commission: EstimatedBonusCommission | Unset
        if isinstance(_estimated_bonus_commission,  Unset):
            estimated_bonus_commission = UNSET
        else:
            estimated_bonus_commission = EstimatedBonusCommission.from_dict(_estimated_bonus_commission)




        _estimated_standard_commission = d.pop("estimated_standard_commission", UNSET)
        estimated_standard_commission: EstimatedStandardCommission | Unset
        if isinstance(_estimated_standard_commission,  Unset):
            estimated_standard_commission = UNSET
        else:
            estimated_standard_commission = EstimatedStandardCommission.from_dict(_estimated_standard_commission)




        _estimated_shop_ads_commission = d.pop("estimated_shop_ads_commission", UNSET)
        estimated_shop_ads_commission: EstimatedShopAdsCommission | Unset
        if isinstance(_estimated_shop_ads_commission,  Unset):
            estimated_shop_ads_commission = UNSET
        else:
            estimated_shop_ads_commission = EstimatedShopAdsCommission.from_dict(_estimated_shop_ads_commission)




        _estimated_commission = d.pop("estimated_commission", UNSET)
        estimated_commission: EstimatedCommission | Unset
        if isinstance(_estimated_commission,  Unset):
            estimated_commission = UNSET
        else:
            estimated_commission = EstimatedCommission.from_dict(_estimated_commission)




        _actual_commission = d.pop("actual_commission", UNSET)
        actual_commission: ActualCommission | Unset
        if isinstance(_actual_commission,  Unset):
            actual_commission = UNSET
        else:
            actual_commission = ActualCommission.from_dict(_actual_commission)




        _actual_bonus_commission = d.pop("actual_bonus_commission", UNSET)
        actual_bonus_commission: ActualBonusCommission | Unset
        if isinstance(_actual_bonus_commission,  Unset):
            actual_bonus_commission = UNSET
        else:
            actual_bonus_commission = ActualBonusCommission.from_dict(_actual_bonus_commission)




        _actual_commission_base = d.pop("actual_commission_base", UNSET)
        actual_commission_base: ActualCommissionBase | Unset
        if isinstance(_actual_commission_base,  Unset):
            actual_commission_base = UNSET
        else:
            actual_commission_base = ActualCommissionBase.from_dict(_actual_commission_base)




        _actual_standard_commission = d.pop("actual_standard_commission", UNSET)
        actual_standard_commission: ActualStandardCommission | Unset
        if isinstance(_actual_standard_commission,  Unset):
            actual_standard_commission = UNSET
        else:
            actual_standard_commission = ActualStandardCommission.from_dict(_actual_standard_commission)




        _actual_shop_ads_commission = d.pop("actual_shop_ads_commission", UNSET)
        actual_shop_ads_commission: ActualShopAdsCommission | Unset
        if isinstance(_actual_shop_ads_commission,  Unset):
            actual_shop_ads_commission = UNSET
        else:
            actual_shop_ads_commission = ActualShopAdsCommission.from_dict(_actual_shop_ads_commission)




        returned_quantity = d.pop("returned_quantity", UNSET)

        refunded_quantity = d.pop("refunded_quantity", UNSET)

        tag = d.pop("tag", UNSET)

        creator_commission_reward_rate = d.pop("creator_commission_reward_rate", UNSET)

        _estimated_creator_commission_reward_fee = d.pop("estimated_creator_commission_reward_fee", UNSET)
        estimated_creator_commission_reward_fee: EstimatedCreatorCommissionRewardFee | Unset
        if isinstance(_estimated_creator_commission_reward_fee,  Unset):
            estimated_creator_commission_reward_fee = UNSET
        else:
            estimated_creator_commission_reward_fee = EstimatedCreatorCommissionRewardFee.from_dict(_estimated_creator_commission_reward_fee)




        _actual_creator_commission_reward_fee = d.pop("actual_creator_commission_reward_fee", UNSET)
        actual_creator_commission_reward_fee: ActualCreatorCommissionRewardFee | Unset
        if isinstance(_actual_creator_commission_reward_fee,  Unset):
            actual_creator_commission_reward_fee = UNSET
        else:
            actual_creator_commission_reward_fee = ActualCreatorCommissionRewardFee.from_dict(_actual_creator_commission_reward_fee)




        _isr = d.pop("isr", UNSET)
        isr: SearchCreatorAffiliateOrdersResponseDataOrderSkuIsr | Unset
        if isinstance(_isr,  Unset):
            isr = UNSET
        else:
            isr = SearchCreatorAffiliateOrdersResponseDataOrderSkuIsr.from_dict(_isr)




        _iva = d.pop("iva", UNSET)
        iva: SearchCreatorAffiliateOrdersResponseDataOrderSkuIva | Unset
        if isinstance(_iva,  Unset):
            iva = UNSET
        else:
            iva = SearchCreatorAffiliateOrdersResponseDataOrderSkuIva.from_dict(_iva)




        _pit = d.pop("pit", UNSET)
        pit: SearchCreatorAffiliateOrdersResponseDataOrderSkuPit | Unset
        if isinstance(_pit,  Unset):
            pit = UNSET
        else:
            pit = SearchCreatorAffiliateOrdersResponseDataOrderSkuPit.from_dict(_pit)




        _shared_with_partner = d.pop("shared_with_partner", UNSET)
        shared_with_partner: SearchCreatorAffiliateOrdersResponseDataOrderSkuSharedWithPartner | Unset
        if isinstance(_shared_with_partner,  Unset):
            shared_with_partner = UNSET
        else:
            shared_with_partner = SearchCreatorAffiliateOrdersResponseDataOrderSkuSharedWithPartner.from_dict(_shared_with_partner)




        _trace_info = d.pop("trace_info", UNSET)
        trace_info: SearchCreatorAffiliateOrdersResponseDataOrderSkuTraceInfo | Unset
        if isinstance(_trace_info,  Unset):
            trace_info = UNSET
        else:
            trace_info = SearchCreatorAffiliateOrdersResponseDataOrderSkuTraceInfo.from_dict(_trace_info)




        last_update_time = d.pop("last_update_time", UNSET)

        is_carousel = d.pop("is_carousel", UNSET)

        search_creator_affiliate_orders_response_data_order_sku = cls(
            id=id,
            campaign_id=campaign_id,
            open_collaboration_id=open_collaboration_id,
            target_collaboration_id=target_collaboration_id,
            product_name=product_name,
            product_id=product_id,
            price=price,
            shop_name=shop_name,
            content_type=content_type,
            content_id=content_id,
            quantity=quantity,
            commission_rate=commission_rate,
            commission_tier_setting=commission_tier_setting,
            commission_model=commission_model,
            commission_bonus_rate=commission_bonus_rate,
            estimated_commission_base=estimated_commission_base,
            standard_commission_rate=standard_commission_rate,
            shop_ads_commission_rate=shop_ads_commission_rate,
            estimated_bonus_commission=estimated_bonus_commission,
            estimated_standard_commission=estimated_standard_commission,
            estimated_shop_ads_commission=estimated_shop_ads_commission,
            estimated_commission=estimated_commission,
            actual_commission=actual_commission,
            actual_bonus_commission=actual_bonus_commission,
            actual_commission_base=actual_commission_base,
            actual_standard_commission=actual_standard_commission,
            actual_shop_ads_commission=actual_shop_ads_commission,
            returned_quantity=returned_quantity,
            refunded_quantity=refunded_quantity,
            tag=tag,
            creator_commission_reward_rate=creator_commission_reward_rate,
            estimated_creator_commission_reward_fee=estimated_creator_commission_reward_fee,
            actual_creator_commission_reward_fee=actual_creator_commission_reward_fee,
            isr=isr,
            iva=iva,
            pit=pit,
            shared_with_partner=shared_with_partner,
            trace_info=trace_info,
            last_update_time=last_update_time,
            is_carousel=is_carousel,
        )


        search_creator_affiliate_orders_response_data_order_sku.additional_properties = d
        return search_creator_affiliate_orders_response_data_order_sku

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
