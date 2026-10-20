from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RefundSuccessWebhookDataLineItem")



@_attrs_define
class RefundSuccessWebhookDataLineItem:
    """ 
        Attributes:
            main_order_id (str | Unset): Main forward order identifier.
            return_line_item_id (str | Unset): Return line-item identifier.
            sku_id (str | Unset): SKU identifier.
            sku_return_request_id (str | Unset): SKU-level return request identifier.
            sub_return_line_item_id (str | Unset): Optional child line-item identifier, only applicable for Virtual Bundle
                returns.
     """

    main_order_id: str | Unset = UNSET
    return_line_item_id: str | Unset = UNSET
    sku_id: str | Unset = UNSET
    sku_return_request_id: str | Unset = UNSET
    sub_return_line_item_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        main_order_id = self.main_order_id

        return_line_item_id = self.return_line_item_id

        sku_id = self.sku_id

        sku_return_request_id = self.sku_return_request_id

        sub_return_line_item_id = self.sub_return_line_item_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if main_order_id is not UNSET:
            field_dict["main_order_id"] = main_order_id
        if return_line_item_id is not UNSET:
            field_dict["return_line_item_id"] = return_line_item_id
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if sku_return_request_id is not UNSET:
            field_dict["sku_return_request_id"] = sku_return_request_id
        if sub_return_line_item_id is not UNSET:
            field_dict["sub_return_line_item_id"] = sub_return_line_item_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        main_order_id = d.pop("main_order_id", UNSET)

        return_line_item_id = d.pop("return_line_item_id", UNSET)

        sku_id = d.pop("sku_id", UNSET)

        sku_return_request_id = d.pop("sku_return_request_id", UNSET)

        sub_return_line_item_id = d.pop("sub_return_line_item_id", UNSET)

        refund_success_webhook_data_line_item = cls(
            main_order_id=main_order_id,
            return_line_item_id=return_line_item_id,
            sku_id=sku_id,
            sku_return_request_id=sku_return_request_id,
            sub_return_line_item_id=sub_return_line_item_id,
        )


        refund_success_webhook_data_line_item.additional_properties = d
        return refund_success_webhook_data_line_item

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
