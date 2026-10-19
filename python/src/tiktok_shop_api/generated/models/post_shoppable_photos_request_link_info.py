from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_shoppable_photos_request_link_info_link import PostShoppablePhotosRequestLinkInfoLink
    from ..models.post_shoppable_photos_request_link_info_shop_info import PostShoppablePhotosRequestLinkInfoShopInfo


T = TypeVar("T", bound="PostShoppablePhotosRequestLinkInfo")


@_attrs_define
class PostShoppablePhotosRequestLinkInfo:
    """
    Attributes:
        post_type (str): 1-LINK_TO_PRODUCT, 2-LINK_TO_SHOP, 3-LINK_TO_ONE_PIC_ONE_PRODUCT
        shop_info (PostShoppablePhotosRequestLinkInfoShopInfo | Unset):
        links (list[PostShoppablePhotosRequestLinkInfoLink] | Unset): Photo Anchor List
    """

    post_type: str
    shop_info: PostShoppablePhotosRequestLinkInfoShopInfo | Unset = UNSET
    links: list[PostShoppablePhotosRequestLinkInfoLink] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post_type = self.post_type

        shop_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shop_info, Unset):
            shop_info = self.shop_info.to_dict()

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "post_type": post_type,
            }
        )
        if shop_info is not UNSET:
            field_dict["shop_info"] = shop_info
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_shoppable_photos_request_link_info_link import (
            PostShoppablePhotosRequestLinkInfoLink,  # noqa: PLC0415
        )
        from ..models.post_shoppable_photos_request_link_info_shop_info import (
            PostShoppablePhotosRequestLinkInfoShopInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        post_type = d.pop("post_type")

        _shop_info = d.pop("shop_info", UNSET)
        shop_info: PostShoppablePhotosRequestLinkInfoShopInfo | Unset
        if isinstance(_shop_info, Unset):
            shop_info = UNSET
        else:
            shop_info = PostShoppablePhotosRequestLinkInfoShopInfo.from_dict(_shop_info)

        _links = d.pop("links", UNSET)
        links: list[PostShoppablePhotosRequestLinkInfoLink] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = PostShoppablePhotosRequestLinkInfoLink.from_dict(links_item_data)

                links.append(links_item)

        post_shoppable_photos_request_link_info = cls(
            post_type=post_type,
            shop_info=shop_info,
            links=links,
        )

        post_shoppable_photos_request_link_info.additional_properties = d
        return post_shoppable_photos_request_link_info

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
