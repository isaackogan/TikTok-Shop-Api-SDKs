from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_responsible_persons_request_locales_item import SearchResponsiblePersonsRequestLocalesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchResponsiblePersonsRequest")


@_attrs_define
class SearchResponsiblePersonsRequest:
    """
    Attributes:
        responsible_person_ids (list[str] | Unset): Filter results by these responsible person IDs.
            Max IDs: The value of `page_size`
        keyword (str | Unset): Filter results to show those that contain this keyword.
            Search scope: name, local_number, email
            Max length: 200 characters

            **Note**: Provide either the `responsible_person_ids` or `keyword`; if both are provided,
            `responsible_person_ids` will take priority.
        locales (list[SearchResponsiblePersonsRequestLocalesItem] | Unset): The BCP-47 locale codes for displaying the
            responsible person information.
            Default: The locale of the seller's registered business address.
            Possible values:
            - de-DE
            - en-IE
            - es-ES
            - fr-FR
            - it-IT
    """

    responsible_person_ids: list[str] | Unset = UNSET
    keyword: str | Unset = UNSET
    locales: list[SearchResponsiblePersonsRequestLocalesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        responsible_person_ids: list[str] | Unset = UNSET
        if not isinstance(self.responsible_person_ids, Unset):
            responsible_person_ids = self.responsible_person_ids

        keyword = self.keyword

        locales: list[str] | Unset = UNSET
        if not isinstance(self.locales, Unset):
            locales = []
            for locales_item_data in self.locales:
                locales_item = locales_item_data.value
                locales.append(locales_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if responsible_person_ids is not UNSET:
            field_dict["responsible_person_ids"] = responsible_person_ids
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if locales is not UNSET:
            field_dict["locales"] = locales

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        responsible_person_ids = cast(list[str], d.pop("responsible_person_ids", UNSET))

        keyword = d.pop("keyword", UNSET)

        _locales = d.pop("locales", UNSET)
        locales: list[SearchResponsiblePersonsRequestLocalesItem] | Unset = UNSET
        if _locales is not UNSET:
            locales = []
            for locales_item_data in _locales:
                locales_item = SearchResponsiblePersonsRequestLocalesItem(locales_item_data)

                locales.append(locales_item)

        search_responsible_persons_request = cls(
            responsible_person_ids=responsible_person_ids,
            keyword=keyword,
            locales=locales,
        )

        search_responsible_persons_request.additional_properties = d
        return search_responsible_persons_request

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
