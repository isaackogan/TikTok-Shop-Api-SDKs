from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_campaign_group_response_data_campaign_group import ListCampaignGroupResponseDataCampaignGroup





T = TypeVar("T", bound="ListCampaignGroupResponseData")



@_attrs_define
class ListCampaignGroupResponseData:
    """ 
        Attributes:
            campaign_groups (list[ListCampaignGroupResponseDataCampaignGroup] | Unset): Always returned. Campaign groups on
                the current page, each with summaries applicable to its type. Returns [] when no results match.
            next_page_token (str | Unset): Opaque token for the next page. An empty string indicates the last page within
                the current query scope. An empty page may still have a next-page token; do not infer completion from its item
                count.
            total_count (int | Unset): Always returned. Nonnegative total for this query, not the current page's item count.
                Consistency across pages is not guaranteed.
     """

    campaign_groups: list[ListCampaignGroupResponseDataCampaignGroup] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_campaign_group_response_data_campaign_group import ListCampaignGroupResponseDataCampaignGroup # noqa: PLC0415
        campaign_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.campaign_groups, Unset):
            campaign_groups = []
            for campaign_groups_item_data in self.campaign_groups:
                campaign_groups_item = campaign_groups_item_data.to_dict()
                campaign_groups.append(campaign_groups_item)



        next_page_token = self.next_page_token

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if campaign_groups is not UNSET:
            field_dict["campaign_groups"] = campaign_groups
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_campaign_group_response_data_campaign_group import ListCampaignGroupResponseDataCampaignGroup # noqa: PLC0415
        d = dict(src_dict)
        _campaign_groups = d.pop("campaign_groups", UNSET)
        campaign_groups: list[ListCampaignGroupResponseDataCampaignGroup] | Unset = UNSET
        if _campaign_groups is not UNSET:
            campaign_groups = []
            for campaign_groups_item_data in _campaign_groups:
                campaign_groups_item = ListCampaignGroupResponseDataCampaignGroup.from_dict(campaign_groups_item_data)



                campaign_groups.append(campaign_groups_item)


        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        list_campaign_group_response_data = cls(
            campaign_groups=campaign_groups,
            next_page_token=next_page_token,
            total_count=total_count,
        )


        list_campaign_group_response_data.additional_properties = d
        return list_campaign_group_response_data

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
