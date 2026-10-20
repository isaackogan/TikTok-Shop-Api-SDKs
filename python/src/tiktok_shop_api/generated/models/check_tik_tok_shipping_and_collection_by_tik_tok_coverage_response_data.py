from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CheckTikTokShippingAndCollectionByTikTokCoverageResponseData")



@_attrs_define
class CheckTikTokShippingAndCollectionByTikTokCoverageResponseData:
    """ 
        Attributes:
            is_tiktok_shipping (bool | Unset): Indicates whether the tracking number is covered by TikTok Shipping (TTS).
            is_tiktok_collection (bool | Unset): Indicates whether the tracking number is covered by Collection by TikTok
                (CBT).
     """

    is_tiktok_shipping: bool | Unset = UNSET
    is_tiktok_collection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        is_tiktok_shipping = self.is_tiktok_shipping

        is_tiktok_collection = self.is_tiktok_collection


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_tiktok_shipping is not UNSET:
            field_dict["is_tiktok_shipping"] = is_tiktok_shipping
        if is_tiktok_collection is not UNSET:
            field_dict["is_tiktok_collection"] = is_tiktok_collection

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_tiktok_shipping = d.pop("is_tiktok_shipping", UNSET)

        is_tiktok_collection = d.pop("is_tiktok_collection", UNSET)

        check_tik_tok_shipping_and_collection_by_tik_tok_coverage_response_data = cls(
            is_tiktok_shipping=is_tiktok_shipping,
            is_tiktok_collection=is_tiktok_collection,
        )


        check_tik_tok_shipping_and_collection_by_tik_tok_coverage_response_data.additional_properties = d
        return check_tik_tok_shipping_and_collection_by_tik_tok_coverage_response_data

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
