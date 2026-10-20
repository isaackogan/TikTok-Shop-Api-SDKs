from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetProductResponseDataSubscribeInfoSubscribeDiscountDetail")



@_attrs_define
class GetProductResponseDataSubscribeInfoSubscribeDiscountDetail:
    """ 
        Attributes:
            discount_level (str | Unset): An enum that communicated the type of discount:
                - REGULAR
                - FIRST_ORDER
                - RETENTION
            discount_value (int | Unset): The value of the discount. A value of 10, would indicate a 10% discount.
     """

    discount_level: str | Unset = UNSET
    discount_value: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        discount_level = self.discount_level

        discount_value = self.discount_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if discount_level is not UNSET:
            field_dict["discount_level"] = discount_level
        if discount_value is not UNSET:
            field_dict["discount_value"] = discount_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        discount_level = d.pop("discount_level", UNSET)

        discount_value = d.pop("discount_value", UNSET)

        get_product_response_data_subscribe_info_subscribe_discount_detail = cls(
            discount_level=discount_level,
            discount_value=discount_value,
        )


        get_product_response_data_subscribe_info_subscribe_discount_detail.additional_properties = d
        return get_product_response_data_subscribe_info_subscribe_discount_detail

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
