from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info_image import QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoImage
  from ..models.query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info_price import QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPrice
  from ..models.query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info_promotion_price import QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPromotionPrice





T = TypeVar("T", bound="QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfo")



@_attrs_define
class QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfo:
    """ 
        Attributes:
            product_id (str | Unset): Product ID
            title (str | Unset): Product titile
            image (QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoImage |
                Unset):
            price (QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPrice |
                Unset):
            promotion_price
                (QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPromotionPrice |
                Unset):
            target_commission (int | Unset): Product target collaboration commission. e.g. 2200 mean 22% commission rate
            open_commission (int | Unset): Product open collaboration commission. e.g. 2200 mean 22% commission rate
            target_ads_commission (int | Unset): Product target ads collaboration commission
            old_target_commission (int | Unset): Product old target collaboration commission
            old_target_ads_commission (int | Unset): Product old target ads collaboration commission
            commission_effective_time (int | Unset): Unix timestamp in milliseconds when the target collaboration commission
                becomes effective.
            ads_commission_effective_time (int | Unset): Unix timestamp in milliseconds when the target collaboration Ads
                commission becomes effective.
            product_status (str | Unset): Product status
                1: Active
                2; Sold out
                3: product deactivated by seller;
                4: product deactivated by platform
                5: product reject
                6: product deleted
     """

    product_id: str | Unset = UNSET
    title: str | Unset = UNSET
    image: QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoImage | Unset = UNSET
    price: QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPrice | Unset = UNSET
    promotion_price: QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPromotionPrice | Unset = UNSET
    target_commission: int | Unset = UNSET
    open_commission: int | Unset = UNSET
    target_ads_commission: int | Unset = UNSET
    old_target_commission: int | Unset = UNSET
    old_target_ads_commission: int | Unset = UNSET
    commission_effective_time: int | Unset = UNSET
    ads_commission_effective_time: int | Unset = UNSET
    product_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info_image import QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoImage # noqa: PLC0415
        from ..models.query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info_price import QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPrice # noqa: PLC0415
        from ..models.query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info_promotion_price import QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPromotionPrice # noqa: PLC0415
        product_id = self.product_id

        title = self.title

        image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image, Unset):
            image = self.image.to_dict()

        price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.price, Unset):
            price = self.price.to_dict()

        promotion_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.promotion_price, Unset):
            promotion_price = self.promotion_price.to_dict()

        target_commission = self.target_commission

        open_commission = self.open_commission

        target_ads_commission = self.target_ads_commission

        old_target_commission = self.old_target_commission

        old_target_ads_commission = self.old_target_ads_commission

        commission_effective_time = self.commission_effective_time

        ads_commission_effective_time = self.ads_commission_effective_time

        product_status = self.product_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if title is not UNSET:
            field_dict["title"] = title
        if image is not UNSET:
            field_dict["image"] = image
        if price is not UNSET:
            field_dict["price"] = price
        if promotion_price is not UNSET:
            field_dict["promotion_price"] = promotion_price
        if target_commission is not UNSET:
            field_dict["target_commission"] = target_commission
        if open_commission is not UNSET:
            field_dict["open_commission"] = open_commission
        if target_ads_commission is not UNSET:
            field_dict["target_ads_commission"] = target_ads_commission
        if old_target_commission is not UNSET:
            field_dict["old_target_commission"] = old_target_commission
        if old_target_ads_commission is not UNSET:
            field_dict["old_target_ads_commission"] = old_target_ads_commission
        if commission_effective_time is not UNSET:
            field_dict["commission_effective_time"] = commission_effective_time
        if ads_commission_effective_time is not UNSET:
            field_dict["ads_commission_effective_time"] = ads_commission_effective_time
        if product_status is not UNSET:
            field_dict["product_status"] = product_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info_image import QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoImage # noqa: PLC0415
        from ..models.query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info_price import QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPrice # noqa: PLC0415
        from ..models.query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info_promotion_price import QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPromotionPrice # noqa: PLC0415
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        title = d.pop("title", UNSET)

        _image = d.pop("image", UNSET)
        image: QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoImage | Unset
        if isinstance(_image,  Unset):
            image = UNSET
        else:
            image = QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoImage.from_dict(_image)




        _price = d.pop("price", UNSET)
        price: QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPrice | Unset
        if isinstance(_price,  Unset):
            price = UNSET
        else:
            price = QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPrice.from_dict(_price)




        _promotion_price = d.pop("promotion_price", UNSET)
        promotion_price: QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPromotionPrice | Unset
        if isinstance(_promotion_price,  Unset):
            promotion_price = UNSET
        else:
            promotion_price = QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfoPromotionPrice.from_dict(_promotion_price)




        target_commission = d.pop("target_commission", UNSET)

        open_commission = d.pop("open_commission", UNSET)

        target_ads_commission = d.pop("target_ads_commission", UNSET)

        old_target_commission = d.pop("old_target_commission", UNSET)

        old_target_ads_commission = d.pop("old_target_ads_commission", UNSET)

        commission_effective_time = d.pop("commission_effective_time", UNSET)

        ads_commission_effective_time = d.pop("ads_commission_effective_time", UNSET)

        product_status = d.pop("product_status", UNSET)

        query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info = cls(
            product_id=product_id,
            title=title,
            image=image,
            price=price,
            promotion_price=promotion_price,
            target_commission=target_commission,
            open_commission=open_commission,
            target_ads_commission=target_ads_commission,
            old_target_commission=old_target_commission,
            old_target_ads_commission=old_target_ads_commission,
            commission_effective_time=commission_effective_time,
            ads_commission_effective_time=ads_commission_effective_time,
            product_status=product_status,
        )


        query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info.additional_properties = d
        return query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info

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
