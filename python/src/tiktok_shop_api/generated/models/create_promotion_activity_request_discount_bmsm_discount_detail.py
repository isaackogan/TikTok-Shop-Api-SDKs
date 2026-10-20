from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_promotion_activity_request_discount_bmsm_discount_detail_threshold_type import CreatePromotionActivityRequestDiscountBmsmDiscountDetailThresholdType
from ..models.create_promotion_activity_request_discount_bmsm_discount_detail_type import CreatePromotionActivityRequestDiscountBmsmDiscountDetailType






T = TypeVar("T", bound="CreatePromotionActivityRequestDiscountBmsmDiscountDetail")



@_attrs_define
class CreatePromotionActivityRequestDiscountBmsmDiscountDetail:
    """ 
        Attributes:
            tier (int): `tier` uses 1-based indexing: the first and second tiers are `1` and `2`, not `0` and `1`. For each
                subsequent tier, both `threshold_value` and `value` must be greater than those of the previous tier. For
                example, if tier `1` has `threshold_value` `20` and `value` `15`, tier `2` must have a `threshold_value` greater
                than `20` and a `value` greater than `15`.
            threshold_type (CreatePromotionActivityRequestDiscountBmsmDiscountDetailThresholdType): The type of purchase
                criteria. Possible enumerations are:
                - `MINIMAL_ITEM_QUANTITY`: Buyer must meet or exceed the minimum spend criteria with eligible products.
                - `MINIMAL_ORDER_AMOUNT`: Buyer must meet or exceed the minimum spend criteria with eligible order.
            threshold_value (str): The purchase threshold for this tier.
                - When `threshold_type==MINIMAL_ITEM_QUANTITY`, enter a positive integer.
                - When `threshold_type==MINIMAL_ORDER_AMOUNT`, enter a positive amount in local currency, with at most two
                decimal places.
            type_ (CreatePromotionActivityRequestDiscountBmsmDiscountDetailType): The type of discount awarded as a benefit.
                The value of the discount is determined by `value`.
                Possible enumerations are:
                - `PERCENTAGE_OFF`: Buyer will receive X% off the price of the eligible products.
                - `AMOUNT_OFF`: Buyer will receive X units of local currency off the price of eligible products.
            value (str): The discount value.
                - When `type==PERCENTAGE_OFF`, enter a positive integer percentage.
                - When `type==AMOUNT_OFF`, enter a positive amount in local currency, with at most two decimal places.
     """

    tier: int
    threshold_type: CreatePromotionActivityRequestDiscountBmsmDiscountDetailThresholdType
    threshold_value: str
    type_: CreatePromotionActivityRequestDiscountBmsmDiscountDetailType
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        tier = self.tier

        threshold_type = self.threshold_type.value

        threshold_value = self.threshold_value

        type_ = self.type_.value

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "tier": tier,
            "threshold_type": threshold_type,
            "threshold_value": threshold_value,
            "type": type_,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tier = d.pop("tier")

        threshold_type = CreatePromotionActivityRequestDiscountBmsmDiscountDetailThresholdType(d.pop("threshold_type"))




        threshold_value = d.pop("threshold_value")

        type_ = CreatePromotionActivityRequestDiscountBmsmDiscountDetailType(d.pop("type"))




        value = d.pop("value")

        create_promotion_activity_request_discount_bmsm_discount_detail = cls(
            tier=tier,
            threshold_type=threshold_type,
            threshold_value=threshold_value,
            type_=type_,
            value=value,
        )


        create_promotion_activity_request_discount_bmsm_discount_detail.additional_properties = d
        return create_promotion_activity_request_discount_bmsm_discount_detail

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
