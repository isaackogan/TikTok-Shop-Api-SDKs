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





T = TypeVar("T", bound="GetProductCampaignResponseDataProductCampaignLinkedCampaign")



@_attrs_define
class GetProductCampaignResponseDataProductCampaignLinkedCampaign:
    """ 
        Attributes:
            campaign_period (CampaignPeriod | Unset):
            id (str | Unset): Positive campaign ID, always returned when the summary exists. Not a campaign group ID. Use it
                with type when querying details. A decimal string from 1 to 9223372036854775807.
            title (str | Unset): Nonempty localized name of the linked campaign. Falls back to the default name if no name
                is available in the requested language; omitted if still unavailable.
            type_ (str | Unset): Type of the linked campaign, used to select its detail endpoint. Omitted if unknown. May
                differ from the current campaign's type.
                Unified campaign type with the same semantics in lists and all four detail models. Distinct from campaign group
                type.
                - PRODUCT: Product campaign.
                - SHOP: Shop campaign.
                - LIVESTREAM: Livestream campaign.
                - SHORT_VIDEO: Short video campaign.
     """

    campaign_period: CampaignPeriod | Unset = UNSET
    id: str | Unset = UNSET
    title: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.campaign_period import CampaignPeriod # noqa: PLC0415
        campaign_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.campaign_period, Unset):
            campaign_period = self.campaign_period.to_dict()

        id = self.id

        title = self.title

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if campaign_period is not UNSET:
            field_dict["campaign_period"] = campaign_period
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.campaign_period import CampaignPeriod # noqa: PLC0415
        d = dict(src_dict)
        _campaign_period = d.pop("campaign_period", UNSET)
        campaign_period: CampaignPeriod | Unset
        if isinstance(_campaign_period,  Unset):
            campaign_period = UNSET
        else:
            campaign_period = CampaignPeriod.from_dict(_campaign_period)




        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        get_product_campaign_response_data_product_campaign_linked_campaign = cls(
            campaign_period=campaign_period,
            id=id,
            title=title,
            type_=type_,
        )


        get_product_campaign_response_data_product_campaign_linked_campaign.additional_properties = d
        return get_product_campaign_response_data_product_campaign_linked_campaign

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
