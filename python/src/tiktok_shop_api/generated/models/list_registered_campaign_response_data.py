from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_registered_campaign_response_data_campaign import ListRegisteredCampaignResponseDataCampaign





T = TypeVar("T", bound="ListRegisteredCampaignResponseData")



@_attrs_define
class ListRegisteredCampaignResponseData:
    """ 
        Attributes:
            campaigns (list[ListRegisteredCampaignResponseDataCampaign] | Unset): Registered campaign summaries on the
                current page. Returns [] when no items are returned; next_page_token may still be nonempty. Does not include
                full details or nested campaign relationships.
            next_page_token (str | Unset): Opaque token for the next page. An empty string indicates the last page within
                the current query scope. An empty page may still have a next-page token; do not infer completion from its item
                count.
            total_count (int | Unset): Nonnegative reference total for the current query scope. May not be an exact total of
                all visible records. Not used to determine whether another page exists.
     """

    campaigns: list[ListRegisteredCampaignResponseDataCampaign] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_registered_campaign_response_data_campaign import ListRegisteredCampaignResponseDataCampaign # noqa: PLC0415
        campaigns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.campaigns, Unset):
            campaigns = []
            for campaigns_item_data in self.campaigns:
                campaigns_item = campaigns_item_data.to_dict()
                campaigns.append(campaigns_item)



        next_page_token = self.next_page_token

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if campaigns is not UNSET:
            field_dict["campaigns"] = campaigns
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_registered_campaign_response_data_campaign import ListRegisteredCampaignResponseDataCampaign # noqa: PLC0415
        d = dict(src_dict)
        _campaigns = d.pop("campaigns", UNSET)
        campaigns: list[ListRegisteredCampaignResponseDataCampaign] | Unset = UNSET
        if _campaigns is not UNSET:
            campaigns = []
            for campaigns_item_data in _campaigns:
                campaigns_item = ListRegisteredCampaignResponseDataCampaign.from_dict(campaigns_item_data)



                campaigns.append(campaigns_item)


        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        list_registered_campaign_response_data = cls(
            campaigns=campaigns,
            next_page_token=next_page_token,
            total_count=total_count,
        )


        list_registered_campaign_response_data.additional_properties = d
        return list_registered_campaign_response_data

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
