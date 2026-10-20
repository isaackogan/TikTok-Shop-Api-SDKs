from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetSPSOverviewResponseDataBenefit")



@_attrs_define
class GetSPSOverviewResponseDataBenefit:
    """ 
        Attributes:
            benefit_name (str | Unset): Benefit display name localized by the requested locale.
            is_unlocked (bool | Unset): Whether the shop has unlocked this benefit.
            unlock_score (str | Unset): Score required to unlock the benefit, from 0 to 5.
     """

    benefit_name: str | Unset = UNSET
    is_unlocked: bool | Unset = UNSET
    unlock_score: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        benefit_name = self.benefit_name

        is_unlocked = self.is_unlocked

        unlock_score = self.unlock_score


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if benefit_name is not UNSET:
            field_dict["benefit_name"] = benefit_name
        if is_unlocked is not UNSET:
            field_dict["is_unlocked"] = is_unlocked
        if unlock_score is not UNSET:
            field_dict["unlock_score"] = unlock_score

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        benefit_name = d.pop("benefit_name", UNSET)

        is_unlocked = d.pop("is_unlocked", UNSET)

        unlock_score = d.pop("unlock_score", UNSET)

        get_sps_overview_response_data_benefit = cls(
            benefit_name=benefit_name,
            is_unlocked=is_unlocked,
            unlock_score=unlock_score,
        )


        get_sps_overview_response_data_benefit.additional_properties = d
        return get_sps_overview_response_data_benefit

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
