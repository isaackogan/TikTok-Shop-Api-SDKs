from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TierCommissionInfo")



@_attrs_define
class TierCommissionInfo:
    """ 
        Attributes:
            commission_rate_after_threshold (int | Unset): Commission rate after the tier threshold is reached, expressed as
                the percentage multiplied
                by 100.
            commission_rate_before_threshold (int | Unset): Commission rate before the tier threshold is reached, expressed
                as the percentage multiplied
                by 100.
            threshold (int | Unset): Threshold at which the tiered commission changes from the rate before the threshold to
                the
                rate after it. The source plan defines the threshold unit and measurement window.
     """

    commission_rate_after_threshold: int | Unset = UNSET
    commission_rate_before_threshold: int | Unset = UNSET
    threshold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        commission_rate_after_threshold = self.commission_rate_after_threshold

        commission_rate_before_threshold = self.commission_rate_before_threshold

        threshold = self.threshold


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if commission_rate_after_threshold is not UNSET:
            field_dict["commission_rate_after_threshold"] = commission_rate_after_threshold
        if commission_rate_before_threshold is not UNSET:
            field_dict["commission_rate_before_threshold"] = commission_rate_before_threshold
        if threshold is not UNSET:
            field_dict["threshold"] = threshold

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        commission_rate_after_threshold = d.pop("commission_rate_after_threshold", UNSET)

        commission_rate_before_threshold = d.pop("commission_rate_before_threshold", UNSET)

        threshold = d.pop("threshold", UNSET)

        tier_commission_info = cls(
            commission_rate_after_threshold=commission_rate_after_threshold,
            commission_rate_before_threshold=commission_rate_before_threshold,
            threshold=threshold,
        )


        tier_commission_info.additional_properties = d
        return tier_commission_info

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
