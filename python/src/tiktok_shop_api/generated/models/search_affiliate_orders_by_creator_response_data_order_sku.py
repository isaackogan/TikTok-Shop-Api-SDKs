from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.actual_bonus_commission import ActualBonusCommission
    from ..models.actual_commission import ActualCommission
    from ..models.actual_commission_base import ActualCommissionBase
    from ..models.actual_creator_commission_reward_fee import ActualCreatorCommissionRewardFee
    from ..models.actual_shop_ads_commission import ActualShopAdsCommission
    from ..models.estimated_bonus_commission import EstimatedBonusCommission
    from ..models.estimated_commission import EstimatedCommission
    from ..models.estimated_commission_base import EstimatedCommissionBase
    from ..models.estimated_creator_commission_reward_fee import EstimatedCreatorCommissionRewardFee
    from ..models.estimated_shop_ads_commission import EstimatedShopAdsCommission
    from ..models.price import Price
    from ..models.search_affiliate_orders_by_creator_response_data_order_sku_trace import (
        SearchAffiliateOrdersByCreatorResponseDataOrderSkuTrace,
    )


T = TypeVar("T", bound="SearchAffiliateOrdersByCreatorResponseDataOrderSku")


@_attrs_define
class SearchAffiliateOrdersByCreatorResponseDataOrderSku:
    """
    Attributes:
        id (str | Unset): The SKU identifier.
        product_id (str | Unset): The product identifier.
        price (Price | Unset):
        quantity (int | Unset): The quantity of this SKU in the order.
        commission_rate (int | Unset): The commission rate associated with the collaboration, in hundredths of a
            percent. The value does not include a percent sign. For example, `3000` represents 30%.
        estimated_commission_base (EstimatedCommissionBase | Unset):
        actual_commission (ActualCommission | Unset):
        shop_ads_commission_rate (int | Unset): The commission rate received by a creator for a sale associated with a
            specific piece of content, in hundredths of a percent. The value does not include a percent sign. For example,
            `3000` represents 30%.
        commission_bonus_rate (int | Unset): The commission bonus rate associated with the collaboration, in hundredths
            of a percent. The value does not include a percent sign. For example, `3000` represents 30%.
        product_name (str | Unset): The product name in the TikTok Shop.
        shop_name (str | Unset): The name of the TIkTok Shop in which the product is offered for sale.
        returned_quantity (int | Unset): The returned quantity of this SKU in the order.
        refunded_quantity (int | Unset): The refunded quantity of this SKU in the order.
        campaign_id (str | Unset): The campaign identifier associated with the order.
        actual_commission_base (ActualCommissionBase | Unset):
        actual_shop_ads_commission (ActualShopAdsCommission | Unset):
        estimated_shop_ads_commission (EstimatedShopAdsCommission | Unset):
        estimated_bonus_commission (EstimatedBonusCommission | Unset):
        delivery_time (int | Unset): Time and date order delivered, UTC+0 timing
        creator_commission_reward_rate (int | Unset): The commission reward rate that affiliate partners allocate to
            creators, in hundredths of a percent. The value does not include a percent sign. For example, `1000` represents
            10%.
        estimated_creator_commission_reward_fee (EstimatedCreatorCommissionRewardFee | Unset):
        actual_creator_commission_reward_fee (ActualCreatorCommissionRewardFee | Unset):
        content_type (str | Unset): The content format of the creator content through which the order was created.
            Possible values:
            - SHOP
            - VIDEO
            - LIVE
            - PRE_LIVE
            - PROMOTION_PAGE
            - LINKSHARE
        content_id (str | Unset): The content identifier for the creator content through which the order was created.
        trace (SearchAffiliateOrdersByCreatorResponseDataOrderSkuTrace | Unset):
        estimated_commission (EstimatedCommission | Unset):
        actual_bonus_commission (ActualBonusCommission | Unset):
    """

    id: str | Unset = UNSET
    product_id: str | Unset = UNSET
    price: Price | Unset = UNSET
    quantity: int | Unset = UNSET
    commission_rate: int | Unset = UNSET
    estimated_commission_base: EstimatedCommissionBase | Unset = UNSET
    actual_commission: ActualCommission | Unset = UNSET
    shop_ads_commission_rate: int | Unset = UNSET
    commission_bonus_rate: int | Unset = UNSET
    product_name: str | Unset = UNSET
    shop_name: str | Unset = UNSET
    returned_quantity: int | Unset = UNSET
    refunded_quantity: int | Unset = UNSET
    campaign_id: str | Unset = UNSET
    actual_commission_base: ActualCommissionBase | Unset = UNSET
    actual_shop_ads_commission: ActualShopAdsCommission | Unset = UNSET
    estimated_shop_ads_commission: EstimatedShopAdsCommission | Unset = UNSET
    estimated_bonus_commission: EstimatedBonusCommission | Unset = UNSET
    delivery_time: int | Unset = UNSET
    creator_commission_reward_rate: int | Unset = UNSET
    estimated_creator_commission_reward_fee: EstimatedCreatorCommissionRewardFee | Unset = UNSET
    actual_creator_commission_reward_fee: ActualCreatorCommissionRewardFee | Unset = UNSET
    content_type: str | Unset = UNSET
    content_id: str | Unset = UNSET
    trace: SearchAffiliateOrdersByCreatorResponseDataOrderSkuTrace | Unset = UNSET
    estimated_commission: EstimatedCommission | Unset = UNSET
    actual_bonus_commission: ActualBonusCommission | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        product_id = self.product_id

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        quantity = self.quantity

        commission_rate = self.commission_rate

        estimated_commission_base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_commission_base, Unset):
            estimated_commission_base = self.estimated_commission_base.to_dict()

        actual_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_commission, Unset):
            actual_commission = self.actual_commission.to_dict()

        shop_ads_commission_rate = self.shop_ads_commission_rate

        commission_bonus_rate = self.commission_bonus_rate

        product_name = self.product_name

        shop_name = self.shop_name

        returned_quantity = self.returned_quantity

        refunded_quantity = self.refunded_quantity

        campaign_id = self.campaign_id

        actual_commission_base: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_commission_base, Unset):
            actual_commission_base = self.actual_commission_base.to_dict()

        actual_shop_ads_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_shop_ads_commission, Unset):
            actual_shop_ads_commission = self.actual_shop_ads_commission.to_dict()

        estimated_shop_ads_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_shop_ads_commission, Unset):
            estimated_shop_ads_commission = self.estimated_shop_ads_commission.to_dict()

        estimated_bonus_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_bonus_commission, Unset):
            estimated_bonus_commission = self.estimated_bonus_commission.to_dict()

        delivery_time = self.delivery_time

        creator_commission_reward_rate = self.creator_commission_reward_rate

        estimated_creator_commission_reward_fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_creator_commission_reward_fee, Unset):
            estimated_creator_commission_reward_fee = self.estimated_creator_commission_reward_fee.to_dict()

        actual_creator_commission_reward_fee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_creator_commission_reward_fee, Unset):
            actual_creator_commission_reward_fee = self.actual_creator_commission_reward_fee.to_dict()

        content_type = self.content_type

        content_id = self.content_id

        trace: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trace, Unset):
            trace = self.trace.to_dict()

        estimated_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.estimated_commission, Unset):
            estimated_commission = self.estimated_commission.to_dict()

        actual_bonus_commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actual_bonus_commission, Unset):
            actual_bonus_commission = self.actual_bonus_commission.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if price is not UNSET:
            field_dict["price"] = price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if commission_rate is not UNSET:
            field_dict["commission_rate"] = commission_rate
        if estimated_commission_base is not UNSET:
            field_dict["estimated_commission_base"] = estimated_commission_base
        if actual_commission is not UNSET:
            field_dict["actual_commission"] = actual_commission
        if shop_ads_commission_rate is not UNSET:
            field_dict["shop_ads_commission_rate"] = shop_ads_commission_rate
        if commission_bonus_rate is not UNSET:
            field_dict["commission_bonus_rate"] = commission_bonus_rate
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if shop_name is not UNSET:
            field_dict["shop_name"] = shop_name
        if returned_quantity is not UNSET:
            field_dict["returned_quantity"] = returned_quantity
        if refunded_quantity is not UNSET:
            field_dict["refunded_quantity"] = refunded_quantity
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if actual_commission_base is not UNSET:
            field_dict["actual_commission_base"] = actual_commission_base
        if actual_shop_ads_commission is not UNSET:
            field_dict["actual_shop_ads_commission"] = actual_shop_ads_commission
        if estimated_shop_ads_commission is not UNSET:
            field_dict["estimated_shop_ads_commission"] = estimated_shop_ads_commission
        if estimated_bonus_commission is not UNSET:
            field_dict["estimated_bonus_commission"] = estimated_bonus_commission
        if delivery_time is not UNSET:
            field_dict["delivery_time"] = delivery_time
        if creator_commission_reward_rate is not UNSET:
            field_dict["creator_commission_reward_rate"] = creator_commission_reward_rate
        if estimated_creator_commission_reward_fee is not UNSET:
            field_dict["estimated_creator_commission_reward_fee"] = estimated_creator_commission_reward_fee
        if actual_creator_commission_reward_fee is not UNSET:
            field_dict["actual_creator_commission_reward_fee"] = actual_creator_commission_reward_fee
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if content_id is not UNSET:
            field_dict["content_id"] = content_id
        if trace is not UNSET:
            field_dict["trace"] = trace
        if estimated_commission is not UNSET:
            field_dict["estimated_commission"] = estimated_commission
        if actual_bonus_commission is not UNSET:
            field_dict["actual_bonus_commission"] = actual_bonus_commission

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.actual_bonus_commission import ActualBonusCommission  # noqa: PLC0415
        from ..models.actual_commission import ActualCommission  # noqa: PLC0415
        from ..models.actual_commission_base import ActualCommissionBase  # noqa: PLC0415
        from ..models.actual_creator_commission_reward_fee import ActualCreatorCommissionRewardFee  # noqa: PLC0415
        from ..models.actual_shop_ads_commission import ActualShopAdsCommission  # noqa: PLC0415
        from ..models.estimated_bonus_commission import EstimatedBonusCommission  # noqa: PLC0415
        from ..models.estimated_commission import EstimatedCommission  # noqa: PLC0415
        from ..models.estimated_commission_base import EstimatedCommissionBase  # noqa: PLC0415
        from ..models.estimated_creator_commission_reward_fee import (
            EstimatedCreatorCommissionRewardFee,  # noqa: PLC0415
        )
        from ..models.estimated_shop_ads_commission import EstimatedShopAdsCommission  # noqa: PLC0415
        from ..models.price import Price  # noqa: PLC0415
        from ..models.search_affiliate_orders_by_creator_response_data_order_sku_trace import (
            SearchAffiliateOrdersByCreatorResponseDataOrderSkuTrace,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        product_id = d.pop("product_id", UNSET)

        _price = d.pop("price", UNSET)
        price: Price | Unset
        if isinstance(_price, Unset):
            price = UNSET
        else:
            price = Price.from_dict(_price)

        quantity = d.pop("quantity", UNSET)

        commission_rate = d.pop("commission_rate", UNSET)

        _estimated_commission_base = d.pop("estimated_commission_base", UNSET)
        estimated_commission_base: EstimatedCommissionBase | Unset
        if isinstance(_estimated_commission_base, Unset):
            estimated_commission_base = UNSET
        else:
            estimated_commission_base = EstimatedCommissionBase.from_dict(_estimated_commission_base)

        _actual_commission = d.pop("actual_commission", UNSET)
        actual_commission: ActualCommission | Unset
        if isinstance(_actual_commission, Unset):
            actual_commission = UNSET
        else:
            actual_commission = ActualCommission.from_dict(_actual_commission)

        shop_ads_commission_rate = d.pop("shop_ads_commission_rate", UNSET)

        commission_bonus_rate = d.pop("commission_bonus_rate", UNSET)

        product_name = d.pop("product_name", UNSET)

        shop_name = d.pop("shop_name", UNSET)

        returned_quantity = d.pop("returned_quantity", UNSET)

        refunded_quantity = d.pop("refunded_quantity", UNSET)

        campaign_id = d.pop("campaign_id", UNSET)

        _actual_commission_base = d.pop("actual_commission_base", UNSET)
        actual_commission_base: ActualCommissionBase | Unset
        if isinstance(_actual_commission_base, Unset):
            actual_commission_base = UNSET
        else:
            actual_commission_base = ActualCommissionBase.from_dict(_actual_commission_base)

        _actual_shop_ads_commission = d.pop("actual_shop_ads_commission", UNSET)
        actual_shop_ads_commission: ActualShopAdsCommission | Unset
        if isinstance(_actual_shop_ads_commission, Unset):
            actual_shop_ads_commission = UNSET
        else:
            actual_shop_ads_commission = ActualShopAdsCommission.from_dict(_actual_shop_ads_commission)

        _estimated_shop_ads_commission = d.pop("estimated_shop_ads_commission", UNSET)
        estimated_shop_ads_commission: EstimatedShopAdsCommission | Unset
        if isinstance(_estimated_shop_ads_commission, Unset):
            estimated_shop_ads_commission = UNSET
        else:
            estimated_shop_ads_commission = EstimatedShopAdsCommission.from_dict(_estimated_shop_ads_commission)

        _estimated_bonus_commission = d.pop("estimated_bonus_commission", UNSET)
        estimated_bonus_commission: EstimatedBonusCommission | Unset
        if isinstance(_estimated_bonus_commission, Unset):
            estimated_bonus_commission = UNSET
        else:
            estimated_bonus_commission = EstimatedBonusCommission.from_dict(_estimated_bonus_commission)

        delivery_time = d.pop("delivery_time", UNSET)

        creator_commission_reward_rate = d.pop("creator_commission_reward_rate", UNSET)

        _estimated_creator_commission_reward_fee = d.pop("estimated_creator_commission_reward_fee", UNSET)
        estimated_creator_commission_reward_fee: EstimatedCreatorCommissionRewardFee | Unset
        if isinstance(_estimated_creator_commission_reward_fee, Unset):
            estimated_creator_commission_reward_fee = UNSET
        else:
            estimated_creator_commission_reward_fee = EstimatedCreatorCommissionRewardFee.from_dict(
                _estimated_creator_commission_reward_fee
            )

        _actual_creator_commission_reward_fee = d.pop("actual_creator_commission_reward_fee", UNSET)
        actual_creator_commission_reward_fee: ActualCreatorCommissionRewardFee | Unset
        if isinstance(_actual_creator_commission_reward_fee, Unset):
            actual_creator_commission_reward_fee = UNSET
        else:
            actual_creator_commission_reward_fee = ActualCreatorCommissionRewardFee.from_dict(
                _actual_creator_commission_reward_fee
            )

        content_type = d.pop("content_type", UNSET)

        content_id = d.pop("content_id", UNSET)

        _trace = d.pop("trace", UNSET)
        trace: SearchAffiliateOrdersByCreatorResponseDataOrderSkuTrace | Unset
        if isinstance(_trace, Unset):
            trace = UNSET
        else:
            trace = SearchAffiliateOrdersByCreatorResponseDataOrderSkuTrace.from_dict(_trace)

        _estimated_commission = d.pop("estimated_commission", UNSET)
        estimated_commission: EstimatedCommission | Unset
        if isinstance(_estimated_commission, Unset):
            estimated_commission = UNSET
        else:
            estimated_commission = EstimatedCommission.from_dict(_estimated_commission)

        _actual_bonus_commission = d.pop("actual_bonus_commission", UNSET)
        actual_bonus_commission: ActualBonusCommission | Unset
        if isinstance(_actual_bonus_commission, Unset):
            actual_bonus_commission = UNSET
        else:
            actual_bonus_commission = ActualBonusCommission.from_dict(_actual_bonus_commission)

        search_affiliate_orders_by_creator_response_data_order_sku = cls(
            id=id,
            product_id=product_id,
            price=price,
            quantity=quantity,
            commission_rate=commission_rate,
            estimated_commission_base=estimated_commission_base,
            actual_commission=actual_commission,
            shop_ads_commission_rate=shop_ads_commission_rate,
            commission_bonus_rate=commission_bonus_rate,
            product_name=product_name,
            shop_name=shop_name,
            returned_quantity=returned_quantity,
            refunded_quantity=refunded_quantity,
            campaign_id=campaign_id,
            actual_commission_base=actual_commission_base,
            actual_shop_ads_commission=actual_shop_ads_commission,
            estimated_shop_ads_commission=estimated_shop_ads_commission,
            estimated_bonus_commission=estimated_bonus_commission,
            delivery_time=delivery_time,
            creator_commission_reward_rate=creator_commission_reward_rate,
            estimated_creator_commission_reward_fee=estimated_creator_commission_reward_fee,
            actual_creator_commission_reward_fee=actual_creator_commission_reward_fee,
            content_type=content_type,
            content_id=content_id,
            trace=trace,
            estimated_commission=estimated_commission,
            actual_bonus_commission=actual_bonus_commission,
        )

        search_affiliate_orders_by_creator_response_data_order_sku.additional_properties = d
        return search_affiliate_orders_by_creator_response_data_order_sku

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
