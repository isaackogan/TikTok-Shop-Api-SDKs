from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenerateCampaignProductPromotionLinksInBatchResponseDataProductPromotionLink")


@_attrs_define
class GenerateCampaignProductPromotionLinksInBatchResponseDataProductPromotionLink:
    """
    Attributes:
        product_id (str | Unset): The ID of the product to promote.
        link (str | Unset): This is the product promotion link that agencies can share with collaborated creators.
            Creators can copy/paste this link into the web browser. Creators will be re-directed to the add-product-link
            page in the Tikotk app. Creators can decide whether to add products to their showcases in the pop-up window.
    """

    product_id: str | Unset = UNSET
    link: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        link = self.link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if link is not UNSET:
            field_dict["link"] = link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        link = d.pop("link", UNSET)

        generate_campaign_product_promotion_links_in_batch_response_data_product_promotion_link = cls(
            product_id=product_id,
            link=link,
        )

        generate_campaign_product_promotion_links_in_batch_response_data_product_promotion_link.additional_properties = d
        return generate_campaign_product_promotion_links_in_batch_response_data_product_promotion_link

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
