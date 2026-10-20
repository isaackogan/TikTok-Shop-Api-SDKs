from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FailedMaterial")



@_attrs_define
class FailedMaterial:
    """ 
        Attributes:
            material_id (str | Unset): Material ID.
            fail_reason (str | Unset): Fail reason.
     """

    material_id: str | Unset = UNSET
    fail_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        material_id = self.material_id

        fail_reason = self.fail_reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if material_id is not UNSET:
            field_dict["material_id"] = material_id
        if fail_reason is not UNSET:
            field_dict["fail_reason"] = fail_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        material_id = d.pop("material_id", UNSET)

        fail_reason = d.pop("fail_reason", UNSET)

        failed_material = cls(
            material_id=material_id,
            fail_reason=fail_reason,
        )


        failed_material.additional_properties = d
        return failed_material

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
