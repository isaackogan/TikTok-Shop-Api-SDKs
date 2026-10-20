from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetBestsellingVideosResponseDataVideoProductInfo")



@_attrs_define
class GetBestsellingVideosResponseDataVideoProductInfo:
    """ 
        Attributes:
            product_id (str | Unset): Product ID in the product anchor. Excludes deactivated and sold-out products.
            product_name (str | Unset): Product name in the product anchor. Deactivated and sold-out products are excluded.
     """

    product_id: str | Unset = UNSET
    product_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        product_name = self.product_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        product_name = d.pop("product_name", UNSET)

        get_bestselling_videos_response_data_video_product_info = cls(
            product_id=product_id,
            product_name=product_name,
        )


        get_bestselling_videos_response_data_video_product_info.additional_properties = d
        return get_bestselling_videos_response_data_video_product_info

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
