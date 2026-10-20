from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="FreeSampleRule")



@_attrs_define
class FreeSampleRule:
    """ 
        Attributes:
            has_free_sample (bool): If set to `true`, free samples are provided to creators invited to the target
                collaboration group. If set to `false`, free samples are not provided.
            is_sample_approval_exempt (bool): If set to `true`, creators invited to the target collaboration are exempt from
                seller review and are automatically approved for a free  product sample. Note that the `has_free_sample`
                property overrides the free sample behavior.
     """

    has_free_sample: bool
    is_sample_approval_exempt: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        has_free_sample = self.has_free_sample

        is_sample_approval_exempt = self.is_sample_approval_exempt


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "has_free_sample": has_free_sample,
            "is_sample_approval_exempt": is_sample_approval_exempt,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_free_sample = d.pop("has_free_sample")

        is_sample_approval_exempt = d.pop("is_sample_approval_exempt")

        free_sample_rule = cls(
            has_free_sample=has_free_sample,
            is_sample_approval_exempt=is_sample_approval_exempt,
        )


        free_sample_rule.additional_properties = d
        return free_sample_rule

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
