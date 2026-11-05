from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailProductStatistic")



@_attrs_define
class GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailProductStatistic:
    """ 
        Attributes:
            sold_num (str | Unset): Number of product units sold through the campaign, encoded as a string.
     """

    sold_num: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        sold_num = self.sold_num


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sold_num is not UNSET:
            field_dict["sold_num"] = sold_num

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sold_num = d.pop("sold_num", UNSET)

        get_seller_partner_campaign_registered_products_response_data_product_detail_product_statistic = cls(
            sold_num=sold_num,
        )


        get_seller_partner_campaign_registered_products_response_data_product_detail_product_statistic.additional_properties = d
        return get_seller_partner_campaign_registered_products_response_data_product_detail_product_statistic

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
