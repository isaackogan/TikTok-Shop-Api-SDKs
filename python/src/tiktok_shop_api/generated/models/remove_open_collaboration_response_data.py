from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RemoveOpenCollaborationResponseData")



@_attrs_define
class RemoveOpenCollaborationResponseData:
    """ 
        Attributes:
            terminated_effective_time (int | Unset): The Unix timestamp, in seconds, when the open collaboration termination
                takes effect. This is usually 00:00 on the next day in the shop's time zone.
     """

    terminated_effective_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        terminated_effective_time = self.terminated_effective_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if terminated_effective_time is not UNSET:
            field_dict["terminated_effective_time"] = terminated_effective_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        terminated_effective_time = d.pop("terminated_effective_time", UNSET)

        remove_open_collaboration_response_data = cls(
            terminated_effective_time=terminated_effective_time,
        )


        remove_open_collaboration_response_data.additional_properties = d
        return remove_open_collaboration_response_data

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
