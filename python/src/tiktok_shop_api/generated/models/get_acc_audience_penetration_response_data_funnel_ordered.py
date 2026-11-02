from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetACCAudiencePenetrationResponseDataFunnelOrdered")



@_attrs_define
class GetACCAudiencePenetrationResponseDataFunnelOrdered:
    """ 
        Attributes:
            not_rate (str | Unset): Percentage of the initial audience represented by ordered.not_value, calculated as
                ordered.not_value / funnel.total.value * 100 and returned as a percentage string, for example "55.12%". Do not
                multiply the returned percentage by 100 again. Unavailable when the initial audience count is not positive.
            not_value (int | Unset): Reported number of audience members in the not-ordered segment for the selected
                reporting window.
            rate (str | Unset): Percentage of the initial audience represented by ordered.value, calculated as ordered.value
                / funnel.total.value * 100 and returned as a percentage string, for example "44.88%". Do not multiply the
                returned percentage by 100 again. Unavailable when the initial audience count is not positive.
            value (int | Unset): Reported number of audience members in the ordered segment for the selected reporting
                window.
     """

    not_rate: str | Unset = UNSET
    not_value: int | Unset = UNSET
    rate: str | Unset = UNSET
    value: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        not_rate = self.not_rate

        not_value = self.not_value

        rate = self.rate

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if not_rate is not UNSET:
            field_dict["not_rate"] = not_rate
        if not_value is not UNSET:
            field_dict["not_value"] = not_value
        if rate is not UNSET:
            field_dict["rate"] = rate
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        not_rate = d.pop("not_rate", UNSET)

        not_value = d.pop("not_value", UNSET)

        rate = d.pop("rate", UNSET)

        value = d.pop("value", UNSET)

        get_acc_audience_penetration_response_data_funnel_ordered = cls(
            not_rate=not_rate,
            not_value=not_value,
            rate=rate,
            value=value,
        )


        get_acc_audience_penetration_response_data_funnel_ordered.additional_properties = d
        return get_acc_audience_penetration_response_data_funnel_ordered

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
