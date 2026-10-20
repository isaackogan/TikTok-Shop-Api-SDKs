from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_responsible_persons_response_data_responsible_person_regional_profile import (
        SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfile,
    )


T = TypeVar("T", bound="SearchResponsiblePersonsResponseDataResponsiblePerson")


@_attrs_define
class SearchResponsiblePersonsResponseDataResponsiblePerson:
    """
    Attributes:
        id (str | Unset): The responsible person ID in TikTok Shop.
        regional_profiles (list[SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfile] | Unset): A list
            of contact details for the responsible person, presented in different languages for each supported EU country.
    """

    id: str | Unset = UNSET
    regional_profiles: list[SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfile] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        regional_profiles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.regional_profiles, Unset):
            regional_profiles = []
            for regional_profiles_item_data in self.regional_profiles:
                regional_profiles_item = regional_profiles_item_data.to_dict()
                regional_profiles.append(regional_profiles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if regional_profiles is not UNSET:
            field_dict["regional_profiles"] = regional_profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_responsible_persons_response_data_responsible_person_regional_profile import (
            SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfile,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _regional_profiles = d.pop("regional_profiles", UNSET)
        regional_profiles: list[SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfile] | Unset = UNSET
        if _regional_profiles is not UNSET:
            regional_profiles = []
            for regional_profiles_item_data in _regional_profiles:
                regional_profiles_item = SearchResponsiblePersonsResponseDataResponsiblePersonRegionalProfile.from_dict(
                    regional_profiles_item_data
                )

                regional_profiles.append(regional_profiles_item)

        search_responsible_persons_response_data_responsible_person = cls(
            id=id,
            regional_profiles=regional_profiles,
        )

        search_responsible_persons_response_data_responsible_person.additional_properties = d
        return search_responsible_persons_response_data_responsible_person

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
