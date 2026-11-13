from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.campaign import Campaign
  from ..models.campaign_period import CampaignPeriod
  from ..models.linked_campaign_group import LinkedCampaignGroup
  from ..models.official_sales_period import OfficialSalesPeriod





T = TypeVar("T", bound="ListCampaignGroupResponseDataCampaignGroup")



@_attrs_define
class ListCampaignGroupResponseDataCampaignGroup:
    """ 
        Attributes:
            available_regions (list[str] | Unset): Applicable countries or regions. Omission does not mean that there are no
                regional restrictions and does not extend shop authorization. Region codes follow [ISO 3166-1
                alpha-2](https://www.iso.org/obp/ui/#search/code/); EU is also supported as an aggregate campaign region. A
                listed code does not guarantee campaign availability or extend authorization.
            campaign_count (int | Unset): Number of campaigns in the group within the current query scope, potentially
                including product, shop, livestream, and short video campaigns. Omission means unknown, not zero. The count is
                not guaranteed to equal the number of campaigns entries.
            campaign_period (CampaignPeriod | Unset):
            campaign_status (str | Unset): Campaign group status. Omission means the status was not provided; it does not
                establish registration eligibility.
                Campaign group status. None of these statuses establishes shop registration eligibility.
                - INEFFECTIVE: Not yet effective.
                - UPCOMING: Starting soon.
                - ONGOING: In progress.
                - EXPIRED: Ended or no longer effective.
            campaigns (list[Campaign] | Unset): Always returned for type=NORMAL; omitted for other types. Campaign summaries
                within the group for this query, without separate pagination. Returns [] when no campaigns are returned; this
                does not establish that the group contains no campaigns. Includes summaries only, without full details or nested
                campaign relationships.
            description (str | Unset): Localized campaign group description. Omitted if no description is available.
            id (str | Unset): Positive campaign group ID, always returned for each item. A decimal string from 1 to
                9223372036854775807.
            is_invited (bool | Unset): Whether the shop is invited. Omission means no result was provided. An invitation
                does not establish registration eligibility.
            linked_campaign_groups (list[LinkedCampaignGroup] | Unset): Applicable only to type=LONG_TERM; omitted for other
                types. Summaries of campaign groups linked to the long-term group, describing associated major sale
                arrangements. These groups are not included in campaign_count. Not paginated separately. Omitted if unavailable;
                [] means no linked group summaries were returned for this query, not that no other links exist.
            official_sales_period (OfficialSalesPeriod | Unset):
            region (str | Unset): Campaign region, which may be EU and need not match the authorized shop's region. Region
                codes follow [ISO 3166-1 alpha-2](https://www.iso.org/obp/ui/#search/code/); EU is also supported as an
                aggregate campaign region. A listed code does not guarantee campaign availability or extend authorization.
            title (str | Unset): Localized campaign group name. Omitted if no name is available.
            type_ (str | Unset): Campaign group type, which determines the summary list returned. If no defined type is
                available, this field and both summary lists are omitted.
                Campaign group type.
                - NORMAL: A regular campaign group.
                - LONG_TERM: A long-term campaign group that may link to multiple regular groups. This does not mean that the
                shop is registered.
     """

    available_regions: list[str] | Unset = UNSET
    campaign_count: int | Unset = UNSET
    campaign_period: CampaignPeriod | Unset = UNSET
    campaign_status: str | Unset = UNSET
    campaigns: list[Campaign] | Unset = UNSET
    description: str | Unset = UNSET
    id: str | Unset = UNSET
    is_invited: bool | Unset = UNSET
    linked_campaign_groups: list[LinkedCampaignGroup] | Unset = UNSET
    official_sales_period: OfficialSalesPeriod | Unset = UNSET
    region: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.campaign import Campaign # noqa: PLC0415
        from ..models.campaign_period import CampaignPeriod # noqa: PLC0415
        from ..models.linked_campaign_group import LinkedCampaignGroup # noqa: PLC0415
        from ..models.official_sales_period import OfficialSalesPeriod # noqa: PLC0415
        available_regions: list[str] | Unset = UNSET
        if not isinstance(self.available_regions, Unset):
            available_regions = self.available_regions



        campaign_count = self.campaign_count

        campaign_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.campaign_period, Unset):
            campaign_period = self.campaign_period.to_dict()

        campaign_status = self.campaign_status

        campaigns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.campaigns, Unset):
            campaigns = []
            for campaigns_item_data in self.campaigns:
                campaigns_item = campaigns_item_data.to_dict()
                campaigns.append(campaigns_item)



        description = self.description

        id = self.id

        is_invited = self.is_invited

        linked_campaign_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_campaign_groups, Unset):
            linked_campaign_groups = []
            for linked_campaign_groups_item_data in self.linked_campaign_groups:
                linked_campaign_groups_item = linked_campaign_groups_item_data.to_dict()
                linked_campaign_groups.append(linked_campaign_groups_item)



        official_sales_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.official_sales_period, Unset):
            official_sales_period = self.official_sales_period.to_dict()

        region = self.region

        title = self.title

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if available_regions is not UNSET:
            field_dict["available_regions"] = available_regions
        if campaign_count is not UNSET:
            field_dict["campaign_count"] = campaign_count
        if campaign_period is not UNSET:
            field_dict["campaign_period"] = campaign_period
        if campaign_status is not UNSET:
            field_dict["campaign_status"] = campaign_status
        if campaigns is not UNSET:
            field_dict["campaigns"] = campaigns
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if is_invited is not UNSET:
            field_dict["is_invited"] = is_invited
        if linked_campaign_groups is not UNSET:
            field_dict["linked_campaign_groups"] = linked_campaign_groups
        if official_sales_period is not UNSET:
            field_dict["official_sales_period"] = official_sales_period
        if region is not UNSET:
            field_dict["region"] = region
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.campaign import Campaign # noqa: PLC0415
        from ..models.campaign_period import CampaignPeriod # noqa: PLC0415
        from ..models.linked_campaign_group import LinkedCampaignGroup # noqa: PLC0415
        from ..models.official_sales_period import OfficialSalesPeriod # noqa: PLC0415
        d = dict(src_dict)
        available_regions = cast(list[str], d.pop("available_regions", UNSET))


        campaign_count = d.pop("campaign_count", UNSET)

        _campaign_period = d.pop("campaign_period", UNSET)
        campaign_period: CampaignPeriod | Unset
        if isinstance(_campaign_period,  Unset):
            campaign_period = UNSET
        else:
            campaign_period = CampaignPeriod.from_dict(_campaign_period)




        campaign_status = d.pop("campaign_status", UNSET)

        _campaigns = d.pop("campaigns", UNSET)
        campaigns: list[Campaign] | Unset = UNSET
        if _campaigns is not UNSET:
            campaigns = []
            for campaigns_item_data in _campaigns:
                campaigns_item = Campaign.from_dict(campaigns_item_data)



                campaigns.append(campaigns_item)


        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        is_invited = d.pop("is_invited", UNSET)

        _linked_campaign_groups = d.pop("linked_campaign_groups", UNSET)
        linked_campaign_groups: list[LinkedCampaignGroup] | Unset = UNSET
        if _linked_campaign_groups is not UNSET:
            linked_campaign_groups = []
            for linked_campaign_groups_item_data in _linked_campaign_groups:
                linked_campaign_groups_item = LinkedCampaignGroup.from_dict(linked_campaign_groups_item_data)



                linked_campaign_groups.append(linked_campaign_groups_item)


        _official_sales_period = d.pop("official_sales_period", UNSET)
        official_sales_period: OfficialSalesPeriod | Unset
        if isinstance(_official_sales_period,  Unset):
            official_sales_period = UNSET
        else:
            official_sales_period = OfficialSalesPeriod.from_dict(_official_sales_period)




        region = d.pop("region", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        list_campaign_group_response_data_campaign_group = cls(
            available_regions=available_regions,
            campaign_count=campaign_count,
            campaign_period=campaign_period,
            campaign_status=campaign_status,
            campaigns=campaigns,
            description=description,
            id=id,
            is_invited=is_invited,
            linked_campaign_groups=linked_campaign_groups,
            official_sales_period=official_sales_period,
            region=region,
            title=title,
            type_=type_,
        )


        list_campaign_group_response_data_campaign_group.additional_properties = d
        return list_campaign_group_response_data_campaign_group

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
