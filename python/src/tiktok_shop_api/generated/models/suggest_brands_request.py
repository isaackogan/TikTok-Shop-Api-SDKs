from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.diagnose_and_optimize_product_request_size_chart_image import DiagnoseAndOptimizeProductRequestSizeChartImage





T = TypeVar("T", bound="SuggestBrandsRequest")



@_attrs_define
class SuggestBrandsRequest:
    """ 
        Attributes:
            product_title (str): The product title used to recommend brands.
            category_id (str | Unset): TikTok Shop category ID. Optional.
            description (str | Unset): The product description. Optional.
            images (list[DiagnoseAndOptimizeProductRequestSizeChartImage] | Unset): Product images. Optional. The
                recommendation service currently uses the first image.
     """

    product_title: str
    category_id: str | Unset = UNSET
    description: str | Unset = UNSET
    images: list[DiagnoseAndOptimizeProductRequestSizeChartImage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.diagnose_and_optimize_product_request_size_chart_image import DiagnoseAndOptimizeProductRequestSizeChartImage # noqa: PLC0415
        product_title = self.product_title

        category_id = self.category_id

        description = self.description

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "product_title": product_title,
        })
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if description is not UNSET:
            field_dict["description"] = description
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnose_and_optimize_product_request_size_chart_image import DiagnoseAndOptimizeProductRequestSizeChartImage # noqa: PLC0415
        d = dict(src_dict)
        product_title = d.pop("product_title")

        category_id = d.pop("category_id", UNSET)

        description = d.pop("description", UNSET)

        _images = d.pop("images", UNSET)
        images: list[DiagnoseAndOptimizeProductRequestSizeChartImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = DiagnoseAndOptimizeProductRequestSizeChartImage.from_dict(images_item_data)



                images.append(images_item)


        suggest_brands_request = cls(
            product_title=product_title,
            category_id=category_id,
            description=description,
            images=images,
        )


        suggest_brands_request.additional_properties = d
        return suggest_brands_request

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
