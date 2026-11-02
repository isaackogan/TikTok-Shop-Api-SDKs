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
  from ..models.get_acc_top_sales_categories_response_data_category import GetACCTopSalesCategoriesResponseDataCategory





T = TypeVar("T", bound="GetACCTopSalesCategoriesResponseData")



@_attrs_define
class GetACCTopSalesCategoriesResponseData:
    """ 
        Attributes:
            categories (list[GetACCTopSalesCategoriesResponseDataCategory] | Unset): Current page of level-2 category
                rankings, with their level-3 children after scope and keyword filtering. Sorting, page_size and page_token apply
                to this top-level list.
            earliest_available_date (datetime.date | Unset): Earliest available UTC data date for the requested shop, brand
                and industry, in YYYY-MM-DD format. The start_date must not precede this date.
            end_date (datetime.date | Unset): Inclusive end date of the data window used for the ranking, in UTC using YYYY-
                MM-DD format. It is the requested date, or the latest available date when date is omitted.
            latest_available_date (datetime.date | Unset): Latest available UTC data date for the requested shop, brand and
                industry, in YYYY-MM-DD format. Used as end_date when date is omitted.
            next_page_token (str | Unset): Token for the next page. Pass this value unchanged as page_token in the next
                request and keep all other request parameters unchanged. An empty string means there are no more pages.
            start_date (datetime.date | Unset): Inclusive start date of the data window used for the ranking, in UTC using
                YYYY-MM-DD format. It is end_date - (trend_days - 1) days.
            total_count (int | Unset): Total number of matching level-2 categories before pagination. Level-3 children are
                excluded.
     """

    categories: list[GetACCTopSalesCategoriesResponseDataCategory] | Unset = UNSET
    earliest_available_date: datetime.date | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    latest_available_date: datetime.date | Unset = UNSET
    next_page_token: str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_top_sales_categories_response_data_category import GetACCTopSalesCategoriesResponseDataCategory # noqa: PLC0415
        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)



        earliest_available_date: str | Unset = UNSET
        if not isinstance(self.earliest_available_date, Unset):
            earliest_available_date = self.earliest_available_date.isoformat()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

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
        if categories is not UNSET:
            field_dict["categories"] = categories
        if earliest_available_date is not UNSET:
            field_dict["earliest_available_date"] = earliest_available_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
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
        from ..models.get_acc_top_sales_categories_response_data_category import GetACCTopSalesCategoriesResponseDataCategory # noqa: PLC0415
        d = dict(src_dict)
        _categories = d.pop("categories", UNSET)
        categories: list[GetACCTopSalesCategoriesResponseDataCategory] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = GetACCTopSalesCategoriesResponseDataCategory.from_dict(categories_item_data)



                categories.append(categories_item)


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




        next_page_token = d.pop("next_page_token", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        total_count = d.pop("total_count", UNSET)

        get_acc_top_sales_categories_response_data = cls(
            categories=categories,
            earliest_available_date=earliest_available_date,
            end_date=end_date,
            latest_available_date=latest_available_date,
            next_page_token=next_page_token,
            start_date=start_date,
            total_count=total_count,
        )


        get_acc_top_sales_categories_response_data.additional_properties = d
        return get_acc_top_sales_categories_response_data

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
