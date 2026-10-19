from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_open_collaborations_response_data_open_collaboration import (
        SearchOpenCollaborationsResponseDataOpenCollaboration,
    )


T = TypeVar("T", bound="SearchOpenCollaborationsResponseData")


@_attrs_define
class SearchOpenCollaborationsResponseData:
    """
    Attributes:
        next_page_token (str | Unset): Pagination token for the next page. Pass this value as `page_token` in the next
            request. An empty value indicates that there are no more results.
        total_count (int | Unset): Total count of products that satisfy all the input search conditions.
        open_collaborations (list[SearchOpenCollaborationsResponseDataOpenCollaboration] | Unset): Open collaborations
            matching the search criteria on the current page.
    """

    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    open_collaborations: list[SearchOpenCollaborationsResponseDataOpenCollaboration] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_page_token = self.next_page_token

        total_count = self.total_count

        open_collaborations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.open_collaborations, Unset):
            open_collaborations = []
            for open_collaborations_item_data in self.open_collaborations:
                open_collaborations_item = open_collaborations_item_data.to_dict()
                open_collaborations.append(open_collaborations_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if open_collaborations is not UNSET:
            field_dict["open_collaborations"] = open_collaborations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_open_collaborations_response_data_open_collaboration import (
            SearchOpenCollaborationsResponseDataOpenCollaboration,  # noqa: PLC0415
        )

        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        _open_collaborations = d.pop("open_collaborations", UNSET)
        open_collaborations: list[SearchOpenCollaborationsResponseDataOpenCollaboration] | Unset = UNSET
        if _open_collaborations is not UNSET:
            open_collaborations = []
            for open_collaborations_item_data in _open_collaborations:
                open_collaborations_item = SearchOpenCollaborationsResponseDataOpenCollaboration.from_dict(
                    open_collaborations_item_data
                )

                open_collaborations.append(open_collaborations_item)

        search_open_collaborations_response_data = cls(
            next_page_token=next_page_token,
            total_count=total_count,
            open_collaborations=open_collaborations,
        )

        search_open_collaborations_response_data.additional_properties = d
        return search_open_collaborations_response_data

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
