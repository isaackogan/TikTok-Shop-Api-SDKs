from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_package_request_package_status import SearchPackageRequestPackageStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchPackageRequest")


@_attrs_define
class SearchPackageRequest:
    """
    Attributes:
        create_time_ge (int | Unset): Filter packages to those created at or after the specified time. Unix timestamp,
            in seconds.
        create_time_lt (int | Unset): Filter packages to those created before the specified time. Unix timestamp, in
            seconds.
        update_time_ge (int | Unset): Filter packages to those updated at or after the specified time. Unix timestamp,
            in seconds.
        update_time_lt (int | Unset): Filter packages to those updated before the specified time. Unix timestamp, in
            seconds.
        package_status (SearchPackageRequestPackageStatus | Unset): Possible values:
            - `TO_FULFILL`
            - `PROCESSING`: Package has been arranged by seller. Waiting for carrier to collect the parcel.
            - `FULFILLING`: Package has been collected by carrier and in transit.
            - `COMPLETED`: Package has been delivered.
            - `CANCELLED`: Package has been canceled. Normally, the package is canceled due to the package being lost or
            damaged.
    """

    create_time_ge: int | Unset = UNSET
    create_time_lt: int | Unset = UNSET
    update_time_ge: int | Unset = UNSET
    update_time_lt: int | Unset = UNSET
    package_status: SearchPackageRequestPackageStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_time_ge = self.create_time_ge

        create_time_lt = self.create_time_lt

        update_time_ge = self.update_time_ge

        update_time_lt = self.update_time_lt

        package_status: str | Unset = UNSET
        if not isinstance(self.package_status, Unset):
            package_status = self.package_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_time_ge is not UNSET:
            field_dict["create_time_ge"] = create_time_ge
        if create_time_lt is not UNSET:
            field_dict["create_time_lt"] = create_time_lt
        if update_time_ge is not UNSET:
            field_dict["update_time_ge"] = update_time_ge
        if update_time_lt is not UNSET:
            field_dict["update_time_lt"] = update_time_lt
        if package_status is not UNSET:
            field_dict["package_status"] = package_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_time_ge = d.pop("create_time_ge", UNSET)

        create_time_lt = d.pop("create_time_lt", UNSET)

        update_time_ge = d.pop("update_time_ge", UNSET)

        update_time_lt = d.pop("update_time_lt", UNSET)

        _package_status = d.pop("package_status", UNSET)
        package_status: SearchPackageRequestPackageStatus | Unset
        if isinstance(_package_status, Unset):
            package_status = UNSET
        else:
            package_status = SearchPackageRequestPackageStatus(_package_status)

        search_package_request = cls(
            create_time_ge=create_time_ge,
            create_time_lt=create_time_lt,
            update_time_ge=update_time_ge,
            update_time_lt=update_time_lt,
            package_status=package_status,
        )

        search_package_request.additional_properties = d
        return search_package_request

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
