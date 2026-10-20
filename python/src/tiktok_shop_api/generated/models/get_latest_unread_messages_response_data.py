from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_latest_unread_messages_response_data_newest_message_list import GetLatestUnreadMessagesResponseDataNewestMessageList





T = TypeVar("T", bound="GetLatestUnreadMessagesResponseData")



@_attrs_define
class GetLatestUnreadMessagesResponseData:
    """ 
        Attributes:
            newest_message_list (list[GetLatestUnreadMessagesResponseDataNewestMessageList] | Unset): The list of unread
                messages from the last minute.
     """

    newest_message_list: list[GetLatestUnreadMessagesResponseDataNewestMessageList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_latest_unread_messages_response_data_newest_message_list import GetLatestUnreadMessagesResponseDataNewestMessageList # noqa: PLC0415
        newest_message_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.newest_message_list, Unset):
            newest_message_list = []
            for newest_message_list_item_data in self.newest_message_list:
                newest_message_list_item = newest_message_list_item_data.to_dict()
                newest_message_list.append(newest_message_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if newest_message_list is not UNSET:
            field_dict["newest_message_list"] = newest_message_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_latest_unread_messages_response_data_newest_message_list import GetLatestUnreadMessagesResponseDataNewestMessageList # noqa: PLC0415
        d = dict(src_dict)
        _newest_message_list = d.pop("newest_message_list", UNSET)
        newest_message_list: list[GetLatestUnreadMessagesResponseDataNewestMessageList] | Unset = UNSET
        if _newest_message_list is not UNSET:
            newest_message_list = []
            for newest_message_list_item_data in _newest_message_list:
                newest_message_list_item = GetLatestUnreadMessagesResponseDataNewestMessageList.from_dict(newest_message_list_item_data)



                newest_message_list.append(newest_message_list_item)


        get_latest_unread_messages_response_data = cls(
            newest_message_list=newest_message_list,
        )


        get_latest_unread_messages_response_data.additional_properties = d
        return get_latest_unread_messages_response_data

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
