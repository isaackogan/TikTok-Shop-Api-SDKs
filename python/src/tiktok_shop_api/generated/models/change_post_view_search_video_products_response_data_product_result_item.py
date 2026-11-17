from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ChangePostViewSearchVideoProductsResponseDataProductResultItem")



@_attrs_define
class ChangePostViewSearchVideoProductsResponseDataProductResultItem:
    """ 
        Attributes:
            operation (str | Unset): UNSPECIFIED means the action is unavailable; BIND adds the association; UNBIND removes
                it.
            product_id (str | Unset): Unique product id.
            status (str | Unset): Business result: UNSPECIFIED means no known outcome; SUCCEEDED means completed;
                PARTIAL_FAILED means some changes failed; FAILED means the requested change failed.
     """

    operation: str | Unset = UNSET
    product_id: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        operation = self.operation

        product_id = self.product_id

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if operation is not UNSET:
            field_dict["operation"] = operation
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation = d.pop("operation", UNSET)

        product_id = d.pop("product_id", UNSET)

        status = d.pop("status", UNSET)

        change_post_view_search_video_products_response_data_product_result_item = cls(
            operation=operation,
            product_id=product_id,
            status=status,
        )


        change_post_view_search_video_products_response_data_product_result_item.additional_properties = d
        return change_post_view_search_video_products_response_data_product_result_item

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
