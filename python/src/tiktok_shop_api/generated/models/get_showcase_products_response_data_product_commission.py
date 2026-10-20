from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShowcaseProductsResponseDataProductCommission")


@_attrs_define
class GetShowcaseProductsResponseDataProductCommission:
    """
    Attributes:
        rate (int | Unset): The commission rate in hundredths of a percent. For example, `3587` is a commission rate of
            `35.87%`. The range of this value is [100, 8000].
        reward_rate (int | Unset): The reward commission rate in hundredths of a percent. For example, `3587` is a
            commission rate of `35.87%`.
    """

    rate: int | Unset = UNSET
    reward_rate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate = self.rate

        reward_rate = self.reward_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate is not UNSET:
            field_dict["rate"] = rate
        if reward_rate is not UNSET:
            field_dict["reward_rate"] = reward_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate", UNSET)

        reward_rate = d.pop("reward_rate", UNSET)

        get_showcase_products_response_data_product_commission = cls(
            rate=rate,
            reward_rate=reward_rate,
        )

        get_showcase_products_response_data_product_commission.additional_properties = d
        return get_showcase_products_response_data_product_commission

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
