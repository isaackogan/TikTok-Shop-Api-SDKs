from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_aftersales_requests_request_whitelisted_data_fields_item import (
    SearchAftersalesRequestsRequestWhitelistedDataFieldsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.search_aftersales_requests_request_filter import SearchAftersalesRequestsRequestFilter
    from ..models.sort import Sort


T = TypeVar("T", bound="SearchAftersalesRequestsRequest")


@_attrs_define
class SearchAftersalesRequestsRequest:
    """
    Attributes:
        whitelisted_data_fields (list[SearchAftersalesRequestsRequestWhitelistedDataFieldsItem] | Unset): Controls which
            additional fields are included for each aftersales request.
            Possible values:
            - `LINE_ITEMS`: Includes `line_items`.
            - `SKU_RETURN_REQUESTS`: Includes `sku_return_requests`.
            - `RETURN_MERCHANDISE_AUTHORIZATIONS`: Includes `return_merchandise_authorizations`.
        filters (SearchAftersalesRequestsRequestFilter | Unset):
        sort (Sort | Unset):
        pagination (Pagination | Unset):
    """

    whitelisted_data_fields: list[SearchAftersalesRequestsRequestWhitelistedDataFieldsItem] | Unset = UNSET
    filters: SearchAftersalesRequestsRequestFilter | Unset = UNSET
    sort: Sort | Unset = UNSET
    pagination: Pagination | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        whitelisted_data_fields: list[str] | Unset = UNSET
        if not isinstance(self.whitelisted_data_fields, Unset):
            whitelisted_data_fields = []
            for whitelisted_data_fields_item_data in self.whitelisted_data_fields:
                whitelisted_data_fields_item = whitelisted_data_fields_item_data.value
                whitelisted_data_fields.append(whitelisted_data_fields_item)

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        sort: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if whitelisted_data_fields is not UNSET:
            field_dict["whitelisted_data_fields"] = whitelisted_data_fields
        if filters is not UNSET:
            field_dict["filters"] = filters
        if sort is not UNSET:
            field_dict["sort"] = sort
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination  # noqa: PLC0415
        from ..models.search_aftersales_requests_request_filter import (
            SearchAftersalesRequestsRequestFilter,  # noqa: PLC0415
        )
        from ..models.sort import Sort  # noqa: PLC0415

        d = dict(src_dict)
        _whitelisted_data_fields = d.pop("whitelisted_data_fields", UNSET)
        whitelisted_data_fields: list[SearchAftersalesRequestsRequestWhitelistedDataFieldsItem] | Unset = UNSET
        if _whitelisted_data_fields is not UNSET:
            whitelisted_data_fields = []
            for whitelisted_data_fields_item_data in _whitelisted_data_fields:
                whitelisted_data_fields_item = SearchAftersalesRequestsRequestWhitelistedDataFieldsItem(
                    whitelisted_data_fields_item_data
                )

                whitelisted_data_fields.append(whitelisted_data_fields_item)

        _filters = d.pop("filters", UNSET)
        filters: SearchAftersalesRequestsRequestFilter | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = SearchAftersalesRequestsRequestFilter.from_dict(_filters)

        _sort = d.pop("sort", UNSET)
        sort: Sort | Unset
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = Sort.from_dict(_sort)

        _pagination = d.pop("pagination", UNSET)
        pagination: Pagination | Unset
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        search_aftersales_requests_request = cls(
            whitelisted_data_fields=whitelisted_data_fields,
            filters=filters,
            sort=sort,
            pagination=pagination,
        )

        search_aftersales_requests_request.additional_properties = d
        return search_aftersales_requests_request

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
