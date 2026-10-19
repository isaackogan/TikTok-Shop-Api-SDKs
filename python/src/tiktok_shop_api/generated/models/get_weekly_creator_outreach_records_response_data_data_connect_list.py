from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWeeklyCreatorOutreachRecordsResponseDataDataConnectList")


@_attrs_define
class GetWeeklyCreatorOutreachRecordsResponseDataDataConnectList:
    """
    Attributes:
        id (str | Unset): Record ID
        creator_open_id (str | Unset): Creator open id
        has_sent_im_message (bool | Unset): Has send im message to creator
        has_sent_invitation (bool | Unset): Has send invitation to creator
        is_paired (bool | Unset): Is shop creator paired
    """

    id: str | Unset = UNSET
    creator_open_id: str | Unset = UNSET
    has_sent_im_message: bool | Unset = UNSET
    has_sent_invitation: bool | Unset = UNSET
    is_paired: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        creator_open_id = self.creator_open_id

        has_sent_im_message = self.has_sent_im_message

        has_sent_invitation = self.has_sent_invitation

        is_paired = self.is_paired

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if creator_open_id is not UNSET:
            field_dict["creator_open_id"] = creator_open_id
        if has_sent_im_message is not UNSET:
            field_dict["has_sent_im_message"] = has_sent_im_message
        if has_sent_invitation is not UNSET:
            field_dict["has_sent_invitation"] = has_sent_invitation
        if is_paired is not UNSET:
            field_dict["is_paired"] = is_paired

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        creator_open_id = d.pop("creator_open_id", UNSET)

        has_sent_im_message = d.pop("has_sent_im_message", UNSET)

        has_sent_invitation = d.pop("has_sent_invitation", UNSET)

        is_paired = d.pop("is_paired", UNSET)

        get_weekly_creator_outreach_records_response_data_data_connect_list = cls(
            id=id,
            creator_open_id=creator_open_id,
            has_sent_im_message=has_sent_im_message,
            has_sent_invitation=has_sent_invitation,
            is_paired=is_paired,
        )

        get_weekly_creator_outreach_records_response_data_data_connect_list.additional_properties = d
        return get_weekly_creator_outreach_records_response_data_data_connect_list

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
