from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGlobalSellerWarehousesResponseDataGlobalWarehouse")


@_attrs_define
class GetGlobalSellerWarehousesResponseDataGlobalWarehouse:
    """
    Attributes:
        id (str | Unset): Global warehouse ID, a unique and immutable primary key, used for all global warehouse
            logistics.
        name (str | Unset): Global warehouse name. This name is not unique across the TikTok Shop system.
        ownership (str | Unset): Possible values:
            - SELLER: Warehouse owned by the seller.
            - PLATFORM_COOPERATION: Warehouse owned by TikTok Shop.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    ownership: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        ownership = self.ownership

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if ownership is not UNSET:
            field_dict["ownership"] = ownership

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        ownership = d.pop("ownership", UNSET)

        get_global_seller_warehouses_response_data_global_warehouse = cls(
            id=id,
            name=name,
            ownership=ownership,
        )

        get_global_seller_warehouses_response_data_global_warehouse.additional_properties = d
        return get_global_seller_warehouses_response_data_global_warehouse

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
