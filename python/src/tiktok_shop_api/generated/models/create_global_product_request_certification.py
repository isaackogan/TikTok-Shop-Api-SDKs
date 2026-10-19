from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file import File
    from ..models.image import Image


T = TypeVar("T", bound="CreateGlobalProductRequestCertification")


@_attrs_define
class CreateGlobalProductRequestCertification:
    """
    Attributes:
        id (str): The ID to identify the type of certification required for the product category.
            Retrieve this value from the [Get Global Category Rules
            API](https://partner.tiktokshop.com/docv2/page/650a056df1fd3102b91b5b8e).
        images (list[Image] | Unset): A list of certification related images.
        files (list[File] | Unset): A list of certification related files.
    """

    id: str
    images: list[Image] | Unset = UNSET
    files: list[File] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if images is not UNSET:
            field_dict["images"] = images
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file import File  # noqa: PLC0415
        from ..models.image import Image  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        _images = d.pop("images", UNSET)
        images: list[Image] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = Image.from_dict(images_item_data)

                images.append(images_item)

        _files = d.pop("files", UNSET)
        files: list[File] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = File.from_dict(files_item_data)

                files.append(files_item)

        create_global_product_request_certification = cls(
            id=id,
            images=images,
            files=files,
        )

        create_global_product_request_certification.additional_properties = d
        return create_global_product_request_certification

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
