from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_activity_response_data_discount_bxgy_discount_discount_type import (
    GetActivityResponseDataDiscountBxgyDiscountDiscountType,
)
from ..models.get_activity_response_data_discount_bxgy_discount_threshold_type import (
    GetActivityResponseDataDiscountBxgyDiscountThresholdType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetActivityResponseDataDiscountBxgyDiscount")


@_attrs_define
class GetActivityResponseDataDiscountBxgyDiscount:
    """
    Attributes:
        threshold_type (GetActivityResponseDataDiscountBxgyDiscountThresholdType | Unset): The purchase criterion
            returned for the activity.
            Possible values:
            - `MINIMAL_ITEM_QUANTITY`: The buyer must purchase at least the specified quantity of eligible products.
            - `MINIMAL_ORDER_AMOUNT`: The eligible-product subtotal must reach the specified amount.
        threshold_value (str | Unset): The purchase threshold returned for the activity, based on `threshold_type`.
            - When `threshold_type==MINIMAL_ITEM_QUANTITY`, this is the number of eligible products the buyer must purchase
            and must be an integer.
            - When `threshold_type==MINIMAL_ORDER_AMOUNT`, this is the eligible-product subtotal the buyer must reach, in
            local currency.
        discount_type (GetActivityResponseDataDiscountBxgyDiscountDiscountType | Unset): The type of discount awarded as
            a benefit. For PERCENTAGE_OFF and AMOUNT_OFF_EACH, the discount amount is determined by `discount_value`.
            Possible enumerations are:
            - `PERCENTAGE_OFF`: Buyer will receive X% off the price of the eligible products.
            - `FREE`: Buyer will receive X eligible products for free.
            - `AMOUNT_OFF_EACH`: Buyer will receive X units of local currency off the price of each eligible product.
        discount_value (str | Unset): Value of the discount.
            - When `type`==`PERCENTAGE_OFF`, the buyer will receive X% off the price of eligible products. If the value
            represents a percentage, it should be an integer.
            - `type`==`AMOUNT_OFF_EACH`, the buyer will receive X units of local currency off the price of each eligible
            products. If the value represents a monetary amount, it should be limited to two decimal places.
        benefit_max_applicable_quantity (str | Unset): The quantity of item Y in a BXGY promotion. This value must be a
            positive integer.
        benefit_max_applicable_times (str | Unset): Optional. The maximum number of times the BXGY benefit can be
            applied within a single order. This value must be a positive integer.
    """

    threshold_type: GetActivityResponseDataDiscountBxgyDiscountThresholdType | Unset = UNSET
    threshold_value: str | Unset = UNSET
    discount_type: GetActivityResponseDataDiscountBxgyDiscountDiscountType | Unset = UNSET
    discount_value: str | Unset = UNSET
    benefit_max_applicable_quantity: str | Unset = UNSET
    benefit_max_applicable_times: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        threshold_type: str | Unset = UNSET
        if not isinstance(self.threshold_type, Unset):
            threshold_type = self.threshold_type.value

        threshold_value = self.threshold_value

        discount_type: str | Unset = UNSET
        if not isinstance(self.discount_type, Unset):
            discount_type = self.discount_type.value

        discount_value = self.discount_value

        benefit_max_applicable_quantity = self.benefit_max_applicable_quantity

        benefit_max_applicable_times = self.benefit_max_applicable_times

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if threshold_type is not UNSET:
            field_dict["threshold_type"] = threshold_type
        if threshold_value is not UNSET:
            field_dict["threshold_value"] = threshold_value
        if discount_type is not UNSET:
            field_dict["discount_type"] = discount_type
        if discount_value is not UNSET:
            field_dict["discount_value"] = discount_value
        if benefit_max_applicable_quantity is not UNSET:
            field_dict["benefit_max_applicable_quantity"] = benefit_max_applicable_quantity
        if benefit_max_applicable_times is not UNSET:
            field_dict["benefit_max_applicable_times"] = benefit_max_applicable_times

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _threshold_type = d.pop("threshold_type", UNSET)
        threshold_type: GetActivityResponseDataDiscountBxgyDiscountThresholdType | Unset
        if isinstance(_threshold_type, Unset):
            threshold_type = UNSET
        else:
            threshold_type = GetActivityResponseDataDiscountBxgyDiscountThresholdType(_threshold_type)

        threshold_value = d.pop("threshold_value", UNSET)

        _discount_type = d.pop("discount_type", UNSET)
        discount_type: GetActivityResponseDataDiscountBxgyDiscountDiscountType | Unset
        if isinstance(_discount_type, Unset):
            discount_type = UNSET
        else:
            discount_type = GetActivityResponseDataDiscountBxgyDiscountDiscountType(_discount_type)

        discount_value = d.pop("discount_value", UNSET)

        benefit_max_applicable_quantity = d.pop("benefit_max_applicable_quantity", UNSET)

        benefit_max_applicable_times = d.pop("benefit_max_applicable_times", UNSET)

        get_activity_response_data_discount_bxgy_discount = cls(
            threshold_type=threshold_type,
            threshold_value=threshold_value,
            discount_type=discount_type,
            discount_value=discount_value,
            benefit_max_applicable_quantity=benefit_max_applicable_quantity,
            benefit_max_applicable_times=benefit_max_applicable_times,
        )

        get_activity_response_data_discount_bxgy_discount.additional_properties = d
        return get_activity_response_data_discount_bxgy_discount

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
