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
  from ..models.get_off_site_performance_details_response_data_content import GetOffSitePerformanceDetailsResponseDataContent





T = TypeVar("T", bound="GetOffSitePerformanceDetailsResponseData")



@_attrs_define
class GetOffSitePerformanceDetailsResponseData:
    """ 
        Attributes:
            contents (list[GetOffSitePerformanceDetailsResponseDataContent] | Unset): Performance records in the current
                page, in the requested sort order. The report selects up to 100 items for each of four descending metric
                rankings: tiktok_shop_gmv, off_site_gmv, total_gmv, and off_site_effect_rate. GMV rankings require a positive
                value for the ranked metric; the effect-rate ranking requires both GMV values to be positive. Results are the
                union of these selections, deduplicated by content ID. The requested sorting and pagination apply only to this
                subset, which may not contain every item of the requested content_type. Available metadata depends on
                content_type.
            latest_available_date (datetime.date | Unset): Latest available report date in the shop's reporting timezone,
                formatted as YYYY-MM-DD. The containing week is selected when date is omitted. Together with the preceding 11
                report weeks, it defines the supported query window; an available date does not guarantee data for every Pixel
                and attribution setting.
            next_page_token (str | Unset): Token for the next page. Pass this value unchanged as page_token in the next
                request and keep all other request parameters unchanged. An empty string means there are no more pages.
            total_count (int | Unset): Total number of unique items in the report candidate set for the current report week,
                Pixel, attribution setting, and content type, before pagination and metadata enrichment. This is not the number
                of items in the current page or all matching items in the shop. Missing or deleted content metadata does not
                reduce the count.
     """

    contents: list[GetOffSitePerformanceDetailsResponseDataContent] | Unset = UNSET
    latest_available_date: datetime.date | Unset = UNSET
    next_page_token: str | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_off_site_performance_details_response_data_content import GetOffSitePerformanceDetailsResponseDataContent # noqa: PLC0415
        contents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contents, Unset):
            contents = []
            for contents_item_data in self.contents:
                contents_item = contents_item_data.to_dict()
                contents.append(contents_item)



        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()

        next_page_token = self.next_page_token

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if contents is not UNSET:
            field_dict["contents"] = contents
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_off_site_performance_details_response_data_content import GetOffSitePerformanceDetailsResponseDataContent # noqa: PLC0415
        d = dict(src_dict)
        _contents = d.pop("contents", UNSET)
        contents: list[GetOffSitePerformanceDetailsResponseDataContent] | Unset = UNSET
        if _contents is not UNSET:
            contents = []
            for contents_item_data in _contents:
                contents_item = GetOffSitePerformanceDetailsResponseDataContent.from_dict(contents_item_data)



                contents.append(contents_item)


        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date,  Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)




        next_page_token = d.pop("next_page_token", UNSET)

        total_count = d.pop("total_count", UNSET)

        get_off_site_performance_details_response_data = cls(
            contents=contents,
            latest_available_date=latest_available_date,
            next_page_token=next_page_token,
            total_count=total_count,
        )


        get_off_site_performance_details_response_data.additional_properties = d
        return get_off_site_performance_details_response_data

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
