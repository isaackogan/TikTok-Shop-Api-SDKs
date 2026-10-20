from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.package_update_webhook_data_package_list import PackageUpdateWebhookDataPackageList





T = TypeVar("T", bound="PackageUpdateWebhookData")



@_attrs_define
class PackageUpdateWebhookData:
    """ 
        Attributes:
            sc_type (str | Unset): Type of the event trigger, with possible values:

                 * COMBINE
                 * CANCEL_COMBINE
                 * SPLIT
                 * CANCEL_SPLIT
                 * ADDRESS_UPDATE_SPLIT
                 * CANCEL_FULFILL_SPLIT
                 * FULFILL_UNCOMBINE
                 * PARTLY_CANCEL_SPLIT
                 * SPLIT_BY_SKU_CANCEL
            role_type (str | Unset): Operator of the event trigger, with possible values:

                 * ROLE_USER
                 * ROLE_SELLER
                 * ROLE_OPERATOR
                 * ROLE_SYSTEM
            package_list (list[PackageUpdateWebhookDataPackageList] | Unset): Package list updated by the event trigger
            update_time (int | Unset): The time when the package was updated, represented as a Unix timestamp (seconds).
     """

    sc_type: str | Unset = UNSET
    role_type: str | Unset = UNSET
    package_list: list[PackageUpdateWebhookDataPackageList] | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.package_update_webhook_data_package_list import PackageUpdateWebhookDataPackageList # noqa: PLC0415
        sc_type = self.sc_type

        role_type = self.role_type

        package_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.package_list, Unset):
            package_list = []
            for package_list_item_data in self.package_list:
                package_list_item = package_list_item_data.to_dict()
                package_list.append(package_list_item)



        update_time = self.update_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sc_type is not UNSET:
            field_dict["sc_type"] = sc_type
        if role_type is not UNSET:
            field_dict["role_type"] = role_type
        if package_list is not UNSET:
            field_dict["package_list"] = package_list
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.package_update_webhook_data_package_list import PackageUpdateWebhookDataPackageList # noqa: PLC0415
        d = dict(src_dict)
        sc_type = d.pop("sc_type", UNSET)

        role_type = d.pop("role_type", UNSET)

        _package_list = d.pop("package_list", UNSET)
        package_list: list[PackageUpdateWebhookDataPackageList] | Unset = UNSET
        if _package_list is not UNSET:
            package_list = []
            for package_list_item_data in _package_list:
                package_list_item = PackageUpdateWebhookDataPackageList.from_dict(package_list_item_data)



                package_list.append(package_list_item)


        update_time = d.pop("update_time", UNSET)

        package_update_webhook_data = cls(
            sc_type=sc_type,
            role_type=role_type,
            package_list=package_list,
            update_time=update_time,
        )


        package_update_webhook_data.additional_properties = d
        return package_update_webhook_data

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
