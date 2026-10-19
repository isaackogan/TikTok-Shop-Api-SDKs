from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_shop_video_performance_details_response_data_performance_viewer_profile_type import (
    GetShopVideoPerformanceDetailsResponseDataPerformanceViewerProfileType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.age_distribution import AgeDistribution
    from ..models.country_distribution import CountryDistribution
    from ..models.gender_distribution import GenderDistribution


T = TypeVar("T", bound="GetShopVideoPerformanceDetailsResponseDataPerformanceViewerProfile")


@_attrs_define
class GetShopVideoPerformanceDetailsResponseDataPerformanceViewerProfile:
    """
    Attributes:
        type_ (GetShopVideoPerformanceDetailsResponseDataPerformanceViewerProfileType | Unset): Viewer profile type.
            Possible values:

            - NEW_FOLLOWER: viewers who newly followed after watching the video

            - VIEWERS: viewers of the video
        gender_distribution (list[GenderDistribution] | Unset): View gender distribution
        age_distribution (list[AgeDistribution] | Unset): Viewer age distribution
        country_distribution (list[CountryDistribution] | Unset): Viewer country distribution.
    """

    type_: GetShopVideoPerformanceDetailsResponseDataPerformanceViewerProfileType | Unset = UNSET
    gender_distribution: list[GenderDistribution] | Unset = UNSET
    age_distribution: list[AgeDistribution] | Unset = UNSET
    country_distribution: list[CountryDistribution] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        gender_distribution: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gender_distribution, Unset):
            gender_distribution = []
            for gender_distribution_item_data in self.gender_distribution:
                gender_distribution_item = gender_distribution_item_data.to_dict()
                gender_distribution.append(gender_distribution_item)

        age_distribution: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.age_distribution, Unset):
            age_distribution = []
            for age_distribution_item_data in self.age_distribution:
                age_distribution_item = age_distribution_item_data.to_dict()
                age_distribution.append(age_distribution_item)

        country_distribution: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.country_distribution, Unset):
            country_distribution = []
            for country_distribution_item_data in self.country_distribution:
                country_distribution_item = country_distribution_item_data.to_dict()
                country_distribution.append(country_distribution_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if gender_distribution is not UNSET:
            field_dict["gender_distribution"] = gender_distribution
        if age_distribution is not UNSET:
            field_dict["age_distribution"] = age_distribution
        if country_distribution is not UNSET:
            field_dict["country_distribution"] = country_distribution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.age_distribution import AgeDistribution  # noqa: PLC0415
        from ..models.country_distribution import CountryDistribution  # noqa: PLC0415
        from ..models.gender_distribution import GenderDistribution  # noqa: PLC0415

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: GetShopVideoPerformanceDetailsResponseDataPerformanceViewerProfileType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GetShopVideoPerformanceDetailsResponseDataPerformanceViewerProfileType(_type_)

        _gender_distribution = d.pop("gender_distribution", UNSET)
        gender_distribution: list[GenderDistribution] | Unset = UNSET
        if _gender_distribution is not UNSET:
            gender_distribution = []
            for gender_distribution_item_data in _gender_distribution:
                gender_distribution_item = GenderDistribution.from_dict(gender_distribution_item_data)

                gender_distribution.append(gender_distribution_item)

        _age_distribution = d.pop("age_distribution", UNSET)
        age_distribution: list[AgeDistribution] | Unset = UNSET
        if _age_distribution is not UNSET:
            age_distribution = []
            for age_distribution_item_data in _age_distribution:
                age_distribution_item = AgeDistribution.from_dict(age_distribution_item_data)

                age_distribution.append(age_distribution_item)

        _country_distribution = d.pop("country_distribution", UNSET)
        country_distribution: list[CountryDistribution] | Unset = UNSET
        if _country_distribution is not UNSET:
            country_distribution = []
            for country_distribution_item_data in _country_distribution:
                country_distribution_item = CountryDistribution.from_dict(country_distribution_item_data)

                country_distribution.append(country_distribution_item)

        get_shop_video_performance_details_response_data_performance_viewer_profile = cls(
            type_=type_,
            gender_distribution=gender_distribution,
            age_distribution=age_distribution,
            country_distribution=country_distribution,
        )

        get_shop_video_performance_details_response_data_performance_viewer_profile.additional_properties = d
        return get_shop_video_performance_details_response_data_performance_viewer_profile

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
