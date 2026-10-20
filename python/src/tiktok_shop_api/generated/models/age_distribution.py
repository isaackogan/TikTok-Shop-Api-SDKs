from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AgeDistribution")



@_attrs_define
class AgeDistribution:
    """ 
        Attributes:
            age (str | Unset): Possible values:
                - 18-24
                - 25-34
                - 35-44
                - 45-54
                - 55+
            percentage (str | Unset): Proportion for the corresponding age group within this viewer profile, expressed as a
                decimal fraction.
     """

    age: str | Unset = UNSET
    percentage: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        age = self.age

        percentage = self.percentage


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if age is not UNSET:
            field_dict["age"] = age
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        age = d.pop("age", UNSET)

        percentage = d.pop("percentage", UNSET)

        age_distribution = cls(
            age=age,
            percentage=percentage,
        )


        age_distribution.additional_properties = d
        return age_distribution

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
