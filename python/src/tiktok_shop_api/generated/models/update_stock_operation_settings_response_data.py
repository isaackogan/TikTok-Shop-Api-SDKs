from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_stock_operation_settings_response_data_stock_operation import (
        UpdateStockOperationSettingsResponseDataStockOperation,
    )


T = TypeVar("T", bound="UpdateStockOperationSettingsResponseData")


@_attrs_define
class UpdateStockOperationSettingsResponseData:
    """
    Attributes:
        stock_operation (UpdateStockOperationSettingsResponseDataStockOperation | Unset):
    """

    stock_operation: UpdateStockOperationSettingsResponseDataStockOperation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stock_operation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stock_operation, Unset):
            stock_operation = self.stock_operation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stock_operation is not UNSET:
            field_dict["stock_operation"] = stock_operation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_stock_operation_settings_response_data_stock_operation import (
            UpdateStockOperationSettingsResponseDataStockOperation,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _stock_operation = d.pop("stock_operation", UNSET)
        stock_operation: UpdateStockOperationSettingsResponseDataStockOperation | Unset
        if isinstance(_stock_operation, Unset):
            stock_operation = UNSET
        else:
            stock_operation = UpdateStockOperationSettingsResponseDataStockOperation.from_dict(_stock_operation)

        update_stock_operation_settings_response_data = cls(
            stock_operation=stock_operation,
        )

        update_stock_operation_settings_response_data.additional_properties = d
        return update_stock_operation_settings_response_data

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
