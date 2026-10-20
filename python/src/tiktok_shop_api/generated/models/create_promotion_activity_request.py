from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_promotion_activity_request_activity_type import CreatePromotionActivityRequestActivityType
from ..models.create_promotion_activity_request_auction_support_type import CreatePromotionActivityRequestAuctionSupportType
from ..models.create_promotion_activity_request_product_level import CreatePromotionActivityRequestProductLevel
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_promotion_activity_request_participation_limit import CreatePromotionActivityRequestParticipationLimit
  from ..models.create_promotion_activity_request_target_user_info import CreatePromotionActivityRequestTargetUserInfo
  from ..models.discount import Discount





T = TypeVar("T", bound="CreatePromotionActivityRequest")



@_attrs_define
class CreatePromotionActivityRequest:
    """ 
        Attributes:
            title (str): Unique name across all your activities. Maximum length: 50 characters for `FLASHSALE` and
                `SHIPPING_DISCOUNT`; 100 characters for `FIXED_PRICE`, `DIRECT_DISCOUNT`, `BUY_MORE_SAVE_MORE`, `BUY_X_GET_Y`,
                and `GIFT_WITH_PURCHASE`.
            activity_type (CreatePromotionActivityRequestActivityType): The type of promotion activity.
                Possible values:
                - `FIXED_PRICE`: A product discount activity with a fixed price.
                - `DIRECT_DISCOUNT`: A product discount activity with a percentage discount.
                - `FLASHSALE`: A flash sale activity.
                - `SHIPPING_DISCOUNT`: A shipping fee discount activity.
                - `BUY_MORE_SAVE_MORE`: A Buy More Save More promotion.
                - `GIFT_WITH_PURCHASE`: A Gift With Purchase promotion.
                - `BUY_X_GET_Y`: A Buy X Get Y promotion.
            product_level (CreatePromotionActivityRequestProductLevel): The product scope of the activity.
                Possible values:
                - `PRODUCT`: Apply the promotion at the product (SPU) level to all SKUs in each selected product.
                - `VARIATION`: Apply the promotion only to selected SKUs.
                - `SHOP`: Apply the promotion to all products in the shop.

                Activity-specific constraints:
                - `FIXED_PRICE`, `DIRECT_DISCOUNT`, and `FLASHSALE` support `PRODUCT` or `VARIATION`.
                - `SHIPPING_DISCOUNT` does not support `VARIATION`.
                - `BUY_MORE_SAVE_MORE` and `BUY_X_GET_Y` support `PRODUCT` or `SHOP`.
                - `GIFT_WITH_PURCHASE` requires `PRODUCT`.

                To set the products or SKUs covered by the activity, use [Update Activity
                Product](https://partner.tiktokshop.com/docv2/page/650d32c42aaa3602b86ccb5c).
            begin_time (int): Activity start time. UNIX timestamp. The value must be greater than the value of the current
                time.
            end_time (int): Activity end time as a Unix timestamp in seconds. For `NORMAL` `FIXED_PRICE`, `DIRECT_DISCOUNT`,
                `FLASHSALE`, `BUY_MORE_SAVE_MORE`, `BUY_X_GET_Y`, and `GIFT_WITH_PURCHASE` activities, it must be at least 600
                seconds after `begin_time`. For a `NORMAL` shipping-discount activity, provide a positive value.
            duration_type (str | Unset): The effective time type of the current activity
                - NORMAL:  `begin_time` and `end_time` must be filled
                - INDEFINITE: `begin_time` and `end_time` aren't required, and the promotion will be a long-term activity which
                runs indefinitely.
                1.  `INDEFINITE` is only valid when `activity_type` is `SHIPPING_DISCOUNT`,
                2. If `duration_type` is `INDEFINITE`, `start_time` and `end_time` should be 0
                Default: NORMAL
            participation_limit (list[CreatePromotionActivityRequestParticipationLimit] | Unset): Buyer participation-limit
                settings. For `BUY_MORE_SAVE_MORE`, `BUY_X_GET_Y`, and `GIFT_WITH_PURCHASE`, provide exactly one entry.
            discount (Discount | Unset):
            target_user_info (CreatePromotionActivityRequestTargetUserInfo | Unset):
            auction_support_type (CreatePromotionActivityRequestAuctionSupportType | Unset): For `SHIPPING_DISCOUNT`
                activities, determines whether auction products are supported.
                Possible values:
                - `ALL`: Support both regular and auction products.
                - `EXCLUDE_AUCTION`: Exclude auction products.
                Default: `ALL`.
     """

    title: str
    activity_type: CreatePromotionActivityRequestActivityType
    product_level: CreatePromotionActivityRequestProductLevel
    begin_time: int
    end_time: int
    duration_type: str | Unset = UNSET
    participation_limit: list[CreatePromotionActivityRequestParticipationLimit] | Unset = UNSET
    discount: Discount | Unset = UNSET
    target_user_info: CreatePromotionActivityRequestTargetUserInfo | Unset = UNSET
    auction_support_type: CreatePromotionActivityRequestAuctionSupportType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_promotion_activity_request_participation_limit import CreatePromotionActivityRequestParticipationLimit # noqa: PLC0415
        from ..models.create_promotion_activity_request_target_user_info import CreatePromotionActivityRequestTargetUserInfo # noqa: PLC0415
        from ..models.discount import Discount # noqa: PLC0415
        title = self.title

        activity_type = self.activity_type.value

        product_level = self.product_level.value

        begin_time = self.begin_time

        end_time = self.end_time

        duration_type = self.duration_type

        participation_limit: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participation_limit, Unset):
            participation_limit = []
            for participation_limit_item_data in self.participation_limit:
                participation_limit_item = participation_limit_item_data.to_dict()
                participation_limit.append(participation_limit_item)



        discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        target_user_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_user_info, Unset):
            target_user_info = self.target_user_info.to_dict()

        auction_support_type: str | Unset = UNSET
        if not isinstance(self.auction_support_type, Unset):
            auction_support_type = self.auction_support_type.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "title": title,
            "activity_type": activity_type,
            "product_level": product_level,
            "begin_time": begin_time,
            "end_time": end_time,
        })
        if duration_type is not UNSET:
            field_dict["duration_type"] = duration_type
        if participation_limit is not UNSET:
            field_dict["participation_limit"] = participation_limit
        if discount is not UNSET:
            field_dict["discount"] = discount
        if target_user_info is not UNSET:
            field_dict["target_user_info"] = target_user_info
        if auction_support_type is not UNSET:
            field_dict["auction_support_type"] = auction_support_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_promotion_activity_request_participation_limit import CreatePromotionActivityRequestParticipationLimit # noqa: PLC0415
        from ..models.create_promotion_activity_request_target_user_info import CreatePromotionActivityRequestTargetUserInfo # noqa: PLC0415
        from ..models.discount import Discount # noqa: PLC0415
        d = dict(src_dict)
        title = d.pop("title")

        activity_type = CreatePromotionActivityRequestActivityType(d.pop("activity_type"))




        product_level = CreatePromotionActivityRequestProductLevel(d.pop("product_level"))




        begin_time = d.pop("begin_time")

        end_time = d.pop("end_time")

        duration_type = d.pop("duration_type", UNSET)

        _participation_limit = d.pop("participation_limit", UNSET)
        participation_limit: list[CreatePromotionActivityRequestParticipationLimit] | Unset = UNSET
        if _participation_limit is not UNSET:
            participation_limit = []
            for participation_limit_item_data in _participation_limit:
                participation_limit_item = CreatePromotionActivityRequestParticipationLimit.from_dict(participation_limit_item_data)



                participation_limit.append(participation_limit_item)


        _discount = d.pop("discount", UNSET)
        discount: Discount | Unset
        if isinstance(_discount,  Unset):
            discount = UNSET
        else:
            discount = Discount.from_dict(_discount)




        _target_user_info = d.pop("target_user_info", UNSET)
        target_user_info: CreatePromotionActivityRequestTargetUserInfo | Unset
        if isinstance(_target_user_info,  Unset):
            target_user_info = UNSET
        else:
            target_user_info = CreatePromotionActivityRequestTargetUserInfo.from_dict(_target_user_info)




        _auction_support_type = d.pop("auction_support_type", UNSET)
        auction_support_type: CreatePromotionActivityRequestAuctionSupportType | Unset
        if isinstance(_auction_support_type,  Unset):
            auction_support_type = UNSET
        else:
            auction_support_type = CreatePromotionActivityRequestAuctionSupportType(_auction_support_type)




        create_promotion_activity_request = cls(
            title=title,
            activity_type=activity_type,
            product_level=product_level,
            begin_time=begin_time,
            end_time=end_time,
            duration_type=duration_type,
            participation_limit=participation_limit,
            discount=discount,
            target_user_info=target_user_info,
            auction_support_type=auction_support_type,
        )


        create_promotion_activity_request.additional_properties = d
        return create_promotion_activity_request

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
