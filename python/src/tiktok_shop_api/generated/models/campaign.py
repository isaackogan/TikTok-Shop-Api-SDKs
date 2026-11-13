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
  from ..models.list_campaign_group_response_data_campaign_group_campaign_registration_summary import ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummary
  from ..models.participation_relation import ParticipationRelation
  from ..models.pending_registration_statistic import PendingRegistrationStatistic
  from ..models.registration_period import RegistrationPeriod





T = TypeVar("T", bound="Campaign")



@_attrs_define
class Campaign:
    """ 
        Attributes:
            campaign_period (CampaignPeriod | Unset):
            campaign_status (str | Unset): Campaign status, using the same enum as campaign details. Omitted if unavailable
                or unknown. Distinct from the registration stage and the shop's registration status.
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
            description (str | Unset): Campaign summary text. Prefers a nonempty description in the requested language,
                falling back to the default description if missing or empty. Omitted if no description is available after
                fallback. Does not include the full detail description.
            has_joined (bool | Unset): Whether the shop has an existing participation record. Omission means no result was
                provided. A record does not establish current approval, effective benefits, or permission to register again.
            id (str | Unset): Positive campaign ID, always returned for each item. Use type to select the product, shop,
                livestream, or short video detail endpoint. A decimal string from 1 to 9223372036854775807.
            is_invited (bool | Unset): Whether the shop is invited. Omission means no result was provided. An invitation
                does not establish registration eligibility.
            participation_relation (ParticipationRelation | Unset):
            pending_registration_statistics (PendingRegistrationStatistic | Unset):
            region (str | Unset): Campaign region, which may be EU and need not match the authorized shop's region. Region
                codes follow [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#search/code/); EU is also supported as an
                aggregate campaign region. A listed code does not guarantee campaign availability or extend authorization.
            registration_mode (str | Unset): Product campaign registration mode, distinguishing standard registration from
                ongoing participation. Omitted for other campaign types. Omission means the mode is unknown. Independent of the
                parent campaign group's type and whether the shop is registered.
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
            registration_summary (ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummary | Unset):
            subtypes (list[str] | Unset): Distinct campaign subtypes. Returns [] when there are explicitly no subtypes;
                omitted if unavailable or not fully representable. Order does not indicate priority.
            title (str | Unset): Task and long-term campaigns retain their original names. Other campaigns prefer a nonempty
                name in the requested language, falling back to the default name if missing or empty. Omitted if no name is
                available after fallback.
            type_ (str | Unset): Always returned for the four defined campaign types. For an unknown type, the summary is
                retained and this field is omitted. Callers must not guess the type or select a detail endpoint without it.
                Unified campaign type with the same semantics in lists and all four detail models. Distinct from campaign group
                type.
                - PRODUCT: Product campaign.
                - SHOP: Shop campaign.
                - LIVESTREAM: Livestream campaign.
                - SHORT_VIDEO: Short video campaign.
     """

    campaign_period: CampaignPeriod | Unset = UNSET
    campaign_status: str | Unset = UNSET
    description: str | Unset = UNSET
    has_joined: bool | Unset = UNSET
    id: str | Unset = UNSET
    is_invited: bool | Unset = UNSET
    participation_relation: ParticipationRelation | Unset = UNSET
    pending_registration_statistics: PendingRegistrationStatistic | Unset = UNSET
    region: str | Unset = UNSET
    registration_mode: str | Unset = UNSET
    registration_period: RegistrationPeriod | Unset = UNSET
    registration_summary: ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummary | Unset = UNSET
    subtypes: list[str] | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.campaign_period import CampaignPeriod # noqa: PLC0415
        from ..models.list_campaign_group_response_data_campaign_group_campaign_registration_summary import ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummary # noqa: PLC0415
        from ..models.participation_relation import ParticipationRelation # noqa: PLC0415
        from ..models.pending_registration_statistic import PendingRegistrationStatistic # noqa: PLC0415
        from ..models.registration_period import RegistrationPeriod # noqa: PLC0415
        campaign_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.campaign_period, Unset):
            campaign_period = self.campaign_period.to_dict()

        campaign_status = self.campaign_status

        description = self.description

        has_joined = self.has_joined

        id = self.id

        is_invited = self.is_invited

        participation_relation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.participation_relation, Unset):
            participation_relation = self.participation_relation.to_dict()

        pending_registration_statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pending_registration_statistics, Unset):
            pending_registration_statistics = self.pending_registration_statistics.to_dict()

        region = self.region

        registration_mode = self.registration_mode

        registration_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_period, Unset):
            registration_period = self.registration_period.to_dict()

        registration_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_summary, Unset):
            registration_summary = self.registration_summary.to_dict()

        subtypes: list[str] | Unset = UNSET
        if not isinstance(self.subtypes, Unset):
            subtypes = self.subtypes



        title = self.title

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if campaign_period is not UNSET:
            field_dict["campaign_period"] = campaign_period
        if campaign_status is not UNSET:
            field_dict["campaign_status"] = campaign_status
        if description is not UNSET:
            field_dict["description"] = description
        if has_joined is not UNSET:
            field_dict["has_joined"] = has_joined
        if id is not UNSET:
            field_dict["id"] = id
        if is_invited is not UNSET:
            field_dict["is_invited"] = is_invited
        if participation_relation is not UNSET:
            field_dict["participation_relation"] = participation_relation
        if pending_registration_statistics is not UNSET:
            field_dict["pending_registration_statistics"] = pending_registration_statistics
        if region is not UNSET:
            field_dict["region"] = region
        if registration_mode is not UNSET:
            field_dict["registration_mode"] = registration_mode
        if registration_period is not UNSET:
            field_dict["registration_period"] = registration_period
        if registration_summary is not UNSET:
            field_dict["registration_summary"] = registration_summary
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
        from ..models.list_campaign_group_response_data_campaign_group_campaign_registration_summary import ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummary # noqa: PLC0415
        from ..models.participation_relation import ParticipationRelation # noqa: PLC0415
        from ..models.pending_registration_statistic import PendingRegistrationStatistic # noqa: PLC0415
        from ..models.registration_period import RegistrationPeriod # noqa: PLC0415
        d = dict(src_dict)
        _campaign_period = d.pop("campaign_period", UNSET)
        campaign_period: CampaignPeriod | Unset
        if isinstance(_campaign_period,  Unset):
            campaign_period = UNSET
        else:
            campaign_period = CampaignPeriod.from_dict(_campaign_period)




        campaign_status = d.pop("campaign_status", UNSET)

        description = d.pop("description", UNSET)

        has_joined = d.pop("has_joined", UNSET)

        id = d.pop("id", UNSET)

        is_invited = d.pop("is_invited", UNSET)

        _participation_relation = d.pop("participation_relation", UNSET)
        participation_relation: ParticipationRelation | Unset
        if isinstance(_participation_relation,  Unset):
            participation_relation = UNSET
        else:
            participation_relation = ParticipationRelation.from_dict(_participation_relation)




        _pending_registration_statistics = d.pop("pending_registration_statistics", UNSET)
        pending_registration_statistics: PendingRegistrationStatistic | Unset
        if isinstance(_pending_registration_statistics,  Unset):
            pending_registration_statistics = UNSET
        else:
            pending_registration_statistics = PendingRegistrationStatistic.from_dict(_pending_registration_statistics)




        region = d.pop("region", UNSET)

        registration_mode = d.pop("registration_mode", UNSET)

        _registration_period = d.pop("registration_period", UNSET)
        registration_period: RegistrationPeriod | Unset
        if isinstance(_registration_period,  Unset):
            registration_period = UNSET
        else:
            registration_period = RegistrationPeriod.from_dict(_registration_period)




        _registration_summary = d.pop("registration_summary", UNSET)
        registration_summary: ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummary | Unset
        if isinstance(_registration_summary,  Unset):
            registration_summary = UNSET
        else:
            registration_summary = ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummary.from_dict(_registration_summary)




        subtypes = cast(list[str], d.pop("subtypes", UNSET))


        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        campaign = cls(
            campaign_period=campaign_period,
            campaign_status=campaign_status,
            description=description,
            has_joined=has_joined,
            id=id,
            is_invited=is_invited,
            participation_relation=participation_relation,
            pending_registration_statistics=pending_registration_statistics,
            region=region,
            registration_mode=registration_mode,
            registration_period=registration_period,
            registration_summary=registration_summary,
            subtypes=subtypes,
            title=title,
            type_=type_,
        )


        campaign.additional_properties = d
        return campaign

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
