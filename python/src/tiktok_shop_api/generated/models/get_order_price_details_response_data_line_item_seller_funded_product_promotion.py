from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_order_price_details_response_data_line_item_seller_funded_product_promotion_discount_type import (
    GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotionDiscountType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotion")


@_attrs_define
class GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotion:
    """
    Attributes:
        activity_id (str | Unset): A unique ID that identifies different promotion activities.
        discount_amount (str | Unset): Discount amount of this activity
        discount_type (GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotionDiscountType | Unset):
            Discount type of this activity. Enumerations:
            - COUPON
            - ACTIVITY
    """

    activity_id: str | Unset = UNSET
    discount_amount: str | Unset = UNSET
    discount_type: GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotionDiscountType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_id = self.activity_id

        discount_amount = self.discount_amount

        discount_type: str | Unset = UNSET
        if not isinstance(self.discount_type, Unset):
            discount_type = self.discount_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_id is not UNSET:
            field_dict["activity_id"] = activity_id
        if discount_amount is not UNSET:
            field_dict["discount_amount"] = discount_amount
        if discount_type is not UNSET:
            field_dict["discount_type"] = discount_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_id = d.pop("activity_id", UNSET)

        discount_amount = d.pop("discount_amount", UNSET)

        _discount_type = d.pop("discount_type", UNSET)
        discount_type: GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotionDiscountType | Unset
        if isinstance(_discount_type, Unset):
            discount_type = UNSET
        else:
            discount_type = GetOrderPriceDetailsResponseDataLineItemSellerFundedProductPromotionDiscountType(
                _discount_type
            )

        get_order_price_details_response_data_line_item_seller_funded_product_promotion = cls(
            activity_id=activity_id,
            discount_amount=discount_amount,
            discount_type=discount_type,
        )

        get_order_price_details_response_data_line_item_seller_funded_product_promotion.additional_properties = d
        return get_order_price_details_response_data_line_item_seller_funded_product_promotion

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
