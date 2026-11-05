from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailRejectedReason")



@_attrs_define
class GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailRejectedReason:
    """ 
        Attributes:
            default_text (str | Unset): Default display text for the product rejection reason.
            starling_key (str | Unset): Internal localization key identifying the product rejection message.
     """

    default_text: str | Unset = UNSET
    starling_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        default_text = self.default_text

        starling_key = self.starling_key


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if default_text is not UNSET:
            field_dict["default_text"] = default_text
        if starling_key is not UNSET:
            field_dict["starling_key"] = starling_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        default_text = d.pop("default_text", UNSET)

        starling_key = d.pop("starling_key", UNSET)

        get_seller_partner_campaign_registered_products_response_data_product_detail_rejected_reason = cls(
            default_text=default_text,
            starling_key=starling_key,
        )


        get_seller_partner_campaign_registered_products_response_data_product_detail_rejected_reason.additional_properties = d
        return get_seller_partner_campaign_registered_products_response_data_product_detail_rejected_reason

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
