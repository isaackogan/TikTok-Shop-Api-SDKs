from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_coupon_response_data_coupon_product_scope import GetCouponResponseDataCouponProductScope
from ..models.get_coupon_response_data_coupon_target_buyer_segment import GetCouponResponseDataCouponTargetBuyerSegment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.claim_duration import ClaimDuration
    from ..models.get_coupon_response_data_coupon_discount import GetCouponResponseDataCouponDiscount
    from ..models.get_coupon_response_data_coupon_live_task import GetCouponResponseDataCouponLiveTask
    from ..models.get_coupon_response_data_coupon_threshold import GetCouponResponseDataCouponThreshold
    from ..models.get_coupon_response_data_coupon_usage_stat import GetCouponResponseDataCouponUsageStat
    from ..models.redemption_duration import RedemptionDuration
    from ..models.usage_limit import UsageLimit


T = TypeVar("T", bound="GetCouponResponseDataCoupon")


@_attrs_define
class GetCouponResponseDataCoupon:
    """
    Attributes:
        id (str | Unset): A unique ID that identifies different coupons.
        title (str | Unset): Seller-specified title of the coupon.
        display_type (str | Unset): The display type of coupons.
            Values:
            - `REGULAR`: Regular coupons which are displayed to TikTok users across all display locations available in TTS,
            including PLPs, PDPs, TikTok Videos, LIVE Rooms, Creator Showcases, and may be shared via TTS Customer Support
            instant messages. Includes coupons which target select customer segments.
            - `LIVE`: Coupons which are only displayed to TikTok users in LIVE Rooms.
            - `CREATOR_EXCLUSIVE`: Coupons that can be claimed through the display channels of the specified creator, such
            as their LIVE Rooms, and their Creator Showcase.
            - `CHAT`: Exclusive coupons that may be sent to customers via TTS customer support chat messages, but are not
            displayed in other display locations.
            - `PROMO_CODE`: Promo codes do not have dedicated display locations on TikTok, but may be shared with customers
            in LIVEs, in TikTok videos, or other social media platforms. They can be claimed by customers entering a claim
            code at checkout or by customers that use a custom promo code landing page URL.
        status (str | Unset): Coupon's promotion status.
            Values:
            - `NOT_START`: Not available to TikTok users until the coupon's configured start time.
            - `ONGOING`: Available to TikTok users.
            - `EXPIRED`: Not available to TikTok users because it has expired.
            - `DEACTIVATED`: Deactivated by the seller and is not available to TikTok users.
        create_time (int | Unset): The UNIX timestamp, in milliseconds, when the coupon was created.
        update_time (int | Unset): The UNIX timestamp, in milliseconds, when the coupon was last updated.
        claim_duration (ClaimDuration | Unset):
        redemption_duration (RedemptionDuration | Unset):
        display_channels (list[str] | Unset): The channels in which the coupons can be displayed or distributed:
            - `ALL`: All channels.
            - `SHOPPING_CENTER`: Only in TikTok Shop shopping center.
            - `CHAT`: Only in TT chat.
            - `LIVE`: Only in TT live.
            - `PRIVATE`: For promotion code. TikTok users won't know the codes until you show them.
            - `PRIVATE_WITH_ALLOW`: A private display-channel value returned for a regular coupon.
            - `VIDEO`: Only in short videos.
            - `SHOWCASE`: Only in showcases.
        promo_code (str | Unset): Promotion code. Returned only when `display_type == 'PROMO_CODE'`. The string contains
            only Unicode letters or digits. The length of the string is in the range of `[6, 12]`.
        target_buyer_segment (GetCouponResponseDataCouponTargetBuyerSegment | Unset): The target buyer segment of the
            coupon. Possible enumerations are:
            - `ALL`: May be discovered and claimed by all TTS buyers.
            - `NEW`:Customers who have never purchased from your shop.
            - `REPEAT_CUSTOMERS`: People who have previously placed orders in your shop and made another purchase within
            certain days(30 days for non-US and 90 days for US).
            - `RECENT_CUSTOMERS`: People who have made their first purchase in your shop in the past certain days(30 days
            for non-US and 90 days for US).
            - `FREQUENT_CUSTOMERS`: Customers with more than 1 purchase within the last 90 days.
            - `LAPSED_CUSTOMERS`: Customers with at least 1 purchase in the past 365 days but no purchases within the last
            certain days(90 days for non-US and 30 days for US).
            - `NEW_FOLLOWERS`: People who started following the TikTok account of your shop in the past 30 days.
            - `EXISTING_ACTIVE_FOLLOWERS`: People who followed the TikTok account of your shop and engaged with your shop
            through LIVE, short videos or product cards in the past 30 days.
        usage_limits (UsageLimit | Unset):
        usage_stats (GetCouponResponseDataCouponUsageStat | Unset):
        discount (GetCouponResponseDataCouponDiscount | Unset):
        threshold (GetCouponResponseDataCouponThreshold | Unset):
        product_scope (GetCouponResponseDataCouponProductScope | Unset): The range of the products which the coupon
            applies to. The possible enumerations are:
            - `FULL_SHOP`: All products sold in the shop are eligible for the coupon.
            - `SPECIFIC_PRODUCTS`: Only specified products are eligible for the coupon. The list of specified products are
            returned in the response of the `get_coupon` API.
        product_ids (list[str] | Unset): The IDs of the eligible products when `product_scope == 'SPECIFIC_PRODUCTS'`.
        seller_tnc (str | Unset): Custom terms & conditions optionally uploaded by the seller when configuring the
            coupon.
        creation_source (str | Unset): The system where the coupon is created:
            - `SELLER_CENTER`: Created via the Promotions section of TikTok Seller Center.
            - `SELLER_APP`: Created via the TikTok Seller Mobile App.
            - `TTS_CRM`: Created via the TikTok Shop CRM.
        live_tasks (list[GetCouponResponseDataCouponLiveTask] | Unset): The tasks which the shopper must fulfill before
            claiming the coupon distributed in TikTok live. Only exists for LIVE coupons in the US and the UK.
    """

    id: str | Unset = UNSET
    title: str | Unset = UNSET
    display_type: str | Unset = UNSET
    status: str | Unset = UNSET
    create_time: int | Unset = UNSET
    update_time: int | Unset = UNSET
    claim_duration: ClaimDuration | Unset = UNSET
    redemption_duration: RedemptionDuration | Unset = UNSET
    display_channels: list[str] | Unset = UNSET
    promo_code: str | Unset = UNSET
    target_buyer_segment: GetCouponResponseDataCouponTargetBuyerSegment | Unset = UNSET
    usage_limits: UsageLimit | Unset = UNSET
    usage_stats: GetCouponResponseDataCouponUsageStat | Unset = UNSET
    discount: GetCouponResponseDataCouponDiscount | Unset = UNSET
    threshold: GetCouponResponseDataCouponThreshold | Unset = UNSET
    product_scope: GetCouponResponseDataCouponProductScope | Unset = UNSET
    product_ids: list[str] | Unset = UNSET
    seller_tnc: str | Unset = UNSET
    creation_source: str | Unset = UNSET
    live_tasks: list[GetCouponResponseDataCouponLiveTask] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        display_type = self.display_type

        status = self.status

        create_time = self.create_time

        update_time = self.update_time

        claim_duration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.claim_duration, Unset):
            claim_duration = self.claim_duration.to_dict()

        redemption_duration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.redemption_duration, Unset):
            redemption_duration = self.redemption_duration.to_dict()

        display_channels: list[str] | Unset = UNSET
        if not isinstance(self.display_channels, Unset):
            display_channels = self.display_channels

        promo_code = self.promo_code

        target_buyer_segment: str | Unset = UNSET
        if not isinstance(self.target_buyer_segment, Unset):
            target_buyer_segment = self.target_buyer_segment.value

        usage_limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage_limits, Unset):
            usage_limits = self.usage_limits.to_dict()

        usage_stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usage_stats, Unset):
            usage_stats = self.usage_stats.to_dict()

        discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        threshold: dict[str, Any] | Unset = UNSET
        if not isinstance(self.threshold, Unset):
            threshold = self.threshold.to_dict()

        product_scope: str | Unset = UNSET
        if not isinstance(self.product_scope, Unset):
            product_scope = self.product_scope.value

        product_ids: list[str] | Unset = UNSET
        if not isinstance(self.product_ids, Unset):
            product_ids = self.product_ids

        seller_tnc = self.seller_tnc

        creation_source = self.creation_source

        live_tasks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.live_tasks, Unset):
            live_tasks = []
            for live_tasks_item_data in self.live_tasks:
                live_tasks_item = live_tasks_item_data.to_dict()
                live_tasks.append(live_tasks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if display_type is not UNSET:
            field_dict["display_type"] = display_type
        if status is not UNSET:
            field_dict["status"] = status
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if claim_duration is not UNSET:
            field_dict["claim_duration"] = claim_duration
        if redemption_duration is not UNSET:
            field_dict["redemption_duration"] = redemption_duration
        if display_channels is not UNSET:
            field_dict["display_channels"] = display_channels
        if promo_code is not UNSET:
            field_dict["promo_code"] = promo_code
        if target_buyer_segment is not UNSET:
            field_dict["target_buyer_segment"] = target_buyer_segment
        if usage_limits is not UNSET:
            field_dict["usage_limits"] = usage_limits
        if usage_stats is not UNSET:
            field_dict["usage_stats"] = usage_stats
        if discount is not UNSET:
            field_dict["discount"] = discount
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if product_scope is not UNSET:
            field_dict["product_scope"] = product_scope
        if product_ids is not UNSET:
            field_dict["product_ids"] = product_ids
        if seller_tnc is not UNSET:
            field_dict["seller_tnc"] = seller_tnc
        if creation_source is not UNSET:
            field_dict["creation_source"] = creation_source
        if live_tasks is not UNSET:
            field_dict["live_tasks"] = live_tasks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_duration import ClaimDuration  # noqa: PLC0415
        from ..models.get_coupon_response_data_coupon_discount import (
            GetCouponResponseDataCouponDiscount,  # noqa: PLC0415
        )
        from ..models.get_coupon_response_data_coupon_live_task import (
            GetCouponResponseDataCouponLiveTask,  # noqa: PLC0415
        )
        from ..models.get_coupon_response_data_coupon_threshold import (
            GetCouponResponseDataCouponThreshold,  # noqa: PLC0415
        )
        from ..models.get_coupon_response_data_coupon_usage_stat import (
            GetCouponResponseDataCouponUsageStat,  # noqa: PLC0415
        )
        from ..models.redemption_duration import RedemptionDuration  # noqa: PLC0415
        from ..models.usage_limit import UsageLimit  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        display_type = d.pop("display_type", UNSET)

        status = d.pop("status", UNSET)

        create_time = d.pop("create_time", UNSET)

        update_time = d.pop("update_time", UNSET)

        _claim_duration = d.pop("claim_duration", UNSET)
        claim_duration: ClaimDuration | Unset
        if isinstance(_claim_duration, Unset):
            claim_duration = UNSET
        else:
            claim_duration = ClaimDuration.from_dict(_claim_duration)

        _redemption_duration = d.pop("redemption_duration", UNSET)
        redemption_duration: RedemptionDuration | Unset
        if isinstance(_redemption_duration, Unset):
            redemption_duration = UNSET
        else:
            redemption_duration = RedemptionDuration.from_dict(_redemption_duration)

        display_channels = cast(list[str], d.pop("display_channels", UNSET))

        promo_code = d.pop("promo_code", UNSET)

        _target_buyer_segment = d.pop("target_buyer_segment", UNSET)
        target_buyer_segment: GetCouponResponseDataCouponTargetBuyerSegment | Unset
        if isinstance(_target_buyer_segment, Unset):
            target_buyer_segment = UNSET
        else:
            target_buyer_segment = GetCouponResponseDataCouponTargetBuyerSegment(_target_buyer_segment)

        _usage_limits = d.pop("usage_limits", UNSET)
        usage_limits: UsageLimit | Unset
        if isinstance(_usage_limits, Unset):
            usage_limits = UNSET
        else:
            usage_limits = UsageLimit.from_dict(_usage_limits)

        _usage_stats = d.pop("usage_stats", UNSET)
        usage_stats: GetCouponResponseDataCouponUsageStat | Unset
        if isinstance(_usage_stats, Unset):
            usage_stats = UNSET
        else:
            usage_stats = GetCouponResponseDataCouponUsageStat.from_dict(_usage_stats)

        _discount = d.pop("discount", UNSET)
        discount: GetCouponResponseDataCouponDiscount | Unset
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = GetCouponResponseDataCouponDiscount.from_dict(_discount)

        _threshold = d.pop("threshold", UNSET)
        threshold: GetCouponResponseDataCouponThreshold | Unset
        if isinstance(_threshold, Unset):
            threshold = UNSET
        else:
            threshold = GetCouponResponseDataCouponThreshold.from_dict(_threshold)

        _product_scope = d.pop("product_scope", UNSET)
        product_scope: GetCouponResponseDataCouponProductScope | Unset
        if isinstance(_product_scope, Unset):
            product_scope = UNSET
        else:
            product_scope = GetCouponResponseDataCouponProductScope(_product_scope)

        product_ids = cast(list[str], d.pop("product_ids", UNSET))

        seller_tnc = d.pop("seller_tnc", UNSET)

        creation_source = d.pop("creation_source", UNSET)

        _live_tasks = d.pop("live_tasks", UNSET)
        live_tasks: list[GetCouponResponseDataCouponLiveTask] | Unset = UNSET
        if _live_tasks is not UNSET:
            live_tasks = []
            for live_tasks_item_data in _live_tasks:
                live_tasks_item = GetCouponResponseDataCouponLiveTask.from_dict(live_tasks_item_data)

                live_tasks.append(live_tasks_item)

        get_coupon_response_data_coupon = cls(
            id=id,
            title=title,
            display_type=display_type,
            status=status,
            create_time=create_time,
            update_time=update_time,
            claim_duration=claim_duration,
            redemption_duration=redemption_duration,
            display_channels=display_channels,
            promo_code=promo_code,
            target_buyer_segment=target_buyer_segment,
            usage_limits=usage_limits,
            usage_stats=usage_stats,
            discount=discount,
            threshold=threshold,
            product_scope=product_scope,
            product_ids=product_ids,
            seller_tnc=seller_tnc,
            creation_source=creation_source,
            live_tasks=live_tasks,
        )

        get_coupon_response_data_coupon.additional_properties = d
        return get_coupon_response_data_coupon

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
