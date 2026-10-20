from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSPSOverviewResponseDataDimension")


@_attrs_define
class GetSPSOverviewResponseDataDimension:
    """
    Attributes:
        name (str | Unset): Dimension name.
        score (str | Unset): Dimension score, from 0 to 5.
        status (str | Unset): Dimension status enum. Possible values include EXCELLENT, GOOD, POOR, CRITICAL and NIL.
        status_text (str | Unset): Dimension status text. Values like Excellent, Good, Normal, Attention.
        weight (str | Unset): Dimension weight as a percent from 0 to 100.
    """

    name: str | Unset = UNSET
    score: str | Unset = UNSET
    status: str | Unset = UNSET
    status_text: str | Unset = UNSET
    weight: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        score = self.score

        status = self.status

        status_text = self.status_text

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if score is not UNSET:
            field_dict["score"] = score
        if status is not UNSET:
            field_dict["status"] = status
        if status_text is not UNSET:
            field_dict["status_text"] = status_text
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        score = d.pop("score", UNSET)

        status = d.pop("status", UNSET)

        status_text = d.pop("status_text", UNSET)

        weight = d.pop("weight", UNSET)

        get_sps_overview_response_data_dimension = cls(
            name=name,
            score=score,
            status=status,
            status_text=status_text,
            weight=weight,
        )

        get_sps_overview_response_data_dimension.additional_properties = d
        return get_sps_overview_response_data_dimension

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
