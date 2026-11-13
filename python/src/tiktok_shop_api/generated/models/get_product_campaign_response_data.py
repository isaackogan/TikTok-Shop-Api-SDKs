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
  from ..models.get_product_campaign_response_data_product_campaign import GetProductCampaignResponseDataProductCampaign





T = TypeVar("T", bound="GetProductCampaignResponseData")



@_attrs_define
class GetProductCampaignResponseData:
    """ 
        Attributes:
            product_campaign (GetProductCampaignResponseDataProductCampaign | Unset):
            query_time (datetime.datetime | Unset): Always returned on success. Time used to determine registration period
                status in this query. RFC 3339 UTC with millisecond precision. Does not mean all data belongs to the same
                transactional snapshot.
     """

    product_campaign: GetProductCampaignResponseDataProductCampaign | Unset = UNSET
    query_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_product_campaign_response_data_product_campaign import GetProductCampaignResponseDataProductCampaign # noqa: PLC0415
        product_campaign: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_campaign, Unset):
            product_campaign = self.product_campaign.to_dict()

        query_time: str | Unset = UNSET
        if not isinstance(self.query_time, Unset):
            query_time = self.query_time.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_campaign is not UNSET:
            field_dict["product_campaign"] = product_campaign
        if query_time is not UNSET:
            field_dict["query_time"] = query_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_campaign_response_data_product_campaign import GetProductCampaignResponseDataProductCampaign # noqa: PLC0415
        d = dict(src_dict)
        _product_campaign = d.pop("product_campaign", UNSET)
        product_campaign: GetProductCampaignResponseDataProductCampaign | Unset
        if isinstance(_product_campaign,  Unset):
            product_campaign = UNSET
        else:
            product_campaign = GetProductCampaignResponseDataProductCampaign.from_dict(_product_campaign)




        _query_time = d.pop("query_time", UNSET)
        query_time: datetime.datetime | Unset
        if isinstance(_query_time,  Unset):
            query_time = UNSET
        else:
            query_time = datetime.datetime.fromisoformat(_query_time)




        get_product_campaign_response_data = cls(
            product_campaign=product_campaign,
            query_time=query_time,
        )


        get_product_campaign_response_data.additional_properties = d
        return get_product_campaign_response_data

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
