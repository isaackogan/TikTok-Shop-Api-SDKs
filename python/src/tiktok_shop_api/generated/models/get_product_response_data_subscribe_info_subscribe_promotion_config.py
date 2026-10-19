from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductResponseDataSubscribeInfoSubscribePromotionConfig")


@_attrs_define
class GetProductResponseDataSubscribeInfoSubscribePromotionConfig:
    """
    Attributes:
        discount_level (str | Unset): An enum that communicated the type of discount:
            - REGULAR
            - FIRST_ORDER
            - RETENTION
        discount_options (list[int] | Unset): The discount options available to the seller for the given discount level.
        max_discount (int | Unset): The maximum discount a seller can set for the associated discount level.
        min_discount (int | Unset): The minimum discount a seller can set for the associated discount level.
    """

    discount_level: str | Unset = UNSET
    discount_options: list[int] | Unset = UNSET
    max_discount: int | Unset = UNSET
    min_discount: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discount_level = self.discount_level

        discount_options: list[int] | Unset = UNSET
        if not isinstance(self.discount_options, Unset):
            discount_options = self.discount_options

        max_discount = self.max_discount

        min_discount = self.min_discount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discount_level is not UNSET:
            field_dict["discount_level"] = discount_level
        if discount_options is not UNSET:
            field_dict["discount_options"] = discount_options
        if max_discount is not UNSET:
            field_dict["max_discount"] = max_discount
        if min_discount is not UNSET:
            field_dict["min_discount"] = min_discount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        discount_level = d.pop("discount_level", UNSET)

        discount_options = cast(list[int], d.pop("discount_options", UNSET))

        max_discount = d.pop("max_discount", UNSET)

        min_discount = d.pop("min_discount", UNSET)

        get_product_response_data_subscribe_info_subscribe_promotion_config = cls(
            discount_level=discount_level,
            discount_options=discount_options,
            max_discount=max_discount,
            min_discount=min_discount,
        )

        get_product_response_data_subscribe_info_subscribe_promotion_config.additional_properties = d
        return get_product_response_data_subscribe_info_subscribe_promotion_config

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
