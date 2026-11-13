from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_shop_campaign_response_data_shop_campaign import GetShopCampaignResponseDataShopCampaign





T = TypeVar("T", bound="GetShopCampaignResponseData")



@_attrs_define
class GetShopCampaignResponseData:
    """ 
        Attributes:
            query_time (datetime.datetime | Unset): Always returned on success. Time used to determine registration period
                status in this query. RFC 3339 UTC with millisecond precision. Does not mean all data belongs to the same
                transactional snapshot.
            shop_campaign (GetShopCampaignResponseDataShopCampaign | Unset):
     """

    query_time: datetime.datetime | Unset = UNSET
    shop_campaign: GetShopCampaignResponseDataShopCampaign | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_campaign_response_data_shop_campaign import GetShopCampaignResponseDataShopCampaign # noqa: PLC0415
        query_time: str | Unset = UNSET
        if not isinstance(self.query_time, Unset):
            query_time = self.query_time.isoformat()

        shop_campaign: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shop_campaign, Unset):
            shop_campaign = self.shop_campaign.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if query_time is not UNSET:
            field_dict["query_time"] = query_time
        if shop_campaign is not UNSET:
            field_dict["shop_campaign"] = shop_campaign

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_campaign_response_data_shop_campaign import GetShopCampaignResponseDataShopCampaign # noqa: PLC0415
        d = dict(src_dict)
        _query_time = d.pop("query_time", UNSET)
        query_time: datetime.datetime | Unset
        if isinstance(_query_time,  Unset):
            query_time = UNSET
        else:
            query_time = datetime.datetime.fromisoformat(_query_time)




        _shop_campaign = d.pop("shop_campaign", UNSET)
        shop_campaign: GetShopCampaignResponseDataShopCampaign | Unset
        if isinstance(_shop_campaign,  Unset):
            shop_campaign = UNSET
        else:
            shop_campaign = GetShopCampaignResponseDataShopCampaign.from_dict(_shop_campaign)




        get_shop_campaign_response_data = cls(
            query_time=query_time,
            shop_campaign=shop_campaign,
        )


        get_shop_campaign_response_data.additional_properties = d
        return get_shop_campaign_response_data

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
