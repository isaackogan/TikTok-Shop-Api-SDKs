from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.district_info import DistrictInfo
    from ..models.get_order_list_response_data_order_recipient_address_delivery_preference import (
        GetOrderListResponseDataOrderRecipientAddressDeliveryPreference,
    )


T = TypeVar("T", bound="GetOrderListResponseDataOrderRecipientAddress")


@_attrs_define
class GetOrderListResponseDataOrderRecipientAddress:
    """
    Attributes:
        full_address (str | Unset): Complete recipient address information.
        phone_number (str | Unset): Recipient telephone number.

            **Note**: If this order uses platform logistics, the phone number will be desensitized.
        name (str | Unset): Recipient name.

            **Note**: If this order uses platform logistics, the recipient name will be desensitized.
        first_name (str | Unset): Recipient first name.

            If the recipient first and last names are not provided separately, this parameter will have the same value as
            the `name` parameter.
        last_name (str | Unset): Recipient last name.

            If the recipient first and last names are not provided separately, this parameter will be empty.
        first_name_local_script (str | Unset): Recipient first name in katakana.
            **Note**: Applicable only for the JP market.
        last_name_local_script (str | Unset): Recipient last name in katakana.
            **Note**: Applicable only for the JP market.
        address_detail (str | Unset): Full recipient detailed address.
        address_line1 (str | Unset): The first line of the street address.
        address_line2 (str | Unset): The second line of the street address.
        address_line3 (str | Unset): The third line of the street address.
        address_line4 (str | Unset): The fourth line of the street address.
        district_info (list[DistrictInfo] | Unset): `district_info` is unavailable under `UNPAID` and `ON_HOLD`
            statuses.
        delivery_preferences (GetOrderListResponseDataOrderRecipientAddressDeliveryPreference | Unset):
        postal_code (str | Unset): The postal code that can be used by seller for shipping. For the US market, this
            refers to the ZIP Code.
        region_code (str | Unset): Region code.
        post_town (str | Unset): Post town of the address
            Note: Available only in UK market
    """

    full_address: str | Unset = UNSET
    phone_number: str | Unset = UNSET
    name: str | Unset = UNSET
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    first_name_local_script: str | Unset = UNSET
    last_name_local_script: str | Unset = UNSET
    address_detail: str | Unset = UNSET
    address_line1: str | Unset = UNSET
    address_line2: str | Unset = UNSET
    address_line3: str | Unset = UNSET
    address_line4: str | Unset = UNSET
    district_info: list[DistrictInfo] | Unset = UNSET
    delivery_preferences: GetOrderListResponseDataOrderRecipientAddressDeliveryPreference | Unset = UNSET
    postal_code: str | Unset = UNSET
    region_code: str | Unset = UNSET
    post_town: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_address = self.full_address

        phone_number = self.phone_number

        name = self.name

        first_name = self.first_name

        last_name = self.last_name

        first_name_local_script = self.first_name_local_script

        last_name_local_script = self.last_name_local_script

        address_detail = self.address_detail

        address_line1 = self.address_line1

        address_line2 = self.address_line2

        address_line3 = self.address_line3

        address_line4 = self.address_line4

        district_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.district_info, Unset):
            district_info = []
            for district_info_item_data in self.district_info:
                district_info_item = district_info_item_data.to_dict()
                district_info.append(district_info_item)

        delivery_preferences: dict[str, Any] | Unset = UNSET
        if not isinstance(self.delivery_preferences, Unset):
            delivery_preferences = self.delivery_preferences.to_dict()

        postal_code = self.postal_code

        region_code = self.region_code

        post_town = self.post_town

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_address is not UNSET:
            field_dict["full_address"] = full_address
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if name is not UNSET:
            field_dict["name"] = name
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if first_name_local_script is not UNSET:
            field_dict["first_name_local_script"] = first_name_local_script
        if last_name_local_script is not UNSET:
            field_dict["last_name_local_script"] = last_name_local_script
        if address_detail is not UNSET:
            field_dict["address_detail"] = address_detail
        if address_line1 is not UNSET:
            field_dict["address_line1"] = address_line1
        if address_line2 is not UNSET:
            field_dict["address_line2"] = address_line2
        if address_line3 is not UNSET:
            field_dict["address_line3"] = address_line3
        if address_line4 is not UNSET:
            field_dict["address_line4"] = address_line4
        if district_info is not UNSET:
            field_dict["district_info"] = district_info
        if delivery_preferences is not UNSET:
            field_dict["delivery_preferences"] = delivery_preferences
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if region_code is not UNSET:
            field_dict["region_code"] = region_code
        if post_town is not UNSET:
            field_dict["post_town"] = post_town

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.district_info import DistrictInfo  # noqa: PLC0415
        from ..models.get_order_list_response_data_order_recipient_address_delivery_preference import (
            GetOrderListResponseDataOrderRecipientAddressDeliveryPreference,  # noqa: PLC0415
        )

        d = dict(src_dict)
        full_address = d.pop("full_address", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        name = d.pop("name", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        first_name_local_script = d.pop("first_name_local_script", UNSET)

        last_name_local_script = d.pop("last_name_local_script", UNSET)

        address_detail = d.pop("address_detail", UNSET)

        address_line1 = d.pop("address_line1", UNSET)

        address_line2 = d.pop("address_line2", UNSET)

        address_line3 = d.pop("address_line3", UNSET)

        address_line4 = d.pop("address_line4", UNSET)

        _district_info = d.pop("district_info", UNSET)
        district_info: list[DistrictInfo] | Unset = UNSET
        if _district_info is not UNSET:
            district_info = []
            for district_info_item_data in _district_info:
                district_info_item = DistrictInfo.from_dict(district_info_item_data)

                district_info.append(district_info_item)

        _delivery_preferences = d.pop("delivery_preferences", UNSET)
        delivery_preferences: GetOrderListResponseDataOrderRecipientAddressDeliveryPreference | Unset
        if isinstance(_delivery_preferences, Unset):
            delivery_preferences = UNSET
        else:
            delivery_preferences = GetOrderListResponseDataOrderRecipientAddressDeliveryPreference.from_dict(
                _delivery_preferences
            )

        postal_code = d.pop("postal_code", UNSET)

        region_code = d.pop("region_code", UNSET)

        post_town = d.pop("post_town", UNSET)

        get_order_list_response_data_order_recipient_address = cls(
            full_address=full_address,
            phone_number=phone_number,
            name=name,
            first_name=first_name,
            last_name=last_name,
            first_name_local_script=first_name_local_script,
            last_name_local_script=last_name_local_script,
            address_detail=address_detail,
            address_line1=address_line1,
            address_line2=address_line2,
            address_line3=address_line3,
            address_line4=address_line4,
            district_info=district_info,
            delivery_preferences=delivery_preferences,
            postal_code=postal_code,
            region_code=region_code,
            post_town=post_town,
        )

        get_order_list_response_data_order_recipient_address.additional_properties = d
        return get_order_list_response_data_order_recipient_address

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
