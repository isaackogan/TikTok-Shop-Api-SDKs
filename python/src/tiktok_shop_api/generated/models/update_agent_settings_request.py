from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="UpdateAgentSettingsRequest")



@_attrs_define
class UpdateAgentSettingsRequest:
    """ 
        Attributes:
            can_accept_chat (bool): Whether the shop owner's customer service account can accept auto-assigned chats.

                - `true`: The agent receives auto-assigned chats and can also manually select chats to respond to.
                - `false`: The agent receives only manually assigned chats.

                For a shop with only one customer service agent, set this field to `true`; `false` is rejected. When using the
                IM API, `true` is recommended.
     """

    can_accept_chat: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        can_accept_chat = self.can_accept_chat


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "can_accept_chat": can_accept_chat,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_accept_chat = d.pop("can_accept_chat")

        update_agent_settings_request = cls(
            can_accept_chat=can_accept_chat,
        )


        update_agent_settings_request.additional_properties = d
        return update_agent_settings_request

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
