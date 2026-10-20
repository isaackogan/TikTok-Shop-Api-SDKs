from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateTime")



@_attrs_define
class CreateTime:
    """ 
        Attributes:
            min_unix_time_inclusive (int | Unset): Inclusive lower bound (Unix seconds).
            max_unix_time_exclusive (int | Unset): Exclusive upper bound (Unix seconds).
     """

    min_unix_time_inclusive: int | Unset = UNSET
    max_unix_time_exclusive: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        min_unix_time_inclusive = self.min_unix_time_inclusive

        max_unix_time_exclusive = self.max_unix_time_exclusive


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_unix_time_inclusive is not UNSET:
            field_dict["min_unix_time_inclusive"] = min_unix_time_inclusive
        if max_unix_time_exclusive is not UNSET:
            field_dict["max_unix_time_exclusive"] = max_unix_time_exclusive

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_unix_time_inclusive = d.pop("min_unix_time_inclusive", UNSET)

        max_unix_time_exclusive = d.pop("max_unix_time_exclusive", UNSET)

        create_time = cls(
            min_unix_time_inclusive=min_unix_time_inclusive,
            max_unix_time_exclusive=max_unix_time_exclusive,
        )


        create_time.additional_properties = d
        return create_time

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
