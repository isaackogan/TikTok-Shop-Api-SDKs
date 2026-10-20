from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateResponsiblePersonResponseData")



@_attrs_define
class CreateResponsiblePersonResponseData:
    """ 
        Attributes:
            responsible_person_id (str | Unset): A unique ID that identifies the responsible person in TikTok Shop.
     """

    responsible_person_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        responsible_person_id = self.responsible_person_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if responsible_person_id is not UNSET:
            field_dict["responsible_person_id"] = responsible_person_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        responsible_person_id = d.pop("responsible_person_id", UNSET)

        create_responsible_person_response_data = cls(
            responsible_person_id=responsible_person_id,
        )


        create_responsible_person_response_data.additional_properties = d
        return create_responsible_person_response_data

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
