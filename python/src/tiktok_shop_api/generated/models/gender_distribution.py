from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gender_distribution_gender import GenderDistributionGender
from ..types import UNSET, Unset

T = TypeVar("T", bound="GenderDistribution")


@_attrs_define
class GenderDistribution:
    """
    Attributes:
        gender (GenderDistributionGender | Unset): Viewer gender. Possible values:

            - MALE: male viewers

            - FEMALE: female viewers
        percentage (str | Unset): Proportion for the corresponding gender within this viewer profile, expressed as a
            decimal fraction.
    """

    gender: GenderDistributionGender | Unset = UNSET
    percentage: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gender: str | Unset = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        percentage = self.percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gender is not UNSET:
            field_dict["gender"] = gender
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _gender = d.pop("gender", UNSET)
        gender: GenderDistributionGender | Unset
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = GenderDistributionGender(_gender)

        percentage = d.pop("percentage", UNSET)

        gender_distribution = cls(
            gender=gender,
            percentage=percentage,
        )

        gender_distribution.additional_properties = d
        return gender_distribution

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
