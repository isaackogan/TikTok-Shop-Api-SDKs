from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.search_cancellations_request_cancel_status_item import SearchCancellationsRequestCancelStatusItem
from ..models.search_cancellations_request_cancel_types_item import SearchCancellationsRequestCancelTypesItem
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchCancellationsRequest")



@_attrs_define
class SearchCancellationsRequest:
    """ 
        Attributes:
            cancel_ids (list[str] | Unset): List of order cancellations IDs.
            order_ids (list[str] | Unset): List of TikTok Shop order IDs.
            buyer_user_ids (list[str] | Unset): List of TikTok Shop buyer user IDs.
            cancel_types (list[SearchCancellationsRequestCancelTypesItem] | Unset): List of order cancellation types.
                Possible values:
                - `CANCEL`: Cancel by seller or system.
                - `BUYER_CANCEL`: Cancel by buyer. Need to be approved by seller or system.
            cancel_status (list[SearchCancellationsRequestCancelStatusItem] | Unset): List of order cancellation statuses.
                Possible values:
                - `CANCELLATION_REQUEST_PENDING`
                - `CANCELLATION_REQUEST_SUCCESS`
                - `CANCELLATION_REQUEST_CANCEL`
                - `CANCELLATION_REQUEST_COMPLETE`

                Please see "API Overview" for more information about these statuses.
            create_time_ge (int | Unset): Filter cancellations to show only orders that have been created after a specified
                date and time. Unix timestamp.
            create_time_lt (int | Unset): Filter cancellations to show only orders that have been created before a specified
                date and time. Unix timestamp.
            update_time_ge (int | Unset): Filter cancellations to show only orders that have been updated after a specified
                date and time. Unix timestamp.
            update_time_lt (int | Unset): Filter cancellations to show only orders that have been updated before a specified
                date and time. Unix timestamp.
            locale (str | Unset): The BCP-47 locale codes for displaying the order, delimited by commas. Default: en-US
                Refer to [Locale codes](678e3a47bae28f030a8c7523) for the list of supported locale codes.
     """

    cancel_ids: list[str] | Unset = UNSET
    order_ids: list[str] | Unset = UNSET
    buyer_user_ids: list[str] | Unset = UNSET
    cancel_types: list[SearchCancellationsRequestCancelTypesItem] | Unset = UNSET
    cancel_status: list[SearchCancellationsRequestCancelStatusItem] | Unset = UNSET
    create_time_ge: int | Unset = UNSET
    create_time_lt: int | Unset = UNSET
    update_time_ge: int | Unset = UNSET
    update_time_lt: int | Unset = UNSET
    locale: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cancel_ids: list[str] | Unset = UNSET
        if not isinstance(self.cancel_ids, Unset):
            cancel_ids = self.cancel_ids



        order_ids: list[str] | Unset = UNSET
        if not isinstance(self.order_ids, Unset):
            order_ids = self.order_ids



        buyer_user_ids: list[str] | Unset = UNSET
        if not isinstance(self.buyer_user_ids, Unset):
            buyer_user_ids = self.buyer_user_ids



        cancel_types: list[str] | Unset = UNSET
        if not isinstance(self.cancel_types, Unset):
            cancel_types = []
            for cancel_types_item_data in self.cancel_types:
                cancel_types_item = cancel_types_item_data.value
                cancel_types.append(cancel_types_item)



        cancel_status: list[str] | Unset = UNSET
        if not isinstance(self.cancel_status, Unset):
            cancel_status = []
            for cancel_status_item_data in self.cancel_status:
                cancel_status_item = cancel_status_item_data.value
                cancel_status.append(cancel_status_item)



        create_time_ge = self.create_time_ge

        create_time_lt = self.create_time_lt

        update_time_ge = self.update_time_ge

        update_time_lt = self.update_time_lt

        locale = self.locale


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cancel_ids is not UNSET:
            field_dict["cancel_ids"] = cancel_ids
        if order_ids is not UNSET:
            field_dict["order_ids"] = order_ids
        if buyer_user_ids is not UNSET:
            field_dict["buyer_user_ids"] = buyer_user_ids
        if cancel_types is not UNSET:
            field_dict["cancel_types"] = cancel_types
        if cancel_status is not UNSET:
            field_dict["cancel_status"] = cancel_status
        if create_time_ge is not UNSET:
            field_dict["create_time_ge"] = create_time_ge
        if create_time_lt is not UNSET:
            field_dict["create_time_lt"] = create_time_lt
        if update_time_ge is not UNSET:
            field_dict["update_time_ge"] = update_time_ge
        if update_time_lt is not UNSET:
            field_dict["update_time_lt"] = update_time_lt
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cancel_ids = cast(list[str], d.pop("cancel_ids", UNSET))


        order_ids = cast(list[str], d.pop("order_ids", UNSET))


        buyer_user_ids = cast(list[str], d.pop("buyer_user_ids", UNSET))


        _cancel_types = d.pop("cancel_types", UNSET)
        cancel_types: list[SearchCancellationsRequestCancelTypesItem] | Unset = UNSET
        if _cancel_types is not UNSET:
            cancel_types = []
            for cancel_types_item_data in _cancel_types:
                cancel_types_item = SearchCancellationsRequestCancelTypesItem(cancel_types_item_data)



                cancel_types.append(cancel_types_item)


        _cancel_status = d.pop("cancel_status", UNSET)
        cancel_status: list[SearchCancellationsRequestCancelStatusItem] | Unset = UNSET
        if _cancel_status is not UNSET:
            cancel_status = []
            for cancel_status_item_data in _cancel_status:
                cancel_status_item = SearchCancellationsRequestCancelStatusItem(cancel_status_item_data)



                cancel_status.append(cancel_status_item)


        create_time_ge = d.pop("create_time_ge", UNSET)

        create_time_lt = d.pop("create_time_lt", UNSET)

        update_time_ge = d.pop("update_time_ge", UNSET)

        update_time_lt = d.pop("update_time_lt", UNSET)

        locale = d.pop("locale", UNSET)

        search_cancellations_request = cls(
            cancel_ids=cancel_ids,
            order_ids=order_ids,
            buyer_user_ids=buyer_user_ids,
            cancel_types=cancel_types,
            cancel_status=cancel_status,
            create_time_ge=create_time_ge,
            create_time_lt=create_time_lt,
            update_time_ge=update_time_ge,
            update_time_lt=update_time_lt,
            locale=locale,
        )


        search_cancellations_request.additional_properties = d
        return search_cancellations_request

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
