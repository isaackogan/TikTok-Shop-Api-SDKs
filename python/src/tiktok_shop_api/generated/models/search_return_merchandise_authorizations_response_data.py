from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_return_merchandise_authorizations_response_data_return_merchandise_authorization import SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorization





T = TypeVar("T", bound="SearchReturnMerchandiseAuthorizationsResponseData")



@_attrs_define
class SearchReturnMerchandiseAuthorizationsResponseData:
    """ 
        Attributes:
            return_merchandise_authorizations
                (list[SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorization] | Unset): List of return
                merchandise authorization (RMA) records matching the filters. This field is omitted when no records match.
            total_count (int | Unset): The total result set size, independent of pagination.
            next_page_token (str | Unset): Used to fetch the next page/set of results.
     """

    return_merchandise_authorizations: list[SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorization] | Unset = UNSET
    total_count: int | Unset = UNSET
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_return_merchandise_authorizations_response_data_return_merchandise_authorization import SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorization # noqa: PLC0415
        return_merchandise_authorizations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.return_merchandise_authorizations, Unset):
            return_merchandise_authorizations = []
            for return_merchandise_authorizations_item_data in self.return_merchandise_authorizations:
                return_merchandise_authorizations_item = return_merchandise_authorizations_item_data.to_dict()
                return_merchandise_authorizations.append(return_merchandise_authorizations_item)



        total_count = self.total_count

        next_page_token = self.next_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if return_merchandise_authorizations is not UNSET:
            field_dict["return_merchandise_authorizations"] = return_merchandise_authorizations
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_return_merchandise_authorizations_response_data_return_merchandise_authorization import SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorization # noqa: PLC0415
        d = dict(src_dict)
        _return_merchandise_authorizations = d.pop("return_merchandise_authorizations", UNSET)
        return_merchandise_authorizations: list[SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorization] | Unset = UNSET
        if _return_merchandise_authorizations is not UNSET:
            return_merchandise_authorizations = []
            for return_merchandise_authorizations_item_data in _return_merchandise_authorizations:
                return_merchandise_authorizations_item = SearchReturnMerchandiseAuthorizationsResponseDataReturnMerchandiseAuthorization.from_dict(return_merchandise_authorizations_item_data)



                return_merchandise_authorizations.append(return_merchandise_authorizations_item)


        total_count = d.pop("total_count", UNSET)

        next_page_token = d.pop("next_page_token", UNSET)

        search_return_merchandise_authorizations_response_data = cls(
            return_merchandise_authorizations=return_merchandise_authorizations,
            total_count=total_count,
            next_page_token=next_page_token,
        )


        search_return_merchandise_authorizations_response_data.additional_properties = d
        return search_return_merchandise_authorizations_response_data

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
