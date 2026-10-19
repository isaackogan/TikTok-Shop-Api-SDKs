from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_global_product_permission_response_data_permissions_item import (
    GetGlobalProductPermissionResponseDataPermissionsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGlobalProductPermissionResponseData")


@_attrs_define
class GetGlobalProductPermissionResponseData:
    """
    Attributes:
        permissions (list[GetGlobalProductPermissionResponseDataPermissionsItem] | Unset): The seller's global product
            permissions.
            Possible values:
            - MANAGE_GLOBAL_PRODUCT: Indicates the seller is permitted to manage global products listed in TikTok Shops
            across multiple countries.
            An empty array means the seller does not have the MANAGE_GLOBAL_PRODUCT permission.
    """

    permissions: list[GetGlobalProductPermissionResponseDataPermissionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permissions: list[str] | Unset = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.value
                permissions.append(permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _permissions = d.pop("permissions", UNSET)
        permissions: list[GetGlobalProductPermissionResponseDataPermissionsItem] | Unset = UNSET
        if _permissions is not UNSET:
            permissions = []
            for permissions_item_data in _permissions:
                permissions_item = GetGlobalProductPermissionResponseDataPermissionsItem(permissions_item_data)

                permissions.append(permissions_item)

        get_global_product_permission_response_data = cls(
            permissions=permissions,
        )

        get_global_product_permission_response_data.additional_properties = d
        return get_global_product_permission_response_data

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
