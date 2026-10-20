from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_info import ContactInfo
    from ..models.get_affiliate_partner_campaign_detail_response_data_target_shop import (
        GetAffiliatePartnerCampaignDetailResponseDataTargetShop,
    )


T = TypeVar("T", bound="GetAffiliatePartnerCampaignDetailResponseData")


@_attrs_define
class GetAffiliatePartnerCampaignDetailResponseData:
    """
    Attributes:
        id (str | Unset): The campaign identifier.
        name (str | Unset): The campaign name. Maximum length: 50 characters.
        description (str | Unset): The campaign description. Maximum length: 1000 characters.
        status (str | Unset): The campaign status. The status is an enumerated type with values:
            - READY
            - UPCOMING
            - ONGOING
            - CLOSED
        region (str | Unset): The region to which the campaign is associated.
        registration_start_time (int | Unset): The scheduled start time for seller product registration as a Unix
            timestamp in seconds. This field can be updated only when the campaign status is `READY` or `UPCOMING`.
        registration_end_time (int | Unset): The scheduled end time for seller product registration as a Unix timestamp
            in seconds. This field is no longer editable when the campaign status is `CLOSED`.
        campaign_start_time (int | Unset): The scheduled campaign start time as a Unix timestamp in seconds. This field
            can be updated only when the campaign status is `READY` or `UPCOMING`.
        campaign_end_time (int | Unset): The scheduled end time in Unix epoch time format for the campaign. Note that
            the end time must be less than 360 days from the start date. This field is no longer editable when the campaign
            status is set to `CLOSED`.
        commission_rate (int | Unset): The total commission rate in hundredths of a percent (0.01%) units proposed by
            the affiliate partner for display to sellers. Commission rate must be greater than 100 and less than 8000.
        contact_info (ContactInfo | Unset):
        target_shops (list[GetAffiliatePartnerCampaignDetailResponseDataTargetShop] | Unset): A list of TikTok Shop
            seller shop codes and names with permission to register for the campaign.
        target_seller_types (list[str] | Unset): A list of seller types eligible to register for the campaign. Use this
            field to broadly target seller types instead of the specific shops listed in `target_shops`. Possible values:
            - LOCAL
            - CROSS_BORDER
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    status: str | Unset = UNSET
    region: str | Unset = UNSET
    registration_start_time: int | Unset = UNSET
    registration_end_time: int | Unset = UNSET
    campaign_start_time: int | Unset = UNSET
    campaign_end_time: int | Unset = UNSET
    commission_rate: int | Unset = UNSET
    contact_info: ContactInfo | Unset = UNSET
    target_shops: list[GetAffiliatePartnerCampaignDetailResponseDataTargetShop] | Unset = UNSET
    target_seller_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        status = self.status

        region = self.region

        registration_start_time = self.registration_start_time

        registration_end_time = self.registration_end_time

        campaign_start_time = self.campaign_start_time

        campaign_end_time = self.campaign_end_time

        commission_rate = self.commission_rate

        contact_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.contact_info, Unset):
            contact_info = self.contact_info.to_dict()

        target_shops: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.target_shops, Unset):
            target_shops = []
            for target_shops_item_data in self.target_shops:
                target_shops_item = target_shops_item_data.to_dict()
                target_shops.append(target_shops_item)

        target_seller_types: list[str] | Unset = UNSET
        if not isinstance(self.target_seller_types, Unset):
            target_seller_types = self.target_seller_types

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if region is not UNSET:
            field_dict["region"] = region
        if registration_start_time is not UNSET:
            field_dict["registration_start_time"] = registration_start_time
        if registration_end_time is not UNSET:
            field_dict["registration_end_time"] = registration_end_time
        if campaign_start_time is not UNSET:
            field_dict["campaign_start_time"] = campaign_start_time
        if campaign_end_time is not UNSET:
            field_dict["campaign_end_time"] = campaign_end_time
        if commission_rate is not UNSET:
            field_dict["commission_rate"] = commission_rate
        if contact_info is not UNSET:
            field_dict["contact_info"] = contact_info
        if target_shops is not UNSET:
            field_dict["target_shops"] = target_shops
        if target_seller_types is not UNSET:
            field_dict["target_seller_types"] = target_seller_types

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_info import ContactInfo  # noqa: PLC0415
        from ..models.get_affiliate_partner_campaign_detail_response_data_target_shop import (
            GetAffiliatePartnerCampaignDetailResponseDataTargetShop,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        region = d.pop("region", UNSET)

        registration_start_time = d.pop("registration_start_time", UNSET)

        registration_end_time = d.pop("registration_end_time", UNSET)

        campaign_start_time = d.pop("campaign_start_time", UNSET)

        campaign_end_time = d.pop("campaign_end_time", UNSET)

        commission_rate = d.pop("commission_rate", UNSET)

        _contact_info = d.pop("contact_info", UNSET)
        contact_info: ContactInfo | Unset
        if isinstance(_contact_info, Unset):
            contact_info = UNSET
        else:
            contact_info = ContactInfo.from_dict(_contact_info)

        _target_shops = d.pop("target_shops", UNSET)
        target_shops: list[GetAffiliatePartnerCampaignDetailResponseDataTargetShop] | Unset = UNSET
        if _target_shops is not UNSET:
            target_shops = []
            for target_shops_item_data in _target_shops:
                target_shops_item = GetAffiliatePartnerCampaignDetailResponseDataTargetShop.from_dict(
                    target_shops_item_data
                )

                target_shops.append(target_shops_item)

        target_seller_types = cast(list[str], d.pop("target_seller_types", UNSET))

        get_affiliate_partner_campaign_detail_response_data = cls(
            id=id,
            name=name,
            description=description,
            status=status,
            region=region,
            registration_start_time=registration_start_time,
            registration_end_time=registration_end_time,
            campaign_start_time=campaign_start_time,
            campaign_end_time=campaign_end_time,
            commission_rate=commission_rate,
            contact_info=contact_info,
            target_shops=target_shops,
            target_seller_types=target_seller_types,
        )

        get_affiliate_partner_campaign_detail_response_data.additional_properties = d
        return get_affiliate_partner_campaign_detail_response_data

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
