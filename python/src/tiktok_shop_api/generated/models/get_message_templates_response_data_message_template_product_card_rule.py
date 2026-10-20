from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetMessageTemplatesResponseDataMessageTemplateProductCardRule")



@_attrs_define
class GetMessageTemplatesResponseDataMessageTemplateProductCardRule:
    """ 
        Attributes:
            min_count (int | Unset): The minimum number of product cards that must be included.
            max_count (int | Unset): The maximum number of product cards that can be included.
     """

    min_count: int | Unset = UNSET
    max_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        min_count = self.min_count

        max_count = self.max_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if min_count is not UNSET:
            field_dict["min_count"] = min_count
        if max_count is not UNSET:
            field_dict["max_count"] = max_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        min_count = d.pop("min_count", UNSET)

        max_count = d.pop("max_count", UNSET)

        get_message_templates_response_data_message_template_product_card_rule = cls(
            min_count=min_count,
            max_count=max_count,
        )


        get_message_templates_response_data_message_template_product_card_rule.additional_properties = d
        return get_message_templates_response_data_message_template_product_card_rule

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
