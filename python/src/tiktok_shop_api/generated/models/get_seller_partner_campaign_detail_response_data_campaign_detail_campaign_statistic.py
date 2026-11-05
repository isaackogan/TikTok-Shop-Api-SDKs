from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetSellerPartnerCampaignDetailResponseDataCampaignDetailCampaignStatistic")



@_attrs_define
class GetSellerPartnerCampaignDetailResponseDataCampaignDetailCampaignStatistic:
    """ 
        Attributes:
            closed_products_num (int | Unset): Number of product registrations in the closed state.
            currency (str | Unset): ISO 4217 currency code for these statistics, such as USD. May be absent or empty when
                unavailable.
            currency_symbol (str | Unset): Display symbol for the statistics currency. A symbol alone does not uniquely
                identify a currency.
            declined_agency_num (int | Unset): Number of agencies that have declined participation in the campaign.
            est_total_commissions (str | Unset): Formatted estimated total commission amount for the campaign.
            joined_agency_num (int | Unset): Number of agencies that have joined the campaign.
            ongoing_products_num (int | Unset): Number of products currently participating in the campaign.
            paid_gmv (str | Unset): Formatted gross merchandise value of paid orders attributed to the campaign. The value
                may
                include a currency symbol.
            paid_order_num (str | Unset): Number of paid orders attributed to the campaign, encoded as a string.
            pending_products_num (int | Unset): Number of submitted products awaiting review.
            rejected_products_num (int | Unset): Number of products rejected from the campaign.
            sale_products_num (str | Unset): Number of campaign products with sales, encoded as a string.
            settled_gmv (str | Unset): Formatted gross merchandise value of settled orders attributed to the campaign.
            settled_order_num (str | Unset): Number of settled orders attributed to the campaign, encoded as a string.
            settled_total_commissions (str | Unset): Formatted settled total commission amount for the campaign.
            statistics_update_time (str | Unset): Time at which the campaign statistics were updated, encoded as a string in
                the format
                provided by the statistics source.
     """

    closed_products_num: int | Unset = UNSET
    currency: str | Unset = UNSET
    currency_symbol: str | Unset = UNSET
    declined_agency_num: int | Unset = UNSET
    est_total_commissions: str | Unset = UNSET
    joined_agency_num: int | Unset = UNSET
    ongoing_products_num: int | Unset = UNSET
    paid_gmv: str | Unset = UNSET
    paid_order_num: str | Unset = UNSET
    pending_products_num: int | Unset = UNSET
    rejected_products_num: int | Unset = UNSET
    sale_products_num: str | Unset = UNSET
    settled_gmv: str | Unset = UNSET
    settled_order_num: str | Unset = UNSET
    settled_total_commissions: str | Unset = UNSET
    statistics_update_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        closed_products_num = self.closed_products_num

        currency = self.currency

        currency_symbol = self.currency_symbol

        declined_agency_num = self.declined_agency_num

        est_total_commissions = self.est_total_commissions

        joined_agency_num = self.joined_agency_num

        ongoing_products_num = self.ongoing_products_num

        paid_gmv = self.paid_gmv

        paid_order_num = self.paid_order_num

        pending_products_num = self.pending_products_num

        rejected_products_num = self.rejected_products_num

        sale_products_num = self.sale_products_num

        settled_gmv = self.settled_gmv

        settled_order_num = self.settled_order_num

        settled_total_commissions = self.settled_total_commissions

        statistics_update_time = self.statistics_update_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if closed_products_num is not UNSET:
            field_dict["closed_products_num"] = closed_products_num
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_symbol is not UNSET:
            field_dict["currency_symbol"] = currency_symbol
        if declined_agency_num is not UNSET:
            field_dict["declined_agency_num"] = declined_agency_num
        if est_total_commissions is not UNSET:
            field_dict["est_total_commissions"] = est_total_commissions
        if joined_agency_num is not UNSET:
            field_dict["joined_agency_num"] = joined_agency_num
        if ongoing_products_num is not UNSET:
            field_dict["ongoing_products_num"] = ongoing_products_num
        if paid_gmv is not UNSET:
            field_dict["paid_gmv"] = paid_gmv
        if paid_order_num is not UNSET:
            field_dict["paid_order_num"] = paid_order_num
        if pending_products_num is not UNSET:
            field_dict["pending_products_num"] = pending_products_num
        if rejected_products_num is not UNSET:
            field_dict["rejected_products_num"] = rejected_products_num
        if sale_products_num is not UNSET:
            field_dict["sale_products_num"] = sale_products_num
        if settled_gmv is not UNSET:
            field_dict["settled_gmv"] = settled_gmv
        if settled_order_num is not UNSET:
            field_dict["settled_order_num"] = settled_order_num
        if settled_total_commissions is not UNSET:
            field_dict["settled_total_commissions"] = settled_total_commissions
        if statistics_update_time is not UNSET:
            field_dict["statistics_update_time"] = statistics_update_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        closed_products_num = d.pop("closed_products_num", UNSET)

        currency = d.pop("currency", UNSET)

        currency_symbol = d.pop("currency_symbol", UNSET)

        declined_agency_num = d.pop("declined_agency_num", UNSET)

        est_total_commissions = d.pop("est_total_commissions", UNSET)

        joined_agency_num = d.pop("joined_agency_num", UNSET)

        ongoing_products_num = d.pop("ongoing_products_num", UNSET)

        paid_gmv = d.pop("paid_gmv", UNSET)

        paid_order_num = d.pop("paid_order_num", UNSET)

        pending_products_num = d.pop("pending_products_num", UNSET)

        rejected_products_num = d.pop("rejected_products_num", UNSET)

        sale_products_num = d.pop("sale_products_num", UNSET)

        settled_gmv = d.pop("settled_gmv", UNSET)

        settled_order_num = d.pop("settled_order_num", UNSET)

        settled_total_commissions = d.pop("settled_total_commissions", UNSET)

        statistics_update_time = d.pop("statistics_update_time", UNSET)

        get_seller_partner_campaign_detail_response_data_campaign_detail_campaign_statistic = cls(
            closed_products_num=closed_products_num,
            currency=currency,
            currency_symbol=currency_symbol,
            declined_agency_num=declined_agency_num,
            est_total_commissions=est_total_commissions,
            joined_agency_num=joined_agency_num,
            ongoing_products_num=ongoing_products_num,
            paid_gmv=paid_gmv,
            paid_order_num=paid_order_num,
            pending_products_num=pending_products_num,
            rejected_products_num=rejected_products_num,
            sale_products_num=sale_products_num,
            settled_gmv=settled_gmv,
            settled_order_num=settled_order_num,
            settled_total_commissions=settled_total_commissions,
            statistics_update_time=statistics_update_time,
        )


        get_seller_partner_campaign_detail_response_data_campaign_detail_campaign_statistic.additional_properties = d
        return get_seller_partner_campaign_detail_response_data_campaign_detail_campaign_statistic

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
