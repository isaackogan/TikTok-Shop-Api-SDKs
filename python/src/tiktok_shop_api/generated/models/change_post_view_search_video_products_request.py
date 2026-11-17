from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.change_post_view_search_video_products_request_operation import ChangePostViewSearchVideoProductsRequestOperation





T = TypeVar("T", bound="ChangePostViewSearchVideoProductsRequest")



@_attrs_define
class ChangePostViewSearchVideoProductsRequest:
    """ 
        Attributes:
            operations (list[ChangePostViewSearchVideoProductsRequestOperation]): Product association changes. Each product
                must occur only once.
     """

    operations: list[ChangePostViewSearchVideoProductsRequestOperation]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.change_post_view_search_video_products_request_operation import ChangePostViewSearchVideoProductsRequestOperation # noqa: PLC0415
        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.to_dict()
            operations.append(operations_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "operations": operations,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_post_view_search_video_products_request_operation import ChangePostViewSearchVideoProductsRequestOperation # noqa: PLC0415
        d = dict(src_dict)
        operations = []
        _operations = d.pop("operations")
        for operations_item_data in (_operations):
            operations_item = ChangePostViewSearchVideoProductsRequestOperation.from_dict(operations_item_data)



            operations.append(operations_item)


        change_post_view_search_video_products_request = cls(
            operations=operations,
        )


        change_post_view_search_video_products_request.additional_properties = d
        return change_post_view_search_video_products_request

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
