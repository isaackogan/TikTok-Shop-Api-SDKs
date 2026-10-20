from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOpenCollaborationResponseDataOpenCollaboration")


@_attrs_define
class CreateOpenCollaborationResponseDataOpenCollaboration:
    """
    Attributes:
        id (str | Unset): The open collaboration identifier.
        product_id (str | Unset): The product identifier.
        effective_time (int | Unset): The time from which the open collaboration commission is effective, expressed as a
            Unix timestamp in seconds.
    """

    id: str | Unset = UNSET
    product_id: str | Unset = UNSET
    effective_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        product_id = self.product_id

        effective_time = self.effective_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if effective_time is not UNSET:
            field_dict["effective_time"] = effective_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        product_id = d.pop("product_id", UNSET)

        effective_time = d.pop("effective_time", UNSET)

        create_open_collaboration_response_data_open_collaboration = cls(
            id=id,
            product_id=product_id,
            effective_time=effective_time,
        )

        create_open_collaboration_response_data_open_collaboration.additional_properties = d
        return create_open_collaboration_response_data_open_collaboration

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
