from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_seller_partner_campaign_candidate_products_response_data_product_detail_image import GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage
  from ..models.price_range import PriceRange
  from ..models.tier_commission_info import TierCommissionInfo





T = TypeVar("T", bound="GetSellerPartnerCampaignCandidateProductsResponseDataProductDetail")



@_attrs_define
class GetSellerPartnerCampaignCandidateProductsResponseDataProductDetail:
    """ 
        Attributes:
            has_registered (bool | Unset): Indicates whether the product is treated as already registered in the campaign. A
                rejected
                product eligible for re-registration may be reported as false.
            image (GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage | Unset):
            is_under_governed (bool | Unset): Indicates whether the product is subject to a governance restriction.
            open_plan_ads_commission_rate (int | Unset): Ads commission rate under the product's Open Plan, expressed as the
                percentage multiplied by
                100.
            open_plan_commission_rate (int | Unset): Product commission rate under the Open Plan, expressed as the
                percentage multiplied by 100.
            price_range (PriceRange | Unset):
            product_id (str | Unset): Product ID encoded as a decimal string.
            product_name (str | Unset): Display name of the product.
            product_stock (int | Unset): Product inventory quantity at the time of the query.
            tier_commission_info (TierCommissionInfo | Unset):
     """

    has_registered: bool | Unset = UNSET
    image: GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage | Unset = UNSET
    is_under_governed: bool | Unset = UNSET
    open_plan_ads_commission_rate: int | Unset = UNSET
    open_plan_commission_rate: int | Unset = UNSET
    price_range: PriceRange | Unset = UNSET
    product_id: str | Unset = UNSET
    product_name: str | Unset = UNSET
    product_stock: int | Unset = UNSET
    tier_commission_info: TierCommissionInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_seller_partner_campaign_candidate_products_response_data_product_detail_image import GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage # noqa: PLC0415
        from ..models.price_range import PriceRange # noqa: PLC0415
        from ..models.tier_commission_info import TierCommissionInfo # noqa: PLC0415
        has_registered = self.has_registered

        image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        is_under_governed = self.is_under_governed

        open_plan_ads_commission_rate = self.open_plan_ads_commission_rate

        open_plan_commission_rate = self.open_plan_commission_rate

        price_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price_range, Unset):
            price_range = self.price_range.to_dict()

        product_id = self.product_id

        product_name = self.product_name

        product_stock = self.product_stock

        tier_commission_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tier_commission_info, Unset):
            tier_commission_info = self.tier_commission_info.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if has_registered is not UNSET:
            field_dict["has_registered"] = has_registered
        if image is not UNSET:
            field_dict["image"] = image
        if is_under_governed is not UNSET:
            field_dict["is_under_governed"] = is_under_governed
        if open_plan_ads_commission_rate is not UNSET:
            field_dict["open_plan_ads_commission_rate"] = open_plan_ads_commission_rate
        if open_plan_commission_rate is not UNSET:
            field_dict["open_plan_commission_rate"] = open_plan_commission_rate
        if price_range is not UNSET:
            field_dict["price_range"] = price_range
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if product_stock is not UNSET:
            field_dict["product_stock"] = product_stock
        if tier_commission_info is not UNSET:
            field_dict["tier_commission_info"] = tier_commission_info

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_seller_partner_campaign_candidate_products_response_data_product_detail_image import GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage # noqa: PLC0415
        from ..models.price_range import PriceRange # noqa: PLC0415
        from ..models.tier_commission_info import TierCommissionInfo # noqa: PLC0415
        d = dict(src_dict)
        has_registered = d.pop("has_registered", UNSET)

        _image = d.pop("image", UNSET)
        image: GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage | Unset
        if isinstance(_image,  Unset):
            image = UNSET
        else:
            image = GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage.from_dict(_image)




        is_under_governed = d.pop("is_under_governed", UNSET)

        open_plan_ads_commission_rate = d.pop("open_plan_ads_commission_rate", UNSET)

        open_plan_commission_rate = d.pop("open_plan_commission_rate", UNSET)

        _price_range = d.pop("price_range", UNSET)
        price_range: PriceRange | Unset
        if isinstance(_price_range,  Unset):
            price_range = UNSET
        else:
            price_range = PriceRange.from_dict(_price_range)




        product_id = d.pop("product_id", UNSET)

        product_name = d.pop("product_name", UNSET)

        product_stock = d.pop("product_stock", UNSET)

        _tier_commission_info = d.pop("tier_commission_info", UNSET)
        tier_commission_info: TierCommissionInfo | Unset
        if isinstance(_tier_commission_info,  Unset):
            tier_commission_info = UNSET
        else:
            tier_commission_info = TierCommissionInfo.from_dict(_tier_commission_info)




        get_seller_partner_campaign_candidate_products_response_data_product_detail = cls(
            has_registered=has_registered,
            image=image,
            is_under_governed=is_under_governed,
            open_plan_ads_commission_rate=open_plan_ads_commission_rate,
            open_plan_commission_rate=open_plan_commission_rate,
            price_range=price_range,
            product_id=product_id,
            product_name=product_name,
            product_stock=product_stock,
            tier_commission_info=tier_commission_info,
        )


        get_seller_partner_campaign_candidate_products_response_data_product_detail.additional_properties = d
        return get_seller_partner_campaign_candidate_products_response_data_product_detail

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
