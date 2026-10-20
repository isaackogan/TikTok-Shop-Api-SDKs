from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_cancellations_response_data_cancellation import SearchCancellationsResponseDataCancellation


T = TypeVar("T", bound="SearchCancellationsResponseData")


@_attrs_define
class SearchCancellationsResponseData:
    """
    Attributes:
        cancellations (list[SearchCancellationsResponseDataCancellation] | Unset): List of order cancellations.
        total_count (int | Unset): The number of cancellations that meet the query conditions.
        next_page_token (str | Unset): An opaque token used to retrieve the next page of results. If this value is non-
            empty, provide it in the `page_token` parameter of the next request. An empty value indicates that there are no
            more results.
    """

    cancellations: list[SearchCancellationsResponseDataCancellation] | Unset = UNSET
    total_count: int | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cancellations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cancellations, Unset):
            cancellations = []
            for cancellations_item_data in self.cancellations:
                cancellations_item = cancellations_item_data.to_dict()
                cancellations.append(cancellations_item)

        total_count = self.total_count

        next_page_token = self.next_page_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancellations is not UNSET:
            field_dict["cancellations"] = cancellations
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_cancellations_response_data_cancellation import (
            SearchCancellationsResponseDataCancellation,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _cancellations = d.pop("cancellations", UNSET)
        cancellations: list[SearchCancellationsResponseDataCancellation] | Unset = UNSET
        if _cancellations is not UNSET:
            cancellations = []
            for cancellations_item_data in _cancellations:
                cancellations_item = SearchCancellationsResponseDataCancellation.from_dict(cancellations_item_data)

                cancellations.append(cancellations_item)

        total_count = d.pop("total_count", UNSET)

        next_page_token = d.pop("next_page_token", UNSET)

        search_cancellations_response_data = cls(
            cancellations=cancellations,
            total_count=total_count,
            next_page_token=next_page_token,
        )

        search_cancellations_response_data.additional_properties = d
        return search_cancellations_response_data

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
