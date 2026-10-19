from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostShoppablePhotosRequestLinkInfoShopInfo")


@_attrs_define
class PostShoppablePhotosRequestLinkInfoShopInfo:
    """
    Attributes:
        shop_id (str | Unset): Shop ID
        group_type (str | Unset): 1 for shop_home_page, 2 for category, 3 for collection
        group_id (str | Unset): Category ID/Collection ID. Use [Get Shop Category And Collection] to retrieve a valid
            category_id or collection_id, then set it in this field
    """

    shop_id: str | Unset = UNSET
    group_type: str | Unset = UNSET
    group_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shop_id = self.shop_id

        group_type = self.group_type

        group_id = self.group_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shop_id is not UNSET:
            field_dict["shop_id"] = shop_id
        if group_type is not UNSET:
            field_dict["group_type"] = group_type
        if group_id is not UNSET:
            field_dict["group_id"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shop_id = d.pop("shop_id", UNSET)

        group_type = d.pop("group_type", UNSET)

        group_id = d.pop("group_id", UNSET)

        post_shoppable_photos_request_link_info_shop_info = cls(
            shop_id=shop_id,
            group_type=group_type,
            group_id=group_id,
        )

        post_shoppable_photos_request_link_info_shop_info.additional_properties = d
        return post_shoppable_photos_request_link_info_shop_info

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
