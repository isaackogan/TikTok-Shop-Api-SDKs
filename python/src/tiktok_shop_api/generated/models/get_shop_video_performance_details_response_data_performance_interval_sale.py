from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_shop_video_performance_details_response_data_performance_interval_sale_breakdown import GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleBreakdown
  from ..models.get_shop_video_performance_details_response_data_performance_interval_sale_overall import GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleOverall





T = TypeVar("T", bound="GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSale")



@_attrs_define
class GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSale:
    """ 
        Attributes:
            overall (GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleOverall | Unset):
            breakdowns (list[GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleBreakdown] | Unset): Breakdown
                data for product-level sales performance in each interval.
     """

    overall: GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleOverall | Unset = UNSET
    breakdowns: list[GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleBreakdown] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_shop_video_performance_details_response_data_performance_interval_sale_breakdown import GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleBreakdown # noqa: PLC0415
        from ..models.get_shop_video_performance_details_response_data_performance_interval_sale_overall import GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleOverall # noqa: PLC0415
        overall: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overall, Unset):
            overall = self.overall.to_dict()

        breakdowns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.breakdowns, Unset):
            breakdowns = []
            for breakdowns_item_data in self.breakdowns:
                breakdowns_item = breakdowns_item_data.to_dict()
                breakdowns.append(breakdowns_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if overall is not UNSET:
            field_dict["overall"] = overall
        if breakdowns is not UNSET:
            field_dict["breakdowns"] = breakdowns

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_shop_video_performance_details_response_data_performance_interval_sale_breakdown import GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleBreakdown # noqa: PLC0415
        from ..models.get_shop_video_performance_details_response_data_performance_interval_sale_overall import GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleOverall # noqa: PLC0415
        d = dict(src_dict)
        _overall = d.pop("overall", UNSET)
        overall: GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleOverall | Unset
        if isinstance(_overall,  Unset):
            overall = UNSET
        else:
            overall = GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleOverall.from_dict(_overall)




        _breakdowns = d.pop("breakdowns", UNSET)
        breakdowns: list[GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleBreakdown] | Unset = UNSET
        if _breakdowns is not UNSET:
            breakdowns = []
            for breakdowns_item_data in _breakdowns:
                breakdowns_item = GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleBreakdown.from_dict(breakdowns_item_data)



                breakdowns.append(breakdowns_item)


        get_shop_video_performance_details_response_data_performance_interval_sale = cls(
            overall=overall,
            breakdowns=breakdowns,
        )


        get_shop_video_performance_details_response_data_performance_interval_sale.additional_properties = d
        return get_shop_video_performance_details_response_data_performance_interval_sale

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
