from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_affiliate_partner_campaign_product_list_response_data_product import GetAffiliatePartnerCampaignProductListResponseDataProduct





T = TypeVar("T", bound="GetAffiliatePartnerCampaignProductListResponseData")



@_attrs_define
class GetAffiliatePartnerCampaignProductListResponseData:
    """ 
        Attributes:
            products (list[GetAffiliatePartnerCampaignProductListResponseDataProduct] | Unset): The list of products.
            next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. When
                this value is non-empty, pass it as `page_token` in the next request and reuse the same `campaign_id`,
                `category_asset_cipher`, `page_size`, `review_status`, `product_name`, `product_id`, `shop_name`, and
                `category_id` values, including any omitted optional filters. An empty `next_page_token` means there are no more
                pages.
            total_count (int | Unset): The total number of products in the list.
     """

    products: list[GetAffiliatePartnerCampaignProductListResponseDataProduct] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_affiliate_partner_campaign_product_list_response_data_product import GetAffiliatePartnerCampaignProductListResponseDataProduct # noqa: PLC0415
        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)



        next_page_token = self.next_page_token

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if products is not UNSET:
            field_dict["products"] = products
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_affiliate_partner_campaign_product_list_response_data_product import GetAffiliatePartnerCampaignProductListResponseDataProduct # noqa: PLC0415
        d = dict(src_dict)
        _products = d.pop("products", UNSET)
        products: list[GetAffiliatePartnerCampaignProductListResponseDataProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = GetAffiliatePartnerCampaignProductListResponseDataProduct.from_dict(products_item_data)



                products.append(products_item)


        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        get_affiliate_partner_campaign_product_list_response_data = cls(
            products=products,
            next_page_token=next_page_token,
            total_count=total_count,
        )


        get_affiliate_partner_campaign_product_list_response_data.additional_properties = d
        return get_affiliate_partner_campaign_product_list_response_data

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
