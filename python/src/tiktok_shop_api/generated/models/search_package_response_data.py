from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_package_response_data_package import SearchPackageResponseDataPackage





T = TypeVar("T", bound="SearchPackageResponseData")



@_attrs_define
class SearchPackageResponseData:
    """ 
        Attributes:
            next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. If this
                value is non-empty, provide it in the `page_token` parameter of the next request. If this value is empty, stop
                pagination.
            total_count (int | Unset): The number of packages that meet the query conditions.
            packages (list[SearchPackageResponseDataPackage] | Unset): The response list of packages.
     """

    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    packages: list[SearchPackageResponseDataPackage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_package_response_data_package import SearchPackageResponseDataPackage # noqa: PLC0415
        next_page_token = self.next_page_token

        total_count = self.total_count

        packages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.packages, Unset):
            packages = []
            for packages_item_data in self.packages:
                packages_item = packages_item_data.to_dict()
                packages.append(packages_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if packages is not UNSET:
            field_dict["packages"] = packages

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_package_response_data_package import SearchPackageResponseDataPackage # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        _packages = d.pop("packages", UNSET)
        packages: list[SearchPackageResponseDataPackage] | Unset = UNSET
        if _packages is not UNSET:
            packages = []
            for packages_item_data in _packages:
                packages_item = SearchPackageResponseDataPackage.from_dict(packages_item_data)



                packages.append(packages_item)


        search_package_response_data = cls(
            next_page_token=next_page_token,
            total_count=total_count,
            packages=packages,
        )


        search_package_response_data.additional_properties = d
        return search_package_response_data

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
