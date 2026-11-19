from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_ai_report_query_rules_response_data_detail_requirement import GetAIReportQueryRulesResponseDataDetailRequirement
  from ..models.get_ai_report_query_rules_response_data_exclusion import GetAIReportQueryRulesResponseDataExclusion
  from ..models.get_ai_report_query_rules_response_data_group import GetAIReportQueryRulesResponseDataGroup





T = TypeVar("T", bound="GetAIReportQueryRulesResponseData")



@_attrs_define
class GetAIReportQueryRulesResponseData:
    """ 
        Attributes:
            detail_requirements (list[GetAIReportQueryRulesResponseDataDetailRequirement] | Unset): Grouping dimensions that
                must be selected when a particular detail field is requested.
            exclusions (list[GetAIReportQueryRulesResponseDataExclusion] | Unset): Metric and dimension combinations that
                are prohibited in every group.
            groups (list[GetAIReportQueryRulesResponseDataGroup] | Unset): Supported combinations of metrics, grouping
                dimensions, filters, dates and detail fields. A query must satisfy all conditions in at least one group, as well
                as exclusions and detail_requirements.
            version (str | Unset): Version of the returned rule set. Compare it with a previously retrieved version to
                detect rule changes.
     """

    detail_requirements: list[GetAIReportQueryRulesResponseDataDetailRequirement] | Unset = UNSET
    exclusions: list[GetAIReportQueryRulesResponseDataExclusion] | Unset = UNSET
    groups: list[GetAIReportQueryRulesResponseDataGroup] | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_ai_report_query_rules_response_data_detail_requirement import GetAIReportQueryRulesResponseDataDetailRequirement # noqa: PLC0415
        from ..models.get_ai_report_query_rules_response_data_exclusion import GetAIReportQueryRulesResponseDataExclusion # noqa: PLC0415
        from ..models.get_ai_report_query_rules_response_data_group import GetAIReportQueryRulesResponseDataGroup # noqa: PLC0415
        detail_requirements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.detail_requirements, Unset):
            detail_requirements = []
            for detail_requirements_item_data in self.detail_requirements:
                detail_requirements_item = detail_requirements_item_data.to_dict()
                detail_requirements.append(detail_requirements_item)



        exclusions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exclusions, Unset):
            exclusions = []
            for exclusions_item_data in self.exclusions:
                exclusions_item = exclusions_item_data.to_dict()
                exclusions.append(exclusions_item)



        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)



        version = self.version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if detail_requirements is not UNSET:
            field_dict["detail_requirements"] = detail_requirements
        if exclusions is not UNSET:
            field_dict["exclusions"] = exclusions
        if groups is not UNSET:
            field_dict["groups"] = groups
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_ai_report_query_rules_response_data_detail_requirement import GetAIReportQueryRulesResponseDataDetailRequirement # noqa: PLC0415
        from ..models.get_ai_report_query_rules_response_data_exclusion import GetAIReportQueryRulesResponseDataExclusion # noqa: PLC0415
        from ..models.get_ai_report_query_rules_response_data_group import GetAIReportQueryRulesResponseDataGroup # noqa: PLC0415
        d = dict(src_dict)
        _detail_requirements = d.pop("detail_requirements", UNSET)
        detail_requirements: list[GetAIReportQueryRulesResponseDataDetailRequirement] | Unset = UNSET
        if _detail_requirements is not UNSET:
            detail_requirements = []
            for detail_requirements_item_data in _detail_requirements:
                detail_requirements_item = GetAIReportQueryRulesResponseDataDetailRequirement.from_dict(detail_requirements_item_data)



                detail_requirements.append(detail_requirements_item)


        _exclusions = d.pop("exclusions", UNSET)
        exclusions: list[GetAIReportQueryRulesResponseDataExclusion] | Unset = UNSET
        if _exclusions is not UNSET:
            exclusions = []
            for exclusions_item_data in _exclusions:
                exclusions_item = GetAIReportQueryRulesResponseDataExclusion.from_dict(exclusions_item_data)



                exclusions.append(exclusions_item)


        _groups = d.pop("groups", UNSET)
        groups: list[GetAIReportQueryRulesResponseDataGroup] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = GetAIReportQueryRulesResponseDataGroup.from_dict(groups_item_data)



                groups.append(groups_item)


        version = d.pop("version", UNSET)

        get_ai_report_query_rules_response_data = cls(
            detail_requirements=detail_requirements,
            exclusions=exclusions,
            groups=groups,
            version=version,
        )


        get_ai_report_query_rules_response_data.additional_properties = d
        return get_ai_report_query_rules_response_data

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
