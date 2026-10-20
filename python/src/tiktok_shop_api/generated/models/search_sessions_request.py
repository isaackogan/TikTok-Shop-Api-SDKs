from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchSessionsRequest")



@_attrs_define
class SearchSessionsRequest:
    """ 
        Attributes:
            begin_time_ge (int): Return sessions whose begin_time is greater than or equal to this Unix timestamp, in
                seconds. Only data from the last 90 days is supported.
            begin_time_lt (int): Return sessions whose begin_time is less than this Unix timestamp, in seconds. The value
                must be greater than or equal to begin_time_ge.
            buyer_nickname (str | Unset): Filter sessions by the buyer's nickname.
     """

    begin_time_ge: int
    begin_time_lt: int
    buyer_nickname: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        begin_time_ge = self.begin_time_ge

        begin_time_lt = self.begin_time_lt

        buyer_nickname = self.buyer_nickname


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "begin_time_ge": begin_time_ge,
            "begin_time_lt": begin_time_lt,
        })
        if buyer_nickname is not UNSET:
            field_dict["buyer_nickname"] = buyer_nickname

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        begin_time_ge = d.pop("begin_time_ge")

        begin_time_lt = d.pop("begin_time_lt")

        buyer_nickname = d.pop("buyer_nickname", UNSET)

        search_sessions_request = cls(
            begin_time_ge=begin_time_ge,
            begin_time_lt=begin_time_lt,
            buyer_nickname=buyer_nickname,
        )


        search_sessions_request.additional_properties = d
        return search_sessions_request

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
