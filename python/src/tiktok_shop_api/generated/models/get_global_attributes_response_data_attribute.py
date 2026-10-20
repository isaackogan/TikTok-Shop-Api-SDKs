from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_global_attributes_response_data_attribute_requirement_condition import GetGlobalAttributesResponseDataAttributeRequirementCondition
  from ..models.get_global_attributes_response_data_attribute_value import GetGlobalAttributesResponseDataAttributeValue





T = TypeVar("T", bound="GetGlobalAttributesResponseDataAttribute")



@_attrs_define
class GetGlobalAttributesResponseDataAttribute:
    """ 
        Attributes:
            id (str | Unset): The ID of the built-in attribute.
            name (str | Unset): The name of the built-in attribute.
            type_ (str | Unset): The attribute type.
                Possible values:
                - SALES_PROPERTY: Indicates sales attributes that define product variants.
                - PRODUCT_PROPERTY: Indicates product attributes that describe the product as a whole.
            is_requried (bool | Unset): A flag indicating whether the product attribute is required across all of the
                seller's markets when creating or editing a product.
                - true: The attribute is required in all of the seller's markets.
                - false: The attribute is not required in all of the seller's markets; it may be required in some markets,
                required only under certain conditions, or optional. Refer to `required_regions`, `optional_regions`, and
                `requirement_conditions` for the specific requirements.

                Applicable only if `type=PRODUCT_PROPERTY`.
            values (list[GetGlobalAttributesResponseDataAttributeValue] | Unset): A list of selectable values for the
                attribute.
            is_multiple_selection (bool | Unset): A flag to indicate if multiple values can be provided for the attribute
                when creating or editing a product.
            is_customizable (bool | Unset): A flag to indicate if the attribute value can be customized by sellers when
                creating or editing a product.
            requirement_conditions (list[GetGlobalAttributesResponseDataAttributeRequirementCondition] | Unset): A list of
                market-specific conditions that determine whether the product attribute is required based on the seller's inputs
                for other attributes. If any condition for a market is met, the attribute is required in that market; otherwise,
                it is optional in that market. This field is omitted when no conditions apply.

                For example, a condition can state that the "Battery type" attribute is required if the seller selects the value
                "Batteries" for the attribute "Contains Batteries or Cells?". For more scenario-based guidance on using this
                parameter, refer to the [Solution
                Guide](https://partner.tiktokshop.com/openlearn/guide/usecase?parent_id=7256668359046153985).

                Applicable only if `type=PRODUCT_PROPERTY` and `optional_regions` is not empty.
            optional_regions (list[str] | Unset): The markets where the attribute is purely optional, or required only under
                certain conditions. Refer to `requirement_conditions` for details on markets with conditional requirements. This
                field is omitted when there are no optional markets.

                Possible values:
                - AT: Austria
                - BE: Belgium
                - CZ: Czech Republic
                - DE: Germany
                - ES: Spain
                - FR: France
                - GB: United Kingdom
                - GR: Greece
                - HU: Hungary
                - ID: Indonesia
                - IT: Italy
                - IE: Ireland
                - JP: Japan
                - MY: Malaysia
                - NL: Netherlands
                - PH: Philippines
                - PL: Poland
                - PT: Portugal
                - SG: Singapore
                - TH: Thailand
                - US: United States
                - VN: Vietnam
                - MX: Mexico
                Applicable only if `is_requried=false`.
            required_regions (list[str] | Unset): The markets where the attribute is required without conditions. When
                `is_requried=true`, this list contains all of the seller's markets. When `is_requried=false`, it contains only
                the markets where the attribute is unconditionally required. This field is omitted when there are no
                unconditionally required markets.

                Possible values:
                - AT: Austria
                - BE: Belgium
                - CZ: Czech Republic
                - DE: Germany
                - ES: Spain
                - FR: France
                - GB: United Kingdom
                - GR: Greece
                - HU: Hungary
                - ID: Indonesia
                - IT: Italy
                - IE: Ireland
                - JP: Japan
                - MY: Malaysia
                - NL: Netherlands
                - PH: Philippines
                - PL: Poland
                - PT: Portugal
                - SG: Singapore
                - TH: Thailand
                - US: United States
                - VN: Vietnam
                - MX: Mexico
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    is_requried: bool | Unset = UNSET
    values: list[GetGlobalAttributesResponseDataAttributeValue] | Unset = UNSET
    is_multiple_selection: bool | Unset = UNSET
    is_customizable: bool | Unset = UNSET
    requirement_conditions: list[GetGlobalAttributesResponseDataAttributeRequirementCondition] | Unset = UNSET
    optional_regions: list[str] | Unset = UNSET
    required_regions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_global_attributes_response_data_attribute_requirement_condition import GetGlobalAttributesResponseDataAttributeRequirementCondition # noqa: PLC0415
        from ..models.get_global_attributes_response_data_attribute_value import GetGlobalAttributesResponseDataAttributeValue # noqa: PLC0415
        id = self.id

        name = self.name

        type_ = self.type_

        is_requried = self.is_requried

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)



        is_multiple_selection = self.is_multiple_selection

        is_customizable = self.is_customizable

        requirement_conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.requirement_conditions, Unset):
            requirement_conditions = []
            for requirement_conditions_item_data in self.requirement_conditions:
                requirement_conditions_item = requirement_conditions_item_data.to_dict()
                requirement_conditions.append(requirement_conditions_item)



        optional_regions: list[str] | Unset = UNSET
        if not isinstance(self.optional_regions, Unset):
            optional_regions = self.optional_regions



        required_regions: list[str] | Unset = UNSET
        if not isinstance(self.required_regions, Unset):
            required_regions = self.required_regions




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if is_requried is not UNSET:
            field_dict["is_requried"] = is_requried
        if values is not UNSET:
            field_dict["values"] = values
        if is_multiple_selection is not UNSET:
            field_dict["is_multiple_selection"] = is_multiple_selection
        if is_customizable is not UNSET:
            field_dict["is_customizable"] = is_customizable
        if requirement_conditions is not UNSET:
            field_dict["requirement_conditions"] = requirement_conditions
        if optional_regions is not UNSET:
            field_dict["optional_regions"] = optional_regions
        if required_regions is not UNSET:
            field_dict["required_regions"] = required_regions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_global_attributes_response_data_attribute_requirement_condition import GetGlobalAttributesResponseDataAttributeRequirementCondition # noqa: PLC0415
        from ..models.get_global_attributes_response_data_attribute_value import GetGlobalAttributesResponseDataAttributeValue # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        is_requried = d.pop("is_requried", UNSET)

        _values = d.pop("values", UNSET)
        values: list[GetGlobalAttributesResponseDataAttributeValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = GetGlobalAttributesResponseDataAttributeValue.from_dict(values_item_data)



                values.append(values_item)


        is_multiple_selection = d.pop("is_multiple_selection", UNSET)

        is_customizable = d.pop("is_customizable", UNSET)

        _requirement_conditions = d.pop("requirement_conditions", UNSET)
        requirement_conditions: list[GetGlobalAttributesResponseDataAttributeRequirementCondition] | Unset = UNSET
        if _requirement_conditions is not UNSET:
            requirement_conditions = []
            for requirement_conditions_item_data in _requirement_conditions:
                requirement_conditions_item = GetGlobalAttributesResponseDataAttributeRequirementCondition.from_dict(requirement_conditions_item_data)



                requirement_conditions.append(requirement_conditions_item)


        optional_regions = cast(list[str], d.pop("optional_regions", UNSET))


        required_regions = cast(list[str], d.pop("required_regions", UNSET))


        get_global_attributes_response_data_attribute = cls(
            id=id,
            name=name,
            type_=type_,
            is_requried=is_requried,
            values=values,
            is_multiple_selection=is_multiple_selection,
            is_customizable=is_customizable,
            requirement_conditions=requirement_conditions,
            optional_regions=optional_regions,
            required_regions=required_regions,
        )


        get_global_attributes_response_data_attribute.additional_properties = d
        return get_global_attributes_response_data_attribute

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
