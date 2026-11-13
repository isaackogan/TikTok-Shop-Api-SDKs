from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_livestream_campaign_response_data_livestream_campaign_super_livestream_target_gmv_threshold import GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestreamTargetGmvThreshold





T = TypeVar("T", bound="GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestream")



@_attrs_define
class GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestream:
    """ 
        Attributes:
            is_enabled (bool | Unset): Whether super livestream is enabled. Omitted if unavailable; not defaulted to false.
            target_gmv_threshold (GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestreamTargetGmvThreshold |
                Unset):
     """

    is_enabled: bool | Unset = UNSET
    target_gmv_threshold: GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestreamTargetGmvThreshold | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_livestream_campaign_response_data_livestream_campaign_super_livestream_target_gmv_threshold import GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestreamTargetGmvThreshold # noqa: PLC0415
        is_enabled = self.is_enabled

        target_gmv_threshold: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_gmv_threshold, Unset):
            target_gmv_threshold = self.target_gmv_threshold.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled
        if target_gmv_threshold is not UNSET:
            field_dict["target_gmv_threshold"] = target_gmv_threshold

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_livestream_campaign_response_data_livestream_campaign_super_livestream_target_gmv_threshold import GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestreamTargetGmvThreshold # noqa: PLC0415
        d = dict(src_dict)
        is_enabled = d.pop("is_enabled", UNSET)

        _target_gmv_threshold = d.pop("target_gmv_threshold", UNSET)
        target_gmv_threshold: GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestreamTargetGmvThreshold | Unset
        if isinstance(_target_gmv_threshold,  Unset):
            target_gmv_threshold = UNSET
        else:
            target_gmv_threshold = GetLivestreamCampaignResponseDataLivestreamCampaignSuperLivestreamTargetGmvThreshold.from_dict(_target_gmv_threshold)




        get_livestream_campaign_response_data_livestream_campaign_super_livestream = cls(
            is_enabled=is_enabled,
            target_gmv_threshold=target_gmv_threshold,
        )


        get_livestream_campaign_response_data_livestream_campaign_super_livestream.additional_properties = d
        return get_livestream_campaign_response_data_livestream_campaign_super_livestream

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
