from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetAIReportQueryRulesResponseDataExclusion")



@_attrs_define
class GetAIReportQueryRulesResponseDataExclusion:
    """ 
        Attributes:
            forbidden_filter_dimensions (list[str] | Unset): Dimensions that cannot appear in filters when this restriction
                is active. Filtering is prohibited even when the dimension is not used for grouping.
            forbidden_group_dimensions (list[str] | Unset): Dimensions that cannot appear in group_dimensions when this
                restriction is active.
            trigger_metric_codes (list[str] | Unset): Selecting at least one of these metric codes activates this
                restriction.
     """

    forbidden_filter_dimensions: list[str] | Unset = UNSET
    forbidden_group_dimensions: list[str] | Unset = UNSET
    trigger_metric_codes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        forbidden_filter_dimensions: list[str] | Unset = UNSET
        if not isinstance(self.forbidden_filter_dimensions, Unset):
            forbidden_filter_dimensions = self.forbidden_filter_dimensions



        forbidden_group_dimensions: list[str] | Unset = UNSET
        if not isinstance(self.forbidden_group_dimensions, Unset):
            forbidden_group_dimensions = self.forbidden_group_dimensions



        trigger_metric_codes: list[str] | Unset = UNSET
        if not isinstance(self.trigger_metric_codes, Unset):
            trigger_metric_codes = self.trigger_metric_codes




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if forbidden_filter_dimensions is not UNSET:
            field_dict["forbidden_filter_dimensions"] = forbidden_filter_dimensions
        if forbidden_group_dimensions is not UNSET:
            field_dict["forbidden_group_dimensions"] = forbidden_group_dimensions
        if trigger_metric_codes is not UNSET:
            field_dict["trigger_metric_codes"] = trigger_metric_codes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        forbidden_filter_dimensions = cast(list[str], d.pop("forbidden_filter_dimensions", UNSET))


        forbidden_group_dimensions = cast(list[str], d.pop("forbidden_group_dimensions", UNSET))


        trigger_metric_codes = cast(list[str], d.pop("trigger_metric_codes", UNSET))


        get_ai_report_query_rules_response_data_exclusion = cls(
            forbidden_filter_dimensions=forbidden_filter_dimensions,
            forbidden_group_dimensions=forbidden_group_dimensions,
            trigger_metric_codes=trigger_metric_codes,
        )


        get_ai_report_query_rules_response_data_exclusion.additional_properties = d
        return get_ai_report_query_rules_response_data_exclusion

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
