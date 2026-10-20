from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.review_affiliate_partner_campaign_product_request_reject_reasons_item import ReviewAffiliatePartnerCampaignProductRequestRejectReasonsItem
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReviewAffiliatePartnerCampaignProductRequest")



@_attrs_define
class ReviewAffiliatePartnerCampaignProductRequest:
    """ 
        Attributes:
            review_result (str): The product review decision by the TikTok Affiliate Partner. This is an enumerated type
                with values:
                - APPROVE
                - REJECT
                - REJECT_FOREVER
            reject_reasons (list[ReviewAffiliatePartnerCampaignProductRequestRejectReasonsItem] | Unset): Rejection reasons
                for the product when `review_result` is `REJECT` or `REJECT_FOREVER`. Possible values for each item:
                - COMMISSION_TOO_LOW
                - PRODUCT_HARD_TO_PROMOTE
                - PRODUCT_TOO_EXPENSIVE
                - NO_SUITABLE_CREATOR
     """

    review_result: str
    reject_reasons: list[ReviewAffiliatePartnerCampaignProductRequestRejectReasonsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        review_result = self.review_result

        reject_reasons: list[str] | Unset = UNSET
        if not isinstance(self.reject_reasons, Unset):
            reject_reasons = []
            for reject_reasons_item_data in self.reject_reasons:
                reject_reasons_item = reject_reasons_item_data.value
                reject_reasons.append(reject_reasons_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "review_result": review_result,
        })
        if reject_reasons is not UNSET:
            field_dict["reject_reasons"] = reject_reasons

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        review_result = d.pop("review_result")

        _reject_reasons = d.pop("reject_reasons", UNSET)
        reject_reasons: list[ReviewAffiliatePartnerCampaignProductRequestRejectReasonsItem] | Unset = UNSET
        if _reject_reasons is not UNSET:
            reject_reasons = []
            for reject_reasons_item_data in _reject_reasons:
                reject_reasons_item = ReviewAffiliatePartnerCampaignProductRequestRejectReasonsItem(reject_reasons_item_data)



                reject_reasons.append(reject_reasons_item)


        review_affiliate_partner_campaign_product_request = cls(
            review_result=review_result,
            reject_reasons=reject_reasons,
        )


        review_affiliate_partner_campaign_product_request.additional_properties = d
        return review_affiliate_partner_campaign_product_request

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
