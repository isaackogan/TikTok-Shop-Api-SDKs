from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_seller_partner_campaign_candidate_products_response_data_product_detail import GetSellerPartnerCampaignCandidateProductsResponseDataProductDetail





T = TypeVar("T", bound="GetSellerPartnerCampaignCandidateProductsResponseData")



@_attrs_define
class GetSellerPartnerCampaignCandidateProductsResponseData:
    """ 
        Attributes:
            next_page_token (str): Pass this token unchanged to retrieve the next page. Empty when no further page is
                available within the supported query window.
            product_detail (list[GetSellerPartnerCampaignCandidateProductsResponseDataProductDetail] | Unset): Preserve the
                singular field name from Athena; its value is a list.
            total_num (int | Unset): Total matching candidate products, not the number in this page.
     """

    next_page_token: str
    product_detail: list[GetSellerPartnerCampaignCandidateProductsResponseDataProductDetail] | Unset = UNSET
    total_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_seller_partner_campaign_candidate_products_response_data_product_detail import GetSellerPartnerCampaignCandidateProductsResponseDataProductDetail # noqa: PLC0415
        next_page_token = self.next_page_token

        product_detail: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_detail, Unset):
            product_detail = []
            for product_detail_item_data in self.product_detail:
                product_detail_item = product_detail_item_data.to_dict()
                product_detail.append(product_detail_item)



        total_num = self.total_num


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "next_page_token": next_page_token,
        })
        if product_detail is not UNSET:
            field_dict["product_detail"] = product_detail
        if total_num is not UNSET:
            field_dict["total_num"] = total_num

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_seller_partner_campaign_candidate_products_response_data_product_detail import GetSellerPartnerCampaignCandidateProductsResponseDataProductDetail # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token")

        _product_detail = d.pop("product_detail", UNSET)
        product_detail: list[GetSellerPartnerCampaignCandidateProductsResponseDataProductDetail] | Unset = UNSET
        if _product_detail is not UNSET:
            product_detail = []
            for product_detail_item_data in _product_detail:
                product_detail_item = GetSellerPartnerCampaignCandidateProductsResponseDataProductDetail.from_dict(product_detail_item_data)



                product_detail.append(product_detail_item)


        total_num = d.pop("total_num", UNSET)

        get_seller_partner_campaign_candidate_products_response_data = cls(
            next_page_token=next_page_token,
            product_detail=product_detail,
            total_num=total_num,
        )


        get_seller_partner_campaign_candidate_products_response_data.additional_properties = d
        return get_seller_partner_campaign_candidate_products_response_data

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
