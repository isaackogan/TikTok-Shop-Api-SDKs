from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetSellerPartnerCampaignDetailResponseDataCampaignDetailInvitedAgencyDetail")



@_attrs_define
class GetSellerPartnerCampaignDetailResponseDataCampaignDetailInvitedAgencyDetail:
    """ 
        Attributes:
            partner_id (str | Unset): ID of the agency or TikTok Shop affiliate partner, encoded as a string.
            partner_name (str | Unset): Display name of the invited agency.
            partner_status (str | Unset): Agency participation state. INVITED means the invitation is pending; JOINED means
                the agency accepted; DECLINED means the agency rejected the invitation.
     """

    partner_id: str | Unset = UNSET
    partner_name: str | Unset = UNSET
    partner_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        partner_id = self.partner_id

        partner_name = self.partner_name

        partner_status = self.partner_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if partner_id is not UNSET:
            field_dict["partner_id"] = partner_id
        if partner_name is not UNSET:
            field_dict["partner_name"] = partner_name
        if partner_status is not UNSET:
            field_dict["partner_status"] = partner_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        partner_id = d.pop("partner_id", UNSET)

        partner_name = d.pop("partner_name", UNSET)

        partner_status = d.pop("partner_status", UNSET)

        get_seller_partner_campaign_detail_response_data_campaign_detail_invited_agency_detail = cls(
            partner_id=partner_id,
            partner_name=partner_name,
            partner_status=partner_status,
        )


        get_seller_partner_campaign_detail_response_data_campaign_detail_invited_agency_detail.additional_properties = d
        return get_seller_partner_campaign_detail_response_data_campaign_detail_invited_agency_detail

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
