from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_inventory_response_data_error_detail_extra_error import UpdateInventoryResponseDataErrorDetailExtraError





T = TypeVar("T", bound="UpdateInventoryResponseDataErrorDetail")



@_attrs_define
class UpdateInventoryResponseDataErrorDetail:
    """ 
        Attributes:
            sku_id (str | Unset): The ID of the SKU where the error occurred.
            extra_errors (list[UpdateInventoryResponseDataErrorDetailExtraError] | Unset): A list of secondary errors or
                issues related to the main error.
     """

    sku_id: str | Unset = UNSET
    extra_errors: list[UpdateInventoryResponseDataErrorDetailExtraError] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_inventory_response_data_error_detail_extra_error import UpdateInventoryResponseDataErrorDetailExtraError # noqa: PLC0415
        sku_id = self.sku_id

        extra_errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extra_errors, Unset):
            extra_errors = []
            for extra_errors_item_data in self.extra_errors:
                extra_errors_item = extra_errors_item_data.to_dict()
                extra_errors.append(extra_errors_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if extra_errors is not UNSET:
            field_dict["extra_errors"] = extra_errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_inventory_response_data_error_detail_extra_error import UpdateInventoryResponseDataErrorDetailExtraError # noqa: PLC0415
        d = dict(src_dict)
        sku_id = d.pop("sku_id", UNSET)

        _extra_errors = d.pop("extra_errors", UNSET)
        extra_errors: list[UpdateInventoryResponseDataErrorDetailExtraError] | Unset = UNSET
        if _extra_errors is not UNSET:
            extra_errors = []
            for extra_errors_item_data in _extra_errors:
                extra_errors_item = UpdateInventoryResponseDataErrorDetailExtraError.from_dict(extra_errors_item_data)



                extra_errors.append(extra_errors_item)


        update_inventory_response_data_error_detail = cls(
            sku_id=sku_id,
            extra_errors=extra_errors,
        )


        update_inventory_response_data_error_detail.additional_properties = d
        return update_inventory_response_data_error_detail

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
