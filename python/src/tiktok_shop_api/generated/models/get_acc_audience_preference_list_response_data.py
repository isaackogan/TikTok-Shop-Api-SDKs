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
  from ..models.get_acc_audience_preference_list_response_data_item import GetACCAudiencePreferenceListResponseDataItem





T = TypeVar("T", bound="GetACCAudiencePreferenceListResponseData")



@_attrs_define
class GetACCAudiencePreferenceListResponseData:
    """ 
        Attributes:
            audience_type (str | Unset): ACC audience segment used for this ranking, corresponding to the request
                `audience_type`.
            earliest_available_date (datetime.date | Unset): Earliest available analysis date for the selected shop, brand
                and industry, in `YYYY-MM-DD` format (UTC). The analysis window must not start before this date.
            end_date (datetime.date | Unset): Inclusive end date of the analysis window, in `YYYY-MM-DD` format (UTC).
                Equals the requested `date`, or the latest available date when `date` is omitted.
            entity_type (str | Unset): Type of entity in this ranking: `PRODUCT`, `LIVE`, `VIDEO` or `PHOTO`, corresponding
                to the request `entity_type`.
            items (list[GetACCAudiencePreferenceListResponseDataItem] | Unset): Current page of ranked entities for the
                requested `entity_type`, after applying the selected audience, scope and filters. Each entry includes its rank,
                entity information and preference metrics. An empty array means no results for the selected entity and filters;
                missing entity metadata does not remove an otherwise valid metrics record.
            latest_available_date (datetime.date | Unset): Latest available analysis date for the selected shop, brand and
                industry, in `YYYY-MM-DD` format (UTC). Used as the analysis end date when the request `date` is omitted.
            next_page_token (str | Unset): Token for the next page. Pass this value unchanged as page_token in the next
                request and keep all other request parameters unchanged. An empty string means there are no more pages.
            scope (str | Unset): Scope used for this ranking: `MY_SHOP` for shop-level results or `MARKET` for market-level
                results.
            start_date (datetime.date | Unset): Inclusive start date of the analysis window, in `YYYY-MM-DD` format (UTC).
                Calculated as `end_date` minus `trend_days - 1` days.
            total_count (int | Unset): Total number of matching ranking entries after filtering and before pagination.
     """

    audience_type: str | Unset = UNSET
    earliest_available_date: datetime.date | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    entity_type: str | Unset = UNSET
    items: list[GetACCAudiencePreferenceListResponseDataItem] | Unset = UNSET
    latest_available_date: datetime.date | Unset = UNSET
    next_page_token: str | Unset = UNSET
    scope: str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_audience_preference_list_response_data_item import GetACCAudiencePreferenceListResponseDataItem # noqa: PLC0415
        audience_type = self.audience_type

        earliest_available_date: str | Unset = UNSET
        if not isinstance(self.earliest_available_date, Unset):
            earliest_available_date = self.earliest_available_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        entity_type = self.entity_type

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()

        next_page_token = self.next_page_token

        scope = self.scope

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if audience_type is not UNSET:
            field_dict["audience_type"] = audience_type
        if earliest_available_date is not UNSET:
            field_dict["earliest_available_date"] = earliest_available_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if entity_type is not UNSET:
            field_dict["entity_type"] = entity_type
        if items is not UNSET:
            field_dict["items"] = items
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if scope is not UNSET:
            field_dict["scope"] = scope
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_acc_audience_preference_list_response_data_item import GetACCAudiencePreferenceListResponseDataItem # noqa: PLC0415
        d = dict(src_dict)
        audience_type = d.pop("audience_type", UNSET)

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




        entity_type = d.pop("entity_type", UNSET)

        _items = d.pop("items", UNSET)
        items: list[GetACCAudiencePreferenceListResponseDataItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = GetACCAudiencePreferenceListResponseDataItem.from_dict(items_item_data)



                items.append(items_item)


        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date,  Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)




        next_page_token = d.pop("next_page_token", UNSET)

        scope = d.pop("scope", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        total_count = d.pop("total_count", UNSET)

        get_acc_audience_preference_list_response_data = cls(
            audience_type=audience_type,
            earliest_available_date=earliest_available_date,
            end_date=end_date,
            entity_type=entity_type,
            items=items,
            latest_available_date=latest_available_date,
            next_page_token=next_page_token,
            scope=scope,
            start_date=start_date,
            total_count=total_count,
        )


        get_acc_audience_preference_list_response_data.additional_properties = d
        return get_acc_audience_preference_list_response_data

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
