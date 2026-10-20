from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.optimize_images_request_image import OptimizeImagesRequestImage





T = TypeVar("T", bound="OptimizeImagesRequest")



@_attrs_define
class OptimizeImagesRequest:
    """ 
        Attributes:
            images (list[OptimizeImagesRequestImage] | Unset): The list of images to be optimized.
                Use the [Upload Product Image API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22) to upload
                the images first and obtain the corresponding image URIs.
                Max count: 200
     """

    images: list[OptimizeImagesRequestImage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.optimize_images_request_image import OptimizeImagesRequestImage # noqa: PLC0415
        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.optimize_images_request_image import OptimizeImagesRequestImage # noqa: PLC0415
        d = dict(src_dict)
        _images = d.pop("images", UNSET)
        images: list[OptimizeImagesRequestImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = OptimizeImagesRequestImage.from_dict(images_item_data)



                images.append(images_item)


        optimize_images_request = cls(
            images=images,
        )


        optimize_images_request.additional_properties = d
        return optimize_images_request

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
