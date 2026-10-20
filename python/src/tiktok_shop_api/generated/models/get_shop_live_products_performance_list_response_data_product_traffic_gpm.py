from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShopLIVEProductsPerformanceListResponseDataProductTrafficGpm")


@_attrs_define
class GetShopLIVEProductsPerformanceListResponseDataProductTrafficGpm:
    """
    Attributes:
        watch_gpm (str | Unset): The Watch GPM is the average GMV generated from 1,000 views of the LIVE.
    """

    watch_gpm: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        watch_gpm = self.watch_gpm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if watch_gpm is not UNSET:
            field_dict["watch_gpm"] = watch_gpm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        watch_gpm = d.pop("watch_gpm", UNSET)

        get_shop_live_products_performance_list_response_data_product_traffic_gpm = cls(
            watch_gpm=watch_gpm,
        )

        get_shop_live_products_performance_list_response_data_product_traffic_gpm.additional_properties = d
        return get_shop_live_products_performance_list_response_data_product_traffic_gpm

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
