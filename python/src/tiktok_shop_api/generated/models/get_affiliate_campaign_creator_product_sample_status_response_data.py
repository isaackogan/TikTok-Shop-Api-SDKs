from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_affiliate_campaign_creator_product_sample_status_response_data_sample_status import GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatus





T = TypeVar("T", bound="GetAffiliateCampaignCreatorProductSampleStatusResponseData")



@_attrs_define
class GetAffiliateCampaignCreatorProductSampleStatusResponseData:
    """ 
        Attributes:
            sample_status (GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatus | Unset):
     """

    sample_status: GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_affiliate_campaign_creator_product_sample_status_response_data_sample_status import GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatus # noqa: PLC0415
        sample_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sample_status, Unset):
            sample_status = self.sample_status.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sample_status is not UNSET:
            field_dict["sample_status"] = sample_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_affiliate_campaign_creator_product_sample_status_response_data_sample_status import GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatus # noqa: PLC0415
        d = dict(src_dict)
        _sample_status = d.pop("sample_status", UNSET)
        sample_status: GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatus | Unset
        if isinstance(_sample_status,  Unset):
            sample_status = UNSET
        else:
            sample_status = GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatus.from_dict(_sample_status)




        get_affiliate_campaign_creator_product_sample_status_response_data = cls(
            sample_status=sample_status,
        )


        get_affiliate_campaign_creator_product_sample_status_response_data.additional_properties = d
        return get_affiliate_campaign_creator_product_sample_status_response_data

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
