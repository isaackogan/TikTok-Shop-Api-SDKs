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
  from ..models.get_seller_partner_campaign_registered_products_response_data_product_detail_product_statistic import GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailProductStatistic
  from ..models.get_seller_partner_campaign_registered_products_response_data_product_detail_rejected_reason import GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailRejectedReason
  from ..models.price_range import PriceRange
  from ..models.tier_commission_info import TierCommissionInfo





T = TypeVar("T", bound="GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetail")



@_attrs_define
class GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetail:
    """ 
        Attributes:
            can_seller_re_register (bool | Unset): Indicates whether the seller may submit the product again after its
                registration was
                rejected.
            has_removed (bool | Unset): Indicates whether the product has been removed or deleted.
            image (GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage | Unset):
            is_new (bool | Unset): Page display flag indicating that the product is newly added.
            is_under_canceling (bool | Unset): Indicates whether the product is currently going through the campaign-exit
                process.
            is_under_governed (bool | Unset): Indicates whether the product is subject to a governance restriction.
            open_plan_ads_commission_rate (int | Unset): Ads commission rate under the product's Open Plan, expressed as the
                percentage multiplied by
                100.
            open_plan_commission_rate (int | Unset): Product commission rate under the Open Plan, expressed as the
                percentage multiplied by 100.
            price_range (PriceRange | Unset):
            product_id (str | Unset): Product ID encoded as a decimal string.
            product_name (str | Unset): Display name of the product.
            product_statistics (GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailProductStatistic |
                Unset):
            product_status (str | Unset): Campaign product registration state. PENDING means awaiting approval; ONGOING
                means approved and participating; REJECTED means rejected; CLOSED means the registration has ended or been
                closed.
            product_stock (int | Unset): Product inventory quantity at the time of the query.
            rejected_reason (list[GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailRejectedReason] |
                Unset): Structured rejection messages with localization keys and default display text.
            sample_quota (int | Unset): Individual free-sample quota; absent if unset. For sub-campaigns this excludes
                shared_sample_quota.
            shared_sample_quota (int | Unset): Free-sample quota shared through the parent or campaign-group mechanism,
                where applicable.
            tier_commission_info (TierCommissionInfo | Unset):
            total_ads_commission_rate (int | Unset): Total Ads commission rate configured for the campaign product,
                expressed as the percentage
                multiplied by 100.
            total_commission_rate (int | Unset): Total campaign commission, percentage multiplied by 100 (1000 = 10%).
     """

    can_seller_re_register: bool | Unset = UNSET
    has_removed: bool | Unset = UNSET
    image: GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage | Unset = UNSET
    is_new: bool | Unset = UNSET
    is_under_canceling: bool | Unset = UNSET
    is_under_governed: bool | Unset = UNSET
    open_plan_ads_commission_rate: int | Unset = UNSET
    open_plan_commission_rate: int | Unset = UNSET
    price_range: PriceRange | Unset = UNSET
    product_id: str | Unset = UNSET
    product_name: str | Unset = UNSET
    product_statistics: GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailProductStatistic | Unset = UNSET
    product_status: str | Unset = UNSET
    product_stock: int | Unset = UNSET
    rejected_reason: list[GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailRejectedReason] | Unset = UNSET
    sample_quota: int | Unset = UNSET
    shared_sample_quota: int | Unset = UNSET
    tier_commission_info: TierCommissionInfo | Unset = UNSET
    total_ads_commission_rate: int | Unset = UNSET
    total_commission_rate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_seller_partner_campaign_candidate_products_response_data_product_detail_image import GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage # noqa: PLC0415
        from ..models.get_seller_partner_campaign_registered_products_response_data_product_detail_product_statistic import GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailProductStatistic # noqa: PLC0415
        from ..models.get_seller_partner_campaign_registered_products_response_data_product_detail_rejected_reason import GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailRejectedReason # noqa: PLC0415
        from ..models.price_range import PriceRange # noqa: PLC0415
        from ..models.tier_commission_info import TierCommissionInfo # noqa: PLC0415
        can_seller_re_register = self.can_seller_re_register

        has_removed = self.has_removed

        image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        is_new = self.is_new

        is_under_canceling = self.is_under_canceling

        is_under_governed = self.is_under_governed

        open_plan_ads_commission_rate = self.open_plan_ads_commission_rate

        open_plan_commission_rate = self.open_plan_commission_rate

        price_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price_range, Unset):
            price_range = self.price_range.to_dict()

        product_id = self.product_id

        product_name = self.product_name

        product_statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_statistics, Unset):
            product_statistics = self.product_statistics.to_dict()

        product_status = self.product_status

        product_stock = self.product_stock

        rejected_reason: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rejected_reason, Unset):
            rejected_reason = []
            for rejected_reason_item_data in self.rejected_reason:
                rejected_reason_item = rejected_reason_item_data.to_dict()
                rejected_reason.append(rejected_reason_item)



        sample_quota = self.sample_quota

        shared_sample_quota = self.shared_sample_quota

        tier_commission_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tier_commission_info, Unset):
            tier_commission_info = self.tier_commission_info.to_dict()

        total_ads_commission_rate = self.total_ads_commission_rate

        total_commission_rate = self.total_commission_rate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if can_seller_re_register is not UNSET:
            field_dict["can_seller_re_register"] = can_seller_re_register
        if has_removed is not UNSET:
            field_dict["has_removed"] = has_removed
        if image is not UNSET:
            field_dict["image"] = image
        if is_new is not UNSET:
            field_dict["is_new"] = is_new
        if is_under_canceling is not UNSET:
            field_dict["is_under_canceling"] = is_under_canceling
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
        if product_statistics is not UNSET:
            field_dict["product_statistics"] = product_statistics
        if product_status is not UNSET:
            field_dict["product_status"] = product_status
        if product_stock is not UNSET:
            field_dict["product_stock"] = product_stock
        if rejected_reason is not UNSET:
            field_dict["rejected_reason"] = rejected_reason
        if sample_quota is not UNSET:
            field_dict["sample_quota"] = sample_quota
        if shared_sample_quota is not UNSET:
            field_dict["shared_sample_quota"] = shared_sample_quota
        if tier_commission_info is not UNSET:
            field_dict["tier_commission_info"] = tier_commission_info
        if total_ads_commission_rate is not UNSET:
            field_dict["total_ads_commission_rate"] = total_ads_commission_rate
        if total_commission_rate is not UNSET:
            field_dict["total_commission_rate"] = total_commission_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_seller_partner_campaign_candidate_products_response_data_product_detail_image import GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage # noqa: PLC0415
        from ..models.get_seller_partner_campaign_registered_products_response_data_product_detail_product_statistic import GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailProductStatistic # noqa: PLC0415
        from ..models.get_seller_partner_campaign_registered_products_response_data_product_detail_rejected_reason import GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailRejectedReason # noqa: PLC0415
        from ..models.price_range import PriceRange # noqa: PLC0415
        from ..models.tier_commission_info import TierCommissionInfo # noqa: PLC0415
        d = dict(src_dict)
        can_seller_re_register = d.pop("can_seller_re_register", UNSET)

        has_removed = d.pop("has_removed", UNSET)

        _image = d.pop("image", UNSET)
        image: GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage | Unset
        if isinstance(_image,  Unset):
            image = UNSET
        else:
            image = GetSellerPartnerCampaignCandidateProductsResponseDataProductDetailImage.from_dict(_image)




        is_new = d.pop("is_new", UNSET)

        is_under_canceling = d.pop("is_under_canceling", UNSET)

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

        _product_statistics = d.pop("product_statistics", UNSET)
        product_statistics: GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailProductStatistic | Unset
        if isinstance(_product_statistics,  Unset):
            product_statistics = UNSET
        else:
            product_statistics = GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailProductStatistic.from_dict(_product_statistics)




        product_status = d.pop("product_status", UNSET)

        product_stock = d.pop("product_stock", UNSET)

        _rejected_reason = d.pop("rejected_reason", UNSET)
        rejected_reason: list[GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailRejectedReason] | Unset = UNSET
        if _rejected_reason is not UNSET:
            rejected_reason = []
            for rejected_reason_item_data in _rejected_reason:
                rejected_reason_item = GetSellerPartnerCampaignRegisteredProductsResponseDataProductDetailRejectedReason.from_dict(rejected_reason_item_data)



                rejected_reason.append(rejected_reason_item)


        sample_quota = d.pop("sample_quota", UNSET)

        shared_sample_quota = d.pop("shared_sample_quota", UNSET)

        _tier_commission_info = d.pop("tier_commission_info", UNSET)
        tier_commission_info: TierCommissionInfo | Unset
        if isinstance(_tier_commission_info,  Unset):
            tier_commission_info = UNSET
        else:
            tier_commission_info = TierCommissionInfo.from_dict(_tier_commission_info)




        total_ads_commission_rate = d.pop("total_ads_commission_rate", UNSET)

        total_commission_rate = d.pop("total_commission_rate", UNSET)

        get_seller_partner_campaign_registered_products_response_data_product_detail = cls(
            can_seller_re_register=can_seller_re_register,
            has_removed=has_removed,
            image=image,
            is_new=is_new,
            is_under_canceling=is_under_canceling,
            is_under_governed=is_under_governed,
            open_plan_ads_commission_rate=open_plan_ads_commission_rate,
            open_plan_commission_rate=open_plan_commission_rate,
            price_range=price_range,
            product_id=product_id,
            product_name=product_name,
            product_statistics=product_statistics,
            product_status=product_status,
            product_stock=product_stock,
            rejected_reason=rejected_reason,
            sample_quota=sample_quota,
            shared_sample_quota=shared_sample_quota,
            tier_commission_info=tier_commission_info,
            total_ads_commission_rate=total_ads_commission_rate,
            total_commission_rate=total_commission_rate,
        )


        get_seller_partner_campaign_registered_products_response_data_product_detail.additional_properties = d
        return get_seller_partner_campaign_registered_products_response_data_product_detail

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
