from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductPrice")



@_attrs_define
class GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailProductPrice:
    """ 
        Attributes:
            min_price (str | Unset): The minimum offered price of the product.
            max_price (str | Unset): The maximum offered price of the product.
            currency (str | Unset): The currency code for the maximum and minimum offered price for the product.
     """

    min_price: str | Unset = UNSET
    max_price: str | Unset = UNSET
    currency: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        min_price = self.min_price

        max_price = self.max_price

        currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_price is not UNSET:
            field_dict["min_price"] = min_price
        if max_price is not UNSET:
            field_dict["max_price"] = max_price
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_price = d.pop("min_price", UNSET)

        max_price = d.pop("max_price", UNSET)

        currency = d.pop("currency", UNSET)

        get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_product_price = cls(
            min_price=min_price,
            max_price=max_price,
            currency=currency,
        )


        get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_product_price.additional_properties = d
        return get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_product_price

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
