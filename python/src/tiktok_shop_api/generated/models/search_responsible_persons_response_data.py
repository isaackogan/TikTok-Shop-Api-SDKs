from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_responsible_persons_response_data_responsible_person import (
        SearchResponsiblePersonsResponseDataResponsiblePerson,
    )


T = TypeVar("T", bound="SearchResponsiblePersonsResponseData")


@_attrs_define
class SearchResponsiblePersonsResponseData:
    """
    Attributes:
        responsible_persons (list[SearchResponsiblePersonsResponseDataResponsiblePerson] | Unset): The list of
            responsible persons that meet the query conditions.
        total_count (int | Unset): The number of responsible persons that meet the query conditions.
        next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. Provide
            this value in the `page_token` parameter of your request if the current response does not return all the
            results.
    """

    responsible_persons: list[SearchResponsiblePersonsResponseDataResponsiblePerson] | Unset = UNSET
    total_count: int | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        responsible_persons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.responsible_persons, Unset):
            responsible_persons = []
            for responsible_persons_item_data in self.responsible_persons:
                responsible_persons_item = responsible_persons_item_data.to_dict()
                responsible_persons.append(responsible_persons_item)

        total_count = self.total_count

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if responsible_persons is not UNSET:
            field_dict["responsible_persons"] = responsible_persons
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_responsible_persons_response_data_responsible_person import (
            SearchResponsiblePersonsResponseDataResponsiblePerson,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _responsible_persons = d.pop("responsible_persons", UNSET)
        responsible_persons: list[SearchResponsiblePersonsResponseDataResponsiblePerson] | Unset = UNSET
        if _responsible_persons is not UNSET:
            responsible_persons = []
            for responsible_persons_item_data in _responsible_persons:
                responsible_persons_item = SearchResponsiblePersonsResponseDataResponsiblePerson.from_dict(
                    responsible_persons_item_data
                )

                responsible_persons.append(responsible_persons_item)

        total_count = d.pop("total_count", UNSET)

        next_page_token = d.pop("next_page_token", UNSET)

        search_responsible_persons_response_data = cls(
            responsible_persons=responsible_persons,
            total_count=total_count,
            next_page_token=next_page_token,
        )

        search_responsible_persons_response_data.additional_properties = d
        return search_responsible_persons_response_data

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
