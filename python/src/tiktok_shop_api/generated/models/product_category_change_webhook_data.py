from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProductCategoryChangeWebhookData")



@_attrs_define
class ProductCategoryChangeWebhookData:
    """ 
        Attributes:
            product_id (str | Unset): ID of the product promoted in the creator's video.
            previous_category_id (str | Unset): The category ID of the product before the category update.
            current_category_id (str | Unset): The category ID of the product after the category update.
            update_time (int | Unset): The time when this category update happens, represented by Unix timestamp.
     """

    product_id: str | Unset = UNSET
    previous_category_id: str | Unset = UNSET
    current_category_id: str | Unset = UNSET
    update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        previous_category_id = self.previous_category_id

        current_category_id = self.current_category_id

        update_time = self.update_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if previous_category_id is not UNSET:
            field_dict["previous_category_id"] = previous_category_id
        if current_category_id is not UNSET:
            field_dict["current_category_id"] = current_category_id
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        previous_category_id = d.pop("previous_category_id", UNSET)

        current_category_id = d.pop("current_category_id", UNSET)

        update_time = d.pop("update_time", UNSET)

        product_category_change_webhook_data = cls(
            product_id=product_id,
            previous_category_id=previous_category_id,
            current_category_id=current_category_id,
            update_time=update_time,
        )


        product_category_change_webhook_data.additional_properties = d
        return product_category_change_webhook_data

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
