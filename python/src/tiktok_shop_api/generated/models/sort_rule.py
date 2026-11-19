from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SortRule")



@_attrs_define
class SortRule:
    """ 
        Attributes:
            sort_field (str): Field to sort by: a selected metric code, a selected dimension code, or time to sort
                chronologically by the calendar time bucket in the shop timezone. A row's start_date and end_date are clipped to
                the requested date range; time refers to the bucket, not a payment or order timestamp.
            sort_order (str | Unset): Sort direction. ASC sorts from smallest to largest; DESC sorts from largest to
                smallest. Default: ASC.
     """

    sort_field: str
    sort_order: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        sort_field = self.sort_field

        sort_order = self.sort_order


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sort_field": sort_field,
        })
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sort_field = d.pop("sort_field")

        sort_order = d.pop("sort_order", UNSET)

        sort_rule = cls(
            sort_field=sort_field,
            sort_order=sort_order,
        )


        sort_rule.additional_properties = d
        return sort_rule

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
