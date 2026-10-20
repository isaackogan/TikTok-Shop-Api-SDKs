from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_promotion_activity_request_auction_support_type import UpdatePromotionActivityRequestAuctionSupportType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.discount import Discount
  from ..models.update_promotion_activity_request_participation_limit import UpdatePromotionActivityRequestParticipationLimit
  from ..models.update_promotion_activity_request_target_user_info import UpdatePromotionActivityRequestTargetUserInfo





T = TypeVar("T", bound="UpdatePromotionActivityRequest")



@_attrs_define
class UpdatePromotionActivityRequest:
    """ 
        Attributes:
            title (str): Activity name. The name must be unique. Maximum length: 50 Unicode characters for a flash-sale
                activity; 50 characters for a shipping-discount activity; 100 Unicode characters for a fixed-price, direct-
                discount, BMSM, BXGY, or GWP activity.
            begin_time (int): Activity start time as a Unix timestamp in seconds. For an INDEFINITE shipping-discount
                activity, set this field to 0. For a fixed-price, direct-discount, flash-sale, BMSM, BXGY, or GWP activity with
                a normal schedule, use a future time when the activity is upcoming; if it is ongoing, use its existing start
                time because that value cannot be changed.
            end_time (int): Activity end time as a Unix timestamp in seconds. For an INDEFINITE shipping-discount activity,
                set this field to 0. For a normal-schedule fixed-price, direct-discount, flash-sale, BMSM, BXGY, or GWP update,
                end_time must be at least 600 seconds after begin_time.
            duration_type (str | Unset): The activity schedule mode.
                - For BMSM, BXGY, and GWP activities, set this field to `NORMAL` and provide the scheduled `begin_time` and
                `end_time`.
                - For a shipping-discount activity, use `NORMAL` for a scheduled activity or `INDEFINITE` for an activity
                without a scheduled end. When this field is omitted for a shipping-discount update, it defaults to `NORMAL`. For
                `INDEFINITE`, set both `begin_time` and `end_time` to `0`.
                - This field is not processed when updating a fixed-price, direct-discount, or flash-sale activity.
            product_level (str | Unset): The promotion's product scope. You must provide this field when updating a BMSM,
                BXGY, GWP, or shipping-discount activity.
                - PRODUCT: Applies to a product and all of its SKUs. Use this value for GWP; BMSM, BXGY, and shipping-discount
                also support it.
                - VARIATION: Applies only to specified SKUs. It is not supported for BMSM, BXGY, GWP, or shipping-discount
                updates.
                - SHOP: Applies to all products in the shop. It is supported for BMSM, BXGY, and shipping-discount, but not GWP.
                This field is not processed for fixed-price, direct-discount, or flash-sale updates. For an ongoing BMSM or BXGY
                activity, keep its existing PRODUCT or SHOP scope.
            participation_limit (list[UpdatePromotionActivityRequestParticipationLimit] | Unset): The buyer participation
                limit. For BMSM, BXGY, and GWP updates, provide exactly one entry. If a BMSM or BXGY activity is ongoing, keep
                its existing participation limit unchanged.
            discount (Discount | Unset):
            target_user_info (UpdatePromotionActivityRequestTargetUserInfo | Unset):
            auction_support_type (UpdatePromotionActivityRequestAuctionSupportType | Unset): Determines whether a shipping-
                discount activity supports auction products. This field is not processed for other activity types.
                Possible values:
                - `ALL`: Supports both standard and auction products.
                - `EXCLUDE_AUCTION`: Excludes auction products.
                When omitted for a shipping-discount update, defaults to `ALL`.
     """

    title: str
    begin_time: int
    end_time: int
    duration_type: str | Unset = UNSET
    product_level: str | Unset = UNSET
    participation_limit: list[UpdatePromotionActivityRequestParticipationLimit] | Unset = UNSET
    discount: Discount | Unset = UNSET
    target_user_info: UpdatePromotionActivityRequestTargetUserInfo | Unset = UNSET
    auction_support_type: UpdatePromotionActivityRequestAuctionSupportType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.discount import Discount # noqa: PLC0415
        from ..models.update_promotion_activity_request_participation_limit import UpdatePromotionActivityRequestParticipationLimit # noqa: PLC0415
        from ..models.update_promotion_activity_request_target_user_info import UpdatePromotionActivityRequestTargetUserInfo # noqa: PLC0415
        title = self.title

        begin_time = self.begin_time

        end_time = self.end_time

        duration_type = self.duration_type

        product_level = self.product_level

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
            "begin_time": begin_time,
            "end_time": end_time,
        })
        if duration_type is not UNSET:
            field_dict["duration_type"] = duration_type
        if product_level is not UNSET:
            field_dict["product_level"] = product_level
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
        from ..models.discount import Discount # noqa: PLC0415
        from ..models.update_promotion_activity_request_participation_limit import UpdatePromotionActivityRequestParticipationLimit # noqa: PLC0415
        from ..models.update_promotion_activity_request_target_user_info import UpdatePromotionActivityRequestTargetUserInfo # noqa: PLC0415
        d = dict(src_dict)
        title = d.pop("title")

        begin_time = d.pop("begin_time")

        end_time = d.pop("end_time")

        duration_type = d.pop("duration_type", UNSET)

        product_level = d.pop("product_level", UNSET)

        _participation_limit = d.pop("participation_limit", UNSET)
        participation_limit: list[UpdatePromotionActivityRequestParticipationLimit] | Unset = UNSET
        if _participation_limit is not UNSET:
            participation_limit = []
            for participation_limit_item_data in _participation_limit:
                participation_limit_item = UpdatePromotionActivityRequestParticipationLimit.from_dict(participation_limit_item_data)



                participation_limit.append(participation_limit_item)


        _discount = d.pop("discount", UNSET)
        discount: Discount | Unset
        if isinstance(_discount,  Unset):
            discount = UNSET
        else:
            discount = Discount.from_dict(_discount)




        _target_user_info = d.pop("target_user_info", UNSET)
        target_user_info: UpdatePromotionActivityRequestTargetUserInfo | Unset
        if isinstance(_target_user_info,  Unset):
            target_user_info = UNSET
        else:
            target_user_info = UpdatePromotionActivityRequestTargetUserInfo.from_dict(_target_user_info)




        _auction_support_type = d.pop("auction_support_type", UNSET)
        auction_support_type: UpdatePromotionActivityRequestAuctionSupportType | Unset
        if isinstance(_auction_support_type,  Unset):
            auction_support_type = UNSET
        else:
            auction_support_type = UpdatePromotionActivityRequestAuctionSupportType(_auction_support_type)




        update_promotion_activity_request = cls(
            title=title,
            begin_time=begin_time,
            end_time=end_time,
            duration_type=duration_type,
            product_level=product_level,
            participation_limit=participation_limit,
            discount=discount,
            target_user_info=target_user_info,
            auction_support_type=auction_support_type,
        )


        update_promotion_activity_request.additional_properties = d
        return update_promotion_activity_request

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
