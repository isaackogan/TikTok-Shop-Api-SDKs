from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_livestream_campaign_response_data_livestream_campaign import GetLivestreamCampaignResponseDataLivestreamCampaign





T = TypeVar("T", bound="GetLivestreamCampaignResponseData")



@_attrs_define
class GetLivestreamCampaignResponseData:
    """ 
        Attributes:
            livestream_campaign (GetLivestreamCampaignResponseDataLivestreamCampaign | Unset):
     """

    livestream_campaign: GetLivestreamCampaignResponseDataLivestreamCampaign | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_livestream_campaign_response_data_livestream_campaign import GetLivestreamCampaignResponseDataLivestreamCampaign # noqa: PLC0415
        livestream_campaign: dict[str, Any] | Unset = UNSET
        if not isinstance(self.livestream_campaign, Unset):
            livestream_campaign = self.livestream_campaign.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if livestream_campaign is not UNSET:
            field_dict["livestream_campaign"] = livestream_campaign

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_livestream_campaign_response_data_livestream_campaign import GetLivestreamCampaignResponseDataLivestreamCampaign # noqa: PLC0415
        d = dict(src_dict)
        _livestream_campaign = d.pop("livestream_campaign", UNSET)
        livestream_campaign: GetLivestreamCampaignResponseDataLivestreamCampaign | Unset
        if isinstance(_livestream_campaign,  Unset):
            livestream_campaign = UNSET
        else:
            livestream_campaign = GetLivestreamCampaignResponseDataLivestreamCampaign.from_dict(_livestream_campaign)




        get_livestream_campaign_response_data = cls(
            livestream_campaign=livestream_campaign,
        )


        get_livestream_campaign_response_data.additional_properties = d
        return get_livestream_campaign_response_data

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
