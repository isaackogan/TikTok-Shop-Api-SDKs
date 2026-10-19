from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_shop_product_performance_detail_response_data_performance_top_content_type import (
    GetShopProductPerformanceDetailResponseDataPerformanceTopContentType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_shop_product_performance_detail_response_data_performance_top_content_content import (
        GetShopProductPerformanceDetailResponseDataPerformanceTopContentContent,
    )


T = TypeVar("T", bound="GetShopProductPerformanceDetailResponseDataPerformanceTopContent")


@_attrs_define
class GetShopProductPerformanceDetailResponseDataPerformanceTopContent:
    """
    Attributes:
        type_ (GetShopProductPerformanceDetailResponseDataPerformanceTopContentType | Unset): Top content type.
            Possible values:
            - LIVE: Live stream content.
            - VIDEO: Video content.
        contents (list[GetShopProductPerformanceDetailResponseDataPerformanceTopContentContent] | Unset): Content
            details
    """

    type_: GetShopProductPerformanceDetailResponseDataPerformanceTopContentType | Unset = UNSET
    contents: list[GetShopProductPerformanceDetailResponseDataPerformanceTopContentContent] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        contents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contents, Unset):
            contents = []
            for contents_item_data in self.contents:
                contents_item = contents_item_data.to_dict()
                contents.append(contents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if contents is not UNSET:
            field_dict["contents"] = contents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_product_performance_detail_response_data_performance_top_content_content import (
            GetShopProductPerformanceDetailResponseDataPerformanceTopContentContent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: GetShopProductPerformanceDetailResponseDataPerformanceTopContentType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GetShopProductPerformanceDetailResponseDataPerformanceTopContentType(_type_)

        _contents = d.pop("contents", UNSET)
        contents: list[GetShopProductPerformanceDetailResponseDataPerformanceTopContentContent] | Unset = UNSET
        if _contents is not UNSET:
            contents = []
            for contents_item_data in _contents:
                contents_item = GetShopProductPerformanceDetailResponseDataPerformanceTopContentContent.from_dict(
                    contents_item_data
                )

                contents.append(contents_item)

        get_shop_product_performance_detail_response_data_performance_top_content = cls(
            type_=type_,
            contents=contents,
        )

        get_shop_product_performance_detail_response_data_performance_top_content.additional_properties = d
        return get_shop_product_performance_detail_response_data_performance_top_content

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
