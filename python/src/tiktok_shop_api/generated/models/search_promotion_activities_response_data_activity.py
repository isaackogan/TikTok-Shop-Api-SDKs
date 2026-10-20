from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_activity_response_data_discount import GetActivityResponseDataDiscount
    from ..models.search_promotion_activities_response_data_activity_participation_limit import (
        SearchPromotionActivitiesResponseDataActivityParticipationLimit,
    )


T = TypeVar("T", bound="SearchPromotionActivitiesResponseDataActivity")


@_attrs_define
class SearchPromotionActivitiesResponseDataActivity:
    """
    Attributes:
        id (str | Unset): A unique ID that identifies different activities.
        title (str | Unset): Activity name (50 characters max).
        activity_type (str | Unset): The type of promotion activity. Possible values:
            - `FIXED_PRICE`: Product discount activity with a fixed price.
            - `DIRECT_DISCOUNT`: Product discount activity with a percentage off.
            - `FLASHSALE`: Flash sale activity.
            - `SHIPPING_DISCOUNT`: Shipping fee discount activity.
            - `BUY_MORE_SAVE_MORE`: Buy More Save More activity.
            - `GIFT_WITH_PURCHASE`: Gift With Purchase activity.
            - `BUY_X_GET_Y`: Buy X Get Y activity.
        duration_type (str | Unset): The effective time type of the current activity
            - NORMAL:  `begin_time` and `end_time` must be filled
            - INDEFINITE: `begin_time` and `end_time` aren't required, and the promotion will be a long-term activity which
            runs indefinitely.
            1.  `INDEFINITE` is only valid when `activity_type` is `SHIPPING_DISCOUNT`,
            2. If `duration_type` is `INDEFINITE`, `start_time` and `end_time` should be 0
            Default: NORMAL
        begin_time (int | Unset): Activity start time, as a Unix timestamp in seconds.
        end_time (int | Unset): Activity end time, as a Unix timestamp in seconds.
        status (str | Unset): Activity status.
            Possible values:
            - DRAFT: Promotion activities with this status are not available to TikTok users.
            - NOT_START: Promotion activities with this status are not available to TikTok users until the set activity
            start time.
            - ONGOING: Promotion activities with this status are available to TikTok users.
            - EXPIRED: Promotion activities with this status are not available to TikTok users because it has expired.
            - DEACTIVATED: The activity has been deactivated by the seller and is not available to TikTok users.
            - NOT_EFFECTIVE:  The activity is terminated by the platform and is not available to TikTok users.
        create_time (int | Unset): The time when the activity was created, as a Unix timestamp in milliseconds.
        update_time (int | Unset): The time when the activity was last updated, as a Unix timestamp in milliseconds.
        product_level (str | Unset): Activity product dimension, values are:
            ​- PRODUCT: Promotion activity applies at the product (SPU) level. Any and all SKUs that are part of this
            product will be subject to the promotion.
            ​- VARIATION: Promotion activity only applies to specified SKUs.
            ​- SHOP: Promotion activity applies to all products in the shop.
        activity_commands (list[str] | Unset): Applicable commands to the activity:
            - IMMUTABLE: The activity cannot be edited or deactivated.
        participation_limit (list[SearchPromotionActivitiesResponseDataActivityParticipationLimit] | Unset): The number
            of times a buyer can participate in the promotion.
        discount (GetActivityResponseDataDiscount | Unset):
        auction_support_type (str | Unset): Whether a `SHIPPING_DISCOUNT` activity supports auction products. This field
            is omitted for other activity types and can be omitted when auction-support data is unavailable.
            Possible values:
            - `ALL`: The activity supports both normal products and auction products.
            - `EXCLUDE_AUCTION`: The activity does not support auction products.
    """

    id: str | Unset = UNSET
    title: str | Unset = UNSET
    activity_type: str | Unset = UNSET
    duration_type: str | Unset = UNSET
    begin_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    status: str | Unset = UNSET
    create_time: int | Unset = UNSET
    update_time: int | Unset = UNSET
    product_level: str | Unset = UNSET
    activity_commands: list[str] | Unset = UNSET
    participation_limit: list[SearchPromotionActivitiesResponseDataActivityParticipationLimit] | Unset = UNSET
    discount: GetActivityResponseDataDiscount | Unset = UNSET
    auction_support_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        activity_type = self.activity_type

        duration_type = self.duration_type

        begin_time = self.begin_time

        end_time = self.end_time

        status = self.status

        create_time = self.create_time

        update_time = self.update_time

        product_level = self.product_level

        activity_commands: list[str] | Unset = UNSET
        if not isinstance(self.activity_commands, Unset):
            activity_commands = self.activity_commands

        participation_limit: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participation_limit, Unset):
            participation_limit = []
            for participation_limit_item_data in self.participation_limit:
                participation_limit_item = participation_limit_item_data.to_dict()
                participation_limit.append(participation_limit_item)

        discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        auction_support_type = self.auction_support_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if activity_type is not UNSET:
            field_dict["activity_type"] = activity_type
        if duration_type is not UNSET:
            field_dict["duration_type"] = duration_type
        if begin_time is not UNSET:
            field_dict["begin_time"] = begin_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if status is not UNSET:
            field_dict["status"] = status
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if product_level is not UNSET:
            field_dict["product_level"] = product_level
        if activity_commands is not UNSET:
            field_dict["activity_commands"] = activity_commands
        if participation_limit is not UNSET:
            field_dict["participation_limit"] = participation_limit
        if discount is not UNSET:
            field_dict["discount"] = discount
        if auction_support_type is not UNSET:
            field_dict["auction_support_type"] = auction_support_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_activity_response_data_discount import GetActivityResponseDataDiscount  # noqa: PLC0415
        from ..models.search_promotion_activities_response_data_activity_participation_limit import (
            SearchPromotionActivitiesResponseDataActivityParticipationLimit,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        activity_type = d.pop("activity_type", UNSET)

        duration_type = d.pop("duration_type", UNSET)

        begin_time = d.pop("begin_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        status = d.pop("status", UNSET)

        create_time = d.pop("create_time", UNSET)

        update_time = d.pop("update_time", UNSET)

        product_level = d.pop("product_level", UNSET)

        activity_commands = cast(list[str], d.pop("activity_commands", UNSET))

        _participation_limit = d.pop("participation_limit", UNSET)
        participation_limit: list[SearchPromotionActivitiesResponseDataActivityParticipationLimit] | Unset = UNSET
        if _participation_limit is not UNSET:
            participation_limit = []
            for participation_limit_item_data in _participation_limit:
                participation_limit_item = SearchPromotionActivitiesResponseDataActivityParticipationLimit.from_dict(
                    participation_limit_item_data
                )

                participation_limit.append(participation_limit_item)

        _discount = d.pop("discount", UNSET)
        discount: GetActivityResponseDataDiscount | Unset
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = GetActivityResponseDataDiscount.from_dict(_discount)

        auction_support_type = d.pop("auction_support_type", UNSET)

        search_promotion_activities_response_data_activity = cls(
            id=id,
            title=title,
            activity_type=activity_type,
            duration_type=duration_type,
            begin_time=begin_time,
            end_time=end_time,
            status=status,
            create_time=create_time,
            update_time=update_time,
            product_level=product_level,
            activity_commands=activity_commands,
            participation_limit=participation_limit,
            discount=discount,
            auction_support_type=auction_support_type,
        )

        search_promotion_activities_response_data_activity.additional_properties = d
        return search_promotion_activities_response_data_activity

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
