from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_acc_audience_preference_summary_response_data_channel_summary import GetACCAudiencePreferenceSummaryResponseDataChannelSummary





T = TypeVar("T", bound="GetACCAudiencePreferenceSummaryResponseData")



@_attrs_define
class GetACCAudiencePreferenceSummaryResponseData:
    """ 
        Attributes:
            audience_type (str | Unset): Audience segment used for the summary, returned as the uppercase audience_type
                value.
            channel_summaries (list[GetACCAudiencePreferenceSummaryResponseDataChannelSummary] | Unset): Channel summaries
                in this order: PRODUCT, LIVE, VIDEO, PHOTO. Lists within each summary can be empty when no items are available.
                These are structured Top 3 results rather than generated narrative text. A list may also be empty when its
                underlying query fails; an empty list alone does not establish that the channel had no activity.
            earliest_available_date (datetime.date | Unset): Earliest date available for the selected shop, brand, and
                industry, in YYYY-MM-DD format (UTC).
            end_date (datetime.date | Unset): Inclusive end date of the reporting window, in YYYY-MM-DD format (UTC).
            latest_available_date (datetime.date | Unset): Latest date available for the selected shop, brand, and industry,
                in YYYY-MM-DD format (UTC).
            scope (str | Unset): Scope used for the summary: MY_SHOP for shop-level data or MARKET for market-level data.
            start_date (datetime.date | Unset): Inclusive start date of the reporting window, in YYYY-MM-DD format (UTC).
     """

    audience_type: str | Unset = UNSET
    channel_summaries: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummary] | Unset = UNSET
    earliest_available_date: datetime.date | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    latest_available_date: datetime.date | Unset = UNSET
    scope: str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary import GetACCAudiencePreferenceSummaryResponseDataChannelSummary # noqa: PLC0415
        audience_type = self.audience_type

        channel_summaries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel_summaries, Unset):
            channel_summaries = []
            for channel_summaries_item_data in self.channel_summaries:
                channel_summaries_item = channel_summaries_item_data.to_dict()
                channel_summaries.append(channel_summaries_item)



        earliest_available_date: str | Unset = UNSET
        if not isinstance(self.earliest_available_date, Unset):
            earliest_available_date = self.earliest_available_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()

        scope = self.scope

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if audience_type is not UNSET:
            field_dict["audience_type"] = audience_type
        if channel_summaries is not UNSET:
            field_dict["channel_summaries"] = channel_summaries
        if earliest_available_date is not UNSET:
            field_dict["earliest_available_date"] = earliest_available_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date
        if scope is not UNSET:
            field_dict["scope"] = scope
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_acc_audience_preference_summary_response_data_channel_summary import GetACCAudiencePreferenceSummaryResponseDataChannelSummary # noqa: PLC0415
        d = dict(src_dict)
        audience_type = d.pop("audience_type", UNSET)

        _channel_summaries = d.pop("channel_summaries", UNSET)
        channel_summaries: list[GetACCAudiencePreferenceSummaryResponseDataChannelSummary] | Unset = UNSET
        if _channel_summaries is not UNSET:
            channel_summaries = []
            for channel_summaries_item_data in _channel_summaries:
                channel_summaries_item = GetACCAudiencePreferenceSummaryResponseDataChannelSummary.from_dict(channel_summaries_item_data)



                channel_summaries.append(channel_summaries_item)


        _earliest_available_date = d.pop("earliest_available_date", UNSET)
        earliest_available_date: datetime.date | Unset
        if isinstance(_earliest_available_date,  Unset):
            earliest_available_date = UNSET
        else:
            earliest_available_date = datetime.date.fromisoformat(_earliest_available_date)




        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date,  Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)




        scope = d.pop("scope", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        get_acc_audience_preference_summary_response_data = cls(
            audience_type=audience_type,
            channel_summaries=channel_summaries,
            earliest_available_date=earliest_available_date,
            end_date=end_date,
            latest_available_date=latest_available_date,
            scope=scope,
            start_date=start_date,
        )


        get_acc_audience_preference_summary_response_data.additional_properties = d
        return get_acc_audience_preference_summary_response_data

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
