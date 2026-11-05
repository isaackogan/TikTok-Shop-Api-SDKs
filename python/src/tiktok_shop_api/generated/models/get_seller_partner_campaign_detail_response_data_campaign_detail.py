from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_campaign_statistic import GetSellerPartnerCampaignDetailResponseDataCampaignDetailCampaignStatistic
  from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_invited_agency_detail import GetSellerPartnerCampaignDetailResponseDataCampaignDetailInvitedAgencyDetail
  from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_seller_campaign_extra import GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerCampaignExtra
  from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_seller_info import GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfo





T = TypeVar("T", bound="GetSellerPartnerCampaignDetailResponseDataCampaignDetail")



@_attrs_define
class GetSellerPartnerCampaignDetailResponseDataCampaignDetail:
    """ 
        Attributes:
            affiliate_partner_name (str | Unset): Name of the agency that initiated the campaign.
            campaign_id (str | Unset): Campaign ID encoded as a decimal string.
            campaign_name (str | Unset): Display name of the campaign.
            campaign_statistics (GetSellerPartnerCampaignDetailResponseDataCampaignDetailCampaignStatistic | Unset):
            can_register (bool | Unset): Campaign-level registration flag. Detail currently derives it from campaign status,
                not
                complete shop/product eligibility.
            commission_rate (int | Unset): Minimum commission rate required by the campaign, expressed as the percentage
                multiplied by
                100; for example, 1200 means 12%.
            description (str | Unset): @redact Free-text campaign description; it may contain personal contact information.
            end_time (str | Unset): Campaign end time, as a Unix timestamp in milliseconds encoded as a string.
            invited_agency_details (list[GetSellerPartnerCampaignDetailResponseDataCampaignDetailInvitedAgencyDetail] |
                Unset): Restricted collaboration relationship data; return only within the authorized
                campaign/seller scope.
            is_auto_register (bool | Unset): Indicates whether automatic registration or approval is enabled for the
                campaign.
            is_registered (bool | Unset): Indicates whether the current shop has joined or registered for the campaign. It
                does not
                mean that every submitted product has been approved.
            is_target_campaign (bool | Unset): Indicates whether the campaign is targeted or invitation-only.
            partner_icon_uri (str | Unset): Resource URI of the agency icon. A resource URI is not necessarily a publicly
                accessible
                URL.
            publish_time (str | Unset): Time at which the campaign was published, as a Unix timestamp in milliseconds
                encoded as a
                string.
            registration_end_time (str | Unset): End of the campaign registration window, as a Unix timestamp in
                milliseconds encoded as a
                string.
            registration_start_time (str | Unset): Start of the campaign registration window, as a Unix timestamp in
                milliseconds encoded as a
                string.
            seller_campaign_extra (GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerCampaignExtra | Unset):
            seller_info (GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfo | Unset):
            start_time (str | Unset): Campaign start time, as a Unix timestamp in milliseconds encoded as a string.
            status (str | Unset): Current campaign state. DRAFT is not submitted; SUBMITTED is submitted for review;
                ONLINE_REGISTRABLE accepts registration; ONLINE_UNREGISTRABLE is online but does not accept registration; ENDED
                has finished; DELETED has been deleted.
            type_ (str | Unset): Campaign creation type. AGENCY_INITIATED is created by an agency; SELLER_INITIATED is
                created by a seller; SELLER_INITIATED_SUB is an agency sub-campaign of a seller campaign; OPS_CAMPAIGN is
                created by operations; OPS_SUB_CAMPAIGN is a sub-campaign of an operations campaign.
            version (str | Unset): Commission model. MVP is the legacy creator/agency split model; MULTI_CREATOR_COMMISSION
                uses total commission. An omitted version has MVP behavior. This is distinct from the API path version.
     """

    affiliate_partner_name: str | Unset = UNSET
    campaign_id: str | Unset = UNSET
    campaign_name: str | Unset = UNSET
    campaign_statistics: GetSellerPartnerCampaignDetailResponseDataCampaignDetailCampaignStatistic | Unset = UNSET
    can_register: bool | Unset = UNSET
    commission_rate: int | Unset = UNSET
    description: str | Unset = UNSET
    end_time: str | Unset = UNSET
    invited_agency_details: list[GetSellerPartnerCampaignDetailResponseDataCampaignDetailInvitedAgencyDetail] | Unset = UNSET
    is_auto_register: bool | Unset = UNSET
    is_registered: bool | Unset = UNSET
    is_target_campaign: bool | Unset = UNSET
    partner_icon_uri: str | Unset = UNSET
    publish_time: str | Unset = UNSET
    registration_end_time: str | Unset = UNSET
    registration_start_time: str | Unset = UNSET
    seller_campaign_extra: GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerCampaignExtra | Unset = UNSET
    seller_info: GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfo | Unset = UNSET
    start_time: str | Unset = UNSET
    status: str | Unset = UNSET
    type_: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_campaign_statistic import GetSellerPartnerCampaignDetailResponseDataCampaignDetailCampaignStatistic # noqa: PLC0415
        from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_invited_agency_detail import GetSellerPartnerCampaignDetailResponseDataCampaignDetailInvitedAgencyDetail # noqa: PLC0415
        from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_seller_campaign_extra import GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerCampaignExtra # noqa: PLC0415
        from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_seller_info import GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfo # noqa: PLC0415
        affiliate_partner_name = self.affiliate_partner_name

        campaign_id = self.campaign_id

        campaign_name = self.campaign_name

        campaign_statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.campaign_statistics, Unset):
            campaign_statistics = self.campaign_statistics.to_dict()

        can_register = self.can_register

        commission_rate = self.commission_rate

        description = self.description

        end_time = self.end_time

        invited_agency_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.invited_agency_details, Unset):
            invited_agency_details = []
            for invited_agency_details_item_data in self.invited_agency_details:
                invited_agency_details_item = invited_agency_details_item_data.to_dict()
                invited_agency_details.append(invited_agency_details_item)



        is_auto_register = self.is_auto_register

        is_registered = self.is_registered

        is_target_campaign = self.is_target_campaign

        partner_icon_uri = self.partner_icon_uri

        publish_time = self.publish_time

        registration_end_time = self.registration_end_time

        registration_start_time = self.registration_start_time

        seller_campaign_extra: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_campaign_extra, Unset):
            seller_campaign_extra = self.seller_campaign_extra.to_dict()

        seller_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_info, Unset):
            seller_info = self.seller_info.to_dict()

        start_time = self.start_time

        status = self.status

        type_ = self.type_

        version = self.version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if affiliate_partner_name is not UNSET:
            field_dict["affiliate_partner_name"] = affiliate_partner_name
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if campaign_name is not UNSET:
            field_dict["campaign_name"] = campaign_name
        if campaign_statistics is not UNSET:
            field_dict["campaign_statistics"] = campaign_statistics
        if can_register is not UNSET:
            field_dict["can_register"] = can_register
        if commission_rate is not UNSET:
            field_dict["commission_rate"] = commission_rate
        if description is not UNSET:
            field_dict["description"] = description
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if invited_agency_details is not UNSET:
            field_dict["invited_agency_details"] = invited_agency_details
        if is_auto_register is not UNSET:
            field_dict["is_auto_register"] = is_auto_register
        if is_registered is not UNSET:
            field_dict["is_registered"] = is_registered
        if is_target_campaign is not UNSET:
            field_dict["is_target_campaign"] = is_target_campaign
        if partner_icon_uri is not UNSET:
            field_dict["partner_icon_uri"] = partner_icon_uri
        if publish_time is not UNSET:
            field_dict["publish_time"] = publish_time
        if registration_end_time is not UNSET:
            field_dict["registration_end_time"] = registration_end_time
        if registration_start_time is not UNSET:
            field_dict["registration_start_time"] = registration_start_time
        if seller_campaign_extra is not UNSET:
            field_dict["seller_campaign_extra"] = seller_campaign_extra
        if seller_info is not UNSET:
            field_dict["seller_info"] = seller_info
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_campaign_statistic import GetSellerPartnerCampaignDetailResponseDataCampaignDetailCampaignStatistic # noqa: PLC0415
        from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_invited_agency_detail import GetSellerPartnerCampaignDetailResponseDataCampaignDetailInvitedAgencyDetail # noqa: PLC0415
        from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_seller_campaign_extra import GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerCampaignExtra # noqa: PLC0415
        from ..models.get_seller_partner_campaign_detail_response_data_campaign_detail_seller_info import GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfo # noqa: PLC0415
        d = dict(src_dict)
        affiliate_partner_name = d.pop("affiliate_partner_name", UNSET)

        campaign_id = d.pop("campaign_id", UNSET)

        campaign_name = d.pop("campaign_name", UNSET)

        _campaign_statistics = d.pop("campaign_statistics", UNSET)
        campaign_statistics: GetSellerPartnerCampaignDetailResponseDataCampaignDetailCampaignStatistic | Unset
        if isinstance(_campaign_statistics,  Unset):
            campaign_statistics = UNSET
        else:
            campaign_statistics = GetSellerPartnerCampaignDetailResponseDataCampaignDetailCampaignStatistic.from_dict(_campaign_statistics)




        can_register = d.pop("can_register", UNSET)

        commission_rate = d.pop("commission_rate", UNSET)

        description = d.pop("description", UNSET)

        end_time = d.pop("end_time", UNSET)

        _invited_agency_details = d.pop("invited_agency_details", UNSET)
        invited_agency_details: list[GetSellerPartnerCampaignDetailResponseDataCampaignDetailInvitedAgencyDetail] | Unset = UNSET
        if _invited_agency_details is not UNSET:
            invited_agency_details = []
            for invited_agency_details_item_data in _invited_agency_details:
                invited_agency_details_item = GetSellerPartnerCampaignDetailResponseDataCampaignDetailInvitedAgencyDetail.from_dict(invited_agency_details_item_data)



                invited_agency_details.append(invited_agency_details_item)


        is_auto_register = d.pop("is_auto_register", UNSET)

        is_registered = d.pop("is_registered", UNSET)

        is_target_campaign = d.pop("is_target_campaign", UNSET)

        partner_icon_uri = d.pop("partner_icon_uri", UNSET)

        publish_time = d.pop("publish_time", UNSET)

        registration_end_time = d.pop("registration_end_time", UNSET)

        registration_start_time = d.pop("registration_start_time", UNSET)

        _seller_campaign_extra = d.pop("seller_campaign_extra", UNSET)
        seller_campaign_extra: GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerCampaignExtra | Unset
        if isinstance(_seller_campaign_extra,  Unset):
            seller_campaign_extra = UNSET
        else:
            seller_campaign_extra = GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerCampaignExtra.from_dict(_seller_campaign_extra)




        _seller_info = d.pop("seller_info", UNSET)
        seller_info: GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfo | Unset
        if isinstance(_seller_info,  Unset):
            seller_info = UNSET
        else:
            seller_info = GetSellerPartnerCampaignDetailResponseDataCampaignDetailSellerInfo.from_dict(_seller_info)




        start_time = d.pop("start_time", UNSET)

        status = d.pop("status", UNSET)

        type_ = d.pop("type", UNSET)

        version = d.pop("version", UNSET)

        get_seller_partner_campaign_detail_response_data_campaign_detail = cls(
            affiliate_partner_name=affiliate_partner_name,
            campaign_id=campaign_id,
            campaign_name=campaign_name,
            campaign_statistics=campaign_statistics,
            can_register=can_register,
            commission_rate=commission_rate,
            description=description,
            end_time=end_time,
            invited_agency_details=invited_agency_details,
            is_auto_register=is_auto_register,
            is_registered=is_registered,
            is_target_campaign=is_target_campaign,
            partner_icon_uri=partner_icon_uri,
            publish_time=publish_time,
            registration_end_time=registration_end_time,
            registration_start_time=registration_start_time,
            seller_campaign_extra=seller_campaign_extra,
            seller_info=seller_info,
            start_time=start_time,
            status=status,
            type_=type_,
            version=version,
        )


        get_seller_partner_campaign_detail_response_data_campaign_detail.additional_properties = d
        return get_seller_partner_campaign_detail_response_data_campaign_detail

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
