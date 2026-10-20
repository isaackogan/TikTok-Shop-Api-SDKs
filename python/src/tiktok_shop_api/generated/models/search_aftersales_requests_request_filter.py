from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_aftersales_requests_request_filter_aftersales_request_statuses_item import SearchAftersalesRequestsRequestFilterAftersalesRequestStatusesItem
from ..models.search_aftersales_requests_request_filter_return_types_item import SearchAftersalesRequestsRequestFilterReturnTypesItem
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.time import Time





T = TypeVar("T", bound="SearchAftersalesRequestsRequestFilter")



@_attrs_define
class SearchAftersalesRequestsRequestFilter:
    """ 
        Attributes:
            aftersales_request_ids (list[str] | Unset): Restricts results to the specified aftersales requests. Each ID must
                be a base-10 integer string that fits in a signed 64-bit integer.
            aftersales_request_statuses (list[SearchAftersalesRequestsRequestFilterAftersalesRequestStatusesItem] | Unset):
                Restricts results to the specified aftersales request statuses.
                Possible values:
                - `INIT`
                - `PENDING_REQUEST_REVIEW`
                - `REQUEST_REVIEW_COMPLETED`
            return_types (list[SearchAftersalesRequestsRequestFilterReturnTypesItem] | Unset): Restricts results to
                aftersales request data which includes at least one sku return request with a given type.
                Possible values:
                - `REFUND`
                - `RETURN_AND_REFUND`
                - `REPLACEMENT`
                - `EXCHANGE`
            main_order_ids (list[str] | Unset): Restricts results to aftersales requests that contain at least one SKU
                return request for a specified main (forward) order. Each main order ID must be a base-10 integer string that
                fits in a signed 64-bit integer.
            buyer_ids (list[str] | Unset): Restricts results to aftersales requests that contain at least one SKU return
                request for a specified buyer. Each buyer ID must be a base-10 integer string that fits in a signed 64-bit
                integer.
            time (Time | Unset):
     """

    aftersales_request_ids: list[str] | Unset = UNSET
    aftersales_request_statuses: list[SearchAftersalesRequestsRequestFilterAftersalesRequestStatusesItem] | Unset = UNSET
    return_types: list[SearchAftersalesRequestsRequestFilterReturnTypesItem] | Unset = UNSET
    main_order_ids: list[str] | Unset = UNSET
    buyer_ids: list[str] | Unset = UNSET
    time: Time | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.time import Time # noqa: PLC0415
        aftersales_request_ids: list[str] | Unset = UNSET
        if not isinstance(self.aftersales_request_ids, Unset):
            aftersales_request_ids = self.aftersales_request_ids



        aftersales_request_statuses: list[str] | Unset = UNSET
        if not isinstance(self.aftersales_request_statuses, Unset):
            aftersales_request_statuses = []
            for aftersales_request_statuses_item_data in self.aftersales_request_statuses:
                aftersales_request_statuses_item = aftersales_request_statuses_item_data.value
                aftersales_request_statuses.append(aftersales_request_statuses_item)



        return_types: list[str] | Unset = UNSET
        if not isinstance(self.return_types, Unset):
            return_types = []
            for return_types_item_data in self.return_types:
                return_types_item = return_types_item_data.value
                return_types.append(return_types_item)



        main_order_ids: list[str] | Unset = UNSET
        if not isinstance(self.main_order_ids, Unset):
            main_order_ids = self.main_order_ids



        buyer_ids: list[str] | Unset = UNSET
        if not isinstance(self.buyer_ids, Unset):
            buyer_ids = self.buyer_ids



        time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aftersales_request_ids is not UNSET:
            field_dict["aftersales_request_ids"] = aftersales_request_ids
        if aftersales_request_statuses is not UNSET:
            field_dict["aftersales_request_statuses"] = aftersales_request_statuses
        if return_types is not UNSET:
            field_dict["return_types"] = return_types
        if main_order_ids is not UNSET:
            field_dict["main_order_ids"] = main_order_ids
        if buyer_ids is not UNSET:
            field_dict["buyer_ids"] = buyer_ids
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.time import Time # noqa: PLC0415
        d = dict(src_dict)
        aftersales_request_ids = cast(list[str], d.pop("aftersales_request_ids", UNSET))


        _aftersales_request_statuses = d.pop("aftersales_request_statuses", UNSET)
        aftersales_request_statuses: list[SearchAftersalesRequestsRequestFilterAftersalesRequestStatusesItem] | Unset = UNSET
        if _aftersales_request_statuses is not UNSET:
            aftersales_request_statuses = []
            for aftersales_request_statuses_item_data in _aftersales_request_statuses:
                aftersales_request_statuses_item = SearchAftersalesRequestsRequestFilterAftersalesRequestStatusesItem(aftersales_request_statuses_item_data)



                aftersales_request_statuses.append(aftersales_request_statuses_item)


        _return_types = d.pop("return_types", UNSET)
        return_types: list[SearchAftersalesRequestsRequestFilterReturnTypesItem] | Unset = UNSET
        if _return_types is not UNSET:
            return_types = []
            for return_types_item_data in _return_types:
                return_types_item = SearchAftersalesRequestsRequestFilterReturnTypesItem(return_types_item_data)



                return_types.append(return_types_item)


        main_order_ids = cast(list[str], d.pop("main_order_ids", UNSET))


        buyer_ids = cast(list[str], d.pop("buyer_ids", UNSET))


        _time = d.pop("time", UNSET)
        time: Time | Unset
        if isinstance(_time,  Unset):
            time = UNSET
        else:
            time = Time.from_dict(_time)




        search_aftersales_requests_request_filter = cls(
            aftersales_request_ids=aftersales_request_ids,
            aftersales_request_statuses=aftersales_request_statuses,
            return_types=return_types,
            main_order_ids=main_order_ids,
            buyer_ids=buyer_ids,
            time=time,
        )


        search_aftersales_requests_request_filter.additional_properties = d
        return search_aftersales_requests_request_filter

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
