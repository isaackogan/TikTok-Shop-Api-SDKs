from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_open_collaboration_sample_rules_response_data_sample_rule import GetOpenCollaborationSampleRulesResponseDataSampleRule





T = TypeVar("T", bound="GetOpenCollaborationSampleRulesResponseData")



@_attrs_define
class GetOpenCollaborationSampleRulesResponseData:
    """ 
        Attributes:
            sample_rules (list[GetOpenCollaborationSampleRulesResponseDataSampleRule] | Unset): The sample rules for the
                requested products. Products whose sample rules have never been created or have been deleted are omitted.
     """

    sample_rules: list[GetOpenCollaborationSampleRulesResponseDataSampleRule] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_open_collaboration_sample_rules_response_data_sample_rule import GetOpenCollaborationSampleRulesResponseDataSampleRule # noqa: PLC0415
        sample_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sample_rules, Unset):
            sample_rules = []
            for sample_rules_item_data in self.sample_rules:
                sample_rules_item = sample_rules_item_data.to_dict()
                sample_rules.append(sample_rules_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sample_rules is not UNSET:
            field_dict["sample_rules"] = sample_rules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_open_collaboration_sample_rules_response_data_sample_rule import GetOpenCollaborationSampleRulesResponseDataSampleRule # noqa: PLC0415
        d = dict(src_dict)
        _sample_rules = d.pop("sample_rules", UNSET)
        sample_rules: list[GetOpenCollaborationSampleRulesResponseDataSampleRule] | Unset = UNSET
        if _sample_rules is not UNSET:
            sample_rules = []
            for sample_rules_item_data in _sample_rules:
                sample_rules_item = GetOpenCollaborationSampleRulesResponseDataSampleRule.from_dict(sample_rules_item_data)



                sample_rules.append(sample_rules_item)


        get_open_collaboration_sample_rules_response_data = cls(
            sample_rules=sample_rules,
        )


        get_open_collaboration_sample_rules_response_data.additional_properties = d
        return get_open_collaboration_sample_rules_response_data

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
