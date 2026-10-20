from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetProductSKPPDetailResponseDataRewardClaimCondition")



@_attrs_define
class GetProductSKPPDetailResponseDataRewardClaimCondition:
    """ 
        Attributes:
            condition_type (str | Unset): Possible values: GMV / ORDER.
            current_value (str | Unset): Current progress; GMV-typed values lead with the currency symbol.
            target_value (str | Unset): Threshold value; same formatting as current_value.
     """

    condition_type: str | Unset = UNSET
    current_value: str | Unset = UNSET
    target_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        condition_type = self.condition_type

        current_value = self.current_value

        target_value = self.target_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if condition_type is not UNSET:
            field_dict["condition_type"] = condition_type
        if current_value is not UNSET:
            field_dict["current_value"] = current_value
        if target_value is not UNSET:
            field_dict["target_value"] = target_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        condition_type = d.pop("condition_type", UNSET)

        current_value = d.pop("current_value", UNSET)

        target_value = d.pop("target_value", UNSET)

        get_product_skpp_detail_response_data_reward_claim_condition = cls(
            condition_type=condition_type,
            current_value=current_value,
            target_value=target_value,
        )


        get_product_skpp_detail_response_data_reward_claim_condition.additional_properties = d
        return get_product_skpp_detail_response_data_reward_claim_condition

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
