from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_live_room_product_stats_response_data_product_stat import GetLiveRoomProductStatsResponseDataProductStat





T = TypeVar("T", bound="GetLiveRoomProductStatsResponseData")



@_attrs_define
class GetLiveRoomProductStatsResponseData:
    """ 
        Attributes:
            product_stats (list[GetLiveRoomProductStatsResponseDataProductStat] | Unset): Statistics for each product in the
                specified live room.
     """

    product_stats: list[GetLiveRoomProductStatsResponseDataProductStat] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_live_room_product_stats_response_data_product_stat import GetLiveRoomProductStatsResponseDataProductStat # noqa: PLC0415
        product_stats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_stats, Unset):
            product_stats = []
            for product_stats_item_data in self.product_stats:
                product_stats_item = product_stats_item_data.to_dict()
                product_stats.append(product_stats_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_stats is not UNSET:
            field_dict["product_stats"] = product_stats

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_live_room_product_stats_response_data_product_stat import GetLiveRoomProductStatsResponseDataProductStat # noqa: PLC0415
        d = dict(src_dict)
        _product_stats = d.pop("product_stats", UNSET)
        product_stats: list[GetLiveRoomProductStatsResponseDataProductStat] | Unset = UNSET
        if _product_stats is not UNSET:
            product_stats = []
            for product_stats_item_data in _product_stats:
                product_stats_item = GetLiveRoomProductStatsResponseDataProductStat.from_dict(product_stats_item_data)



                product_stats.append(product_stats_item)


        get_live_room_product_stats_response_data = cls(
            product_stats=product_stats,
        )


        get_live_room_product_stats_response_data.additional_properties = d
        return get_live_room_product_stats_response_data

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
