from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_sessions_response_data_session import SearchSessionsResponseDataSession





T = TypeVar("T", bound="SearchSessionsResponseData")



@_attrs_define
class SearchSessionsResponseData:
    """ 
        Attributes:
            next_page_token (str | Unset): If there is no more record, this field will be ""(empty string).
            sessions (list[SearchSessionsResponseDataSession] | Unset): Customer service sessions that match the request
                filters.
     """

    next_page_token: str | Unset = UNSET
    sessions: list[SearchSessionsResponseDataSession] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_sessions_response_data_session import SearchSessionsResponseDataSession # noqa: PLC0415
        next_page_token = self.next_page_token

        sessions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sessions, Unset):
            sessions = []
            for sessions_item_data in self.sessions:
                sessions_item = sessions_item_data.to_dict()
                sessions.append(sessions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if sessions is not UNSET:
            field_dict["sessions"] = sessions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_sessions_response_data_session import SearchSessionsResponseDataSession # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        _sessions = d.pop("sessions", UNSET)
        sessions: list[SearchSessionsResponseDataSession] | Unset = UNSET
        if _sessions is not UNSET:
            sessions = []
            for sessions_item_data in _sessions:
                sessions_item = SearchSessionsResponseDataSession.from_dict(sessions_item_data)



                sessions.append(sessions_item)


        search_sessions_response_data = cls(
            next_page_token=next_page_token,
            sessions=sessions,
        )


        search_sessions_response_data.additional_properties = d
        return search_sessions_response_data

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
