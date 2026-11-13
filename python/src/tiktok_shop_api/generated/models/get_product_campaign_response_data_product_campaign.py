from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.benefit import Benefit
  from ..models.campaign_group import CampaignGroup
  from ..models.campaign_period import CampaignPeriod
  from ..models.get_product_campaign_response_data_product_campaign_fee import GetProductCampaignResponseDataProductCampaignFee
  from ..models.get_product_campaign_response_data_product_campaign_linked_campaign import GetProductCampaignResponseDataProductCampaignLinkedCampaign
  from ..models.get_product_campaign_response_data_product_campaign_participation_rule import GetProductCampaignResponseDataProductCampaignParticipationRule
  from ..models.get_product_campaign_response_data_product_campaign_registration_limit import GetProductCampaignResponseDataProductCampaignRegistrationLimit
  from ..models.get_product_campaign_response_data_product_campaign_registration_period import GetProductCampaignResponseDataProductCampaignRegistrationPeriod
  from ..models.get_product_campaign_response_data_product_campaign_shop_participation import GetProductCampaignResponseDataProductCampaignShopParticipation
  from ..models.registration_availability import RegistrationAvailability
  from ..models.shop_eligibility import ShopEligibility





T = TypeVar("T", bound="GetProductCampaignResponseDataProductCampaign")



