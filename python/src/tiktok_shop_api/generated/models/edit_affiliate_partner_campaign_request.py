from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.edit_affiliate_partner_campaign_request_target_seller_types_item import EditAffiliatePartnerCampaignRequestTargetSellerTypesItem
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.contact_info import ContactInfo





T = TypeVar("T", bound="EditAffiliatePartnerCampaignRequest")



@_attrs_define
class EditAffiliatePartnerCampaignRequest:
    """ 
        Attributes:
            name (str | Unset): The campaign name. It must contain 1 to 50 characters and must not start with a space.
            description (str | Unset): The campaign description. It must contain 1 to 1000 characters and must not start
                with a space.
            campaign_start_time (int | Unset): The scheduled campaign start time as a Unix timestamp in seconds. This field
                can be updated only when the campaign status is `READY` or `UPCOMING`.
            campaign_end_time (int | Unset): The scheduled end time in Unix epoch time format for the campaign. Note that
                the end time must be less than 360 days from the start date. This field is no longer editable when the campaign
                status is set to `CLOSED`.
            registration_start_time (int | Unset): The scheduled start time for seller product registration, as a Unix
                timestamp in seconds. This field can be updated only when the campaign status is `READY` or `UPCOMING`.
            registration_end_time (int | Unset): The scheduled end time for seller product registration, as a Unix timestamp
                in seconds. This field is no longer editable when the campaign status is `CLOSED`.
            commission_rate (int | Unset): The total commission rate, in units of 0.01%, proposed by the affiliate partner
                for display to sellers. The value must be between 100 and 8000, inclusive.
            contact_info (ContactInfo | Unset):
            target_shop_codes (list[str] | Unset): A list of TikTok Shop seller shop codes to allow to register for the
                campaign. The seller shop code in available in TikTok Shop Seller Central by clicking on the Seller Profile icon
                in the top right of the user interface. The list must be less than 100 items in length.
            target_seller_types (list[EditAffiliatePartnerCampaignRequestTargetSellerTypesItem] | Unset): A list of eligible
                seller types to allow to register for the campaign. Use this field to broadly target types of sellers instead of
                specific sellers in the `target_shop_codes` field. This is an enumerated type with possible values:
                - LOCAL
                - CROSS_BORDER
     """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    campaign_start_time: int | Unset = UNSET
    campaign_end_time: int | Unset = UNSET
    registration_start_time: int | Unset = UNSET
    registration_end_time: int | Unset = UNSET
    commission_rate: int | Unset = UNSET
    contact_info: ContactInfo | Unset = UNSET
    target_shop_codes: list[str] | Unset = UNSET
    target_seller_types: list[EditAffiliatePartnerCampaignRequestTargetSellerTypesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.contact_info import ContactInfo # noqa: PLC0415
        name = self.name

        description = self.description

        campaign_start_time = self.campaign_start_time

        campaign_end_time = self.campaign_end_time

        registration_start_time = self.registration_start_time

        registration_end_time = self.registration_end_time

        commission_rate = self.commission_rate

        contact_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_info, Unset):
            contact_info = self.contact_info.to_dict()

        target_shop_codes: list[str] | Unset = UNSET
        if not isinstance(self.target_shop_codes, Unset):
            target_shop_codes = self.target_shop_codes



        target_seller_types: list[str] | Unset = UNSET
        if not isinstance(self.target_seller_types, Unset):
            target_seller_types = []
            for target_seller_types_item_data in self.target_seller_types:
                target_seller_types_item = target_seller_types_item_data.value
                target_seller_types.append(target_seller_types_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if campaign_start_time is not UNSET:
            field_dict["campaign_start_time"] = campaign_start_time
        if campaign_end_time is not UNSET:
            field_dict["campaign_end_time"] = campaign_end_time
        if registration_start_time is not UNSET:
            field_dict["registration_start_time"] = registration_start_time
        if registration_end_time is not UNSET:
            field_dict["registration_end_time"] = registration_end_time
        if commission_rate is not UNSET:
            field_dict["commission_rate"] = commission_rate
        if contact_info is not UNSET:
            field_dict["contact_info"] = contact_info
        if target_shop_codes is not UNSET:
            field_dict["target_shop_codes"] = target_shop_codes
        if target_seller_types is not UNSET:
            field_dict["target_seller_types"] = target_seller_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_info import ContactInfo # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        campaign_start_time = d.pop("campaign_start_time", UNSET)

        campaign_end_time = d.pop("campaign_end_time", UNSET)

        registration_start_time = d.pop("registration_start_time", UNSET)

        registration_end_time = d.pop("registration_end_time", UNSET)

        commission_rate = d.pop("commission_rate", UNSET)

        _contact_info = d.pop("contact_info", UNSET)
        contact_info: ContactInfo | Unset
        if isinstance(_contact_info,  Unset):
            contact_info = UNSET
        else:
            contact_info = ContactInfo.from_dict(_contact_info)




        target_shop_codes = cast(list[str], d.pop("target_shop_codes", UNSET))


        _target_seller_types = d.pop("target_seller_types", UNSET)
        target_seller_types: list[EditAffiliatePartnerCampaignRequestTargetSellerTypesItem] | Unset = UNSET
        if _target_seller_types is not UNSET:
            target_seller_types = []
            for target_seller_types_item_data in _target_seller_types:
                target_seller_types_item = EditAffiliatePartnerCampaignRequestTargetSellerTypesItem(target_seller_types_item_data)



                target_seller_types.append(target_seller_types_item)


        edit_affiliate_partner_campaign_request = cls(
            name=name,
            description=description,
            campaign_start_time=campaign_start_time,
            campaign_end_time=campaign_end_time,
            registration_start_time=registration_start_time,
            registration_end_time=registration_end_time,
            commission_rate=commission_rate,
            contact_info=contact_info,
            target_shop_codes=target_shop_codes,
            target_seller_types=target_seller_types,
        )


        edit_affiliate_partner_campaign_request.additional_properties = d
        return edit_affiliate_partner_campaign_request

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
