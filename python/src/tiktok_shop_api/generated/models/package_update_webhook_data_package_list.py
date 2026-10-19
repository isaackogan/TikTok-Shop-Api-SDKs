from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageUpdateWebhookDataPackageList")


@_attrs_define
class PackageUpdateWebhookDataPackageList:
    """
    Attributes:
        package_id (str | Unset): The identification of a package
        order_id_list (list[str] | Unset): List of order IDs in a given package
    """

    package_id: str | Unset = UNSET
    order_id_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        package_id = self.package_id

        order_id_list: list[str] | Unset = UNSET
        if not isinstance(self.order_id_list, Unset):
            order_id_list = self.order_id_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package_id is not UNSET:
            field_dict["package_id"] = package_id
        if order_id_list is not UNSET:
            field_dict["order_id_list"] = order_id_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        package_id = d.pop("package_id", UNSET)

        order_id_list = cast(list[str], d.pop("order_id_list", UNSET))

        package_update_webhook_data_package_list = cls(
            package_id=package_id,
            order_id_list=order_id_list,
        )

        package_update_webhook_data_package_list.additional_properties = d
        return package_update_webhook_data_package_list

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
