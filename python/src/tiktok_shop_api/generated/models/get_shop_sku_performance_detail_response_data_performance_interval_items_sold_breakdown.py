from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShopSKUPerformanceDetailResponseDataPerformanceIntervalItemsSoldBreakdown")


@_attrs_define
class GetShopSKUPerformanceDetailResponseDataPerformanceIntervalItemsSoldBreakdown:
    """
    Attributes:
        amount (int | Unset): Number of units sold for the corresponding type.
        type_ (str | Unset): Items-sold breakdown type.
            Possible values:
            - LIVE: Live stream content.
            - VIDEO: Video content.
            - PRODUCT_CARD: Product card.
    """

    amount: int | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        type_ = d.pop("type", UNSET)

        get_shop_sku_performance_detail_response_data_performance_interval_items_sold_breakdown = cls(
            amount=amount,
            type_=type_,
        )

        get_shop_sku_performance_detail_response_data_performance_interval_items_sold_breakdown.additional_properties = d
        return get_shop_sku_performance_detail_response_data_performance_interval_items_sold_breakdown

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
