from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicGenderDistribution")


@_attrs_define
class SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicGenderDistribution:
    """
    Attributes:
        gender (str | Unset): A particular gender, "MALE" or "FEMALE"
        percentage_ge (int | Unset): Greater than or equal to a certain percentage, scaled up by 10,000 times.
            For example, 6000 stands for 0.6 or 60%
    """

    gender: str | Unset = UNSET
    percentage_ge: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gender = self.gender

        percentage_ge = self.percentage_ge

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gender is not UNSET:
            field_dict["gender"] = gender
        if percentage_ge is not UNSET:
            field_dict["percentage_ge"] = percentage_ge

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gender = d.pop("gender", UNSET)

        percentage_ge = d.pop("percentage_ge", UNSET)

        search_creators_in_creator_marketplace_request_follower_demographic_gender_distribution = cls(
            gender=gender,
            percentage_ge=percentage_ge,
        )

        search_creators_in_creator_marketplace_request_follower_demographic_gender_distribution.additional_properties = d
        return search_creators_in_creator_marketplace_request_follower_demographic_gender_distribution

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
