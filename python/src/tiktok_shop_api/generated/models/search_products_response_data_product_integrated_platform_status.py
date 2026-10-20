from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SearchProductsResponseDataProductIntegratedPlatformStatus")



@_attrs_define
class SearchProductsResponseDataProductIntegratedPlatformStatus:
    """ 
        Attributes:
            platform (str | Unset): The integrated platform name.
                Possible values:
                - TOKOPEDIA
            status (str | Unset): The product status in the integrated platform.
                Possible values:
                - DRAFT
                - PENDING
                - FAILED
                - ACTIVATE
                - SELLER_DEACTIVATED
                - PLATFORM_DEACTIVATED
                - FREEZE
                - DELETED
     """

    platform: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        platform = self.platform

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if platform is not UNSET:
            field_dict["platform"] = platform
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        platform = d.pop("platform", UNSET)

        status = d.pop("status", UNSET)

        search_products_response_data_product_integrated_platform_status = cls(
            platform=platform,
            status=status,
        )


        search_products_response_data_product_integrated_platform_status.additional_properties = d
        return search_products_response_data_product_integrated_platform_status

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
