from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_global_product_response_data_certification_file import GetGlobalProductResponseDataCertificationFile
  from ..models.get_global_product_response_data_certification_image import GetGlobalProductResponseDataCertificationImage





T = TypeVar("T", bound="GetGlobalProductResponseDataCertification")



@_attrs_define
class GetGlobalProductResponseDataCertification:
    """ 
        Attributes:
            id (str | Unset): The ID to identify the type of certification required for the product category.
            title (str | Unset): The title of the certification type.
            files (list[GetGlobalProductResponseDataCertificationFile] | Unset): A list of certification related files.
            images (list[GetGlobalProductResponseDataCertificationImage] | Unset): A list of certification related images.
     """

    id: str | Unset = UNSET
    title: str | Unset = UNSET
    files: list[GetGlobalProductResponseDataCertificationFile] | Unset = UNSET
    images: list[GetGlobalProductResponseDataCertificationImage] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_global_product_response_data_certification_file import GetGlobalProductResponseDataCertificationFile # noqa: PLC0415
        from ..models.get_global_product_response_data_certification_image import GetGlobalProductResponseDataCertificationImage # noqa: PLC0415
        id = self.id

        title = self.title

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)



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
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if files is not UNSET:
            field_dict["files"] = files
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_global_product_response_data_certification_file import GetGlobalProductResponseDataCertificationFile # noqa: PLC0415
        from ..models.get_global_product_response_data_certification_image import GetGlobalProductResponseDataCertificationImage # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        _files = d.pop("files", UNSET)
        files: list[GetGlobalProductResponseDataCertificationFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = GetGlobalProductResponseDataCertificationFile.from_dict(files_item_data)



                files.append(files_item)


        _images = d.pop("images", UNSET)
        images: list[GetGlobalProductResponseDataCertificationImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = GetGlobalProductResponseDataCertificationImage.from_dict(images_item_data)



                images.append(images_item)


        get_global_product_response_data_certification = cls(
            id=id,
            title=title,
            files=files,
            images=images,
        )


        get_global_product_response_data_certification.additional_properties = d
        return get_global_product_response_data_certification

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
