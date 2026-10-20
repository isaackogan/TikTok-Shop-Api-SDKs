from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_creators_in_creator_marketplace_response_data_creator_top_follower_demographic_major_gender import SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographicMajorGender





T = TypeVar("T", bound="SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographic")



@_attrs_define
class SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographic:
    """ 
        Attributes:
            age_ranges (list[str] | Unset): Return the top 3 age ranges of the followers. Ranges are :
                AGE_RANGE_18_24: "18-24",
                AGE_RANGE_25_34: "25-34",
                AGE_RANGE_35_44: "35-44",
                AGE_RANGE_45_54: "45-54",
                AGE_RANGE_55_AND_ABOVE: "55+"
            major_gender (SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographicMajorGender | Unset):
     """

    age_ranges: list[str] | Unset = UNSET
    major_gender: SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographicMajorGender | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_creators_in_creator_marketplace_response_data_creator_top_follower_demographic_major_gender import SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographicMajorGender # noqa: PLC0415
        age_ranges: list[str] | Unset = UNSET
        if not isinstance(self.age_ranges, Unset):
            age_ranges = self.age_ranges



        major_gender: dict[str, Any] | Unset = UNSET
        if not isinstance(self.major_gender, Unset):
            major_gender = self.major_gender.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if age_ranges is not UNSET:
            field_dict["age_ranges"] = age_ranges
        if major_gender is not UNSET:
            field_dict["major_gender"] = major_gender

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_creators_in_creator_marketplace_response_data_creator_top_follower_demographic_major_gender import SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographicMajorGender # noqa: PLC0415
        d = dict(src_dict)
        age_ranges = cast(list[str], d.pop("age_ranges", UNSET))


        _major_gender = d.pop("major_gender", UNSET)
        major_gender: SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographicMajorGender | Unset
        if isinstance(_major_gender,  Unset):
            major_gender = UNSET
        else:
            major_gender = SearchCreatorsInCreatorMarketplaceResponseDataCreatorTopFollowerDemographicMajorGender.from_dict(_major_gender)




        search_creators_in_creator_marketplace_response_data_creator_top_follower_demographic = cls(
            age_ranges=age_ranges,
            major_gender=major_gender,
        )


        search_creators_in_creator_marketplace_response_data_creator_top_follower_demographic.additional_properties = d
        return search_creators_in_creator_marketplace_response_data_creator_top_follower_demographic

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
