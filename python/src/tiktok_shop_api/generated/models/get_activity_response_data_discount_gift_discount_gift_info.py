from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_activity_response_data_discount_gift_discount_gift_info_gift_detail import GetActivityResponseDataDiscountGiftDiscountGiftInfoGiftDetail





T = TypeVar("T", bound="GetActivityResponseDataDiscountGiftDiscountGiftInfo")



@_attrs_define
class GetActivityResponseDataDiscountGiftDiscountGiftInfo:
    """ 
        Attributes:
            tier (int | Unset): `tier` uses 1-based indexing, i.e. the first and second tiers are counted "1, 2", not "0,
                1".
                `threshold_value` for a given tier must be greater than that of the previous tier.
                E.g. If `tier`==1 has `threshold_value`==`2`, `tier`==2 must have `threshold_value` > `2`.
            threshold_type (str | Unset): purchase threshold type of discount. Possible enumerations are:
                - `MINIMAL_ITEM_QUANTITY`: Buyer must meet or exceed the minimum spend criteria with eligible products.
                - `MINIMAL_ORDER_AMOUNT`: Buyer must meet or exceed the minimum spend criteria with eligible order.
            threshold_value (str | Unset): The purchase threshold value of the gift, based on `threshold_type`. Determined
                by the user.
                - When `threshold_type==MINIMAL_ITEM_QUANTITY`, the buyer must purchase at least the specified number of
                eligible products (for example, 3 eligible products). If it represents a quantity, it must be an integer.
                - When `threshold_type==MINIMAL_ORDER_AMOUNT`, the eligible-product subtotal must meet or exceed the specified
                value in local currency (for example, 3 units of local currency). If it represents an order value, it must be
                limited to two decimal places.
            gift_details (list[GetActivityResponseDataDiscountGiftDiscountGiftInfoGiftDetail] | Unset): Gift configurations
                related to Gift With Purchase (GWP) promotions.
     """

    tier: int | Unset = UNSET
    threshold_type: str | Unset = UNSET
    threshold_value: str | Unset = UNSET
    gift_details: list[GetActivityResponseDataDiscountGiftDiscountGiftInfoGiftDetail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_activity_response_data_discount_gift_discount_gift_info_gift_detail import GetActivityResponseDataDiscountGiftDiscountGiftInfoGiftDetail # noqa: PLC0415
        tier = self.tier

        threshold_type = self.threshold_type

        threshold_value = self.threshold_value

        gift_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gift_details, Unset):
            gift_details = []
            for gift_details_item_data in self.gift_details:
                gift_details_item = gift_details_item_data.to_dict()
                gift_details.append(gift_details_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if tier is not UNSET:
            field_dict["tier"] = tier
        if threshold_type is not UNSET:
            field_dict["threshold_type"] = threshold_type
        if threshold_value is not UNSET:
            field_dict["threshold_value"] = threshold_value
        if gift_details is not UNSET:
            field_dict["gift_details"] = gift_details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_activity_response_data_discount_gift_discount_gift_info_gift_detail import GetActivityResponseDataDiscountGiftDiscountGiftInfoGiftDetail # noqa: PLC0415
        d = dict(src_dict)
        tier = d.pop("tier", UNSET)

        threshold_type = d.pop("threshold_type", UNSET)

        threshold_value = d.pop("threshold_value", UNSET)

        _gift_details = d.pop("gift_details", UNSET)
        gift_details: list[GetActivityResponseDataDiscountGiftDiscountGiftInfoGiftDetail] | Unset = UNSET
        if _gift_details is not UNSET:
            gift_details = []
            for gift_details_item_data in _gift_details:
                gift_details_item = GetActivityResponseDataDiscountGiftDiscountGiftInfoGiftDetail.from_dict(gift_details_item_data)



                gift_details.append(gift_details_item)


        get_activity_response_data_discount_gift_discount_gift_info = cls(
            tier=tier,
            threshold_type=threshold_type,
            threshold_value=threshold_value,
            gift_details=gift_details,
        )


        get_activity_response_data_discount_gift_discount_gift_info.additional_properties = d
        return get_activity_response_data_discount_gift_discount_gift_info

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
