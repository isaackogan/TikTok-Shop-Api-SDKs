from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="GetSellerCarouselPermissionResponseData")



@_attrs_define
class GetSellerCarouselPermissionResponseData:
    """ 
        Attributes:
            has_auto_post_permission (bool): Whether the currently authorized seller has auto-post permission for carousel
                publishing.
            has_photo_mode_permission (bool): Whether the currently authorized seller has photo mode permission for carousel
                publishing.
     """

    has_auto_post_permission: bool
    has_photo_mode_permission: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        has_auto_post_permission = self.has_auto_post_permission

        has_photo_mode_permission = self.has_photo_mode_permission


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "has_auto_post_permission": has_auto_post_permission,
            "has_photo_mode_permission": has_photo_mode_permission,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_auto_post_permission = d.pop("has_auto_post_permission")

        has_photo_mode_permission = d.pop("has_photo_mode_permission")

        get_seller_carousel_permission_response_data = cls(
            has_auto_post_permission=has_auto_post_permission,
            has_photo_mode_permission=has_photo_mode_permission,
        )


        get_seller_carousel_permission_response_data.additional_properties = d
        return get_seller_carousel_permission_response_data

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
