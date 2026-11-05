from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.creator_preference import CreatorPreference





T = TypeVar("T", bound="GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerCampaignExtra")



@_attrs_define
class GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerCampaignExtra:
    """ 
        Attributes:
            creator_preferences (CreatorPreference | Unset):
            exclusives (list[str] | Unset): Selected exclusive benefits, represented by the Starling keys from the campaign-
                configuration options.
            invited_agency_num (int | Unset): Number of agencies invited to the seller campaign.
            max_total_commission_rate (int | Unset): Maximum total commission rate for the seller campaign, expressed as the
                percentage
                multiplied by 100.
            min_total_commission_rate (int | Unset): Minimum total commission rate for the seller campaign, expressed as the
                percentage
                multiplied by 100.
            objectives (list[str] | Unset): Selected collaboration objectives, represented by the Starling keys from the
                campaign-
                configuration options.
            parent_campaign_id (str | Unset): ID of the parent seller campaign associated with this sub-campaign, encoded as
                a string.
            registration_type (str | Unset): Agency registration policy. ALL_AGENCIES allows all eligible agencies to
                register; INVITE_ONLY allows only invited agencies.
            sample_availability (str | Unset): Text describing sample availability for the campaign. This is distinct from a
                product-level
                sample quota.
     """

    creator_preferences: CreatorPreference | Unset = UNSET
    exclusives: list[str] | Unset = UNSET
    invited_agency_num: int | Unset = UNSET
    max_total_commission_rate: int | Unset = UNSET
    min_total_commission_rate: int | Unset = UNSET
    objectives: list[str] | Unset = UNSET
    parent_campaign_id: str | Unset = UNSET
    registration_type: str | Unset = UNSET
    sample_availability: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.creator_preference import CreatorPreference # noqa: PLC0415
        creator_preferences: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator_preferences, Unset):
            creator_preferences = self.creator_preferences.to_dict()

        exclusives: list[str] | Unset = UNSET
        if not isinstance(self.exclusives, Unset):
            exclusives = self.exclusives



        invited_agency_num = self.invited_agency_num

        max_total_commission_rate = self.max_total_commission_rate

        min_total_commission_rate = self.min_total_commission_rate

        objectives: list[str] | Unset = UNSET
        if not isinstance(self.objectives, Unset):
            objectives = self.objectives



        parent_campaign_id = self.parent_campaign_id

        registration_type = self.registration_type

        sample_availability = self.sample_availability


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if creator_preferences is not UNSET:
            field_dict["creator_preferences"] = creator_preferences
        if exclusives is not UNSET:
            field_dict["exclusives"] = exclusives
        if invited_agency_num is not UNSET:
            field_dict["invited_agency_num"] = invited_agency_num
        if max_total_commission_rate is not UNSET:
            field_dict["max_total_commission_rate"] = max_total_commission_rate
        if min_total_commission_rate is not UNSET:
            field_dict["min_total_commission_rate"] = min_total_commission_rate
        if objectives is not UNSET:
            field_dict["objectives"] = objectives
        if parent_campaign_id is not UNSET:
            field_dict["parent_campaign_id"] = parent_campaign_id
        if registration_type is not UNSET:
            field_dict["registration_type"] = registration_type
        if sample_availability is not UNSET:
            field_dict["sample_availability"] = sample_availability

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator_preference import CreatorPreference # noqa: PLC0415
        d = dict(src_dict)
        _creator_preferences = d.pop("creator_preferences", UNSET)
        creator_preferences: CreatorPreference | Unset
        if isinstance(_creator_preferences,  Unset):
            creator_preferences = UNSET
        else:
            creator_preferences = CreatorPreference.from_dict(_creator_preferences)




        exclusives = cast(list[str], d.pop("exclusives", UNSET))


        invited_agency_num = d.pop("invited_agency_num", UNSET)

        max_total_commission_rate = d.pop("max_total_commission_rate", UNSET)

        min_total_commission_rate = d.pop("min_total_commission_rate", UNSET)

        objectives = cast(list[str], d.pop("objectives", UNSET))


        parent_campaign_id = d.pop("parent_campaign_id", UNSET)

        registration_type = d.pop("registration_type", UNSET)

        sample_availability = d.pop("sample_availability", UNSET)

        get_seller_partner_campaign_detail_response_data_campaign_detail_seller_campaign_extra = cls(
            creator_preferences=creator_preferences,
            exclusives=exclusives,
            invited_agency_num=invited_agency_num,
            max_total_commission_rate=max_total_commission_rate,
            min_total_commission_rate=min_total_commission_rate,
            objectives=objectives,
            parent_campaign_id=parent_campaign_id,
            registration_type=registration_type,
            sample_availability=sample_availability,
        )


        get_seller_partner_campaign_detail_response_data_campaign_detail_seller_campaign_extra.additional_properties = d
        return get_seller_partner_campaign_detail_response_data_campaign_detail_seller_campaign_extra

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
