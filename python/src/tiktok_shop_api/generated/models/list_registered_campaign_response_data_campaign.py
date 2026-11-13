from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.campaign_period import CampaignPeriod
  from ..models.list_registered_campaign_response_data_campaign_bargain_statistic import ListRegisteredCampaignResponseDataCampaignBargainStatistic
  from ..models.list_registered_campaign_response_data_campaign_registration_statistic import ListRegisteredCampaignResponseDataCampaignRegistrationStatistic
  from ..models.registration_period import RegistrationPeriod





T = TypeVar("T", bound="ListRegisteredCampaignResponseDataCampaign")



@_attrs_define
class ListRegisteredCampaignResponseDataCampaign:
    """ 
        Attributes:
            bargain_statistics (ListRegisteredCampaignResponseDataCampaignBargainStatistic | Unset):
            campaign_period (CampaignPeriod | Unset):
            campaign_status (str | Unset): Campaign status, using the same enum as other lists and details. Omitted if
                unavailable or unknown. Distinct from the shop's registration status.
                Unified status for product, shop, livestream, and short video campaigns, shared by lists and details. Campaign
                groups use CampaignGroupStatus.
                Represents the overall campaign process, separately from the registration period, participation eligibility, and
                review status of the shop's registration.
                DEACTIVATED is returned only when deactivation is explicitly distinguished. Campaigns already classified as
                EXPIRED retain EXPIRED; the specific reason for ending is not inferred.
                - INEFFECTIVE: The campaign is not yet effective or is currently unavailable.
                - UPCOMING: Registration has not started. This does not simply mean that the campaign execution period has not
                started.
                - ACTIVE: The campaign process is open, covering the period from registration opening to campaign completion,
                including registration, the wait for campaign execution, and execution itself. It does not mean that
                registration is still open, campaign execution has started, or benefits are effective for the shop.
                - EXPIRED: The campaign has ended or is no longer effective. May include deactivated campaigns whose
                deactivation is not distinguished; it does not guarantee a scheduled end.
                - DEACTIVATED: The campaign is explicitly deactivated. Not inferred from time intervals or EXPIRED status.
            id (str | Unset): Positive campaign ID, always returned for each item. Use type to select one of the four detail
                endpoints. Do not use a campaign group ID. A decimal string from 1 to 9223372036854775807.
            region (str | Unset): Campaign region, which may be EU. It need not match the authorized shop's region and does
                not grant access to additional shops. Region codes follow [ISO 3166-1
                alpha-2](https://www.iso.org/obp/ui/#search/code/); EU is also supported as an aggregate campaign region. A
                listed code does not guarantee campaign availability or extend authorization.
            registration_mode (str | Unset): Product campaign registration mode, with the same meaning as registration_mode
                in Campaign. Omitted for other campaign types. Omission means the mode is unknown.
                Product campaign registration mode. Independent of the four campaign types, direct or bundle participation, and
                whether the shop is registered.
                Describes the participation model offered by the campaign. Rolling registration may cover linked campaigns;
                standard registration does not imply ongoing participation.
                Omission means the registration mode is unknown, not STANDARD. Do not infer the mode from the title or whether
                the linked campaign list is empty.
                - STANDARD: Standard registration without ongoing participation in linked campaigns. Does not mean registration
                is limited to once; actual registration limits and bundle participation must be assessed separately.
                - ROLLING: Ongoing registration that can enable continued participation in linked campaigns according to their
                rules. Does not guarantee existing registration, synchronization, or eligibility for all linked campaigns.
            registration_period (RegistrationPeriod | Unset):
            registration_statistics (ListRegisteredCampaignResponseDataCampaignRegistrationStatistic | Unset):
            subtypes (list[str] | Unset): Distinct campaign subtypes. Order does not indicate priority. Returns [] when
                there are explicitly no subtypes; omitted if unknown or not fully representable.
            title (str | Unset): Nonempty name returned according to the registered campaign list's localization rules.
                Omitted if unavailable; no placeholder is used.
            type_ (str | Unset): Campaign type. Returns the corresponding value for the four known types. For an unknown
                type, the summary is retained and this field is omitted. Do not guess a detail endpoint or statistics unit.
                Unified campaign type with the same semantics in lists and all four detail models. Distinct from campaign group
                type.
                - PRODUCT: Product campaign.
                - SHOP: Shop campaign.
                - LIVESTREAM: Livestream campaign.
                - SHORT_VIDEO: Short video campaign.
     """

    bargain_statistics: ListRegisteredCampaignResponseDataCampaignBargainStatistic | Unset = UNSET
    campaign_period: CampaignPeriod | Unset = UNSET
    campaign_status: str | Unset = UNSET
    id: str | Unset = UNSET
    region: str | Unset = UNSET
    registration_mode: str | Unset = UNSET
    registration_period: RegistrationPeriod | Unset = UNSET
    registration_statistics: ListRegisteredCampaignResponseDataCampaignRegistrationStatistic | Unset = UNSET
    subtypes: list[str] | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.campaign_period import CampaignPeriod # noqa: PLC0415
        from ..models.list_registered_campaign_response_data_campaign_bargain_statistic import ListRegisteredCampaignResponseDataCampaignBargainStatistic # noqa: PLC0415
        from ..models.list_registered_campaign_response_data_campaign_registration_statistic import ListRegisteredCampaignResponseDataCampaignRegistrationStatistic # noqa: PLC0415
        from ..models.registration_period import RegistrationPeriod # noqa: PLC0415
        bargain_statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bargain_statistics, Unset):
            bargain_statistics = self.bargain_statistics.to_dict()

        campaign_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.campaign_period, Unset):
            campaign_period = self.campaign_period.to_dict()

        campaign_status = self.campaign_status

        id = self.id

        region = self.region

        registration_mode = self.registration_mode

        registration_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_period, Unset):
            registration_period = self.registration_period.to_dict()

        registration_statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_statistics, Unset):
            registration_statistics = self.registration_statistics.to_dict()

        subtypes: list[str] | Unset = UNSET
        if not isinstance(self.subtypes, Unset):
            subtypes = self.subtypes



        title = self.title

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bargain_statistics is not UNSET:
            field_dict["bargain_statistics"] = bargain_statistics
        if campaign_period is not UNSET:
            field_dict["campaign_period"] = campaign_period
        if campaign_status is not UNSET:
            field_dict["campaign_status"] = campaign_status
        if id is not UNSET:
            field_dict["id"] = id
        if region is not UNSET:
            field_dict["region"] = region
        if registration_mode is not UNSET:
            field_dict["registration_mode"] = registration_mode
        if registration_period is not UNSET:
            field_dict["registration_period"] = registration_period
        if registration_statistics is not UNSET:
            field_dict["registration_statistics"] = registration_statistics
        if subtypes is not UNSET:
            field_dict["subtypes"] = subtypes
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.campaign_period import CampaignPeriod # noqa: PLC0415
        from ..models.list_registered_campaign_response_data_campaign_bargain_statistic import ListRegisteredCampaignResponseDataCampaignBargainStatistic # noqa: PLC0415
        from ..models.list_registered_campaign_response_data_campaign_registration_statistic import ListRegisteredCampaignResponseDataCampaignRegistrationStatistic # noqa: PLC0415
        from ..models.registration_period import RegistrationPeriod # noqa: PLC0415
        d = dict(src_dict)
        _bargain_statistics = d.pop("bargain_statistics", UNSET)
        bargain_statistics: ListRegisteredCampaignResponseDataCampaignBargainStatistic | Unset
        if isinstance(_bargain_statistics,  Unset):
            bargain_statistics = UNSET
        else:
            bargain_statistics = ListRegisteredCampaignResponseDataCampaignBargainStatistic.from_dict(_bargain_statistics)




        _campaign_period = d.pop("campaign_period", UNSET)
        campaign_period: CampaignPeriod | Unset
        if isinstance(_campaign_period,  Unset):
            campaign_period = UNSET
        else:
            campaign_period = CampaignPeriod.from_dict(_campaign_period)




        campaign_status = d.pop("campaign_status", UNSET)

        id = d.pop("id", UNSET)

        region = d.pop("region", UNSET)

        registration_mode = d.pop("registration_mode", UNSET)

        _registration_period = d.pop("registration_period", UNSET)
        registration_period: RegistrationPeriod | Unset
        if isinstance(_registration_period,  Unset):
            registration_period = UNSET
        else:
            registration_period = RegistrationPeriod.from_dict(_registration_period)




        _registration_statistics = d.pop("registration_statistics", UNSET)
        registration_statistics: ListRegisteredCampaignResponseDataCampaignRegistrationStatistic | Unset
        if isinstance(_registration_statistics,  Unset):
            registration_statistics = UNSET
        else:
            registration_statistics = ListRegisteredCampaignResponseDataCampaignRegistrationStatistic.from_dict(_registration_statistics)




        subtypes = cast(list[str], d.pop("subtypes", UNSET))


        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        list_registered_campaign_response_data_campaign = cls(
            bargain_statistics=bargain_statistics,
            campaign_period=campaign_period,
            campaign_status=campaign_status,
            id=id,
            region=region,
            registration_mode=registration_mode,
            registration_period=registration_period,
            registration_statistics=registration_statistics,
            subtypes=subtypes,
            title=title,
            type_=type_,
        )


        list_registered_campaign_response_data_campaign.additional_properties = d
        return list_registered_campaign_response_data_campaign

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
