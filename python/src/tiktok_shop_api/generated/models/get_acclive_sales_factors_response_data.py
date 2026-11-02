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
  from ..models.get_acclive_sales_factors_response_data_factor import GetACCLIVESalesFactorsResponseDataFactor





T = TypeVar("T", bound="GetACCLIVESalesFactorsResponseData")



@_attrs_define
class GetACCLIVESalesFactorsResponseData:
    """ 
        Attributes:
            earliest_available_date (datetime.date | Unset): Earliest available reporting date for the requested shop,
                brand, and industry, in YYYY-MM-DD format (UTC). The reporting window must not start before this date.
            end_date (datetime.date | Unset): Inclusive end date of the reporting window, in YYYY-MM-DD format (UTC). This
                is date when supplied, or latest_available_date when date is omitted.
            factors (list[GetACCLIVESalesFactorsResponseDataFactor] | Unset): LIVE type factors for the current page,
                ordered by sort_field and sort_order. An empty array means no factors were returned for this page and selection.
            latest_available_date (datetime.date | Unset): Latest available reporting date for the requested shop, brand,
                and industry, in YYYY-MM-DD format (UTC). This is the default end_date when date is omitted.
            next_page_token (str | Unset): Token for the next page. Pass this value unchanged as page_token in the next
                request and keep all other request parameters unchanged. An empty string means there are no more pages.
            start_date (datetime.date | Unset): Inclusive start date of the reporting window, in YYYY-MM-DD format (UTC),
                calculated as end_date minus (trend_days - 1) days.
            total_count (int | Unset): Total number of factor rows matching the selected scope, category, and keyword before
                pagination.
     """

    earliest_available_date: datetime.date | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    factors: list[GetACCLIVESalesFactorsResponseDataFactor] | Unset = UNSET
    latest_available_date: datetime.date | Unset = UNSET
    next_page_token: str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acclive_sales_factors_response_data_factor import GetACCLIVESalesFactorsResponseDataFactor # noqa: PLC0415
        earliest_available_date: str | Unset = UNSET
        if not isinstance(self.earliest_available_date, Unset):
            earliest_available_date = self.earliest_available_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        factors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.factors, Unset):
            factors = []
            for factors_item_data in self.factors:
                factors_item = factors_item_data.to_dict()
                factors.append(factors_item)



        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()

        next_page_token = self.next_page_token

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if earliest_available_date is not UNSET:
            field_dict["earliest_available_date"] = earliest_available_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if factors is not UNSET:
            field_dict["factors"] = factors
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_acclive_sales_factors_response_data_factor import GetACCLIVESalesFactorsResponseDataFactor # noqa: PLC0415
        d = dict(src_dict)
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




        _factors = d.pop("factors", UNSET)
        factors: list[GetACCLIVESalesFactorsResponseDataFactor] | Unset = UNSET
        if _factors is not UNSET:
            factors = []
            for factors_item_data in _factors:
                factors_item = GetACCLIVESalesFactorsResponseDataFactor.from_dict(factors_item_data)



                factors.append(factors_item)


        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date,  Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)




        next_page_token = d.pop("next_page_token", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        total_count = d.pop("total_count", UNSET)

        get_acclive_sales_factors_response_data = cls(
            earliest_available_date=earliest_available_date,
            end_date=end_date,
            factors=factors,
            latest_available_date=latest_available_date,
            next_page_token=next_page_token,
            start_date=start_date,
            total_count=total_count,
        )


        get_acclive_sales_factors_response_data.additional_properties = d
        return get_acclive_sales_factors_response_data

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
