from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateStockOperationSettingsResponseDataStockOperation")



@_attrs_define
class UpdateStockOperationSettingsResponseDataStockOperation:
    """ 
        Attributes:
            failed_sku_ids (list[str] | Unset): Update inventory rule failed SkuID list
            success_sku_ids (list[str] | Unset): List of SkuIDs that successfully updated inventory rules
     """

    failed_sku_ids: list[str] | Unset = UNSET
    success_sku_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        failed_sku_ids: list[str] | Unset = UNSET
        if not isinstance(self.failed_sku_ids, Unset):
            failed_sku_ids = self.failed_sku_ids



        success_sku_ids: list[str] | Unset = UNSET
        if not isinstance(self.success_sku_ids, Unset):
            success_sku_ids = self.success_sku_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if failed_sku_ids is not UNSET:
            field_dict["failed_sku_ids"] = failed_sku_ids
        if success_sku_ids is not UNSET:
            field_dict["success_sku_ids"] = success_sku_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        failed_sku_ids = cast(list[str], d.pop("failed_sku_ids", UNSET))


        success_sku_ids = cast(list[str], d.pop("success_sku_ids", UNSET))


        update_stock_operation_settings_response_data_stock_operation = cls(
            failed_sku_ids=failed_sku_ids,
            success_sku_ids=success_sku_ids,
        )


        update_stock_operation_settings_response_data_stock_operation.additional_properties = d
        return update_stock_operation_settings_response_data_stock_operation

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
