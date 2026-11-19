from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetAIReportQueryRulesResponseDataDetailRequirement")



@_attrs_define
class GetAIReportQueryRulesResponseDataDetailRequirement:
    """ 
        Attributes:
            detail_field (str | Unset): Detail field code that activates this requirement when included in the request
                detail_fields.
            required_group_dimensions (list[str] | Unset): Every dimension in this list must appear in the request
                group_dimensions when the specified detail field is selected. These are grouping dimensions, not metric codes.
     """

    detail_field: str | Unset = UNSET
    required_group_dimensions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        detail_field = self.detail_field

        required_group_dimensions: list[str] | Unset = UNSET
        if not isinstance(self.required_group_dimensions, Unset):
            required_group_dimensions = self.required_group_dimensions




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if detail_field is not UNSET:
            field_dict["detail_field"] = detail_field
        if required_group_dimensions is not UNSET:
            field_dict["required_group_dimensions"] = required_group_dimensions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        detail_field = d.pop("detail_field", UNSET)

        required_group_dimensions = cast(list[str], d.pop("required_group_dimensions", UNSET))


        get_ai_report_query_rules_response_data_detail_requirement = cls(
            detail_field=detail_field,
            required_group_dimensions=required_group_dimensions,
        )


        get_ai_report_query_rules_response_data_detail_requirement.additional_properties = d
        return get_ai_report_query_rules_response_data_detail_requirement

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
