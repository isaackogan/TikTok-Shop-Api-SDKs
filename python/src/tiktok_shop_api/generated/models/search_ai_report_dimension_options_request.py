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
  from ..models.creator import Creator





T = TypeVar("T", bound="SearchAIReportDimensionOptionsRequest")



@_attrs_define
class SearchAIReportDimensionOptionsRequest:
    """ 
        Attributes:
            dimension_code (str): Code of the dimension whose filter values you want to find. Select it from the catalog.
                Candidate lookup is not available for main_order_id (order ID).
            creator (Creator | Unset):
            end_date (datetime.date | Unset): Last included date of the metric data used to find entity candidates, in YYYY-
                MM-DD format and the shop timezone. Required with start_date for all entity searches except product_id or sku_id
                with a nonempty keyword. It must not be earlier than start_date. Fixed attribute options and those two keyword
                lookup modes ignore dates.
            keyword (str | Unset): Search condition for an entity dimension. product_id: Product search text. sku_id: Exact
                numeric SKU ID, not a SKU name or partial ID. room_id: Exact numeric LIVE ID. item_id: Exact numeric video ID.
                author_id: Do not supply keyword; use creator.creator_open_id. Omit keyword to list candidates from metric data,
                which requires both dates. Nonempty product_id and sku_id lookups do not require dates. Fixed attribute
                dimensions ignore keyword.
            metric_codes (list[str] | Unset): Metric codes for entity searches based on metric data. The first metric
                determines descending candidate order; pay_amt ranks by GMV. If omitted or empty, candidates are ordered by time
                descending. Fixed attribute options and product_id/sku_id lookups with a nonempty keyword ignore this field.
            start_date (datetime.date | Unset): First included date of the metric data used to find entity candidates, in
                YYYY-MM-DD format and the shop timezone. Required with end_date for all entity searches except product_id or
                sku_id with a nonempty keyword. Fixed attribute options and those two keyword lookup modes ignore dates.
     """

    dimension_code: str
    creator: Creator | Unset = UNSET
    end_date: datetime.date | Unset = UNSET
    keyword: str | Unset = UNSET
    metric_codes: list[str] | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.creator import Creator # noqa: PLC0415
        dimension_code = self.dimension_code

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        keyword = self.keyword

        metric_codes: list[str] | Unset = UNSET
        if not isinstance(self.metric_codes, Unset):
            metric_codes = self.metric_codes



        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "dimension_code": dimension_code,
        })
        if creator is not UNSET:
            field_dict["creator"] = creator
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if keyword is not UNSET:
            field_dict["keyword"] = keyword
        if metric_codes is not UNSET:
            field_dict["metric_codes"] = metric_codes
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator import Creator # noqa: PLC0415
        d = dict(src_dict)
        dimension_code = d.pop("dimension_code")

        _creator = d.pop("creator", UNSET)
        creator: Creator | Unset
        if isinstance(_creator,  Unset):
            creator = UNSET
        else:
            creator = Creator.from_dict(_creator)




        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.date | Unset
        if isinstance(_end_date,  Unset):
            end_date = UNSET
        else:
            end_date = datetime.date.fromisoformat(_end_date)




        keyword = d.pop("keyword", UNSET)

        metric_codes = cast(list[str], d.pop("metric_codes", UNSET))


        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = datetime.date.fromisoformat(_start_date)




        search_ai_report_dimension_options_request = cls(
            dimension_code=dimension_code,
            creator=creator,
            end_date=end_date,
            keyword=keyword,
            metric_codes=metric_codes,
            start_date=start_date,
        )


        search_ai_report_dimension_options_request.additional_properties = d
        return search_ai_report_dimension_options_request

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
