from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetShopGroupAndRelatedShopsResponseDataShopGroupDataShopGroup")


@_attrs_define
class GetShopGroupAndRelatedShopsResponseDataShopGroupDataShopGroup:
    """
    Attributes:
        source (str | Unset): Used to distinguish the creation source of product interoperability groups.
            If it is a product interoperability group formed by a US local merchant opening an MX store, the enumeration
            value is: '1 -> US_MX_ONBOARD'
            If it is a product interoperability group formed by a Chinese cross-border merchant opening an MX store, the
            enumeration value is '2 -> GS_POP'.
        shop_group_name (str | Unset): The unique name representing the product interoperability group
    """

    source: str | Unset = UNSET
    shop_group_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        shop_group_name = self.shop_group_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if shop_group_name is not UNSET:
            field_dict["shop_group_name"] = shop_group_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source", UNSET)

        shop_group_name = d.pop("shop_group_name", UNSET)

        get_shop_group_and_related_shops_response_data_shop_group_data_shop_group = cls(
            source=source,
            shop_group_name=shop_group_name,
        )

        get_shop_group_and_related_shops_response_data_shop_group_data_shop_group.additional_properties = d
        return get_shop_group_and_related_shops_response_data_shop_group_data_shop_group

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
