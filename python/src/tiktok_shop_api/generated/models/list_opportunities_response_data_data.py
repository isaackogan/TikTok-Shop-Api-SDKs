from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_opportunities_response_data_data_opportunity import ListOpportunitiesResponseDataDataOpportunity


T = TypeVar("T", bound="ListOpportunitiesResponseDataData")


@_attrs_define
class ListOpportunitiesResponseDataData:
    """
    Attributes:
        opportunities (list[ListOpportunitiesResponseDataDataOpportunity] | Unset): The opportunities returned on the
            current page.
        next_page_token (str | Unset): Pagination token to pass as `page_token` in the next request. This field is
            omitted when there are no more results.
        total_count (int | Unset): Total number of matching opportunities (approximate).
    """

    opportunities: list[ListOpportunitiesResponseDataDataOpportunity] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        opportunities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.opportunities, Unset):
            opportunities = []
            for opportunities_item_data in self.opportunities:
                opportunities_item = opportunities_item_data.to_dict()
                opportunities.append(opportunities_item)

        next_page_token = self.next_page_token

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opportunities is not UNSET:
            field_dict["opportunities"] = opportunities
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_opportunities_response_data_data_opportunity import (
            ListOpportunitiesResponseDataDataOpportunity,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _opportunities = d.pop("opportunities", UNSET)
        opportunities: list[ListOpportunitiesResponseDataDataOpportunity] | Unset = UNSET
        if _opportunities is not UNSET:
            opportunities = []
            for opportunities_item_data in _opportunities:
                opportunities_item = ListOpportunitiesResponseDataDataOpportunity.from_dict(opportunities_item_data)

                opportunities.append(opportunities_item)

        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        list_opportunities_response_data_data = cls(
            opportunities=opportunities,
            next_page_token=next_page_token,
            total_count=total_count,
        )

        list_opportunities_response_data_data.additional_properties = d
        return list_opportunities_response_data_data

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
