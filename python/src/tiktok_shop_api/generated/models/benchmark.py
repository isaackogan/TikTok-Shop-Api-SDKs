from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Benchmark")


@_attrs_define
class Benchmark:
    """
    Attributes:
        excellent_threshold (str | Unset): Excellent tier threshold.
        poor_threshold (str | Unset): Poor tier threshold.
    """

    excellent_threshold: str | Unset = UNSET
    poor_threshold: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        excellent_threshold = self.excellent_threshold

        poor_threshold = self.poor_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if excellent_threshold is not UNSET:
            field_dict["excellent_threshold"] = excellent_threshold
        if poor_threshold is not UNSET:
            field_dict["poor_threshold"] = poor_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        excellent_threshold = d.pop("excellent_threshold", UNSET)

        poor_threshold = d.pop("poor_threshold", UNSET)

        benchmark = cls(
            excellent_threshold=excellent_threshold,
            poor_threshold=poor_threshold,
        )

        benchmark.additional_properties = d
        return benchmark

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
