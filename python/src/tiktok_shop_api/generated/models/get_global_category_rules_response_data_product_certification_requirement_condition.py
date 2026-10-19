from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_global_category_rules_response_data_product_certification_requirement_condition_condition_type import (
    GetGlobalCategoryRulesResponseDataProductCertificationRequirementConditionConditionType,
)
from ..models.get_global_category_rules_response_data_product_certification_requirement_condition_region import (
    GetGlobalCategoryRulesResponseDataProductCertificationRequirementConditionRegion,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGlobalCategoryRulesResponseDataProductCertificationRequirementCondition")


@_attrs_define
class GetGlobalCategoryRulesResponseDataProductCertificationRequirementCondition:
    """
    Attributes:
        region (GetGlobalCategoryRulesResponseDataProductCertificationRequirementConditionRegion | Unset): The market
            where the certification is required when the conditions are met.
            Possible values:
            - AT: Austria
            - BE: Belgium
            - CZ: Czechia
            - DE: Germany
            - ES: Spain
            - FR: France
            - GB: United Kingdom
            - GR: Greece
            - HU: Hungary
            - ID: Indonesia
            - IE: Ireland
            - IT: Italy
            - JP: Japan
            - MX: Mexico
            - MY: Malaysia
            - NL: Netherlands
            - PH: Philippines
            - PL: Poland
            - PT: Portugal
            - SG: Singapore
            - TH: Thailand
            - US: United States
            - VN: Vietnam
        condition_type (GetGlobalCategoryRulesResponseDataProductCertificationRequirementConditionConditionType |
            Unset): The type of condition.
            Possible values:
            - VALUE_ID_MATCH: The condition is true when the seller selects a value whose ID matches the one specified in
            this condition.
        attribute_id (str | Unset): The ID of the product attribute that is being evaluated by the condition.
        attribute_value_id (str | Unset): The ID of the product attribute value that must match the seller's input for
            the condition to be true.
    """

    region: GetGlobalCategoryRulesResponseDataProductCertificationRequirementConditionRegion | Unset = UNSET
    condition_type: GetGlobalCategoryRulesResponseDataProductCertificationRequirementConditionConditionType | Unset = (
        UNSET
    )
    attribute_id: str | Unset = UNSET
    attribute_value_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region: str | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        condition_type: str | Unset = UNSET
        if not isinstance(self.condition_type, Unset):
            condition_type = self.condition_type.value

        attribute_id = self.attribute_id

        attribute_value_id = self.attribute_value_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region is not UNSET:
            field_dict["region"] = region
        if condition_type is not UNSET:
            field_dict["condition_type"] = condition_type
        if attribute_id is not UNSET:
            field_dict["attribute_id"] = attribute_id
        if attribute_value_id is not UNSET:
            field_dict["attribute_value_id"] = attribute_value_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _region = d.pop("region", UNSET)
        region: GetGlobalCategoryRulesResponseDataProductCertificationRequirementConditionRegion | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = GetGlobalCategoryRulesResponseDataProductCertificationRequirementConditionRegion(_region)

        _condition_type = d.pop("condition_type", UNSET)
        condition_type: GetGlobalCategoryRulesResponseDataProductCertificationRequirementConditionConditionType | Unset
        if isinstance(_condition_type, Unset):
            condition_type = UNSET
        else:
            condition_type = GetGlobalCategoryRulesResponseDataProductCertificationRequirementConditionConditionType(
                _condition_type
            )

        attribute_id = d.pop("attribute_id", UNSET)

        attribute_value_id = d.pop("attribute_value_id", UNSET)

        get_global_category_rules_response_data_product_certification_requirement_condition = cls(
            region=region,
            condition_type=condition_type,
            attribute_id=attribute_id,
            attribute_value_id=attribute_value_id,
        )

        get_global_category_rules_response_data_product_certification_requirement_condition.additional_properties = d
        return get_global_category_rules_response_data_product_certification_requirement_condition

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
