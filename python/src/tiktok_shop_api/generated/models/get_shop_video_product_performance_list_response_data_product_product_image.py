from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetShopVideoProductPerformanceListResponseDataProductProductImage")



@_attrs_define
class GetShopVideoProductPerformanceListResponseDataProductProductImage:
    """ 
        Attributes:
            thumb_uri (str | Unset): URI of the product thumbnail image.
            thumb_url_list (list[str] | Unset): URLs of the product thumbnail image.
     """

    thumb_uri: str | Unset = UNSET
    thumb_url_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        thumb_uri = self.thumb_uri

        thumb_url_list: list[str] | Unset = UNSET
        if not isinstance(self.thumb_url_list, Unset):
            thumb_url_list = self.thumb_url_list




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if thumb_uri is not UNSET:
            field_dict["thumb_uri"] = thumb_uri
        if thumb_url_list is not UNSET:
            field_dict["thumb_url_list"] = thumb_url_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        thumb_uri = d.pop("thumb_uri", UNSET)

        thumb_url_list = cast(list[str], d.pop("thumb_url_list", UNSET))


        get_shop_video_product_performance_list_response_data_product_product_image = cls(
            thumb_uri=thumb_uri,
            thumb_url_list=thumb_url_list,
        )


        get_shop_video_product_performance_list_response_data_product_product_image.additional_properties = d
        return get_shop_video_product_performance_list_response_data_product_product_image

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
