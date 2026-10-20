from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CheckCreatorOutreachEligibilityRequestCreatorInfo")



@_attrs_define
class CheckCreatorOutreachEligibilityRequestCreatorInfo:
    """ 
        Attributes:
            creator_open_id (str): Creator Open ID.
     """

    creator_open_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        creator_open_id = self.creator_open_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "creator_open_id": creator_open_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        creator_open_id = d.pop("creator_open_id")

        check_creator_outreach_eligibility_request_creator_info = cls(
            creator_open_id=creator_open_id,
        )


        check_creator_outreach_eligibility_request_creator_info.additional_properties = d
        return check_creator_outreach_eligibility_request_creator_info

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
