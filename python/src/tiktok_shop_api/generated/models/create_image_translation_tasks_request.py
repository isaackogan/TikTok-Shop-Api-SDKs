from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.create_image_translation_tasks_request_image import CreateImageTranslationTasksRequestImage





T = TypeVar("T", bound="CreateImageTranslationTasksRequest")



@_attrs_define
class CreateImageTranslationTasksRequest:
    """ 
        Attributes:
            images (list[CreateImageTranslationTasksRequestImage]): The list of images to translate.
                Use the [Upload Product Image API](https://partner.tiktokshop.com/docv2/page/6509df95defece02be598a22) to upload
                the images first and obtain the corresponding image URIs.

                **Note**: A request can contain at most 20 image URI and target language combinations in total. The
                recommendations to specify up to 5 images and up to 20 target languages are not independent limits that can be
                used together; the total number of combinations must remain 20 or fewer. For example, you can submit 10 images
                with 2 target languages each, but you can't submit 10 images with 5 target languages each.
     """

    images: list[CreateImageTranslationTasksRequestImage]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_image_translation_tasks_request_image import CreateImageTranslationTasksRequestImage # noqa: PLC0415
        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "images": images,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_image_translation_tasks_request_image import CreateImageTranslationTasksRequestImage # noqa: PLC0415
        d = dict(src_dict)
        images = []
        _images = d.pop("images")
        for images_item_data in (_images):
            images_item = CreateImageTranslationTasksRequestImage.from_dict(images_item_data)



            images.append(images_item)


        create_image_translation_tasks_request = cls(
            images=images,
        )


        create_image_translation_tasks_request.additional_properties = d
        return create_image_translation_tasks_request

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
