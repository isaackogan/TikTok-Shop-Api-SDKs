from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailIndicatorData"
)


@_attrs_define
class GetCampaignProductPerformanceListResponseDataCampaignProductStatisticCampaignProductDetailIndicatorData:
    """
    Attributes:
        paid_order_num (str | Unset): The total number of paid orders. `paid_order_num` = `actual_order_num` + {number
            of paid but returned orders}
        actual_order_num (str | Unset): The actual number of paid orders.
        estimated_amount (str | Unset): The total payment amount corresponding to `paid_order_num`.
        actual_amount (str | Unset): GMV, the total payment amount corresponding to `actual_order_num`.
        estimated_partner_commission (str | Unset): The partner commission amount corresponding to paid_order_num.
        actual_partner_commission (str | Unset): The partner commission amount corresponding to actual_order_num.
        creator_sales_num (str | Unset): The number of creators credited with at least one product sale.
        collaborated_creators_num (str | Unset): The total number of creators collaborating on the campaign.
        promoted_creator_num (str | Unset): The number of creators involved in the partner plan.
        sample_requested_creator_num (str | Unset): The total number of creators that applied for a sample.
    """

    paid_order_num: str | Unset = UNSET
    actual_order_num: str | Unset = UNSET
    estimated_amount: str | Unset = UNSET
    actual_amount: str | Unset = UNSET
    estimated_partner_commission: str | Unset = UNSET
    actual_partner_commission: str | Unset = UNSET
    creator_sales_num: str | Unset = UNSET
    collaborated_creators_num: str | Unset = UNSET
    promoted_creator_num: str | Unset = UNSET
    sample_requested_creator_num: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        paid_order_num = self.paid_order_num

        actual_order_num = self.actual_order_num

        estimated_amount = self.estimated_amount

        actual_amount = self.actual_amount

        estimated_partner_commission = self.estimated_partner_commission

        actual_partner_commission = self.actual_partner_commission

        creator_sales_num = self.creator_sales_num

        collaborated_creators_num = self.collaborated_creators_num

        promoted_creator_num = self.promoted_creator_num

        sample_requested_creator_num = self.sample_requested_creator_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paid_order_num is not UNSET:
            field_dict["paid_order_num"] = paid_order_num
        if actual_order_num is not UNSET:
            field_dict["actual_order_num"] = actual_order_num
        if estimated_amount is not UNSET:
            field_dict["estimated_amount"] = estimated_amount
        if actual_amount is not UNSET:
            field_dict["actual_amount"] = actual_amount
        if estimated_partner_commission is not UNSET:
            field_dict["estimated_partner_commission"] = estimated_partner_commission
        if actual_partner_commission is not UNSET:
            field_dict["actual_partner_commission"] = actual_partner_commission
        if creator_sales_num is not UNSET:
            field_dict["creator_sales_num"] = creator_sales_num
        if collaborated_creators_num is not UNSET:
            field_dict["collaborated_creators_num"] = collaborated_creators_num
        if promoted_creator_num is not UNSET:
            field_dict["promoted_creator_num"] = promoted_creator_num
        if sample_requested_creator_num is not UNSET:
            field_dict["sample_requested_creator_num"] = sample_requested_creator_num

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        paid_order_num = d.pop("paid_order_num", UNSET)

        actual_order_num = d.pop("actual_order_num", UNSET)

        estimated_amount = d.pop("estimated_amount", UNSET)

        actual_amount = d.pop("actual_amount", UNSET)

        estimated_partner_commission = d.pop("estimated_partner_commission", UNSET)

        actual_partner_commission = d.pop("actual_partner_commission", UNSET)

        creator_sales_num = d.pop("creator_sales_num", UNSET)

        collaborated_creators_num = d.pop("collaborated_creators_num", UNSET)

        promoted_creator_num = d.pop("promoted_creator_num", UNSET)

        sample_requested_creator_num = d.pop("sample_requested_creator_num", UNSET)

        get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_indicator_data = cls(
            paid_order_num=paid_order_num,
            actual_order_num=actual_order_num,
            estimated_amount=estimated_amount,
            actual_amount=actual_amount,
            estimated_partner_commission=estimated_partner_commission,
            actual_partner_commission=actual_partner_commission,
            creator_sales_num=creator_sales_num,
            collaborated_creators_num=collaborated_creators_num,
            promoted_creator_num=promoted_creator_num,
            sample_requested_creator_num=sample_requested_creator_num,
        )

        get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_indicator_data.additional_properties = d
        return get_campaign_product_performance_list_response_data_campaign_product_statistic_campaign_product_detail_indicator_data

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
