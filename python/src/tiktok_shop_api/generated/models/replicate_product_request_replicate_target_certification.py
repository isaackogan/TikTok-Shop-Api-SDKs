from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.image import Image
  from ..models.replicate_product_request_replicate_target_certification_file import ReplicateProductRequestReplicateTargetCertificationFile





T = TypeVar("T", bound="ReplicateProductRequestReplicateTargetCertification")



@_attrs_define
class ReplicateProductRequestReplicateTargetCertification:
    """ 
        Attributes:
            id (str): The ID to identify the type of certification required for the product category.
                Retrieve this value from the [Get Category Rules
                API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9).
            expiration_date (int | Unset): The expiration date of this certification expressed in unix timestamp (seconds)
                UTC+0.
                This field may be required for certain certifications. Use the [Get Category Rules
                API](https://partner.tiktokshop.com/docv2/page/6509c0febace3e02b74594a9) to find out the requirements.
            files (list[ReplicateProductRequestReplicateTargetCertificationFile] | Unset): A list of certification related
                files.
            images (list[Image] | Unset): A list of certification related images.
     """

    id: str
    expiration_date: int | Unset = UNSET
    files: list[ReplicateProductRequestReplicateTargetCertificationFile] | Unset = UNSET
    images: list[Image] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.image import Image # noqa: PLC0415
        from ..models.replicate_product_request_replicate_target_certification_file import ReplicateProductRequestReplicateTargetCertificationFile # noqa: PLC0415
        id = self.id

        expiration_date = self.expiration_date

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
            "id": id,
        })
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if files is not UNSET:
            field_dict["files"] = files
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image import Image # noqa: PLC0415
        from ..models.replicate_product_request_replicate_target_certification_file import ReplicateProductRequestReplicateTargetCertificationFile # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id")

        expiration_date = d.pop("expiration_date", UNSET)

        _files = d.pop("files", UNSET)
        files: list[ReplicateProductRequestReplicateTargetCertificationFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = ReplicateProductRequestReplicateTargetCertificationFile.from_dict(files_item_data)



                files.append(files_item)


        _images = d.pop("images", UNSET)
        images: list[Image] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = Image.from_dict(images_item_data)



                images.append(images_item)


        replicate_product_request_replicate_target_certification = cls(
            id=id,
            expiration_date=expiration_date,
            files=files,
            images=images,
        )


        replicate_product_request_replicate_target_certification.additional_properties = d
        return replicate_product_request_replicate_target_certification

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
