from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.generate_campaign_product_promotion_links_in_batch_response_data_product_promotion_link import GenerateCampaignProductPromotionLinksInBatchResponseDataProductPromotionLink





T = TypeVar("T", bound="GenerateCampaignProductPromotionLinksInBatchResponseData")



@_attrs_define
class GenerateCampaignProductPromotionLinksInBatchResponseData:
    """ 
        Attributes:
            product_promotion_links (list[GenerateCampaignProductPromotionLinksInBatchResponseDataProductPromotionLink] |
                Unset): The list of products for which the promotion links are generated successfully.
            failed_product_ids (list[str] | Unset): The list of products for which the promotion links failed to be
                generated.
     """

    product_promotion_links: list[GenerateCampaignProductPromotionLinksInBatchResponseDataProductPromotionLink] | Unset = UNSET
    failed_product_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.generate_campaign_product_promotion_links_in_batch_response_data_product_promotion_link import GenerateCampaignProductPromotionLinksInBatchResponseDataProductPromotionLink # noqa: PLC0415
        product_promotion_links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_promotion_links, Unset):
            product_promotion_links = []
            for product_promotion_links_item_data in self.product_promotion_links:
                product_promotion_links_item = product_promotion_links_item_data.to_dict()
                product_promotion_links.append(product_promotion_links_item)



        failed_product_ids: list[str] | Unset = UNSET
        if not isinstance(self.failed_product_ids, Unset):
            failed_product_ids = self.failed_product_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_promotion_links is not UNSET:
            field_dict["product_promotion_links"] = product_promotion_links
        if failed_product_ids is not UNSET:
            field_dict["failed_product_ids"] = failed_product_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generate_campaign_product_promotion_links_in_batch_response_data_product_promotion_link import GenerateCampaignProductPromotionLinksInBatchResponseDataProductPromotionLink # noqa: PLC0415
        d = dict(src_dict)
        _product_promotion_links = d.pop("product_promotion_links", UNSET)
        product_promotion_links: list[GenerateCampaignProductPromotionLinksInBatchResponseDataProductPromotionLink] | Unset = UNSET
        if _product_promotion_links is not UNSET:
            product_promotion_links = []
            for product_promotion_links_item_data in _product_promotion_links:
                product_promotion_links_item = GenerateCampaignProductPromotionLinksInBatchResponseDataProductPromotionLink.from_dict(product_promotion_links_item_data)



                product_promotion_links.append(product_promotion_links_item)


        failed_product_ids = cast(list[str], d.pop("failed_product_ids", UNSET))


        generate_campaign_product_promotion_links_in_batch_response_data = cls(
            product_promotion_links=product_promotion_links,
            failed_product_ids=failed_product_ids,
        )


        generate_campaign_product_promotion_links_in_batch_response_data.additional_properties = d
        return generate_campaign_product_promotion_links_in_batch_response_data

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
