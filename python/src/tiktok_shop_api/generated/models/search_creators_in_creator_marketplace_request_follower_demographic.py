from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_creators_in_creator_marketplace_request_follower_demographic_count_range import (
        SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicCountRange,
    )
    from ..models.search_creators_in_creator_marketplace_request_follower_demographic_gender_distribution import (
        SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicGenderDistribution,
    )


T = TypeVar("T", bound="SearchCreatorsInCreatorMarketplaceRequestFollowerDemographic")


@_attrs_define
class SearchCreatorsInCreatorMarketplaceRequestFollowerDemographic:
    """
    Attributes:
        age_ranges (list[str] | Unset): Follower age filtering options, which are range intervals, include:
            AGE_RANGE_18_24: "18-24",
            AGE_RANGE_25_34: "25-34",
            AGE_RANGE_35_44: "35-44",
            AGE_RANGE_45_54: "45-54",
            AGE_RANGE_55_AND_ABOVE: "55+"
        count_range (SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicCountRange | Unset):
        gender_distribution (SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicGenderDistribution | Unset):
    """

    age_ranges: list[str] | Unset = UNSET
    count_range: SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicCountRange | Unset = UNSET
    gender_distribution: SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicGenderDistribution | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        age_ranges: list[str] | Unset = UNSET
        if not isinstance(self.age_ranges, Unset):
            age_ranges = self.age_ranges

        count_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.count_range, Unset):
            count_range = self.count_range.to_dict()

        gender_distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gender_distribution, Unset):
            gender_distribution = self.gender_distribution.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if age_ranges is not UNSET:
            field_dict["age_ranges"] = age_ranges
        if count_range is not UNSET:
            field_dict["count_range"] = count_range
        if gender_distribution is not UNSET:
            field_dict["gender_distribution"] = gender_distribution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_creators_in_creator_marketplace_request_follower_demographic_count_range import (
            SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicCountRange,  # noqa: PLC0415
        )
        from ..models.search_creators_in_creator_marketplace_request_follower_demographic_gender_distribution import (
            SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicGenderDistribution,  # noqa: PLC0415
        )

        d = dict(src_dict)
        age_ranges = cast(list[str], d.pop("age_ranges", UNSET))

        _count_range = d.pop("count_range", UNSET)
        count_range: SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicCountRange | Unset
        if isinstance(_count_range, Unset):
            count_range = UNSET
        else:
            count_range = SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicCountRange.from_dict(_count_range)

        _gender_distribution = d.pop("gender_distribution", UNSET)
        gender_distribution: SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicGenderDistribution | Unset
        if isinstance(_gender_distribution, Unset):
            gender_distribution = UNSET
        else:
            gender_distribution = (
                SearchCreatorsInCreatorMarketplaceRequestFollowerDemographicGenderDistribution.from_dict(
                    _gender_distribution
                )
            )

        search_creators_in_creator_marketplace_request_follower_demographic = cls(
            age_ranges=age_ranges,
            count_range=count_range,
            gender_distribution=gender_distribution,
        )

        search_creators_in_creator_marketplace_request_follower_demographic.additional_properties = d
        return search_creators_in_creator_marketplace_request_follower_demographic

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
