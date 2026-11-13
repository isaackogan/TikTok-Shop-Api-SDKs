from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="OfficialSalesPeriod")



@_attrs_define
class OfficialSalesPeriod:
    """ 
        Attributes:
            end_time (datetime.datetime | Unset): End time in RFC 3339 UTC with millisecond precision. Omitted if
                unavailable.
            start_time (datetime.datetime | Unset): Start time in RFC 3339 UTC with millisecond precision. Omitted if
                unavailable.
     """

    end_time: datetime.datetime | Unset = UNSET
    start_time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        end_time: str | Unset = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        start_time: str | Unset = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if start_time is not UNSET:
            field_dict["start_time"] = start_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _end_time = d.pop("end_time", UNSET)
        end_time: datetime.datetime | Unset
        if isinstance(_end_time,  Unset):
            end_time = UNSET
        else:
            end_time = datetime.datetime.fromisoformat(_end_time)




        _start_time = d.pop("start_time", UNSET)
        start_time: datetime.datetime | Unset
        if isinstance(_start_time,  Unset):
            start_time = UNSET
        else:
            start_time = datetime.datetime.fromisoformat(_start_time)




        official_sales_period = cls(
            end_time=end_time,
            start_time=start_time,
        )


        official_sales_period.additional_properties = d
        return official_sales_period

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
