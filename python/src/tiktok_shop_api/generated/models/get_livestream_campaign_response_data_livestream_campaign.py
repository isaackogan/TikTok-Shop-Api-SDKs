from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agreement import Agreement
  from ..models.benefit import Benefit
  from ..models.campaign_period import CampaignPeriod
  from ..models.get_livestream_campaign_response_data_livestream_campaign_participation_requirement import GetLivestreamCampaignResponseDataLivestreamCampaignParticipationRequirement
  from ..models.get_livestream_campaign_response_data_livestream_campaign_session_statistic import GetLivestreamCampaignResponseDataLivestreamCampaignSessionStatistic
  from ..models.get_livestream_campaign_response_data_livestream_campaign_super_livestream import GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestream
  from ..models.registration_period import RegistrationPeriod
  from ..models.registration_summary import RegistrationSummary





T = TypeVar("T", bound="GetLivestreamCampaignResponseDataLivestreamCampaign")



@_attrs_define
class GetLivestreamCampaignResponseDataLivestreamCampaign:
    """ 
        Attributes:
            agreement (Agreement | Unset):
            benefits (list[Benefit] | Unset): Benefits and exposure information applicable to the shop, including
                conditions, responsible parties, and limits. Does not guarantee returns.
            campaign_group_id (str | Unset): Positive ID of the campaign group. Omitted if unavailable. A decimal string
                from 1 to 9223372036854775807.
            campaign_period (CampaignPeriod | Unset):
            campaign_status (str | Unset): Campaign status, using the same enum as lists and other detail types. Omitted if
                unknown. Does not establish the shop's registration eligibility.
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
            description (str | Unset): Localized campaign introduction as sanitized HTML rich text, preserving text, images,
                links, and their order. Render as HTML rather than plain text. Scripts, event handlers, and unsafe URLs are
                removed. Omitted when no content is available. May not cover all participation rules, benefits, or fee terms.
            id (str | Unset): Always returned when the object exists and matches the requested livestream_campaign_id. A
                decimal string from 1 to 9223372036854775807.
            is_invited (bool | Unset): Whether the shop is invited. Omission means unknown. An invitation does not guarantee
                registration availability.
            participation_requirements (GetLivestreamCampaignResponseDataLivestreamCampaignParticipationRequirement |
                Unset):
            region (str | Unset): Campaign region, which may be EU. It need not match the authorized shop's region and does
                not extend shop authorization. Region codes follow [ISO 3166-1
                alpha-2](https://www.iso.org/obp/ui/#search/code/); EU is also supported as an aggregate campaign region. A
                listed code does not guarantee campaign availability or extend authorization.
            registration_period (RegistrationPeriod | Unset):
            registration_status (str | Unset): Campaign registration stage. Does not indicate whether the shop is already
                registered or can register.

                - NOT_STARTED: Registration has not started.
                - OPEN: Registration is open. Does not establish the shop's registration eligibility.
                - CLOSED: Registration has ended.
            registration_summary (RegistrationSummary | Unset):
            session_statistics (GetLivestreamCampaignResponseDataLivestreamCampaignSessionStatistic | Unset):
            subtype (str | Unset): Always returned when the object exists. Supports featured livestreams and livestream
                competitions only. Use GetShortVideoCampaign for short video campaigns.
                Livestream campaign subtype, represented separately from the broad category in CampaignType.
                - KEY_LIVESTREAM: Featured livestream, including those with super livestream settings enabled.
                - LIVESTREAM_COMPETITION: Livestream competition.
            super_livestream (GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestream | Unset):
            target_seller_type (str | Unset): Seller types targeted by the campaign, not the current seller's type. Omitted
                if unavailable.
                Seller types targeted by the campaign.
                - ALL: Local and cross-border sellers.
                - LOCAL: Local sellers.
                - CROSS_BORDER: Cross-border sellers.
            title (str | Unset): Localized campaign name. Uses the default name if text in the requested language is
                missing. Omitted if the requested-language name is explicitly empty or no name is ultimately available.
            type_ (str | Unset): Always returned when the object exists. Fixed to LIVESTREAM, consistent with the campaign
                type in lists.
                Unified campaign type with the same semantics in lists and all four detail models. Distinct from campaign group
                type.
                - PRODUCT: Product campaign.
                - SHOP: Shop campaign.
                - LIVESTREAM: Livestream campaign.
                - SHORT_VIDEO: Short video campaign.
     """

    agreement: Agreement | Unset = UNSET
    benefits: list[Benefit] | Unset = UNSET
    campaign_group_id: str | Unset = UNSET
    campaign_period: CampaignPeriod | Unset = UNSET
    campaign_status: str | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    is_invited: bool | Unset = UNSET
    participation_requirements: GetLivestreamCampaignResponseDataLivestreamCampaignParticipationRequirement | Unset = UNSET
    region: str | Unset = UNSET
    registration_period: RegistrationPeriod | Unset = UNSET
    registration_status: str | Unset = UNSET
    registration_summary: RegistrationSummary | Unset = UNSET
    session_statistics: GetLivestreamCampaignResponseDataLivestreamCampaignSessionStatistic | Unset = UNSET
    subtype: str | Unset = UNSET
    super_livestream: GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestream | Unset = UNSET
    target_seller_type: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agreement import Agreement # noqa: PLC0415
        from ..models.benefit import Benefit # noqa: PLC0415
        from ..models.campaign_period import CampaignPeriod # noqa: PLC0415
        from ..models.get_livestream_campaign_response_data_livestream_campaign_participation_requirement import GetLivestreamCampaignResponseDataLivestreamCampaignParticipationRequirement # noqa: PLC0415
        from ..models.get_livestream_campaign_response_data_livestream_campaign_session_statistic import GetLivestreamCampaignResponseDataLivestreamCampaignSessionStatistic # noqa: PLC0415
        from ..models.get_livestream_campaign_response_data_livestream_campaign_super_livestream import GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestream # noqa: PLC0415
        from ..models.registration_period import RegistrationPeriod # noqa: PLC0415
        from ..models.registration_summary import RegistrationSummary # noqa: PLC0415
        agreement: dict[str, Any] | Unset = UNSET
        if not isinstance(self.agreement, Unset):
            agreement = self.agreement.to_dict()

        benefits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.benefits, Unset):
            benefits = []
            for benefits_item_data in self.benefits:
                benefits_item = benefits_item_data.to_dict()
                benefits.append(benefits_item)



        campaign_group_id = self.campaign_group_id

        campaign_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.campaign_period, Unset):
            campaign_period = self.campaign_period.to_dict()

        campaign_status = self.campaign_status

        description = self.description

        id = self.id

        is_invited = self.is_invited

        participation_requirements: dict[str, Any] | Unset = UNSET
        if not isinstance(self.participation_requirements, Unset):
            participation_requirements = self.participation_requirements.to_dict()

        region = self.region

        registration_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_period, Unset):
            registration_period = self.registration_period.to_dict()

        registration_status = self.registration_status

        registration_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_summary, Unset):
            registration_summary = self.registration_summary.to_dict()

        session_statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.session_statistics, Unset):
            session_statistics = self.session_statistics.to_dict()

        subtype = self.subtype

        super_livestream: dict[str, Any] | Unset = UNSET
        if not isinstance(self.super_livestream, Unset):
            super_livestream = self.super_livestream.to_dict()

        target_seller_type = self.target_seller_type

        title = self.title

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if agreement is not UNSET:
            field_dict["agreement"] = agreement
        if benefits is not UNSET:
            field_dict["benefits"] = benefits
        if campaign_group_id is not UNSET:
            field_dict["campaign_group_id"] = campaign_group_id
        if campaign_period is not UNSET:
            field_dict["campaign_period"] = campaign_period
        if campaign_status is not UNSET:
            field_dict["campaign_status"] = campaign_status
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if is_invited is not UNSET:
            field_dict["is_invited"] = is_invited
        if participation_requirements is not UNSET:
            field_dict["participation_requirements"] = participation_requirements
        if region is not UNSET:
            field_dict["region"] = region
        if registration_period is not UNSET:
            field_dict["registration_period"] = registration_period
        if registration_status is not UNSET:
            field_dict["registration_status"] = registration_status
        if registration_summary is not UNSET:
            field_dict["registration_summary"] = registration_summary
        if session_statistics is not UNSET:
            field_dict["session_statistics"] = session_statistics
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if super_livestream is not UNSET:
            field_dict["super_livestream"] = super_livestream
        if target_seller_type is not UNSET:
            field_dict["target_seller_type"] = target_seller_type
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agreement import Agreement # noqa: PLC0415
        from ..models.benefit import Benefit # noqa: PLC0415
        from ..models.campaign_period import CampaignPeriod # noqa: PLC0415
        from ..models.get_livestream_campaign_response_data_livestream_campaign_participation_requirement import GetLivestreamCampaignResponseDataLivestreamCampaignParticipationRequirement # noqa: PLC0415
        from ..models.get_livestream_campaign_response_data_livestream_campaign_session_statistic import GetLivestreamCampaignResponseDataLivestreamCampaignSessionStatistic # noqa: PLC0415
        from ..models.get_livestream_campaign_response_data_livestream_campaign_super_livestream import GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestream # noqa: PLC0415
        from ..models.registration_period import RegistrationPeriod # noqa: PLC0415
        from ..models.registration_summary import RegistrationSummary # noqa: PLC0415
        d = dict(src_dict)
        _agreement = d.pop("agreement", UNSET)
        agreement: Agreement | Unset
        if isinstance(_agreement,  Unset):
            agreement = UNSET
        else:
            agreement = Agreement.from_dict(_agreement)




        _benefits = d.pop("benefits", UNSET)
        benefits: list[Benefit] | Unset = UNSET
        if _benefits is not UNSET:
            benefits = []
            for benefits_item_data in _benefits:
                benefits_item = Benefit.from_dict(benefits_item_data)



                benefits.append(benefits_item)


        campaign_group_id = d.pop("campaign_group_id", UNSET)

        _campaign_period = d.pop("campaign_period", UNSET)
        campaign_period: CampaignPeriod | Unset
        if isinstance(_campaign_period,  Unset):
            campaign_period = UNSET
        else:
            campaign_period = CampaignPeriod.from_dict(_campaign_period)




        campaign_status = d.pop("campaign_status", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        is_invited = d.pop("is_invited", UNSET)

        _participation_requirements = d.pop("participation_requirements", UNSET)
        participation_requirements: GetLivestreamCampaignResponseDataLivestreamCampaignParticipationRequirement | Unset
        if isinstance(_participation_requirements,  Unset):
            participation_requirements = UNSET
        else:
            participation_requirements = GetLivestreamCampaignResponseDataLivestreamCampaignParticipationRequirement.from_dict(_participation_requirements)




        region = d.pop("region", UNSET)

        _registration_period = d.pop("registration_period", UNSET)
        registration_period: RegistrationPeriod | Unset
        if isinstance(_registration_period,  Unset):
            registration_period = UNSET
        else:
            registration_period = RegistrationPeriod.from_dict(_registration_period)




        registration_status = d.pop("registration_status", UNSET)

        _registration_summary = d.pop("registration_summary", UNSET)
        registration_summary: RegistrationSummary | Unset
        if isinstance(_registration_summary,  Unset):
            registration_summary = UNSET
        else:
            registration_summary = RegistrationSummary.from_dict(_registration_summary)




        _session_statistics = d.pop("session_statistics", UNSET)
        session_statistics: GetLivestreamCampaignResponseDataLivestreamCampaignSessionStatistic | Unset
        if isinstance(_session_statistics,  Unset):
            session_statistics = UNSET
        else:
            session_statistics = GetLivestreamCampaignResponseDataLivestreamCampaignSessionStatistic.from_dict(_session_statistics)




        subtype = d.pop("subtype", UNSET)

        _super_livestream = d.pop("super_livestream", UNSET)
        super_livestream: GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestream | Unset
        if isinstance(_super_livestream,  Unset):
            super_livestream = UNSET
        else:
            super_livestream = GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestream.from_dict(_super_livestream)




        target_seller_type = d.pop("target_seller_type", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        get_livestream_campaign_response_data_livestream_campaign = cls(
            agreement=agreement,
            benefits=benefits,
            campaign_group_id=campaign_group_id,
            campaign_period=campaign_period,
            campaign_status=campaign_status,
            description=description,
            id=id,
            is_invited=is_invited,
            participation_requirements=participation_requirements,
            region=region,
            registration_period=registration_period,
            registration_status=registration_status,
            registration_summary=registration_summary,
            session_statistics=session_statistics,
            subtype=subtype,
            super_livestream=super_livestream,
            target_seller_type=target_seller_type,
            title=title,
            type_=type_,
        )


        get_livestream_campaign_response_data_livestream_campaign.additional_properties = d
        return get_livestream_campaign_response_data_livestream_campaign

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
