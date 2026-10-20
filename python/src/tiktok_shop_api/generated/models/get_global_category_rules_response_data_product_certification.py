from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_global_category_rules_response_data_product_certification_requirement_condition import GetGlobalCategoryRulesResponseDataProductCertificationRequirementCondition





T = TypeVar("T", bound="GetGlobalCategoryRulesResponseDataProductCertification")



@_attrs_define
class GetGlobalCategoryRulesResponseDataProductCertification:
    """ 
        Attributes:
            id (str | Unset): The ID to identify the type of certification required.
            name (str | Unset): The name of the certification type.
            is_required (bool | Unset): A flag to indicate if the certification is required **globally**.
                - true: The certification is required in all regions.
                - false: The certification is required only in some regions, or if certain conditions are met. Refer to
                `required_regions` and `requirement_conditions` for the specific requirements.
            sample_image_url (str | Unset): The URL to view an image of the sample certification document.
            required_regions (list[str] | Unset): The markets where the certification is required, without conditions.
                Possible values:
                - DE: Germany
                - ES: Spain
                - FR: France
                - GB: United Kingdom
                - ID: Indonesia
                - IT: Italy
                - IE: Ireland
                - JP: Japan
                - MY: Malaysia
                - PH: Philippines
                - SG: Singapore
                - TH: Thailand
                - US: United States
                - VN: Vietnam
                - MX: Mexico

                Applicable only if `is_required=false`.
            optional_regions (list[str] | Unset): The markets where the certification is purely optional, or required only
                under certain conditions. Refer to `requirement_conditions` for details on markets with conditional
                requirements.

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

                Applicable only if `is_required=false`.
            requirement_conditions (list[GetGlobalCategoryRulesResponseDataProductCertificationRequirementCondition] |
                Unset): A list of conditions that determine if the certification is required in a market based on the seller's
                inputs for a product attribute. If any of the conditions is met, the certification is required; otherwise, it is
                optional.

                For example, there's a condition that states that the "Safety Data Sheet (SDS) for flammable materials"
                certification is required if the seller selects the value "Yes" for the attribute "Flammable Liquid?". For more
                scenario-based guidance on using this parameter, refer to the [Solution
                Guide](https://partner.tiktokshop.com/openlearn/guide/usecase?parent_id=7256668359046153985).

                Applicable only if `optional_regions` is not empty.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    is_required: bool | Unset = UNSET
    sample_image_url: str | Unset = UNSET
    required_regions: list[str] | Unset = UNSET
    optional_regions: list[str] | Unset = UNSET
    requirement_conditions: list[GetGlobalCategoryRulesResponseDataProductCertificationRequirementCondition] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_global_category_rules_response_data_product_certification_requirement_condition import GetGlobalCategoryRulesResponseDataProductCertificationRequirementCondition # noqa: PLC0415
        id = self.id

        name = self.name

        is_required = self.is_required

        sample_image_url = self.sample_image_url

        required_regions: list[str] | Unset = UNSET
        if not isinstance(self.required_regions, Unset):
            required_regions = self.required_regions



        optional_regions: list[str] | Unset = UNSET
        if not isinstance(self.optional_regions, Unset):
            optional_regions = self.optional_regions



        requirement_conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requirement_conditions, Unset):
            requirement_conditions = []
            for requirement_conditions_item_data in self.requirement_conditions:
                requirement_conditions_item = requirement_conditions_item_data.to_dict()
                requirement_conditions.append(requirement_conditions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if is_required is not UNSET:
            field_dict["is_required"] = is_required
        if sample_image_url is not UNSET:
            field_dict["sample_image_url"] = sample_image_url
        if required_regions is not UNSET:
            field_dict["required_regions"] = required_regions
        if optional_regions is not UNSET:
            field_dict["optional_regions"] = optional_regions
        if requirement_conditions is not UNSET:
            field_dict["requirement_conditions"] = requirement_conditions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_global_category_rules_response_data_product_certification_requirement_condition import GetGlobalCategoryRulesResponseDataProductCertificationRequirementCondition # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        is_required = d.pop("is_required", UNSET)

        sample_image_url = d.pop("sample_image_url", UNSET)

        required_regions = cast(list[str], d.pop("required_regions", UNSET))


        optional_regions = cast(list[str], d.pop("optional_regions", UNSET))


        _requirement_conditions = d.pop("requirement_conditions", UNSET)
        requirement_conditions: list[GetGlobalCategoryRulesResponseDataProductCertificationRequirementCondition] | Unset = UNSET
        if _requirement_conditions is not UNSET:
            requirement_conditions = []
            for requirement_conditions_item_data in _requirement_conditions:
                requirement_conditions_item = GetGlobalCategoryRulesResponseDataProductCertificationRequirementCondition.from_dict(requirement_conditions_item_data)



                requirement_conditions.append(requirement_conditions_item)


        get_global_category_rules_response_data_product_certification = cls(
            id=id,
            name=name,
            is_required=is_required,
            sample_image_url=sample_image_url,
            required_regions=required_regions,
            optional_regions=optional_regions,
            requirement_conditions=requirement_conditions,
        )


        get_global_category_rules_response_data_product_certification.additional_properties = d
        return get_global_category_rules_response_data_product_certification

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
