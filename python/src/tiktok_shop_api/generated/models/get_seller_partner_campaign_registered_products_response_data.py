from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_seller_partner_campaign_registered_products_response_data_product_detail import GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetail





T = TypeVar("T", bound="GetSellerPartnerCampaignRegisteredProductsResponseData")



@_attrs_define
class GetSellerPartnerCampaignRegisteredProductsResponseData:
    """ 
        Attributes:
            next_page_token (str): Pass this token unchanged to retrieve the next page. Empty when no further page is
                available within the supported query window.
            closed_num (int | Unset): Number of closed registrations.
            ongoing_num (int | Unset): Number of ongoing registrations.
            pending_num (int | Unset): Number of pending registrations.
            product_details (list[GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetail] | Unset):
                Registration records for the current campaign and authorized seller.
            rejected_num (int | Unset): Number of rejected registrations.
            total_num (int | Unset): Total matching registrations, not the number in this page.
     """

    next_page_token: str
    closed_num: int | Unset = UNSET
    ongoing_num: int | Unset = UNSET
    pending_num: int | Unset = UNSET
    product_details: list[GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetail] | Unset = UNSET
    rejected_num: int | Unset = UNSET
    total_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_seller_partner_campaign_registered_products_response_data_product_detail import GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetail # noqa: PLC0415
        next_page_token = self.next_page_token

        closed_num = self.closed_num

        ongoing_num = self.ongoing_num

        pending_num = self.pending_num

        product_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_details, Unset):
            product_details = []
            for product_details_item_data in self.product_details:
                product_details_item = product_details_item_data.to_dict()
                product_details.append(product_details_item)



        rejected_num = self.rejected_num

        total_num = self.total_num


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "next_page_token": next_page_token,
        })
        if closed_num is not UNSET:
            field_dict["closed_num"] = closed_num
        if ongoing_num is not UNSET:
            field_dict["ongoing_num"] = ongoing_num
        if pending_num is not UNSET:
            field_dict["pending_num"] = pending_num
        if product_details is not UNSET:
            field_dict["product_details"] = product_details
        if rejected_num is not UNSET:
            field_dict["rejected_num"] = rejected_num
        if total_num is not UNSET:
            field_dict["total_num"] = total_num

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_seller_partner_campaign_registered_products_response_data_product_detail import GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetail # noqa: PLC0415
        d = dict(src_dict)
        next_page_token = d.pop("next_page_token")

        closed_num = d.pop("closed_num", UNSET)

        ongoing_num = d.pop("ongoing_num", UNSET)

        pending_num = d.pop("pending_num", UNSET)

        _product_details = d.pop("product_details", UNSET)
        product_details: list[GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetail] | Unset = UNSET
        if _product_details is not UNSET:
            product_details = []
            for product_details_item_data in _product_details:
                product_details_item = GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetail.from_dict(product_details_item_data)



                product_details.append(product_details_item)


        rejected_num = d.pop("rejected_num", UNSET)

        total_num = d.pop("total_num", UNSET)

        get_seller_partner_campaign_registered_products_response_data = cls(
            next_page_token=next_page_token,
            closed_num=closed_num,
            ongoing_num=ongoing_num,
            pending_num=pending_num,
            product_details=product_details,
            rejected_num=rejected_num,
            total_num=total_num,
        )


        get_seller_partner_campaign_registered_products_response_data.additional_properties = d
        return get_seller_partner_campaign_registered_products_response_data

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
