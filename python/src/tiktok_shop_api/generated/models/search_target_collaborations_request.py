from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_target_collaborations_request_creator_accept_status import SearchTargetCollaborationsRequestCreatorAcceptStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_target_collaborations_request_search_param import SearchTargetCollaborationsRequestSearchParam





T = TypeVar("T", bound="SearchTargetCollaborationsRequest")



@_attrs_define
class SearchTargetCollaborationsRequest:
    """ 
        Attributes:
            collaboration_status (str): Filtering by target collaborations' status.
                You can query based on:
                - ONGOING: If you use ONGOING to search, the remaining validity period of the returned target collaborations
                will be greater than 7 days.
                - EXPIRING: If you use EXPIRING to search, the remaining validity period of the returned target collaborations
                will be less than 7 days.
                - VALID: If you use VALID to search, all returned target collaborations will be valid.
                - CANCELING: If you use CANCELING to search, all returned target collaborations will be in the process of
                canceling.
                - COMPLETED: If you use COMPLETED to search, all returned target collaborations will be in the state of
                completed, including expired and canceled.
            creator_accept_status (SearchTargetCollaborationsRequestCreatorAcceptStatus | Unset): Filter target
                collaborations by the acceptance status of invited creators.
                Allowed values:
                - ACCEPT: The creators have added the products to their showcases.
                - ALL: Do not filter by whether the creators have added the products to their showcases.
                Default: ALL.
            free_sample_setting (str | Unset): Filtering by target collaborations' free sample setting.
                You can query based on:
                - "WITH_FREE_SAMPLE"
                - "ALL"
                By default, the target collaborations will be searched by "ALL" setting.
            search_param (SearchTargetCollaborationsRequestSearchParam | Unset):
            creator_user_open_id (str | Unset): The creator's TikTok User Open ID. Provide this field to filter target
                collaborations for the specified creator. [More details](https://partner.tiktokshop.com/docv2/page/3obfokj6)
     """

    collaboration_status: str
    creator_accept_status: SearchTargetCollaborationsRequestCreatorAcceptStatus | Unset = UNSET
    free_sample_setting: str | Unset = UNSET
    search_param: SearchTargetCollaborationsRequestSearchParam | Unset = UNSET
    creator_user_open_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_target_collaborations_request_search_param import SearchTargetCollaborationsRequestSearchParam # noqa: PLC0415
        collaboration_status = self.collaboration_status

        creator_accept_status: str | Unset = UNSET
        if not isinstance(self.creator_accept_status, Unset):
            creator_accept_status = self.creator_accept_status.value


        free_sample_setting = self.free_sample_setting

        search_param: dict[str, Any] | Unset = UNSET
        if not isinstance(self.search_param, Unset):
            search_param = self.search_param.to_dict()

        creator_user_open_id = self.creator_user_open_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "collaboration_status": collaboration_status,
        })
        if creator_accept_status is not UNSET:
            field_dict["creator_accept_status"] = creator_accept_status
        if free_sample_setting is not UNSET:
            field_dict["free_sample_setting"] = free_sample_setting
        if search_param is not UNSET:
            field_dict["search_param"] = search_param
        if creator_user_open_id is not UNSET:
            field_dict["creator_user_open_id"] = creator_user_open_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_target_collaborations_request_search_param import SearchTargetCollaborationsRequestSearchParam # noqa: PLC0415
        d = dict(src_dict)
        collaboration_status = d.pop("collaboration_status")

        _creator_accept_status = d.pop("creator_accept_status", UNSET)
        creator_accept_status: SearchTargetCollaborationsRequestCreatorAcceptStatus | Unset
        if isinstance(_creator_accept_status,  Unset):
            creator_accept_status = UNSET
        else:
            creator_accept_status = SearchTargetCollaborationsRequestCreatorAcceptStatus(_creator_accept_status)




        free_sample_setting = d.pop("free_sample_setting", UNSET)

        _search_param = d.pop("search_param", UNSET)
        search_param: SearchTargetCollaborationsRequestSearchParam | Unset
        if isinstance(_search_param,  Unset):
            search_param = UNSET
        else:
            search_param = SearchTargetCollaborationsRequestSearchParam.from_dict(_search_param)




        creator_user_open_id = d.pop("creator_user_open_id", UNSET)

        search_target_collaborations_request = cls(
            collaboration_status=collaboration_status,
            creator_accept_status=creator_accept_status,
            free_sample_setting=free_sample_setting,
            search_param=search_param,
            creator_user_open_id=creator_user_open_id,
        )


        search_target_collaborations_request.additional_properties = d
        return search_target_collaborations_request

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
