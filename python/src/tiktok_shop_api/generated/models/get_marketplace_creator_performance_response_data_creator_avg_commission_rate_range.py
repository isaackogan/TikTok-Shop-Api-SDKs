from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetMarketplaceCreatorPerformanceResponseDataCreatorAvgCommissionRateRange")


@_attrs_define
class GetMarketplaceCreatorPerformanceResponseDataCreatorAvgCommissionRateRange:
    """
    Attributes:
        minimum_amount (int | Unset): The smallest average commission rate in hundredths of a percent.
        maximum_amount (int | Unset): The largest average commission rate in hundredths of a percent.
    """

    minimum_amount: int | Unset = UNSET
    maximum_amount: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        minimum_amount = self.minimum_amount

        maximum_amount = self.maximum_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if minimum_amount is not UNSET:
            field_dict["minimum_amount"] = minimum_amount
        if maximum_amount is not UNSET:
            field_dict["maximum_amount"] = maximum_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        minimum_amount = d.pop("minimum_amount", UNSET)

        maximum_amount = d.pop("maximum_amount", UNSET)

        get_marketplace_creator_performance_response_data_creator_avg_commission_rate_range = cls(
            minimum_amount=minimum_amount,
            maximum_amount=maximum_amount,
        )

        get_marketplace_creator_performance_response_data_creator_avg_commission_rate_range.additional_properties = d
        return get_marketplace_creator_performance_response_data_creator_avg_commission_rate_range

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
