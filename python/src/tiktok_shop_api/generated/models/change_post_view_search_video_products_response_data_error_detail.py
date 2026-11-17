from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ChangePostViewSearchVideoProductsResponseDataErrorDetail")



@_attrs_define
class ChangePostViewSearchVideoProductsResponseDataErrorDetail:
    """ 
        Attributes:
            operation (str): UNSPECIFIED means the action is unavailable; BIND adds the association; UNBIND removes it.
            product_id (str): Unique product id.
     """

    operation: str
    product_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        operation = self.operation

        product_id = self.product_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "operation": operation,
            "product_id": product_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation = d.pop("operation")

        product_id = d.pop("product_id")

        change_post_view_search_video_products_response_data_error_detail = cls(
            operation=operation,
            product_id=product_id,
        )


        change_post_view_search_video_products_response_data_error_detail.additional_properties = d
        return change_post_view_search_video_products_response_data_error_detail

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
