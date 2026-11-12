from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="Material")



@_attrs_define
class Material:
    """ 
        Attributes:
            uri (str): The TOS URI of the uploaded image material.
            expire_time (datetime.datetime | Unset): The expiration time in RFC 3339 format. Omit this field when the
                material never expires.
            image_description (str | Unset): The seller-provided description of the material.
     """

    uri: str
    expire_time: datetime.datetime | Unset = UNSET
    image_description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        uri = self.uri

        expire_time: str | Unset = UNSET
        if not isinstance(self.expire_time, Unset):
            expire_time = self.expire_time.isoformat()

        image_description = self.image_description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "uri": uri,
        })
        if expire_time is not UNSET:
            field_dict["expire_time"] = expire_time
        if image_description is not UNSET:
            field_dict["image_description"] = image_description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uri = d.pop("uri")

        _expire_time = d.pop("expire_time", UNSET)
        expire_time: datetime.datetime | Unset
        if isinstance(_expire_time,  Unset):
            expire_time = UNSET
        else:
            expire_time = datetime.datetime.fromisoformat(_expire_time)




        image_description = d.pop("image_description", UNSET)

        material = cls(
            uri=uri,
            expire_time=expire_time,
            image_description=image_description,
        )


        material.additional_properties = d
        return material

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
