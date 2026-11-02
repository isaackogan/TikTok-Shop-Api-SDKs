from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetACCBrandsResponseDataBrand")



@_attrs_define
class GetACCBrandsResponseDataBrand:
    """ 
        Attributes:
            brand_id (str | Unset): ID of the authorized brand. Use it together with industry_id from this same record when
                calling the other ACC data APIs.
            brand_logo_url (str | Unset): URL of the authorized brand's logo.
            brand_name (str | Unset): Name of the authorized brand.
            industry_id (str | Unset): ID of the industry associated with the brand. Use it together with brand_id from this
                same record when calling the other ACC data APIs.
            industry_name (str | Unset): Name of the industry associated with the brand.
            shop_id (str | Unset): ID of the current shop to which this brand authorization applies. This is a read-only
                response identifier; the shop used by ACC requests is determined from the authorized shop context.
            shop_name (str | Unset): Name of the current shop to which this brand authorization applies.
            ttms_id (str | Unset): TTMS identifier associated with the brand. Returned for reference only; do not pass it as
                a business parameter to the ACC APIs.
     """

    brand_id: str | Unset = UNSET
    brand_logo_url: str | Unset = UNSET
    brand_name: str | Unset = UNSET
    industry_id: str | Unset = UNSET
    industry_name: str | Unset = UNSET
    shop_id: str | Unset = UNSET
    shop_name: str | Unset = UNSET
    ttms_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        brand_id = self.brand_id

        brand_logo_url = self.brand_logo_url

        brand_name = self.brand_name

        industry_id = self.industry_id

        industry_name = self.industry_name

        shop_id = self.shop_id

        shop_name = self.shop_name

        ttms_id = self.ttms_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if brand_id is not UNSET:
            field_dict["brand_id"] = brand_id
        if brand_logo_url is not UNSET:
            field_dict["brand_logo_url"] = brand_logo_url
        if brand_name is not UNSET:
            field_dict["brand_name"] = brand_name
        if industry_id is not UNSET:
            field_dict["industry_id"] = industry_id
        if industry_name is not UNSET:
            field_dict["industry_name"] = industry_name
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if shop_name is not UNSET:
            field_dict["shop_name"] = shop_name
        if ttms_id is not UNSET:
            field_dict["ttms_id"] = ttms_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brand_id = d.pop("brand_id", UNSET)

        brand_logo_url = d.pop("brand_logo_url", UNSET)

        brand_name = d.pop("brand_name", UNSET)

        industry_id = d.pop("industry_id", UNSET)

        industry_name = d.pop("industry_name", UNSET)

        shop_id = d.pop("shop_id", UNSET)

        shop_name = d.pop("shop_name", UNSET)

        ttms_id = d.pop("ttms_id", UNSET)

        get_acc_brands_response_data_brand = cls(
            brand_id=brand_id,
            brand_logo_url=brand_logo_url,
            brand_name=brand_name,
            industry_id=industry_id,
            industry_name=industry_name,
            shop_id=shop_id,
            shop_name=shop_name,
            ttms_id=ttms_id,
        )


        get_acc_brands_response_data_brand.additional_properties = d
        return get_acc_brands_response_data_brand

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
