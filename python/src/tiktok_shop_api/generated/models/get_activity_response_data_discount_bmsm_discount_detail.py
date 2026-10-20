from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetActivityResponseDataDiscountBmsmDiscountDetail")


@_attrs_define
class GetActivityResponseDataDiscountBmsmDiscountDetail:
    """
    Attributes:
        tier (int | Unset): `tier` uses 1-based indexing, i.e. the first and second tiers are counted "1, 2", not "0,
            1".
            `threshold_value` and `value` for a given tier must be greater than that of the previous tier.
            E.g. If `tier`==1 has `threshold_value`==`20` and `value`== `15`, `tier`==2 must have `threshold_value` > `20`
            and `value`>`15`.
        threshold_type (str | Unset): The type of purchase criteria. Possible enumerations are:
            - `MINIMAL_ITEM_QUANTITY`: Buyer must meet or exceed the minimum spend criteria with eligible products.
            - `MINIMAL_ORDER_AMOUNT`: Buyer must meet or exceed the minimum spend criteria with eligible order.
        threshold_value (str | Unset): The purchase threshold of the discount, based on the `threshold_type`, e.g., "3".
            Determined by user.
            - When `threshold_type==NO_THRESHOLD`, this value is not required.
            - When `threshold_type==MINIMAL_ITEM_QUANTITY`, buyer must purchase at least the specified number of eligible
            products (e.g. must purchase 3 or more eligible products to receive the benefit). If it represents a quantity,
            it must be an integer.
            - When `threshold_type==MINIMAL_ORDER_AMOUNT`, the eligible product subtotal for the buyer's order must meet or
            exceed the specified order value in local currency (e.g. buyer's order subtotal must be at least $3 to receive
            the benefit). If it represents an order value, it must be limited to two decimal places.
        type_ (str | Unset): The type of discount awarded as a benefit. The value of the discount is determined by
            `value`.
            Possible enumerations are:
            - `PERCENTAGE_OFF`: Buyer will receive X% off the price of the eligible products.
            - `AMOUNT_OFF`: Buyer will receive X units of local currency off the price of eligible products.
        value (str | Unset): Value of the discount.
            - When `type`==`PERCENTAGE_OFF`, the buyer will receive X% off the price of eligible products. If the value
            represents a percentage, it should be an integer.
            - `type`==`AMOUNT_OFF`, the buyer will receive X units of local currency off the price of eligible products. If
            the value represents a monetary amount, it should be limited to two decimal places.
    """

    tier: int | Unset = UNSET
    threshold_type: str | Unset = UNSET
    threshold_value: str | Unset = UNSET
    type_: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tier = self.tier

        threshold_type = self.threshold_type

        threshold_value = self.threshold_value

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tier is not UNSET:
            field_dict["tier"] = tier
        if threshold_type is not UNSET:
            field_dict["threshold_type"] = threshold_type
        if threshold_value is not UNSET:
            field_dict["threshold_value"] = threshold_value
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tier = d.pop("tier", UNSET)

        threshold_type = d.pop("threshold_type", UNSET)

        threshold_value = d.pop("threshold_value", UNSET)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        get_activity_response_data_discount_bmsm_discount_detail = cls(
            tier=tier,
            threshold_type=threshold_type,
            threshold_value=threshold_value,
            type_=type_,
            value=value,
        )

        get_activity_response_data_discount_bmsm_discount_detail.additional_properties = d
        return get_activity_response_data_discount_bmsm_discount_detail

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
