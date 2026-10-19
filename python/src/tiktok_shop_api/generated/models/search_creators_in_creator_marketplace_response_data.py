from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_creators_in_creator_marketplace_response_data_creator import (
        SearchCreatorsInCreatorMarketplaceResponseDataCreator,
    )


T = TypeVar("T", bound="SearchCreatorsInCreatorMarketplaceResponseData")


@_attrs_define
class SearchCreatorsInCreatorMarketplaceResponseData:
    """
    Attributes:
        next_page_token (str | Unset): Pagination token for the next page. To continue, pass this value as query
            parameter `page_token`, pass the `search_key` returned in the same response as request-body `search_key`, and
            reuse the same `page_size`. An empty token means there are no more results.
        search_key (str | Unset): Search key for continuing the same search with stable results. Pass this value as
            search_key in the next request.
        creators (list[SearchCreatorsInCreatorMarketplaceResponseDataCreator] | Unset): Creator records with basic
            profile, content performance, follower, GMV, and sales-range information. Included fields depend on the
            requested `data_groups`.
    """

    next_page_token: str | Unset = UNSET
    search_key: str | Unset = UNSET
    creators: list[SearchCreatorsInCreatorMarketplaceResponseDataCreator] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_page_token = self.next_page_token

        search_key = self.search_key

        creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = []
            for creators_item_data in self.creators:
                creators_item = creators_item_data.to_dict()
                creators.append(creators_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if search_key is not UNSET:
            field_dict["search_key"] = search_key
        if creators is not UNSET:
            field_dict["creators"] = creators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_creators_in_creator_marketplace_response_data_creator import (
            SearchCreatorsInCreatorMarketplaceResponseDataCreator,  # noqa: PLC0415
        )

        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        search_key = d.pop("search_key", UNSET)

        _creators = d.pop("creators", UNSET)
        creators: list[SearchCreatorsInCreatorMarketplaceResponseDataCreator] | Unset = UNSET
        if _creators is not UNSET:
            creators = []
            for creators_item_data in _creators:
                creators_item = SearchCreatorsInCreatorMarketplaceResponseDataCreator.from_dict(creators_item_data)

                creators.append(creators_item)

        search_creators_in_creator_marketplace_response_data = cls(
            next_page_token=next_page_token,
            search_key=search_key,
            creators=creators,
        )

        search_creators_in_creator_marketplace_response_data.additional_properties = d
        return search_creators_in_creator_marketplace_response_data

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
