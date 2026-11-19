from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="GetAIReportCampaignPeriodsResponseDataCampaign")



@_attrs_define
class GetAIReportCampaignPeriodsResponseDataCampaign:
    """ 
        Attributes:
            end_date (datetime.date | Unset): Last day of the campaign, inclusive, in YYYY-MM-DD format and the shop
                region's configured local timezone, not UTC. Use it as end_date to query campaign data.
            is_ended (bool | Unset): Current campaign status returned by the campaign service. True means the campaign has
                ended; false means it is ongoing.
            name (str | Unset): Name of the promotional campaign.
            start_date (datetime.date | Unset): First day of the campaign, inclusive, in YYYY-MM-DD format and the shop
                region's configured local timezone, not UTC. Use it as start_date to query campaign data.
     """

    end_date: datetime.date | Unset = UNSET
    is_ended: bool | Unset = UNSET
    name: str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        is_ended = self.is_ended

        name = self.name

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if is_ended is not UNSET:
            field_dict["is_ended"] = is_ended
        if name is not UNSET:
            field_dict["name"] = name
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        is_ended = d.pop("is_ended", UNSET)

        name = d.pop("name", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        get_ai_report_campaign_periods_response_data_campaign = cls(
            end_date=end_date,
            is_ended=is_ended,
            name=name,
            start_date=start_date,
        )


        get_ai_report_campaign_periods_response_data_campaign.additional_properties = d
        return get_ai_report_campaign_periods_response_data_campaign

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
