from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetAIReportQueryRulesResponseDataGroupFilter")



@_attrs_define
class GetAIReportQueryRulesResponseDataGroupFilter:
    """ 
        Attributes:
            dimension_code (str | Unset): Dimension code that may be used in filters[].code for this group.
            max_value_count (int | Unset): Maximum number of values allowed in one filter for this dimension. A value of -1
                means the group does not set a per-dimension limit; request array limits still apply.
     """

    dimension_code: str | Unset = UNSET
    max_value_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        dimension_code = self.dimension_code

        max_value_count = self.max_value_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if dimension_code is not UNSET:
            field_dict["dimension_code"] = dimension_code
        if max_value_count is not UNSET:
            field_dict["max_value_count"] = max_value_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dimension_code = d.pop("dimension_code", UNSET)

        max_value_count = d.pop("max_value_count", UNSET)

        get_ai_report_query_rules_response_data_group_filter = cls(
            dimension_code=dimension_code,
            max_value_count=max_value_count,
        )


        get_ai_report_query_rules_response_data_group_filter.additional_properties = d
        return get_ai_report_query_rules_response_data_group_filter

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
