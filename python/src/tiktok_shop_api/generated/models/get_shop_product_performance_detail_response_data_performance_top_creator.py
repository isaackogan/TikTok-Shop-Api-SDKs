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





T = TypeVar("T", bound="GetShopProductPerformanceDetailResponseDataPerformanceTopCreator")



@_attrs_define
class GetShopProductPerformanceDetailResponseDataPerformanceTopCreator:
    """ 
        Attributes:
            creator_open_id (str | Unset): Creator/s open id, use this open id to identify the unique creator.
            creator_name (str | Unset): Creator name shown on the profile page.
            creator_profile (str | Unset): The URL to the creator's profile picture.
            gmv (Gmv | Unset):
            items_sold (int | Unset): Number of items sold by this creator.
     """

    creator_open_id: str | Unset = UNSET
    creator_name: str | Unset = UNSET
    creator_profile: str | Unset = UNSET
    gmv: Gmv | Unset = UNSET
    items_sold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gmv import Gmv # noqa: PLC0415
        creator_open_id = self.creator_open_id

        creator_name = self.creator_name

        creator_profile = self.creator_profile

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        items_sold = self.items_sold


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if creator_open_id is not UNSET:
            field_dict["creator_open_id"] = creator_open_id
        if creator_name is not UNSET:
            field_dict["creator_name"] = creator_name
        if creator_profile is not UNSET:
            field_dict["creator_profile"] = creator_profile
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gmv import Gmv # noqa: PLC0415
        d = dict(src_dict)
        creator_open_id = d.pop("creator_open_id", UNSET)

        creator_name = d.pop("creator_name", UNSET)

        creator_profile = d.pop("creator_profile", UNSET)

        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv,  Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)




        items_sold = d.pop("items_sold", UNSET)

        get_shop_product_performance_detail_response_data_performance_top_creator = cls(
            creator_open_id=creator_open_id,
            creator_name=creator_name,
            creator_profile=creator_profile,
            gmv=gmv,
            items_sold=items_sold,
        )


        get_shop_product_performance_detail_response_data_performance_top_creator.additional_properties = d
        return get_shop_product_performance_detail_response_data_performance_top_creator

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
