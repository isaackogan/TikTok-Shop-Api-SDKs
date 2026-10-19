from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShopGroupAndRelatedShopsResponseDataShopGroupDataShop")


@_attrs_define
class GetShopGroupAndRelatedShopsResponseDataShopGroupDataShop:
    """
    Attributes:
        shop_id (str | Unset): The ID of the shop.
        seller_id (str | Unset): The global seller ID associated with the shop.
        shop_name (str | Unset): The name of the shop.
        shop_region (str | Unset): Region where the shop operates
    """

    shop_id: str | Unset = UNSET
    seller_id: str | Unset = UNSET
    shop_name: str | Unset = UNSET
    shop_region: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shop_id = self.shop_id

        seller_id = self.seller_id

        shop_name = self.shop_name

        shop_region = self.shop_region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if seller_id is not UNSET:
            field_dict["seller_id"] = seller_id
        if shop_name is not UNSET:
            field_dict["shop_name"] = shop_name
        if shop_region is not UNSET:
            field_dict["shop_region"] = shop_region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shop_id = d.pop("shop_id", UNSET)

        seller_id = d.pop("seller_id", UNSET)

        shop_name = d.pop("shop_name", UNSET)

        shop_region = d.pop("shop_region", UNSET)

        get_shop_group_and_related_shops_response_data_shop_group_data_shop = cls(
            shop_id=shop_id,
            seller_id=seller_id,
            shop_name=shop_name,
            shop_region=shop_region,
        )

        get_shop_group_and_related_shops_response_data_shop_group_data_shop.additional_properties = d
        return get_shop_group_and_related_shops_response_data_shop_group_data_shop

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
