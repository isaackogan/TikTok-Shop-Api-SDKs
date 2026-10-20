from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PostShoppablePhotosRequestLinkInfoLink")



@_attrs_define
class PostShoppablePhotosRequestLinkInfoLink:
    """ 
        Attributes:
            product_id (str | Unset): Product ID
            link_title (str | Unset): Photo Anchor Title:The title to be shown on the product anchor. Anchor title should be
                shorter than 30 characters
     """

    product_id: str | Unset = UNSET
    link_title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        link_title = self.link_title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if link_title is not UNSET:
            field_dict["link_title"] = link_title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        link_title = d.pop("link_title", UNSET)

        post_shoppable_photos_request_link_info_link = cls(
            product_id=product_id,
            link_title=link_title,
        )


        post_shoppable_photos_request_link_info_link.additional_properties = d
        return post_shoppable_photos_request_link_info_link

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
