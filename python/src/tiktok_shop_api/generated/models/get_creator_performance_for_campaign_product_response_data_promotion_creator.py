from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_creator_performance_for_campaign_product_response_data_promotion_creator_creator import GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorCreator
  from ..models.get_creator_performance_for_campaign_product_response_data_promotion_creator_paid_amount import GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorPaidAmount





T = TypeVar("T", bound="GetCreatorPerformanceForCampaignProductResponseDataPromotionCreator")



@_attrs_define
class GetCreatorPerformanceForCampaignProductResponseDataPromotionCreator:
    """ 
        Attributes:
            paid_amount (GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorPaidAmount | Unset):
            room_count (int | Unset): The number of live broadcast rooms associated with this promotion.
            video_count (int | Unset): The total number of videos associated with this promotion published by creators.
            free_sample_status (str | Unset): Status of the Creator's sample application.
                - NOT_REQUESTED
                - PENDING
                - AWAITING_SHIPMENT
                - AWAITING_COLLECTION
                - SHIPPED
                - CONTENT_PENDING
                - REJECT_CANCELLED
                - OVERDUE_CANCELLED
                - UNFULFIL_CANCELLED
                - DEL_PLAN_CANCELLED
                - SELLER_NOT_SHIP_CANCELLED
                - WITHDRAW_CANCELLED
                - UNFULFILLABLE_CANCELLED
                - OPERATOR_MANUAL_CANCELLED
                - OPERATOR_MANUAL_FAILED
                - OPERATOR_MANUAL_COMPLETED
                - COMPLETED
            commission (str | Unset): The commission rate in hundredths of a percent (0.01%). For example, a value of 1000
                is 10.00%.
            effective_end_time (str | Unset): The effective end time for the collaboration in Unix epoch time format.
            effective_start_time (str | Unset): The effective start time for the collaboration in Unix epoch time format.
            creator (GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorCreator | Unset):
            affiliate_product_id (str | Unset): The affiliate product identifier.
     """

    paid_amount: GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorPaidAmount | Unset = UNSET
    room_count: int | Unset = UNSET
    video_count: int | Unset = UNSET
    free_sample_status: str | Unset = UNSET
    commission: str | Unset = UNSET
    effective_end_time: str | Unset = UNSET
    effective_start_time: str | Unset = UNSET
    creator: GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorCreator | Unset = UNSET
    affiliate_product_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_creator_performance_for_campaign_product_response_data_promotion_creator_creator import GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorCreator # noqa: PLC0415
        from ..models.get_creator_performance_for_campaign_product_response_data_promotion_creator_paid_amount import GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorPaidAmount # noqa: PLC0415
        paid_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paid_amount, Unset):
            paid_amount = self.paid_amount.to_dict()

        room_count = self.room_count

        video_count = self.video_count

        free_sample_status = self.free_sample_status

        commission = self.commission

        effective_end_time = self.effective_end_time

        effective_start_time = self.effective_start_time

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        affiliate_product_id = self.affiliate_product_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if paid_amount is not UNSET:
            field_dict["paid_amount"] = paid_amount
        if room_count is not UNSET:
            field_dict["room_count"] = room_count
        if video_count is not UNSET:
            field_dict["video_count"] = video_count
        if free_sample_status is not UNSET:
            field_dict["free_sample_status"] = free_sample_status
        if commission is not UNSET:
            field_dict["commission"] = commission
        if effective_end_time is not UNSET:
            field_dict["effective_end_time"] = effective_end_time
        if effective_start_time is not UNSET:
            field_dict["effective_start_time"] = effective_start_time
        if creator is not UNSET:
            field_dict["creator"] = creator
        if affiliate_product_id is not UNSET:
            field_dict["affiliate_product_id"] = affiliate_product_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creator_performance_for_campaign_product_response_data_promotion_creator_creator import GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorCreator # noqa: PLC0415
        from ..models.get_creator_performance_for_campaign_product_response_data_promotion_creator_paid_amount import GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorPaidAmount # noqa: PLC0415
        d = dict(src_dict)
        _paid_amount = d.pop("paid_amount", UNSET)
        paid_amount: GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorPaidAmount | Unset
        if isinstance(_paid_amount,  Unset):
            paid_amount = UNSET
        else:
            paid_amount = GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorPaidAmount.from_dict(_paid_amount)




        room_count = d.pop("room_count", UNSET)

        video_count = d.pop("video_count", UNSET)

        free_sample_status = d.pop("free_sample_status", UNSET)

        commission = d.pop("commission", UNSET)

        effective_end_time = d.pop("effective_end_time", UNSET)

        effective_start_time = d.pop("effective_start_time", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorCreator | Unset
        if isinstance(_creator,  Unset):
            creator = UNSET
        else:
            creator = GetCreatorPerformanceForCampaignProductResponseDataPromotionCreatorCreator.from_dict(_creator)




        affiliate_product_id = d.pop("affiliate_product_id", UNSET)

        get_creator_performance_for_campaign_product_response_data_promotion_creator = cls(
            paid_amount=paid_amount,
            room_count=room_count,
            video_count=video_count,
            free_sample_status=free_sample_status,
            commission=commission,
            effective_end_time=effective_end_time,
            effective_start_time=effective_start_time,
            creator=creator,
            affiliate_product_id=affiliate_product_id,
        )


        get_creator_performance_for_campaign_product_response_data_promotion_creator.additional_properties = d
        return get_creator_performance_for_campaign_product_response_data_promotion_creator

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
