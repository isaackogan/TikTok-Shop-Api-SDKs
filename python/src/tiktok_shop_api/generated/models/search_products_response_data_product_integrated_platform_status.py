from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_products_response_data_product_integrated_platform_status_platform import (
    SearchProductsResponseDataProductIntegratedPlatformStatusPlatform,
)
from ..models.search_products_response_data_product_integrated_platform_status_status import (
    SearchProductsResponseDataProductIntegratedPlatformStatusStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchProductsResponseDataProductIntegratedPlatformStatus")


@_attrs_define
class SearchProductsResponseDataProductIntegratedPlatformStatus:
    """
    Attributes:
        platform (SearchProductsResponseDataProductIntegratedPlatformStatusPlatform | Unset): The integrated platform
            name.
            Possible values:
            - TOKOPEDIA
        status (SearchProductsResponseDataProductIntegratedPlatformStatusStatus | Unset): The product status in the
            integrated platform.
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

    platform: SearchProductsResponseDataProductIntegratedPlatformStatusPlatform | Unset = UNSET
    status: SearchProductsResponseDataProductIntegratedPlatformStatusStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform is not UNSET:
            field_dict["platform"] = platform
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _platform = d.pop("platform", UNSET)
        platform: SearchProductsResponseDataProductIntegratedPlatformStatusPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = SearchProductsResponseDataProductIntegratedPlatformStatusPlatform(_platform)

        _status = d.pop("status", UNSET)
        status: SearchProductsResponseDataProductIntegratedPlatformStatusStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SearchProductsResponseDataProductIntegratedPlatformStatusStatus(_status)

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
