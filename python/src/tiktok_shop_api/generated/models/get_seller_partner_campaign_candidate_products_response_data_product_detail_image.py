from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage")



@_attrs_define
class GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage:
    """ 
        Attributes:
            height (int | Unset): Original image height in pixels.
            thumb_uri (str | Unset): Internal resource URI of the image thumbnail.
            thumb_url_list (list[str] | Unset): URLs for the image thumbnail.
            uri (str | Unset): Internal resource URI of the image. It is distinct from a publicly accessible image URL.
            url_list (list[str] | Unset): URLs for the image.
            width (int | Unset): Original image width in pixels.
     """

    height: int | Unset = UNSET
    thumb_uri: str | Unset = UNSET
    thumb_url_list: list[str] | Unset = UNSET
    uri: str | Unset = UNSET
    url_list: list[str] | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        height = self.height

        thumb_uri = self.thumb_uri

        thumb_url_list: list[str] | Unset = UNSET
        if not isinstance(self.thumb_url_list, Unset):
            thumb_url_list = self.thumb_url_list



        uri = self.uri

        url_list: list[str] | Unset = UNSET
        if not isinstance(self.url_list, Unset):
            url_list = self.url_list



        width = self.width


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if height is not UNSET:
            field_dict["height"] = height
        if thumb_uri is not UNSET:
            field_dict["thumb_uri"] = thumb_uri
        if thumb_url_list is not UNSET:
            field_dict["thumb_url_list"] = thumb_url_list
        if uri is not UNSET:
            field_dict["uri"] = uri
        if url_list is not UNSET:
            field_dict["url_list"] = url_list
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height", UNSET)

        thumb_uri = d.pop("thumb_uri", UNSET)

        thumb_url_list = cast(list[str], d.pop("thumb_url_list", UNSET))


        uri = d.pop("uri", UNSET)

        url_list = cast(list[str], d.pop("url_list", UNSET))


        width = d.pop("width", UNSET)

        get_seller_partner_campaign_candidate_products_response_data_product_detail_image = cls(
            height=height,
            thumb_uri=thumb_uri,
            thumb_url_list=thumb_url_list,
            uri=uri,
            url_list=url_list,
            width=width,
        )


        get_seller_partner_campaign_candidate_products_response_data_product_detail_image.additional_properties = d
        return get_seller_partner_campaign_candidate_products_response_data_product_detail_image

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
