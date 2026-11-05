from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.register_seller_partner_campaign_products_request_campaign_contact_info import RegisterSellerPartnerCampaignProductsRequestCampaignContactInfo





T = TypeVar("T", bound="RegisterSellerPartnerCampaignProductsRequest")



@_attrs_define
class RegisterSellerPartnerCampaignProductsRequest:
    """ 
        Attributes:
            campaign_contact_info (list[RegisterSellerPartnerCampaignProductsRequestCampaignContactInfo]): Authorized seller
                contact entries for this submission. EMAIL is required. Optional WHATSAPP requires region_code; other types are
                rejected. At most one entry per contact type is allowed. Contact values must not be logged or exposed in
                responses.
            product_ids (list[str]): Required. 1-200 unique positive product IDs for one campaign; all products must belong
                to the authorized shop. IDs must fit a signed 64-bit integer.
            total_commission_rate (int): Required. Total commission rate applied to the submitted batch of products,
                expressed as the percentage multiplied by 100 (1500 = 15%). When creator_commission_rate and
                partner_commission_rate are provided, their sum must equal total_commission_rate. Allowed range is 100-8000
                (1%-80%).
            creator_commission_rate (int | Unset): Creator commission rate for the legacy commission model, expressed as the
                percentage multiplied by 100 (900 = 9%). Required together with partner_commission_rate only when
                campaign_detail.version returned by Get Seller Partner Campaign Detail is MVP or omitted. For
                MULTI_CREATOR_COMMISSION, provide total_commission_rate instead. When both split rates are provided,
                creator_commission_rate + partner_commission_rate must equal total_commission_rate. Both split rates must be
                supplied together and each must be between 100 and 7900 (1%-79%).
            partner_commission_rate (int | Unset): Partner commission rate for the legacy commission model, expressed as the
                percentage multiplied by 100 (600 = 6%). Required together with creator_commission_rate only when
                campaign_detail.version returned by Get Seller Partner Campaign Detail is MVP or omitted. For
                MULTI_CREATOR_COMMISSION, provide total_commission_rate instead. When both split rates are provided,
                creator_commission_rate + partner_commission_rate must equal total_commission_rate. Both split rates must be
                supplied together and each must be between 100 and 7900 (1%-79%).
            product_ads_commission_rate (Any | Unset): Product ID -> Ads commission, percentage * 100. Existing Athena range
                is
                100-8000; shop feature permission and campaign/Open Plan thresholds still apply.
                Only keys for products in product_ids are accepted. A subset is allowed;
                omitted products have no ads commission supplied by this request.
            sample_quota (int | Unset): Free-sample quota for each product in the batch, not a per-product map. Optional
                integer from 0 to 100000000; omission preserves the existing default and 0 is allowed.
     """

    campaign_contact_info: list[RegisterSellerPartnerCampaignProductsRequestCampaignContactInfo]
    product_ids: list[str]
    total_commission_rate: int
    creator_commission_rate: int | Unset = UNSET
    partner_commission_rate: int | Unset = UNSET
    product_ads_commission_rate: Any | Unset = UNSET
    sample_quota: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.register_seller_partner_campaign_products_request_campaign_contact_info import RegisterSellerPartnerCampaignProductsRequestCampaignContactInfo # noqa: PLC0415
        campaign_contact_info = []
        for campaign_contact_info_item_data in self.campaign_contact_info:
            campaign_contact_info_item = campaign_contact_info_item_data.to_dict()
            campaign_contact_info.append(campaign_contact_info_item)



        product_ids = self.product_ids



        total_commission_rate = self.total_commission_rate

        creator_commission_rate = self.creator_commission_rate

        partner_commission_rate = self.partner_commission_rate

        product_ads_commission_rate = self.product_ads_commission_rate

        sample_quota = self.sample_quota


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "campaign_contact_info": campaign_contact_info,
            "product_ids": product_ids,
            "total_commission_rate": total_commission_rate,
        })
        if creator_commission_rate is not UNSET:
            field_dict["creator_commission_rate"] = creator_commission_rate
        if partner_commission_rate is not UNSET:
            field_dict["partner_commission_rate"] = partner_commission_rate
        if product_ads_commission_rate is not UNSET:
            field_dict["product_ads_commission_rate"] = product_ads_commission_rate
        if sample_quota is not UNSET:
            field_dict["sample_quota"] = sample_quota

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.register_seller_partner_campaign_products_request_campaign_contact_info import RegisterSellerPartnerCampaignProductsRequestCampaignContactInfo # noqa: PLC0415
        d = dict(src_dict)
        campaign_contact_info = []
        _campaign_contact_info = d.pop("campaign_contact_info")
        for campaign_contact_info_item_data in (_campaign_contact_info):
            campaign_contact_info_item = RegisterSellerPartnerCampaignProductsRequestCampaignContactInfo.from_dict(campaign_contact_info_item_data)



            campaign_contact_info.append(campaign_contact_info_item)


        product_ids = cast(list[str], d.pop("product_ids"))


        total_commission_rate = d.pop("total_commission_rate")

        creator_commission_rate = d.pop("creator_commission_rate", UNSET)

        partner_commission_rate = d.pop("partner_commission_rate", UNSET)

        product_ads_commission_rate = d.pop("product_ads_commission_rate", UNSET)

        sample_quota = d.pop("sample_quota", UNSET)

        register_seller_partner_campaign_products_request = cls(
            campaign_contact_info=campaign_contact_info,
            product_ids=product_ids,
            total_commission_rate=total_commission_rate,
            creator_commission_rate=creator_commission_rate,
            partner_commission_rate=partner_commission_rate,
            product_ads_commission_rate=product_ads_commission_rate,
            sample_quota=sample_quota,
        )


        register_seller_partner_campaign_products_request.additional_properties = d
        return register_seller_partner_campaign_products_request

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
