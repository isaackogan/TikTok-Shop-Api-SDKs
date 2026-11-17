from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.change_post_view_search_video_products_response_data_product_result_item import ChangePostViewSearchVideoProductsResponseDataProductResultItem





T = TypeVar("T", bound="ChangePostViewSearchVideoProductsResponseDataProductResult")



@_attrs_define
class ChangePostViewSearchVideoProductsResponseDataProductResult:
    """ 
        Attributes:
            items (list[ChangePostViewSearchVideoProductsResponseDataProductResultItem] | Unset): One result for each
                submitted product.
            status (str | Unset): Business result: UNSPECIFIED means no known outcome; SUCCEEDED means completed;
                PARTIAL_FAILED means some changes failed; FAILED means the requested change failed.
     """

    items: list[ChangePostViewSearchVideoProductsResponseDataProductResultItem] | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.change_post_view_search_video_products_response_data_product_result_item import ChangePostViewSearchVideoProductsResponseDataProductResultItem # noqa: PLC0415
        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_post_view_search_video_products_response_data_product_result_item import ChangePostViewSearchVideoProductsResponseDataProductResultItem # noqa: PLC0415
        d = dict(src_dict)
        _items = d.pop("items", UNSET)
        items: list[ChangePostViewSearchVideoProductsResponseDataProductResultItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = ChangePostViewSearchVideoProductsResponseDataProductResultItem.from_dict(items_item_data)



                items.append(items_item)


        status = d.pop("status", UNSET)

        change_post_view_search_video_products_response_data_product_result = cls(
            items=items,
            status=status,
        )


        change_post_view_search_video_products_response_data_product_result.additional_properties = d
        return change_post_view_search_video_products_response_data_product_result

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
