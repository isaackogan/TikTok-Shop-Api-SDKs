from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateFBTMCFOrderRequestConsigneeAddress")



@_attrs_define
class CreateFBTMCFOrderRequestConsigneeAddress:
    """ 
        Attributes:
            country_code (str): The consignee address country code in two-character ISO 3166-1 alpha-2 format. Only `US` is
                accepted.
            state_or_region (str): Consignee address state or region
            city (str): Consignee address city
            address_line_1 (str): The detail address line 1
            district_or_county (str | Unset): Consignee address district or county
            address_line_2 (str | Unset): The detail address line 2
            postal_code (str | Unset): The 5-digit US ZIP code for the consignee address.
     """

    country_code: str
    state_or_region: str
    city: str
    address_line_1: str
    district_or_county: str | Unset = UNSET
    address_line_2: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        state_or_region = self.state_or_region

        city = self.city

        address_line_1 = self.address_line_1

        district_or_county = self.district_or_county

        address_line_2 = self.address_line_2

        postal_code = self.postal_code


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "country_code": country_code,
            "state_or_region": state_or_region,
            "city": city,
            "address_line_1": address_line_1,
        })
        if district_or_county is not UNSET:
            field_dict["district_or_county"] = district_or_county
        if address_line_2 is not UNSET:
            field_dict["address_line_2"] = address_line_2
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_code = d.pop("country_code")

        state_or_region = d.pop("state_or_region")

        city = d.pop("city")

        address_line_1 = d.pop("address_line_1")

        district_or_county = d.pop("district_or_county", UNSET)

        address_line_2 = d.pop("address_line_2", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        create_fbtmcf_order_request_consignee_address = cls(
            country_code=country_code,
            state_or_region=state_or_region,
            city=city,
            address_line_1=address_line_1,
            district_or_county=district_or_county,
            address_line_2=address_line_2,
            postal_code=postal_code,
        )


        create_fbtmcf_order_request_consignee_address.additional_properties = d
        return create_fbtmcf_order_request_consignee_address

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