@_attrs_define
class GetProductCampaignResponseDataProductCampaign:
    """ 
        Attributes:
            available_regions (list[str] | Unset): Specific country or region codes covered by this campaign, when
                available. For a campaign whose region is EU, this list identifies the specific countries covered. This field is
                not restricted to EU campaigns. Omission does not mean unrestricted regional coverage. A listed region does not
                establish the shop's eligibility to register or extend its authorization scope.
            benefits (list[Benefit] | Unset): Always returned. General campaign benefits and conditions applicable to the
                shop, excluding per-product tier benefits. Returns [] if no information is available.
            campaign_group (CampaignGroup | Unset):
            campaign_period (CampaignPeriod | Unset):
            campaign_status (str | Unset): Always returned. Uses the same enum as lists and other detail types. Does not
                directly indicate whether the current time is within the campaign execution period.
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
            fees (GetProductCampaignResponseDataProductCampaignFee | Unset):
            id (str | Unset): Always returned and matches the requested product_campaign_id. A decimal string from 1 to
                9223372036854775807.
            linked_campaigns (list[GetProductCampaignResponseDataProductCampaignLinkedCampaign] | Unset): Summaries of
                specific campaigns linked through rolling registration. Applicable only to ROLLING mode and not paginated
                separately. Omitted if unavailable. [] means no linked summaries were returned for this query, not that no other
                links exist. Excludes nested relationships, full campaign details, and synchronization statistics.
            participation_rules (GetProductCampaignResponseDataProductCampaignParticipationRule | Unset):
            region (str | Unset): Always returned. Applicable campaign region, which may be EU and need not match the
                authorized shop's shop_region. Region codes follow [ISO 3166-1
                alpha-2](https://www.iso.org/obp/ui/#search/code/); EU is also supported as an aggregate campaign region. A
                listed code does not guarantee campaign availability or extend authorization.
            registration_availability (RegistrationAvailability | Unset):
            registration_limit (GetProductCampaignResponseDataProductCampaignRegistrationLimit | Unset):
            registration_mode (str | Unset): Registration mode of this product campaign. Omission means unknown. Independent
                of the parent campaign group's type and whether the shop is registered.
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
            registration_period (GetProductCampaignResponseDataProductCampaignRegistrationPeriod | Unset):
            shop_eligibility (ShopEligibility | Unset):
            shop_participation (GetProductCampaignResponseDataProductCampaignShopParticipation | Unset):
            subtypes (list[str] | Unset): Always returned. Distinct applicable public campaign subtypes. Returns [] if there
                are none. Order does not indicate priority.
            title (str | Unset): Always returned. Nonempty product campaign name.
            type_ (str | Unset): Always returned and fixed to PRODUCT, consistent with CampaignType in lists. Other campaign
                types are not accepted.
                Unified campaign type with the same semantics in lists and all four detail models. Distinct from campaign group
                type.
                - PRODUCT: Product campaign.
                - SHOP: Shop campaign.
                - LIVESTREAM: Livestream campaign.
                - SHORT_VIDEO: Short video campaign.
     """

    available_regions: list[str] | Unset = UNSET
    benefits: list[Benefit] | Unset = UNSET
    campaign_group: CampaignGroup | Unset = UNSET
    campaign_period: CampaignPeriod | Unset = UNSET
    campaign_status: str | Unset = UNSET
    description: str | Unset = UNSET
    fees: GetProductCampaignResponseDataProductCampaignFee | Unset = UNSET
    id: str | Unset = UNSET
    linked_campaigns: list[GetProductCampaignResponseDataProductCampaignLinkedCampaign] | Unset = UNSET
    participation_rules: GetProductCampaignResponseDataProductCampaignParticipationRule | Unset = UNSET
    region: str | Unset = UNSET
    registration_availability: RegistrationAvailability | Unset = UNSET
    registration_limit: GetProductCampaignResponseDataProductCampaignRegistrationLimit | Unset = UNSET
    registration_mode: str | Unset = UNSET
    registration_period: GetProductCampaignResponseDataProductCampaignRegistrationPeriod | Unset = UNSET
    shop_eligibility: ShopEligibility | Unset = UNSET
    shop_participation: GetProductCampaignResponseDataProductCampaignShopParticipation | Unset = UNSET
    subtypes: list[str] | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.benefit import Benefit # noqa: PLC0415
        from ..models.campaign_group import CampaignGroup # noqa: PLC0415
        from ..models.campaign_period import CampaignPeriod # noqa: PLC0415
        from ..models.get_product_campaign_response_data_product_campaign_fee import GetProductCampaignResponseDataProductCampaignFee # noqa: PLC0415
        from ..models.get_product_campaign_response_data_product_campaign_linked_campaign import GetProductCampaignResponseDataProductCampaignLinkedCampaign # noqa: PLC0415
        from ..models.get_product_campaign_response_data_product_campaign_participation_rule import GetProductCampaignResponseDataProductCampaignParticipationRule # noqa: PLC0415
        from ..models.get_product_campaign_response_data_product_campaign_registration_limit import GetProductCampaignResponseDataProductCampaignRegistrationLimit # noqa: PLC0415
        from ..models.get_product_campaign_response_data_product_campaign_registration_period import GetProductCampaignResponseDataProductCampaignRegistrationPeriod # noqa: PLC0415
        from ..models.get_product_campaign_response_data_product_campaign_shop_participation import GetProductCampaignResponseDataProductCampaignShopParticipation # noqa: PLC0415
        from ..models.registration_availability import RegistrationAvailability # noqa: PLC0415
        from ..models.shop_eligibility import ShopEligibility # noqa: PLC0415
        available_regions: list[str] | Unset = UNSET
        if not isinstance(self.available_regions, Unset):
            available_regions = self.available_regions



        benefits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.benefits, Unset):
            benefits = []
            for benefits_item_data in self.benefits:
                benefits_item = benefits_item_data.to_dict()
                benefits.append(benefits_item)



        campaign_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.campaign_group, Unset):
            campaign_group = self.campaign_group.to_dict()

        campaign_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.campaign_period, Unset):
            campaign_period = self.campaign_period.to_dict()

        campaign_status = self.campaign_status

        description = self.description

        fees: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fees, Unset):
            fees = self.fees.to_dict()

        id = self.id

        linked_campaigns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_campaigns, Unset):
            linked_campaigns = []
            for linked_campaigns_item_data in self.linked_campaigns:
                linked_campaigns_item = linked_campaigns_item_data.to_dict()
                linked_campaigns.append(linked_campaigns_item)



        participation_rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.participation_rules, Unset):
            participation_rules = self.participation_rules.to_dict()

        region = self.region

        registration_availability: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_availability, Unset):
            registration_availability = self.registration_availability.to_dict()

        registration_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_limit, Unset):
            registration_limit = self.registration_limit.to_dict()

        registration_mode = self.registration_mode

        registration_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_period, Unset):
            registration_period = self.registration_period.to_dict()

        shop_eligibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shop_eligibility, Unset):
            shop_eligibility = self.shop_eligibility.to_dict()

        shop_participation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shop_participation, Unset):
            shop_participation = self.shop_participation.to_dict()

        subtypes: list[str] | Unset = UNSET
        if not isinstance(self.subtypes, Unset):
            subtypes = self.subtypes



        title = self.title

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if available_regions is not UNSET:
            field_dict["available_regions"] = available_regions
        if benefits is not UNSET:
            field_dict["benefits"] = benefits
        if campaign_group is not UNSET:
            field_dict["campaign_group"] = campaign_group
        if campaign_period is not UNSET:
            field_dict["campaign_period"] = campaign_period
        if campaign_status is not UNSET:
            field_dict["campaign_status"] = campaign_status
        if description is not UNSET:
            field_dict["description"] = description
        if fees is not UNSET:
            field_dict["fees"] = fees
        if id is not UNSET:
            field_dict["id"] = id
        if linked_campaigns is not UNSET:
            field_dict["linked_campaigns"] = linked_campaigns
        if participation_rules is not UNSET:
            field_dict["participation_rules"] = participation_rules
        if region is not UNSET:
            field_dict["region"] = region
        if registration_availability is not UNSET:
            field_dict["registration_availability"] = registration_availability
        if registration_limit is not UNSET:
            field_dict["registration_limit"] = registration_limit
        if registration_mode is not UNSET:
            field_dict["registration_mode"] = registration_mode
        if registration_period is not UNSET:
            field_dict["registration_period"] = registration_period
        if shop_eligibility is not UNSET:
            field_dict["shop_eligibility"] = shop_eligibility
        if shop_participation is not UNSET:
            field_dict["shop_participation"] = shop_participation
        if subtypes is not UNSET:
            field_dict["subtypes"] = subtypes
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.benefit import Benefit # noqa: PLC0415
        from ..models.campaign_group import CampaignGroup # noqa: PLC0415
        from ..models.campaign_period import CampaignPeriod # noqa: PLC0415
        from ..models.get_product_campaign_response_data_product_campaign_fee import GetProductCampaignResponseDataProductCampaignFee # noqa: PLC0415
        from ..models.get_product_campaign_response_data_product_campaign_linked_campaign import GetProductCampaignResponseDataProductCampaignLinkedCampaign # noqa: PLC0415
        from ..models.get_product_campaign_response_data_product_campaign_participation_rule import GetProductCampaignResponseDataProductCampaignParticipationRule # noqa: PLC0415
        from ..models.get_product_campaign_response_data_product_campaign_registration_limit import GetProductCampaignResponseDataProductCampaignRegistrationLimit # noqa: PLC0415
        from ..models.get_product_campaign_response_data_product_campaign_registration_period import GetProductCampaignResponseDataProductCampaignRegistrationPeriod # noqa: PLC0415
        from ..models.get_product_campaign_response_data_product_campaign_shop_participation import GetProductCampaignResponseDataProductCampaignShopParticipation # noqa: PLC0415
        from ..models.registration_availability import RegistrationAvailability # noqa: PLC0415
        from ..models.shop_eligibility import ShopEligibility # noqa: PLC0415
        d = dict(src_dict)
        available_regions = cast(list[str], d.pop("available_regions", UNSET))


        _benefits = d.pop("benefits", UNSET)
        benefits: list[Benefit] | Unset = UNSET
        if _benefits is not UNSET:
            benefits = []
            for benefits_item_data in _benefits:
                benefits_item = Benefit.from_dict(benefits_item_data)



                benefits.append(benefits_item)


        _campaign_group = d.pop("campaign_group", UNSET)
        campaign_group: CampaignGroup | Unset
        if isinstance(_campaign_group,  Unset):
            campaign_group = UNSET
        else:
            campaign_group = CampaignGroup.from_dict(_campaign_group)




        _campaign_period = d.pop("campaign_period", UNSET)
        campaign_period: CampaignPeriod | Unset
        if isinstance(_campaign_period,  Unset):
            campaign_period = UNSET
        else:
            campaign_period = CampaignPeriod.from_dict(_campaign_period)




        campaign_status = d.pop("campaign_status", UNSET)

        description = d.pop("description", UNSET)

        _fees = d.pop("fees", UNSET)
        fees: GetProductCampaignResponseDataProductCampaignFee | Unset
        if isinstance(_fees,  Unset):
            fees = UNSET
        else:
            fees = GetProductCampaignResponseDataProductCampaignFee.from_dict(_fees)




        id = d.pop("id", UNSET)

        _linked_campaigns = d.pop("linked_campaigns", UNSET)
        linked_campaigns: list[GetProductCampaignResponseDataProductCampaignLinkedCampaign] | Unset = UNSET
        if _linked_campaigns is not UNSET:
            linked_campaigns = []
            for linked_campaigns_item_data in _linked_campaigns:
                linked_campaigns_item = GetProductCampaignResponseDataProductCampaignLinkedCampaign.from_dict(linked_campaigns_item_data)



                linked_campaigns.append(linked_campaigns_item)


        _participation_rules = d.pop("participation_rules", UNSET)
        participation_rules: GetProductCampaignResponseDataProductCampaignParticipationRule | Unset
        if isinstance(_participation_rules,  Unset):
            participation_rules = UNSET
        else:
            participation_rules = GetProductCampaignResponseDataProductCampaignParticipationRule.from_dict(_participation_rules)




        region = d.pop("region", UNSET)

        _registration_availability = d.pop("registration_availability", UNSET)
        registration_availability: RegistrationAvailability | Unset
        if isinstance(_registration_availability,  Unset):
            registration_availability = UNSET
        else:
            registration_availability = RegistrationAvailability.from_dict(_registration_availability)




        _registration_limit = d.pop("registration_limit", UNSET)
        registration_limit: GetProductCampaignResponseDataProductCampaignRegistrationLimit | Unset
        if isinstance(_registration_limit,  Unset):
            registration_limit = UNSET
        else:
            registration_limit = GetProductCampaignResponseDataProductCampaignRegistrationLimit.from_dict(_registration_limit)




        registration_mode = d.pop("registration_mode", UNSET)

        _registration_period = d.pop("registration_period", UNSET)
        registration_period: GetProductCampaignResponseDataProductCampaignRegistrationPeriod | Unset
        if isinstance(_registration_period,  Unset):
            registration_period = UNSET
        else:
            registration_period = GetProductCampaignResponseDataProductCampaignRegistrationPeriod.from_dict(_registration_period)




        _shop_eligibility = d.pop("shop_eligibility", UNSET)
        shop_eligibility: ShopEligibility | Unset
        if isinstance(_shop_eligibility,  Unset):
            shop_eligibility = UNSET
        else:
            shop_eligibility = ShopEligibility.from_dict(_shop_eligibility)




        _shop_participation = d.pop("shop_participation", UNSET)
        shop_participation: GetProductCampaignResponseDataProductCampaignShopParticipation | Unset
        if isinstance(_shop_participation,  Unset):
            shop_participation = UNSET
        else:
            shop_participation = GetProductCampaignResponseDataProductCampaignShopParticipation.from_dict(_shop_participation)




        subtypes = cast(list[str], d.pop("subtypes", UNSET))


        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        get_product_campaign_response_data_product_campaign = cls(
            available_regions=available_regions,
            benefits=benefits,
            campaign_group=campaign_group,
            campaign_period=campaign_period,
            campaign_status=campaign_status,
            description=description,
            fees=fees,
            id=id,
            linked_campaigns=linked_campaigns,
            participation_rules=participation_rules,
            region=region,
            registration_availability=registration_availability,
            registration_limit=registration_limit,
            registration_mode=registration_mode,
            registration_period=registration_period,
            shop_eligibility=shop_eligibility,
            shop_participation=shop_participation,
            subtypes=subtypes,
            title=title,
            type_=type_,
        )


        get_product_campaign_response_data_product_campaign.additional_properties = d
        return get_product_campaign_response_data_product_campaign

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
