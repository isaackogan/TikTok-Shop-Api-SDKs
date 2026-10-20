from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographicMajorGender")



@_attrs_define
class SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographicMajorGender:
    """ 
        Attributes:
            gender (str | Unset): Top follower gender category of the creator, "MALE" or "FEMALE"
            percentage (int | Unset): Percentage of top follower gender, scaled up by 10,000 times.
                For example, 6524 stands for 0.6524 or 65.24%. You can then infer that the opposite gender would be 0.3476 or
                34.76%.
     """

    gender: str | Unset = UNSET
    percentage: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        gender = self.gender

        percentage = self.percentage


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if gender is not UNSET:
            field_dict["gender"] = gender
        if percentage is not UNSET:
            field_dict["percentage"] = percentage

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gender = d.pop("gender", UNSET)

        percentage = d.pop("percentage", UNSET)

        search_creators_in_creator_marketplace_response_data_creator_top_follower_demographic_major_gender = cls(
            gender=gender,
            percentage=percentage,
        )


        search_creators_in_creator_marketplace_response_data_creator_top_follower_demographic_major_gender.additional_properties = d
        return search_creators_in_creator_marketplace_response_data_creator_top_follower_demographic_major_gender

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
