from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetOrderSplitAttributesResponseDataSplitAttributeMustSplitReason")



@_attrs_define
class GetOrderSplitAttributesResponseDataSplitAttributeMustSplitReason:
    """ 
        Attributes:
            type_ (str | Unset): It will return which type of verification is hit. There are two types of verification:
                CATEGORY_ITEM_LIMITATION means category verification and TOTAL_COUNT_LIMITATION means total product quantity
                verification.
            category_id (str | Unset): The category ID associated with this split limitation. A value is returned when
                `type` is `CATEGORY_ITEM_LIMITATION`; no value is returned when `type` is `TOTAL_COUNT_LIMITATION`.
            max_count (str | Unset): For category verification, return the maximum quantity of goods allowed for this
                category in a single package; for total product quantity verification within the package, return the total
                quantity limit of goods in a single package.
     """

    type_: str | Unset = UNSET
    category_id: str | Unset = UNSET
    max_count: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        category_id = self.category_id

        max_count = self.max_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if max_count is not UNSET:
            field_dict["max_count"] = max_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        category_id = d.pop("category_id", UNSET)

        max_count = d.pop("max_count", UNSET)

        get_order_split_attributes_response_data_split_attribute_must_split_reason = cls(
            type_=type_,
            category_id=category_id,
            max_count=max_count,
        )


        get_order_split_attributes_response_data_split_attribute_must_split_reason.additional_properties = d
        return get_order_split_attributes_response_data_split_attribute_must_split_reason

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
