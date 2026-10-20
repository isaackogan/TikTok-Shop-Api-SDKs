from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchCombinablePackagesResponseDataCombinablePackage")


@_attrs_define
class SearchCombinablePackagesResponseDataCombinablePackage:
    """
    Attributes:
        id (str | Unset): The pre-generated package ID obtained after calling the Search Draft Package API. Use this ID
            when confirming the package combination.
        order_ids (list[str] | Unset): List of order IDs for this package.
    """

    id: str | Unset = UNSET
    order_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        order_ids: list[str] | Unset = UNSET
        if not isinstance(self.order_ids, Unset):
            order_ids = self.order_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if order_ids is not UNSET:
            field_dict["order_ids"] = order_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        order_ids = cast(list[str], d.pop("order_ids", UNSET))

        search_combinable_packages_response_data_combinable_package = cls(
            id=id,
            order_ids=order_ids,
        )

        search_combinable_packages_response_data_combinable_package.additional_properties = d
        return search_combinable_packages_response_data_combinable_package

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
