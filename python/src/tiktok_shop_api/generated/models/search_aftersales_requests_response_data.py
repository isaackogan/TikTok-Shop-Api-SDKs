from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_aftersales_requests_response_data_aftersales_request import SearchAftersalesRequestsResponseDataAftersalesRequest





T = TypeVar("T", bound="SearchAftersalesRequestsResponseData")



@_attrs_define
class SearchAftersalesRequestsResponseData:
    """ 
        Attributes:
            aftersales_requests (list[SearchAftersalesRequestsResponseDataAftersalesRequest] | Unset): List of aftersales
                requests matching the filters. This field is omitted when no aftersales requests match.
            total_count (int | Unset): The total result set size, independent of pagination.
            next_page_token (str | Unset): Used to fetch the next page/set of results.
     """

    aftersales_requests: list[SearchAftersalesRequestsResponseDataAftersalesRequest] | Unset = UNSET
    total_count: int | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_aftersales_requests_response_data_aftersales_request import SearchAftersalesRequestsResponseDataAftersalesRequest # noqa: PLC0415
        aftersales_requests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aftersales_requests, Unset):
            aftersales_requests = []
            for aftersales_requests_item_data in self.aftersales_requests:
                aftersales_requests_item = aftersales_requests_item_data.to_dict()
                aftersales_requests.append(aftersales_requests_item)



        total_count = self.total_count

        next_page_token = self.next_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aftersales_requests is not UNSET:
            field_dict["aftersales_requests"] = aftersales_requests
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_aftersales_requests_response_data_aftersales_request import SearchAftersalesRequestsResponseDataAftersalesRequest # noqa: PLC0415
        d = dict(src_dict)
        _aftersales_requests = d.pop("aftersales_requests", UNSET)
        aftersales_requests: list[SearchAftersalesRequestsResponseDataAftersalesRequest] | Unset = UNSET
        if _aftersales_requests is not UNSET:
            aftersales_requests = []
            for aftersales_requests_item_data in _aftersales_requests:
                aftersales_requests_item = SearchAftersalesRequestsResponseDataAftersalesRequest.from_dict(aftersales_requests_item_data)



                aftersales_requests.append(aftersales_requests_item)


        total_count = d.pop("total_count", UNSET)

        next_page_token = d.pop("next_page_token", UNSET)

        search_aftersales_requests_response_data = cls(
            aftersales_requests=aftersales_requests,
            total_count=total_count,
            next_page_token=next_page_token,
        )


        search_aftersales_requests_response_data.additional_properties = d
        return search_aftersales_requests_response_data

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
