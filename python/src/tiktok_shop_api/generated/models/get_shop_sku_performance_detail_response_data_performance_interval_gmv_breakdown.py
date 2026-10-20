from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetShopSKUPerformanceDetailResponseDataPerformanceIntervalGmvBreakdown")



@_attrs_define
class GetShopSKUPerformanceDetailResponseDataPerformanceIntervalGmvBreakdown:
    """ 
        Attributes:
            amount (str | Unset): GMV amount for the corresponding type and currency.
            currency (str | Unset): GMV currency code (ISO 4217 standard). If LOCAL currency is requested, the value will be
                the local currency code of where the shop is registered (e.g. GBP).
            type_ (str | Unset): GMV breakdown type.
                Possible values:
                - LIVE: Live stream content.
                - VIDEO: Video content.
                - PRODUCT_CARD: Product card.
     """

    amount: str | Unset = UNSET
    currency: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        currency = self.currency

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        type_ = d.pop("type", UNSET)

        get_shop_sku_performance_detail_response_data_performance_interval_gmv_breakdown = cls(
            amount=amount,
            currency=currency,
            type_=type_,
        )


        get_shop_sku_performance_detail_response_data_performance_interval_gmv_breakdown.additional_properties = d
        return get_shop_sku_performance_detail_response_data_performance_interval_gmv_breakdown

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
