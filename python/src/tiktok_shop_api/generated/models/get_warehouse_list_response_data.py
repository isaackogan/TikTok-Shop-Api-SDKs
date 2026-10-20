from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_warehouse_list_response_data_warehouse import GetWarehouseListResponseDataWarehouse


T = TypeVar("T", bound="GetWarehouseListResponseData")


@_attrs_define
class GetWarehouseListResponseData:
    """
    Attributes:
        warehouses (list[GetWarehouseListResponseDataWarehouse] | Unset): Warehouses returned for the seller. This field
            is omitted when the result contains no warehouse.
    """

    warehouses: list[GetWarehouseListResponseDataWarehouse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warehouses, Unset):
            warehouses = []
            for warehouses_item_data in self.warehouses:
                warehouses_item = warehouses_item_data.to_dict()
                warehouses.append(warehouses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warehouses is not UNSET:
            field_dict["warehouses"] = warehouses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_warehouse_list_response_data_warehouse import (
            GetWarehouseListResponseDataWarehouse,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _warehouses = d.pop("warehouses", UNSET)
        warehouses: list[GetWarehouseListResponseDataWarehouse] | Unset = UNSET
        if _warehouses is not UNSET:
            warehouses = []
            for warehouses_item_data in _warehouses:
                warehouses_item = GetWarehouseListResponseDataWarehouse.from_dict(warehouses_item_data)

                warehouses.append(warehouses_item)

        get_warehouse_list_response_data = cls(
            warehouses=warehouses,
        )

        get_warehouse_list_response_data.additional_properties = d
        return get_warehouse_list_response_data

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
