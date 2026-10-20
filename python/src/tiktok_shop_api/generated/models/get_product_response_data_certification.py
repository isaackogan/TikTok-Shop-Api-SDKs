from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_product_response_data_certification_file import GetProductResponseDataCertificationFile
  from ..models.get_product_response_data_certification_image import GetProductResponseDataCertificationImage





T = TypeVar("T", bound="GetProductResponseDataCertification")



@_attrs_define
class GetProductResponseDataCertification:
    """ 
        Attributes:
            expiration_date (int | Unset): The expiration date of this certification expressed in unix timestamp (seconds)
                UTC+0.
            files (list[GetProductResponseDataCertificationFile] | Unset): A list of certification related files.
            id (str | Unset): The ID to identify the type of certification required for the product.
            images (list[GetProductResponseDataCertificationImage] | Unset): A list of certification related images.
            title (str | Unset): The title of the certification type.
     """

    expiration_date: int | Unset = UNSET
    files: list[GetProductResponseDataCertificationFile] | Unset = UNSET
    id: str | Unset = UNSET
    images: list[GetProductResponseDataCertificationImage] | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_product_response_data_certification_file import GetProductResponseDataCertificationFile # noqa: PLC0415
        from ..models.get_product_response_data_certification_image import GetProductResponseDataCertificationImage # noqa: PLC0415
        expiration_date = self.expiration_date

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)



        id = self.id

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)



        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if files is not UNSET:
            field_dict["files"] = files
        if id is not UNSET:
            field_dict["id"] = id
        if images is not UNSET:
            field_dict["images"] = images
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_response_data_certification_file import GetProductResponseDataCertificationFile # noqa: PLC0415
        from ..models.get_product_response_data_certification_image import GetProductResponseDataCertificationImage # noqa: PLC0415
        d = dict(src_dict)
        expiration_date = d.pop("expiration_date", UNSET)

        _files = d.pop("files", UNSET)
        files: list[GetProductResponseDataCertificationFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = GetProductResponseDataCertificationFile.from_dict(files_item_data)



                files.append(files_item)


        id = d.pop("id", UNSET)

        _images = d.pop("images", UNSET)
        images: list[GetProductResponseDataCertificationImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = GetProductResponseDataCertificationImage.from_dict(images_item_data)



                images.append(images_item)


        title = d.pop("title", UNSET)

        get_product_response_data_certification = cls(
            expiration_date=expiration_date,
            files=files,
            id=id,
            images=images,
            title=title,
        )


        get_product_response_data_certification.additional_properties = d
        return get_product_response_data_certification

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
