from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_coupon_response_data_coupon_threshold_type import GetCouponResponseDataCouponThresholdType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.min_spend import MinSpend


T = TypeVar("T", bound="GetCouponResponseDataCouponThreshold")


@_attrs_define
class GetCouponResponseDataCouponThreshold:
    """
    Attributes:
        type_ (GetCouponResponseDataCouponThresholdType | Unset): The type of purchase criteria. Possible enumerations
            are:
            - `NONE`: No minimum purchase criteria.
            - `MIN_SPEND`: Buyer must meet or exceed the minimum spend criteria with eligible products.
        min_spend (MinSpend | Unset):
    """

    type_: GetCouponResponseDataCouponThresholdType | Unset = UNSET
    min_spend: MinSpend | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        min_spend: dict[str, Any] | Unset = UNSET
        if not isinstance(self.min_spend, Unset):
            min_spend = self.min_spend.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if min_spend is not UNSET:
            field_dict["min_spend"] = min_spend

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.min_spend import MinSpend  # noqa: PLC0415

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: GetCouponResponseDataCouponThresholdType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GetCouponResponseDataCouponThresholdType(_type_)

        _min_spend = d.pop("min_spend", UNSET)
        min_spend: MinSpend | Unset
        if isinstance(_min_spend, Unset):
            min_spend = UNSET
        else:
            min_spend = MinSpend.from_dict(_min_spend)

        get_coupon_response_data_coupon_threshold = cls(
            type_=type_,
            min_spend=min_spend,
        )

        get_coupon_response_data_coupon_threshold.additional_properties = d
        return get_coupon_response_data_coupon_threshold

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
