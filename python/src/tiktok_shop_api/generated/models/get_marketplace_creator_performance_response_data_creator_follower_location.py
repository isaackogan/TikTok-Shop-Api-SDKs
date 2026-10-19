from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerLocation")


@_attrs_define
class GetMarketplaceCreatorPerformanceResponseDataCreatorFollowerLocation:
    """
    Attributes:
        key (str | Unset): The country code for the follower location (for example, ID).
        value (str | Unset): The proportion of followers from this location, expressed as a decimal (e.g., 0.3705 =
            37.05%).
    """

    key: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        get_marketplace_creator_performance_response_data_creator_follower_location = cls(
            key=key,
            value=value,
        )

        get_marketplace_creator_performance_response_data_creator_follower_location.additional_properties = d
        return get_marketplace_creator_performance_response_data_creator_follower_location

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
