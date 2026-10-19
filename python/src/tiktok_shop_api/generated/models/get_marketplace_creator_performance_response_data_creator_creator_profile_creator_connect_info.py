from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorConnectInfo")


@_attrs_define
class GetMarketplaceCreatorPerformanceResponseDataCreatorCreatorProfileCreatorConnectInfo:
    """
    Attributes:
        is_paired (bool | Unset): Creator is paired or not
        is_connect (bool | Unset): Creator is connect or not
        is_blocked (bool | Unset): Creator is blocked or not
    """

    is_paired: bool | Unset = UNSET
    is_connect: bool | Unset = UNSET
    is_blocked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_paired = self.is_paired

        is_connect = self.is_connect

        is_blocked = self.is_blocked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_paired is not UNSET:
            field_dict["is_paired"] = is_paired
        if is_connect is not UNSET:
            field_dict["is_connect"] = is_connect
        if is_blocked is not UNSET:
            field_dict["is_blocked"] = is_blocked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_paired = d.pop("is_paired", UNSET)

        is_connect = d.pop("is_connect", UNSET)

        is_blocked = d.pop("is_blocked", UNSET)

        get_marketplace_creator_performance_response_data_creator_creator_profile_creator_connect_info = cls(
            is_paired=is_paired,
            is_connect=is_connect,
            is_blocked=is_blocked,
        )

        get_marketplace_creator_performance_response_data_creator_creator_profile_creator_connect_info.additional_properties = d
        return get_marketplace_creator_performance_response_data_creator_creator_profile_creator_connect_info

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
