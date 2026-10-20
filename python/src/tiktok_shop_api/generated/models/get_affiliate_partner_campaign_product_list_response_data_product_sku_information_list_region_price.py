from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListRegionPrice")



@_attrs_define
class GetAffiliatePartnerCampaignProductListResponseDataProductSkuInformationListRegionPrice:
    """ 
        Attributes:
            region_code (str | Unset): the region code of the sku
            currency (str | Unset): The currency of the SKU price.
                Possible values based on the region:
                - BRL:  Brazil
                - EUR: France, Germany, Ireland, Italy, Spain
                - GBP: United Kingdom
                - IDR: Indonesia
                - JPY: Japan
                - MXN: Mexico
                - MYR: Malaysia
                - PHP: Philippines
                - SGD: Singapore
                - THB: Thailand
                - USD: United States
                - VND: Vietnam
            list_price (str | Unset): The SKU's list price information that has been verified to be legitimate by the audit
                team. This is equivalent to the manufacturer's suggested retail price (MSRP), or the recommended retail price
                (RRP).
            sale_price (str | Unset): The SKU's selling price, inclusive of tax.
                Applicable only for cross-border sellers from China.
            localized_dutiable_price (str | Unset): localized dutiable price
     """

    region_code: str | Unset = UNSET
    currency: str | Unset = UNSET
    list_price: str | Unset = UNSET
    sale_price: str | Unset = UNSET
    localized_dutiable_price: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        region_code = self.region_code

        currency = self.currency

        list_price = self.list_price

        sale_price = self.sale_price

        localized_dutiable_price = self.localized_dutiable_price


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if region_code is not UNSET:
            field_dict["region_code"] = region_code
        if currency is not UNSET:
            field_dict["currency"] = currency
        if list_price is not UNSET:
            field_dict["list_price"] = list_price
        if sale_price is not UNSET:
            field_dict["sale_price"] = sale_price
        if localized_dutiable_price is not UNSET:
            field_dict["localized_dutiable_price"] = localized_dutiable_price

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        region_code = d.pop("region_code", UNSET)

        currency = d.pop("currency", UNSET)

        list_price = d.pop("list_price", UNSET)

        sale_price = d.pop("sale_price", UNSET)

        localized_dutiable_price = d.pop("localized_dutiable_price", UNSET)

        get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_region_price = cls(
            region_code=region_code,
            currency=currency,
            list_price=list_price,
            sale_price=sale_price,
            localized_dutiable_price=localized_dutiable_price,
        )


        get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_region_price.additional_properties = d
        return get_affiliate_partner_campaign_product_list_response_data_product_sku_information_list_region_price

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
