from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAffiliatePartnerCampaignListResponseDataCampaign")


@_attrs_define
class GetAffiliatePartnerCampaignListResponseDataCampaign:
    """
    Attributes:
        id (str | Unset): The campaign identifier.
        name (str | Unset): The campaign name.
        status (str | Unset): The campaign status. The status is an enumerated type with values:
            - READY
            - UPCOMING
            - ONGOING
            - CLOSED
        registration_start_time (int | Unset): The scheduled start time in Unix epoch format for seller product
            registration. Note that this field can be updated when the campaign status is set to `READY` or `UPCOMING` only.
        registration_end_time (int | Unset): The scheduled end time in Unix epoch time format for seller product
            registration. This field is no longer editable when the campaign status is set to `CLOSED`.
        campaign_start_time (int | Unset): The scheduled start time in Unix epoch time format for the campaign. Note
            that this field can be updated when the campaign status is set to `READY` or `UPCOMING` only.
        campaign_end_time (int | Unset): The scheduled end time in Unix epoch time format for the campaign. Note that
            the end time must be less than 360 days from the start date. This field is no longer editable when the campaign
            status is set to `CLOSED`.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: str | Unset = UNSET
    registration_start_time: int | Unset = UNSET
    registration_end_time: int | Unset = UNSET
    campaign_start_time: int | Unset = UNSET
    campaign_end_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status

        registration_start_time = self.registration_start_time

        registration_end_time = self.registration_end_time

        campaign_start_time = self.campaign_start_time

        campaign_end_time = self.campaign_end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if registration_start_time is not UNSET:
            field_dict["registration_start_time"] = registration_start_time
        if registration_end_time is not UNSET:
            field_dict["registration_end_time"] = registration_end_time
        if campaign_start_time is not UNSET:
            field_dict["campaign_start_time"] = campaign_start_time
        if campaign_end_time is not UNSET:
            field_dict["campaign_end_time"] = campaign_end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        registration_start_time = d.pop("registration_start_time", UNSET)

        registration_end_time = d.pop("registration_end_time", UNSET)

        campaign_start_time = d.pop("campaign_start_time", UNSET)

        campaign_end_time = d.pop("campaign_end_time", UNSET)

        get_affiliate_partner_campaign_list_response_data_campaign = cls(
            id=id,
            name=name,
            status=status,
            registration_start_time=registration_start_time,
            registration_end_time=registration_end_time,
            campaign_start_time=campaign_start_time,
            campaign_end_time=campaign_end_time,
        )

        get_affiliate_partner_campaign_list_response_data_campaign.additional_properties = d
        return get_affiliate_partner_campaign_list_response_data_campaign

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
