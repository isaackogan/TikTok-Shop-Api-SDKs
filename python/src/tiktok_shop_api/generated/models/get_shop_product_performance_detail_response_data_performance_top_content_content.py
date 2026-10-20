from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gmv import Gmv





T = TypeVar("T", bound="GetShopProductPerformanceDetailResponseDataPerformanceTopContentContent")



@_attrs_define
class GetShopProductPerformanceDetailResponseDataPerformanceTopContentContent:
    """ 
        Attributes:
            content_id (str | Unset): LIVE session ID or video ID
            items_sold (int | Unset): Number of items sold in the corresponding content.
            gmv (Gmv | Unset):
     """

    content_id: str | Unset = UNSET
    items_sold: int | Unset = UNSET
    gmv: Gmv | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gmv import Gmv # noqa: PLC0415
        content_id = self.content_id

        items_sold = self.items_sold

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if content_id is not UNSET:
            field_dict["content_id"] = content_id
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold
        if gmv is not UNSET:
            field_dict["gmv"] = gmv

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gmv import Gmv # noqa: PLC0415
        d = dict(src_dict)
        content_id = d.pop("content_id", UNSET)

        items_sold = d.pop("items_sold", UNSET)

        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv,  Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)




        get_shop_product_performance_detail_response_data_performance_top_content_content = cls(
            content_id=content_id,
            items_sold=items_sold,
            gmv=gmv,
        )


        get_shop_product_performance_detail_response_data_performance_top_content_content.additional_properties = d
        return get_shop_product_performance_detail_response_data_performance_top_content_content

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
