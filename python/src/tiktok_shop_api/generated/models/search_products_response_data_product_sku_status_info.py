from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchProductsResponseDataProductSkuStatusInfo")


@_attrs_define
class SearchProductsResponseDataProductSkuStatusInfo:
    """
    Attributes:
        status (str | Unset): The SKU status in TikTok Shop.
            Possible values:
            - NORMAL
            - DEACTIVATED
        deactivation_source (str | Unset): The deactivation source of the SKU with `DEACTIVATED` status.
            Possible values:
            - SELLER: Indicates that the seller deactivated the SKU
            - PLATFORM: Indicates that the platform de-activated the SKU due to violation reasons
            - COMBO_RELATION: Indicates that the platform de-activated the combined-SKU due to the deactivation of sub-SKU.
    """

    status: str | Unset = UNSET
    deactivation_source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        deactivation_source = self.deactivation_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if deactivation_source is not UNSET:
            field_dict["deactivation_source"] = deactivation_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        deactivation_source = d.pop("deactivation_source", UNSET)

        search_products_response_data_product_sku_status_info = cls(
            status=status,
            deactivation_source=deactivation_source,
        )

        search_products_response_data_product_sku_status_info.additional_properties = d
        return search_products_response_data_product_sku_status_info

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
