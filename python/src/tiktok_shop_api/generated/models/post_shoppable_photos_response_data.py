from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.post_shoppable_photos_response_data_photo import PostShoppablePhotosResponseDataPhoto





T = TypeVar("T", bound="PostShoppablePhotosResponseData")



@_attrs_define
class PostShoppablePhotosResponseData:
    """ 
        Attributes:
            photo (PostShoppablePhotosResponseDataPhoto | Unset):
            quota (str | Unset): Content posting quota for the creator. Returned on successful publish; included in the
                error message on failure; omitted if no quota restriction applies.
     """

    photo: PostShoppablePhotosResponseDataPhoto | Unset = UNSET
    quota: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_shoppable_photos_response_data_photo import PostShoppablePhotosResponseDataPhoto # noqa: PLC0415
        photo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.photo, Unset):
            photo = self.photo.to_dict()

        quota = self.quota


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if photo is not UNSET:
            field_dict["photo"] = photo
        if quota is not UNSET:
            field_dict["quota"] = quota

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_shoppable_photos_response_data_photo import PostShoppablePhotosResponseDataPhoto # noqa: PLC0415
        d = dict(src_dict)
        _photo = d.pop("photo", UNSET)
        photo: PostShoppablePhotosResponseDataPhoto | Unset
        if isinstance(_photo,  Unset):
            photo = UNSET
        else:
            photo = PostShoppablePhotosResponseDataPhoto.from_dict(_photo)




        quota = d.pop("quota", UNSET)

        post_shoppable_photos_response_data = cls(
            photo=photo,
            quota=quota,
        )


        post_shoppable_photos_response_data.additional_properties = d
        return post_shoppable_photos_response_data

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
