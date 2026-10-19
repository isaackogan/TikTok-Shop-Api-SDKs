from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_open_collaboration_response_data_open_collaboration import (
        CreateOpenCollaborationResponseDataOpenCollaboration,
    )


T = TypeVar("T", bound="CreateOpenCollaborationResponseData")


@_attrs_define
class CreateOpenCollaborationResponseData:
    """
    Attributes:
        open_collaboration (CreateOpenCollaborationResponseDataOpenCollaboration | Unset):
    """

    open_collaboration: CreateOpenCollaborationResponseDataOpenCollaboration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_collaboration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.open_collaboration, Unset):
            open_collaboration = self.open_collaboration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_collaboration is not UNSET:
            field_dict["open_collaboration"] = open_collaboration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_open_collaboration_response_data_open_collaboration import (
            CreateOpenCollaborationResponseDataOpenCollaboration,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _open_collaboration = d.pop("open_collaboration", UNSET)
        open_collaboration: CreateOpenCollaborationResponseDataOpenCollaboration | Unset
        if isinstance(_open_collaboration, Unset):
            open_collaboration = UNSET
        else:
            open_collaboration = CreateOpenCollaborationResponseDataOpenCollaboration.from_dict(_open_collaboration)

        create_open_collaboration_response_data = cls(
            open_collaboration=open_collaboration,
        )

        create_open_collaboration_response_data.additional_properties = d
        return create_open_collaboration_response_data

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
