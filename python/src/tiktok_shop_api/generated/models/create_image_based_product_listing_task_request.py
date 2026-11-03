from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_image_based_product_listing_task_request_scene import CreateImageBasedProductListingTaskRequestScene
from typing import cast

if TYPE_CHECKING:
  from ..models.image import Image





T = TypeVar("T", bound="CreateImageBasedProductListingTaskRequest")



@_attrs_define
class CreateImageBasedProductListingTaskRequest:
    """ 
        Attributes:
            category_id (str): The ID of the leaf category selected for the product.
            images (list[Image]): Exactly one product image used for the image-based product listing task. Do not include an
                image containing personal data.
            product_title (str): Product title used to predict product properties. Do not include personal data.
            scene (CreateImageBasedProductListingTaskRequestScene): Scene of the image-based product listing task.
                Possible values:
                - `PROPERTY_RECOMMENDATION`: Recommends product properties and values.
     """

    category_id: str
    images: list[Image]
    product_title: str
    scene: CreateImageBasedProductListingTaskRequestScene
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.image import Image # noqa: PLC0415
        category_id = self.category_id

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)



        product_title = self.product_title

        scene = self.scene.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "category_id": category_id,
            "images": images,
            "product_title": product_title,
            "scene": scene,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image import Image # noqa: PLC0415
        d = dict(src_dict)
        category_id = d.pop("category_id")

        images = []
        _images = d.pop("images")
        for images_item_data in (_images):
            images_item = Image.from_dict(images_item_data)



            images.append(images_item)


        product_title = d.pop("product_title")

        scene = CreateImageBasedProductListingTaskRequestScene(d.pop("scene"))




        create_image_based_product_listing_task_request = cls(
            category_id=category_id,
            images=images,
            product_title=product_title,
            scene=scene,
        )


        create_image_based_product_listing_task_request.additional_properties = d
        return create_image_based_product_listing_task_request

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
