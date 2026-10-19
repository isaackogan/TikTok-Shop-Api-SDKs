from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_activity_response_data_activity_type import GetActivityResponseDataActivityType
from ..models.get_activity_response_data_auction_support_type import GetActivityResponseDataAuctionSupportType
from ..models.get_activity_response_data_product_level import GetActivityResponseDataProductLevel
from ..models.get_activity_response_data_status import GetActivityResponseDataStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_activity_response_data_benefit_product import GetActivityResponseDataBenefitProduct
    from ..models.get_activity_response_data_discount import GetActivityResponseDataDiscount
    from ..models.get_activity_response_data_participation_limit import GetActivityResponseDataParticipationLimit
    from ..models.get_activity_response_data_product import GetActivityResponseDataProduct
    from ..models.get_activity_response_data_target_user_info import GetActivityResponseDataTargetUserInfo


T = TypeVar("T", bound="GetActivityResponseData")


@_attrs_define
class GetActivityResponseData:
    """
    Attributes:
        activity_id (str | Unset): A unique ID that identifies different activities.
        title (str | Unset): Activity name (50 characters max.) The name must be unique.
        activity_type (GetActivityResponseDataActivityType | Unset): The activity type.
            Possible values:
            - `FIXED_PRICE`: A product discount activity with a fixed price.
            - `DIRECT_DISCOUNT`: A product discount activity with a percentage discount.
            - `FLASHSALE`: A flash sale activity.
            - `SHIPPING_DISCOUNT`: A shipping fee discount activity.
            - `BUY_MORE_SAVE_MORE`: A Buy More Save More promotion.
            - `GIFT_WITH_PURCHASE`: A Gift With Purchase promotion.
            - `BUY_X_GET_Y`: A Buy X Get Y promotion.
        duration_type (str | Unset): The effective time type of the current activity
            - NORMAL:  `begin_time` and `end_time` must be filled
            - INDEFINITE: `begin_time` and `end_time` aren't required, and the promotion will be a long-term activity which
            runs indefinitely.
            1.  `INDEFINITE` is only valid when `activity_type` is `SHIPPING_DISCOUNT`,
            2. If `duration_type` is `INDEFINITE`, `start_time` and `end_time` should be 0
            Default: NORMAL
        begin_time (int | Unset): Activity start time as a UNIX timestamp in seconds.
        end_time (int | Unset): Activity end time as a UNIX timestamp in seconds.
        participation_limit (list[GetActivityResponseDataParticipationLimit] | Unset): The number of times a buyer can
            participate in the promotion.
        products (list[GetActivityResponseDataProduct] | Unset): Product List.
            Note:If  `FIXED_PRICE`, `DIRECT_DISCOUNT` and `FLASHSALE` activity that ended more than 180 days,this field is
            empty.
        status (GetActivityResponseDataStatus | Unset): Activity status.
            Possible values:
            - DRAFT: Promotion activities with this status are not available to TikTok users.
            - NOT_START: Promotion activities with this status are not available to TikTok users until the set activity
            start time.
            - ONGOING: Promotion activities with this status are available to TikTok users.
            - EXPIRED: Promotion activities with this status are not available to TikTok users because it has expired.
            - DEACTIVATED: The activity has been deactivated by the seller and is not available to TikTok users.
            - NOT_EFFECTIVE:  The activity is terminated by the platform and is not available to TikTok users.
        create_time (int | Unset): Activity creation time as a UNIX timestamp in milliseconds.
        update_time (int | Unset): Activity update time as a UNIX timestamp in milliseconds.
        product_level (GetActivityResponseDataProductLevel | Unset): Activity product dimension, values are:
            - PRODUCT: Product level promotion activity.
            - VARIATION: SKU level promotion activity.
            - SHOP: Shop level promotion activity.
        activity_commands (list[str] | Unset): Applicable commands to the activity:
            - IMMUTABLE: The activity cann't be editable or deactivated
        discount (GetActivityResponseDataDiscount | Unset):
        target_user_info (GetActivityResponseDataTargetUserInfo | Unset):
        benefit_products (list[GetActivityResponseDataBenefitProduct] | Unset): Benefit products in BXGY promotions
        auction_support_type (GetActivityResponseDataAuctionSupportType | Unset): Whether a `SHIPPING_DISCOUNT` activity
            supports auction products. This field is omitted for other activity types and can also be omitted for a
            shipping-discount activity when auction-support data is unavailable.
            Possible values:
            - `ALL`: The activity supports both normal products and auction products.
            - `EXCLUDE_AUCTION`: The activity does not support auction products.
    """

    activity_id: str | Unset = UNSET
    title: str | Unset = UNSET
    activity_type: GetActivityResponseDataActivityType | Unset = UNSET
    duration_type: str | Unset = UNSET
    begin_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    participation_limit: list[GetActivityResponseDataParticipationLimit] | Unset = UNSET
    products: list[GetActivityResponseDataProduct] | Unset = UNSET
    status: GetActivityResponseDataStatus | Unset = UNSET
    create_time: int | Unset = UNSET
    update_time: int | Unset = UNSET
    product_level: GetActivityResponseDataProductLevel | Unset = UNSET
    activity_commands: list[str] | Unset = UNSET
    discount: GetActivityResponseDataDiscount | Unset = UNSET
    target_user_info: GetActivityResponseDataTargetUserInfo | Unset = UNSET
    benefit_products: list[GetActivityResponseDataBenefitProduct] | Unset = UNSET
    auction_support_type: GetActivityResponseDataAuctionSupportType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_id = self.activity_id

        title = self.title

        activity_type: str | Unset = UNSET
        if not isinstance(self.activity_type, Unset):
            activity_type = self.activity_type.value

        duration_type = self.duration_type

        begin_time = self.begin_time

        end_time = self.end_time

        participation_limit: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participation_limit, Unset):
            participation_limit = []
            for participation_limit_item_data in self.participation_limit:
                participation_limit_item = participation_limit_item_data.to_dict()
                participation_limit.append(participation_limit_item)

        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        create_time = self.create_time

        update_time = self.update_time

        product_level: str | Unset = UNSET
        if not isinstance(self.product_level, Unset):
            product_level = self.product_level.value

        activity_commands: list[str] | Unset = UNSET
        if not isinstance(self.activity_commands, Unset):
            activity_commands = self.activity_commands

        discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        target_user_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_user_info, Unset):
            target_user_info = self.target_user_info.to_dict()

        benefit_products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.benefit_products, Unset):
            benefit_products = []
            for benefit_products_item_data in self.benefit_products:
                benefit_products_item = benefit_products_item_data.to_dict()
                benefit_products.append(benefit_products_item)

        auction_support_type: str | Unset = UNSET
        if not isinstance(self.auction_support_type, Unset):
            auction_support_type = self.auction_support_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_id is not UNSET:
            field_dict["activity_id"] = activity_id
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
        if participation_limit is not UNSET:
            field_dict["participation_limit"] = participation_limit
        if products is not UNSET:
            field_dict["products"] = products
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
        if discount is not UNSET:
            field_dict["discount"] = discount
        if target_user_info is not UNSET:
            field_dict["target_user_info"] = target_user_info
        if benefit_products is not UNSET:
            field_dict["benefit_products"] = benefit_products
        if auction_support_type is not UNSET:
            field_dict["auction_support_type"] = auction_support_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_activity_response_data_benefit_product import (
            GetActivityResponseDataBenefitProduct,  # noqa: PLC0415
        )
        from ..models.get_activity_response_data_discount import GetActivityResponseDataDiscount  # noqa: PLC0415
        from ..models.get_activity_response_data_participation_limit import (
            GetActivityResponseDataParticipationLimit,  # noqa: PLC0415
        )
        from ..models.get_activity_response_data_product import GetActivityResponseDataProduct  # noqa: PLC0415
        from ..models.get_activity_response_data_target_user_info import (
            GetActivityResponseDataTargetUserInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        activity_id = d.pop("activity_id", UNSET)

        title = d.pop("title", UNSET)

        _activity_type = d.pop("activity_type", UNSET)
        activity_type: GetActivityResponseDataActivityType | Unset
        if isinstance(_activity_type, Unset):
            activity_type = UNSET
        else:
            activity_type = GetActivityResponseDataActivityType(_activity_type)

        duration_type = d.pop("duration_type", UNSET)

        begin_time = d.pop("begin_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        _participation_limit = d.pop("participation_limit", UNSET)
        participation_limit: list[GetActivityResponseDataParticipationLimit] | Unset = UNSET
        if _participation_limit is not UNSET:
            participation_limit = []
            for participation_limit_item_data in _participation_limit:
                participation_limit_item = GetActivityResponseDataParticipationLimit.from_dict(
                    participation_limit_item_data
                )

                participation_limit.append(participation_limit_item)

        _products = d.pop("products", UNSET)
        products: list[GetActivityResponseDataProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = GetActivityResponseDataProduct.from_dict(products_item_data)

                products.append(products_item)

        _status = d.pop("status", UNSET)
        status: GetActivityResponseDataStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetActivityResponseDataStatus(_status)

        create_time = d.pop("create_time", UNSET)

        update_time = d.pop("update_time", UNSET)

        _product_level = d.pop("product_level", UNSET)
        product_level: GetActivityResponseDataProductLevel | Unset
        if isinstance(_product_level, Unset):
            product_level = UNSET
        else:
            product_level = GetActivityResponseDataProductLevel(_product_level)

        activity_commands = cast(list[str], d.pop("activity_commands", UNSET))

        _discount = d.pop("discount", UNSET)
        discount: GetActivityResponseDataDiscount | Unset
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = GetActivityResponseDataDiscount.from_dict(_discount)

        _target_user_info = d.pop("target_user_info", UNSET)
        target_user_info: GetActivityResponseDataTargetUserInfo | Unset
        if isinstance(_target_user_info, Unset):
            target_user_info = UNSET
        else:
            target_user_info = GetActivityResponseDataTargetUserInfo.from_dict(_target_user_info)

        _benefit_products = d.pop("benefit_products", UNSET)
        benefit_products: list[GetActivityResponseDataBenefitProduct] | Unset = UNSET
        if _benefit_products is not UNSET:
            benefit_products = []
            for benefit_products_item_data in _benefit_products:
                benefit_products_item = GetActivityResponseDataBenefitProduct.from_dict(benefit_products_item_data)

                benefit_products.append(benefit_products_item)

        _auction_support_type = d.pop("auction_support_type", UNSET)
        auction_support_type: GetActivityResponseDataAuctionSupportType | Unset
        if isinstance(_auction_support_type, Unset):
            auction_support_type = UNSET
        else:
            auction_support_type = GetActivityResponseDataAuctionSupportType(_auction_support_type)

        get_activity_response_data = cls(
            activity_id=activity_id,
            title=title,
            activity_type=activity_type,
            duration_type=duration_type,
            begin_time=begin_time,
            end_time=end_time,
            participation_limit=participation_limit,
            products=products,
            status=status,
            create_time=create_time,
            update_time=update_time,
            product_level=product_level,
            activity_commands=activity_commands,
            discount=discount,
            target_user_info=target_user_info,
            benefit_products=benefit_products,
            auction_support_type=auction_support_type,
        )

        get_activity_response_data.additional_properties = d
        return get_activity_response_data

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
