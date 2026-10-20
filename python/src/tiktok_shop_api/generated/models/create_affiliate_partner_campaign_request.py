from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_affiliate_partner_campaign_request_target_seller_types_item import CreateAffiliatePartnerCampaignRequestTargetSellerTypesItem
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_affiliate_partner_campaign_request_contact_info import CreateAffiliatePartnerCampaignRequestContactInfo





T = TypeVar("T", bound="CreateAffiliatePartnerCampaignRequest")



@_attrs_define
class CreateAffiliatePartnerCampaignRequest:
    """ 
        Attributes:
            name (str): The campaign name. Must contain 1 to 50 characters, inclusive, and must not start with a space.
            description (str): The campaign description. Must contain 1 to 1000 characters, inclusive, and must not start
                with a space.
            campaign_start_time (int): The scheduled campaign start time as a Unix timestamp in seconds. It must not be
                earlier than the current time. In subsequent edits, this value can be changed only when the campaign status is
                `READY` or `UPCOMING`.
            campaign_end_time (int): The scheduled campaign end time as a Unix timestamp in seconds. It must be later than
                `campaign_start_time`, and the campaign period must be between 1 and 360 days, inclusive. In subsequent edits,
                this value cannot be changed when the campaign status is `CLOSED`.
            registration_start_time (int): The scheduled start time for seller product registration as a Unix timestamp in
                seconds. It must be equal to `campaign_start_time`. In subsequent edits, this value can be changed only when the
                campaign status is `READY` or `UPCOMING`.
            registration_end_time (int): The scheduled end time for seller product registration as a Unix timestamp in
                seconds. It must be later than `registration_start_time`; the registration period must be at least 1 day and
                must not extend beyond `campaign_end_time`. In subsequent edits, this value cannot be changed when the campaign
                status is `CLOSED`.
            commission_rate (int): The total commission rate, in hundredths of a percent (0.01%) units, proposed by the
                affiliate partner for display to sellers. The value must be between 100 and 8000, inclusive.
            contact_info (CreateAffiliatePartnerCampaignRequestContactInfo):
            target_shop_codes (list[str] | Unset): A list of TikTok Shop seller shop codes that may register for the
                campaign. Find a seller's shop code in TikTok Shop Seller Central by selecting the Seller Profile icon in the
                top-right corner of the user interface. Specify exactly one of `target_shop_codes` and `target_seller_types`.
                The list must contain fewer than 100 items.
            target_seller_types (list[CreateAffiliatePartnerCampaignRequestTargetSellerTypesItem] | Unset): A list of
                eligible seller types that may register for the campaign. Use this field to target seller types instead of
                specific sellers in `target_shop_codes`. Specify exactly one of `target_seller_types` and `target_shop_codes`.
                Possible values:
                - `LOCAL`
                - `CROSS_BORDER`
     """

    name: str
    description: str
    campaign_start_time: int
    campaign_end_time: int
    registration_start_time: int
    registration_end_time: int
    commission_rate: int
    contact_info: CreateAffiliatePartnerCampaignRequestContactInfo
    target_shop_codes: list[str] | Unset = UNSET
    target_seller_types: list[CreateAffiliatePartnerCampaignRequestTargetSellerTypesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_affiliate_partner_campaign_request_contact_info import CreateAffiliatePartnerCampaignRequestContactInfo # noqa: PLC0415
        name = self.name

        description = self.description

        campaign_start_time = self.campaign_start_time

        campaign_end_time = self.campaign_end_time

        registration_start_time = self.registration_start_time

        registration_end_time = self.registration_end_time

        commission_rate = self.commission_rate

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
            "name": name,
            "description": description,
            "campaign_start_time": campaign_start_time,
            "campaign_end_time": campaign_end_time,
            "registration_start_time": registration_start_time,
            "registration_end_time": registration_end_time,
            "commission_rate": commission_rate,
            "contact_info": contact_info,
        })
        if target_shop_codes is not UNSET:
            field_dict["target_shop_codes"] = target_shop_codes
        if target_seller_types is not UNSET:
            field_dict["target_seller_types"] = target_seller_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_affiliate_partner_campaign_request_contact_info import CreateAffiliatePartnerCampaignRequestContactInfo # noqa: PLC0415
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        campaign_start_time = d.pop("campaign_start_time")

        campaign_end_time = d.pop("campaign_end_time")

        registration_start_time = d.pop("registration_start_time")

        registration_end_time = d.pop("registration_end_time")

        commission_rate = d.pop("commission_rate")

        contact_info = CreateAffiliatePartnerCampaignRequestContactInfo.from_dict(d.pop("contact_info"))




        target_shop_codes = cast(list[str], d.pop("target_shop_codes", UNSET))


        _target_seller_types = d.pop("target_seller_types", UNSET)
        target_seller_types: list[CreateAffiliatePartnerCampaignRequestTargetSellerTypesItem] | Unset = UNSET
        if _target_seller_types is not UNSET:
            target_seller_types = []
            for target_seller_types_item_data in _target_seller_types:
                target_seller_types_item = CreateAffiliatePartnerCampaignRequestTargetSellerTypesItem(target_seller_types_item_data)



                target_seller_types.append(target_seller_types_item)


        create_affiliate_partner_campaign_request = cls(
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


        create_affiliate_partner_campaign_request.additional_properties = d
        return create_affiliate_partner_campaign_request

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
