from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SKUStatusChangeWebhookDataSku")



@_attrs_define
class SKUStatusChangeWebhookDataSku:
    """ 
        Attributes:
            sku_id (str | Unset): The ID of the SKU whose status changed.
            status (str | Unset): The new SKU status. Possible values: `CREATED`, `DELETED`, `ACTIVATED`, `DEACTIVATED`.
            deactivation_source (str | Unset): The source of deactivation. This field is returned only when `status` is
                `DEACTIVATED`. Possible values: `SELLER`, `PLATFORM`, `COMBO_RELATION`.
     """

    sku_id: str | Unset = UNSET
    status: str | Unset = UNSET
    deactivation_source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        sku_id = self.sku_id

        status = self.status

        deactivation_source = self.deactivation_source


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if status is not UNSET:
            field_dict["status"] = status
        if deactivation_source is not UNSET:
            field_dict["deactivation_source"] = deactivation_source

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sku_id = d.pop("sku_id", UNSET)

        status = d.pop("status", UNSET)

        deactivation_source = d.pop("deactivation_source", UNSET)

        sku_status_change_webhook_data_sku = cls(
            sku_id=sku_id,
            status=status,
            deactivation_source=deactivation_source,
        )


        sku_status_change_webhook_data_sku.additional_properties = d
        return sku_status_change_webhook_data_sku

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
