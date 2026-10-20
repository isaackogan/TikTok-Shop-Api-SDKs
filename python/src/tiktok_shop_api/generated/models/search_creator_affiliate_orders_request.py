from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchCreatorAffiliateOrdersRequest")



@_attrs_define
class SearchCreatorAffiliateOrdersRequest:
    """ 
        Attributes:
            create_time_ge (int | Unset): Filter orders to show only those that are created on or after the specified date
                and time. Unix timestamp.
                Note:
                `create_time_ge` and `create_time_lt` together constitute the creation time filter condition.
                - If `create_time_ge` is filled but `create_time_lt` is empty, `create_time_lt` will default to the current
                time.
                - If `create_time_lt` is filled but `create_time_ge` is empty, `create_time_ge` will default to the earliest
                shop time.
            create_time_lt (int | Unset): Filter orders to show only those created before the specified time, expressed as a
                Unix timestamp in seconds. Refer to the notes in `create_time_ge` for more usage information.
     """

    create_time_ge: int | Unset = UNSET
    create_time_lt: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        create_time_ge = self.create_time_ge

        create_time_lt = self.create_time_lt


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if create_time_ge is not UNSET:
            field_dict["create_time_ge"] = create_time_ge
        if create_time_lt is not UNSET:
            field_dict["create_time_lt"] = create_time_lt

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_time_ge = d.pop("create_time_ge", UNSET)

        create_time_lt = d.pop("create_time_lt", UNSET)

        search_creator_affiliate_orders_request = cls(
            create_time_ge=create_time_ge,
            create_time_lt=create_time_lt,
        )


        search_creator_affiliate_orders_request.additional_properties = d
        return search_creator_affiliate_orders_request

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
