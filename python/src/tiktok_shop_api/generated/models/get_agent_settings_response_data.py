from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAgentSettingsResponseData")


@_attrs_define
class GetAgentSettingsResponseData:
    """
    Attributes:
        can_accept_chat (bool | Unset): Whether the current agent can accept chat.
            If true, the agent will receive auto-assigned chats. The agent can manually select chats to respond.
            If false, the agent will receive manually assigned chats only.
    """

    can_accept_chat: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_accept_chat = self.can_accept_chat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if can_accept_chat is not UNSET:
            field_dict["can_accept_chat"] = can_accept_chat

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_accept_chat = d.pop("can_accept_chat", UNSET)

        get_agent_settings_response_data = cls(
            can_accept_chat=can_accept_chat,
        )

        get_agent_settings_response_data.additional_properties = d
        return get_agent_settings_response_data

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
