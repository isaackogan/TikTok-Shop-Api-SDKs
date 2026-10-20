from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfileGmv")


@_attrs_define
class GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorTrendProfileGmv:
    """
    Attributes:
        amount (str | Unset): GMV amount
        symbol (str | Unset): GMV symbol
    """

    amount: str | Unset = UNSET
    symbol: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        symbol = self.symbol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if symbol is not UNSET:
            field_dict["symbol"] = symbol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        symbol = d.pop("symbol", UNSET)

        get_marketplace_creator_performance_response_data_creator_creator_profile_creator_trend_profile_gmv = cls(
            amount=amount,
            symbol=symbol,
        )

        get_marketplace_creator_performance_response_data_creator_creator_profile_creator_trend_profile_gmv.additional_properties = d
        return get_marketplace_creator_performance_response_data_creator_creator_profile_creator_trend_profile_gmv

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
