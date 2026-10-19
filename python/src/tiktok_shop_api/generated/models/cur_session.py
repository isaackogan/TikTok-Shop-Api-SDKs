from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cur_session_phase import CurSessionPhase
from ..types import UNSET, Unset

T = TypeVar("T", bound="CurSession")


@_attrs_define
class CurSession:
    """
    Attributes:
        id (str | Unset): Current session id.
        phase (CurSessionPhase | Unset): Current phase of the session.
            Possible enumerations:
            - `AUTO_REPLY` — The session is being handled by automatic replies or chatbot responses.
            - `QUEUED` — The session is waiting to be assigned to an agent.
            - `ASSIGNED` — The session has been assigned to an agent.
    """

    id: str | Unset = UNSET
    phase: CurSessionPhase | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        phase: str | Unset = UNSET
        if not isinstance(self.phase, Unset):
            phase = self.phase.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if phase is not UNSET:
            field_dict["phase"] = phase

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _phase = d.pop("phase", UNSET)
        phase: CurSessionPhase | Unset
        if isinstance(_phase, Unset):
            phase = UNSET
        else:
            phase = CurSessionPhase(_phase)

        cur_session = cls(
            id=id,
            phase=phase,
        )

        cur_session.additional_properties = d
        return cur_session

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
