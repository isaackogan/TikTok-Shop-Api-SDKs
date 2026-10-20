from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_shoppable_video_request_video_info import PostShoppableVideoRequestVideoInfo
    from ..models.product_link_info import ProductLinkInfo


T = TypeVar("T", bound="PostShoppableVideoRequest")


@_attrs_define
class PostShoppableVideoRequest:
    """
    Attributes:
        video_info (PostShoppableVideoRequestVideoInfo):
        product_link_info (ProductLinkInfo):
    """

    video_info: PostShoppableVideoRequestVideoInfo
    product_link_info: ProductLinkInfo
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        video_info = self.video_info.to_dict()

        product_link_info = self.product_link_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "video_info": video_info,
                "product_link_info": product_link_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_shoppable_video_request_video_info import PostShoppableVideoRequestVideoInfo  # noqa: PLC0415
        from ..models.product_link_info import ProductLinkInfo  # noqa: PLC0415

        d = dict(src_dict)
        video_info = PostShoppableVideoRequestVideoInfo.from_dict(d.pop("video_info"))

        product_link_info = ProductLinkInfo.from_dict(d.pop("product_link_info"))

        post_shoppable_video_request = cls(
            video_info=video_info,
            product_link_info=product_link_info,
        )

        post_shoppable_video_request.additional_properties = d
        return post_shoppable_video_request

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
