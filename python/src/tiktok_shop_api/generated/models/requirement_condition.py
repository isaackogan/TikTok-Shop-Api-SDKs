from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RequirementCondition")



@_attrs_define
class RequirementCondition:
    """ 
        Attributes:
            condition_type (str | Unset): The type of condition.
                Possible values:
                - VALUE_ID_MATCH: The condition is true when the seller selects a value whose ID matches the one specified in
                this condition.
            attribute_id (str | Unset): The ID of the product attribute that is being evaluated by the condition.
            attribute_value_id (str | Unset): The ID of the product attribute value that must match the seller's input for
                the condition to be true.
     """

    condition_type: str | Unset = UNSET
    attribute_id: str | Unset = UNSET
    attribute_value_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        condition_type = self.condition_type

        attribute_id = self.attribute_id

        attribute_value_id = self.attribute_value_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
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
        condition_type = d.pop("condition_type", UNSET)

        attribute_id = d.pop("attribute_id", UNSET)

        attribute_value_id = d.pop("attribute_value_id", UNSET)

        requirement_condition = cls(
            condition_type=condition_type,
            attribute_id=attribute_id,
            attribute_value_id=attribute_value_id,
        )


        requirement_condition.additional_properties = d
        return requirement_condition

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
