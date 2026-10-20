from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateStockOperationSettingsRequestStockOperationSetting")


@_attrs_define
class UpdateStockOperationSettingsRequestStockOperationSetting:
    """
    Attributes:
        enable_auto_restock (bool | Unset): Controls automatic inventory replenishment after a seller-fulfilled (FBM)
            order is canceled. When at least one SKU is supplied, omitting `stock_operation_setting` or
            `enable_auto_restock` uses `false`.
            - `true`: Enable automatic replenishment for the specified SKUs.
            - `false`: Disable automatic replenishment for the specified SKUs.
    """

    enable_auto_restock: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable_auto_restock = self.enable_auto_restock

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable_auto_restock is not UNSET:
            field_dict["enable_auto_restock"] = enable_auto_restock

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_auto_restock = d.pop("enable_auto_restock", UNSET)

        update_stock_operation_settings_request_stock_operation_setting = cls(
            enable_auto_restock=enable_auto_restock,
        )

        update_stock_operation_settings_request_stock_operation_setting.additional_properties = d
        return update_stock_operation_settings_request_stock_operation_setting

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
