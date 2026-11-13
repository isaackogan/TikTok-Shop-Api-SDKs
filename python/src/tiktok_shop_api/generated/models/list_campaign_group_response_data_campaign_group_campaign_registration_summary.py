from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_campaign_group_response_data_campaign_group_campaign_registration_summary_registration_block_reason import ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummaryRegistrationBlockReason





T = TypeVar("T", bound="ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummary")



@_attrs_define
class ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummary:
    """ 
        Attributes:
            is_eligible (bool | Unset): Whether the list-level eligibility conditions are met. Omitted if no conclusion is
                available.
            is_registration_available (bool | Unset): Whether registration can be entered according to the list-level
                assessment. Omitted if no conclusion is available.
            registration_block_reason
                (ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummaryRegistrationBlockReason | Unset):
     """

    is_eligible: bool | Unset = UNSET
    is_registration_available: bool | Unset = UNSET
    registration_block_reason: ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummaryRegistrationBlockReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_campaign_group_response_data_campaign_group_campaign_registration_summary_registration_block_reason import ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummaryRegistrationBlockReason # noqa: PLC0415
        is_eligible = self.is_eligible

        is_registration_available = self.is_registration_available

        registration_block_reason: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_block_reason, Unset):
            registration_block_reason = self.registration_block_reason.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_eligible is not UNSET:
            field_dict["is_eligible"] = is_eligible
        if is_registration_available is not UNSET:
            field_dict["is_registration_available"] = is_registration_available
        if registration_block_reason is not UNSET:
            field_dict["registration_block_reason"] = registration_block_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_campaign_group_response_data_campaign_group_campaign_registration_summary_registration_block_reason import ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummaryRegistrationBlockReason # noqa: PLC0415
        d = dict(src_dict)
        is_eligible = d.pop("is_eligible", UNSET)

        is_registration_available = d.pop("is_registration_available", UNSET)

        _registration_block_reason = d.pop("registration_block_reason", UNSET)
        registration_block_reason: ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummaryRegistrationBlockReason | Unset
        if isinstance(_registration_block_reason,  Unset):
            registration_block_reason = UNSET
        else:
            registration_block_reason = ListCampaignGroupResponseDataCampaignGroupCampaignRegistrationSummaryRegistrationBlockReason.from_dict(_registration_block_reason)




        list_campaign_group_response_data_campaign_group_campaign_registration_summary = cls(
            is_eligible=is_eligible,
            is_registration_available=is_registration_available,
            registration_block_reason=registration_block_reason,
        )


        list_campaign_group_response_data_campaign_group_campaign_registration_summary.additional_properties = d
        return list_campaign_group_response_data_campaign_group_campaign_registration_summary

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
