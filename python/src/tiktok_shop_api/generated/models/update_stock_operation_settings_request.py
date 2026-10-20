from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_stock_operation_settings_request_stock_operation_setting import UpdateStockOperationSettingsRequestStockOperationSetting





T = TypeVar("T", bound="UpdateStockOperationSettingsRequest")



@_attrs_define
class UpdateStockOperationSettingsRequest:
    """ 
        Attributes:
            seller_id (str): Identifies the seller whose settings are being modified.
            sku_ids (list[str] | Unset): List of specific SKU IDs. Up to 500 SKUs in a batch.
            stock_operation_setting (UpdateStockOperationSettingsRequestStockOperationSetting | Unset):
     """

    seller_id: str
    sku_ids: list[str] | Unset = UNSET
    stock_operation_setting: UpdateStockOperationSettingsRequestStockOperationSetting | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_stock_operation_settings_request_stock_operation_setting import UpdateStockOperationSettingsRequestStockOperationSetting # noqa: PLC0415
        seller_id = self.seller_id

        sku_ids: list[str] | Unset = UNSET
        if not isinstance(self.sku_ids, Unset):
            sku_ids = self.sku_ids



        stock_operation_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stock_operation_setting, Unset):
            stock_operation_setting = self.stock_operation_setting.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "seller_id": seller_id,
        })
        if sku_ids is not UNSET:
            field_dict["sku_ids"] = sku_ids
        if stock_operation_setting is not UNSET:
            field_dict["stock_operation_setting"] = stock_operation_setting

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_stock_operation_settings_request_stock_operation_setting import UpdateStockOperationSettingsRequestStockOperationSetting # noqa: PLC0415
        d = dict(src_dict)
        seller_id = d.pop("seller_id")

        sku_ids = cast(list[str], d.pop("sku_ids", UNSET))


        _stock_operation_setting = d.pop("stock_operation_setting", UNSET)
        stock_operation_setting: UpdateStockOperationSettingsRequestStockOperationSetting | Unset
        if isinstance(_stock_operation_setting,  Unset):
            stock_operation_setting = UNSET
        else:
            stock_operation_setting = UpdateStockOperationSettingsRequestStockOperationSetting.from_dict(_stock_operation_setting)




        update_stock_operation_settings_request = cls(
            seller_id=seller_id,
            sku_ids=sku_ids,
            stock_operation_setting=stock_operation_setting,
        )


        update_stock_operation_settings_request.additional_properties = d
        return update_stock_operation_settings_request

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
