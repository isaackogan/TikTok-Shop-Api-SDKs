from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.upload_shoppable_photo_file_response_data_photo_file import UploadShoppablePhotoFileResponseDataPhotoFile





T = TypeVar("T", bound="UploadShoppablePhotoFileResponseData")



@_attrs_define
class UploadShoppablePhotoFileResponseData:
    """ 
        Attributes:
            photo_file (UploadShoppablePhotoFileResponseDataPhotoFile | Unset):
     """

    photo_file: UploadShoppablePhotoFileResponseDataPhotoFile | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.upload_shoppable_photo_file_response_data_photo_file import UploadShoppablePhotoFileResponseDataPhotoFile # noqa: PLC0415
        photo_file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.photo_file, Unset):
            photo_file = self.photo_file.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if photo_file is not UNSET:
            field_dict["photo_file"] = photo_file

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_shoppable_photo_file_response_data_photo_file import UploadShoppablePhotoFileResponseDataPhotoFile # noqa: PLC0415
        d = dict(src_dict)
        _photo_file = d.pop("photo_file", UNSET)
        photo_file: UploadShoppablePhotoFileResponseDataPhotoFile | Unset
        if isinstance(_photo_file,  Unset):
            photo_file = UNSET
        else:
            photo_file = UploadShoppablePhotoFileResponseDataPhotoFile.from_dict(_photo_file)




        upload_shoppable_photo_file_response_data = cls(
            photo_file=photo_file,
        )


        upload_shoppable_photo_file_response_data.additional_properties = d
        return upload_shoppable_photo_file_response_data

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
