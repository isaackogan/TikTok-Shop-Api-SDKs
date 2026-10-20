from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_combinable_packages_response_data_combinable_package import (
        SearchCombinablePackagesResponseDataCombinablePackage,
    )


T = TypeVar("T", bound="SearchCombinablePackagesResponseData")


@_attrs_define
class SearchCombinablePackagesResponseData:
    """
    Attributes:
        combinable_packages (list[SearchCombinablePackagesResponseDataCombinablePackage] | Unset): List of eligible
            packages that can be combined.
        next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. Provide
            this value in the `page_token` parameter of your request if the current response does not return all the
            results.
        total_count (int | Unset): The number of combinable packages counted by this result.
    """

    combinable_packages: list[SearchCombinablePackagesResponseDataCombinablePackage] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        combinable_packages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.combinable_packages, Unset):
            combinable_packages = []
            for combinable_packages_item_data in self.combinable_packages:
                combinable_packages_item = combinable_packages_item_data.to_dict()
                combinable_packages.append(combinable_packages_item)

        next_page_token = self.next_page_token

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if combinable_packages is not UNSET:
            field_dict["combinable_packages"] = combinable_packages
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_combinable_packages_response_data_combinable_package import (
            SearchCombinablePackagesResponseDataCombinablePackage,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _combinable_packages = d.pop("combinable_packages", UNSET)
        combinable_packages: list[SearchCombinablePackagesResponseDataCombinablePackage] | Unset = UNSET
        if _combinable_packages is not UNSET:
            combinable_packages = []
            for combinable_packages_item_data in _combinable_packages:
                combinable_packages_item = SearchCombinablePackagesResponseDataCombinablePackage.from_dict(
                    combinable_packages_item_data
                )

                combinable_packages.append(combinable_packages_item)

        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        search_combinable_packages_response_data = cls(
            combinable_packages=combinable_packages,
            next_page_token=next_page_token,
            total_count=total_count,
        )

        search_combinable_packages_response_data.additional_properties = d
        return search_combinable_packages_response_data

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
