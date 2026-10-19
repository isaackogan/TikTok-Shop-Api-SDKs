from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_category_rules_response_data_fee_type import GetCategoryRulesResponseDataFeeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCategoryRulesResponseDataFee")


@_attrs_define
class GetCategoryRulesResponseDataFee:
    """
    Attributes:
        type_ (GetCategoryRulesResponseDataFeeType | Unset): The type of fee.
            Possible values: PFAND
        is_required (bool | Unset): A flag to indicate whether information about the fee is required.
    """

    type_: GetCategoryRulesResponseDataFeeType | Unset = UNSET
    is_required: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        is_required = self.is_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if is_required is not UNSET:
            field_dict["is_required"] = is_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: GetCategoryRulesResponseDataFeeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GetCategoryRulesResponseDataFeeType(_type_)

        is_required = d.pop("is_required", UNSET)

        get_category_rules_response_data_fee = cls(
            type_=type_,
            is_required=is_required,
        )

        get_category_rules_response_data_fee.additional_properties = d
        return get_category_rules_response_data_fee

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
