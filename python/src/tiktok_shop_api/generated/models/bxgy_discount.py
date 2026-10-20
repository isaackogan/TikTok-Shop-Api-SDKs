from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bxgy_discount_discount_type import BxgyDiscountDiscountType
from ..models.bxgy_discount_threshold_type import BxgyDiscountThresholdType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BxgyDiscount")


@_attrs_define
class BxgyDiscount:
    """
    Attributes:
        threshold_type (BxgyDiscountThresholdType): The purchase criterion.
            Possible values:
            - `MINIMAL_ITEM_QUANTITY`: The buyer must purchase at least the configured quantity of eligible products.
            - `MINIMAL_ORDER_AMOUNT`: The eligible-product subtotal must reach the configured amount.
        threshold_value (str): The purchase threshold determined by `threshold_type`.
            - When `threshold_type==MINIMAL_ITEM_QUANTITY`, enter a positive integer no greater than `10`.
            - When `threshold_type==MINIMAL_ORDER_AMOUNT`, enter a positive eligible-product subtotal in local currency,
            with at most two decimal places.
        discount_type (BxgyDiscountDiscountType): The type of benefit.
            Possible values:
            - PERCENTAGE_OFF: Apply the percentage specified by discount_value to eligible products.
            - FREE: Provide the configured quantity of eligible products for free.
            - AMOUNT_OFF_EACH: Deduct the local-currency amount specified by discount_value from each eligible product.
        discount_value (str): Value of the discount.
            - When `type`==`PERCENTAGE_OFF`, the buyer will receive X% off the price of eligible products. If the value
            represents a percentage, it should be an integer.
            - `type`==`AMOUNT_OFF_EACH`, the buyer will receive X units of local currency off the price of each eligible
            products. If the value represents a monetary amount, it should be limited to two decimal places.
        benefit_max_applicable_quantity (str): The quantity of item Y awarded each time the Buy X Get Y benefit applies.
            Enter a positive integer no greater than `20`.
        benefit_max_applicable_times (str | Unset): Optional. The maximum number of times the Buy X Get Y benefit can be
            applied in one order. Enter a positive integer no greater than `50`.
    """

    threshold_type: BxgyDiscountThresholdType
    threshold_value: str
    discount_type: BxgyDiscountDiscountType
    discount_value: str
    benefit_max_applicable_quantity: str
    benefit_max_applicable_times: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        threshold_type = self.threshold_type.value

        threshold_value = self.threshold_value

        discount_type = self.discount_type.value

        discount_value = self.discount_value

        benefit_max_applicable_quantity = self.benefit_max_applicable_quantity

        benefit_max_applicable_times = self.benefit_max_applicable_times

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "threshold_type": threshold_type,
                "threshold_value": threshold_value,
                "discount_type": discount_type,
                "discount_value": discount_value,
                "benefit_max_applicable_quantity": benefit_max_applicable_quantity,
            }
        )
        if benefit_max_applicable_times is not UNSET:
            field_dict["benefit_max_applicable_times"] = benefit_max_applicable_times

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        threshold_type = BxgyDiscountThresholdType(d.pop("threshold_type"))

        threshold_value = d.pop("threshold_value")

        discount_type = BxgyDiscountDiscountType(d.pop("discount_type"))

        discount_value = d.pop("discount_value")

        benefit_max_applicable_quantity = d.pop("benefit_max_applicable_quantity")

        benefit_max_applicable_times = d.pop("benefit_max_applicable_times", UNSET)

        bxgy_discount = cls(
            threshold_type=threshold_type,
            threshold_value=threshold_value,
            discount_type=discount_type,
            discount_value=discount_value,
            benefit_max_applicable_quantity=benefit_max_applicable_quantity,
            benefit_max_applicable_times=benefit_max_applicable_times,
        )

        bxgy_discount.additional_properties = d
        return bxgy_discount

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
