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
  from ..models.gpm import Gpm





T = TypeVar("T", bound="GetShopVideoProductPerformanceListResponseDataProduct")



@_attrs_define
class GetShopVideoProductPerformanceListResponseDataProduct:
    """ 
        Attributes:
            ctr (str | Unset): Ratio of product clicks to product impressions in raw decimal format.
            customers (int | Unset): Number of customers who purchased the product.
            daily_avg_buyers (str | Unset): Average number of buyers per day for the current product.
            gmv (Gmv | Unset):
            gpm (Gpm | Unset):
            id (str | Unset): The ID of the product promoted in the video.
            name (str | Unset): The name of the product promoted in the video.
            product_clicks (int | Unset): Number of product clicks.
            product_impressions (int | Unset): Number of product impressions.
            units_sold (int | Unset): Number of units sold for the current product.
     """

    ctr: str | Unset = UNSET
    customers: int | Unset = UNSET
    daily_avg_buyers: str | Unset = UNSET
    gmv: Gmv | Unset = UNSET
    gpm: Gpm | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    product_clicks: int | Unset = UNSET
    product_impressions: int | Unset = UNSET
    units_sold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gmv import Gmv # noqa: PLC0415
        from ..models.gpm import Gpm # noqa: PLC0415
        ctr = self.ctr

        customers = self.customers

        daily_avg_buyers = self.daily_avg_buyers

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        gpm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpm, Unset):
            gpm = self.gpm.to_dict()

        id = self.id

        name = self.name

        product_clicks = self.product_clicks

        product_impressions = self.product_impressions

        units_sold = self.units_sold


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ctr is not UNSET:
            field_dict["ctr"] = ctr
        if customers is not UNSET:
            field_dict["customers"] = customers
        if daily_avg_buyers is not UNSET:
            field_dict["daily_avg_buyers"] = daily_avg_buyers
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if gpm is not UNSET:
            field_dict["gpm"] = gpm
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if product_clicks is not UNSET:
            field_dict["product_clicks"] = product_clicks
        if product_impressions is not UNSET:
            field_dict["product_impressions"] = product_impressions
        if units_sold is not UNSET:
            field_dict["units_sold"] = units_sold

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gmv import Gmv # noqa: PLC0415
        from ..models.gpm import Gpm # noqa: PLC0415
        d = dict(src_dict)
        ctr = d.pop("ctr", UNSET)

        customers = d.pop("customers", UNSET)

        daily_avg_buyers = d.pop("daily_avg_buyers", UNSET)

        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv,  Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)




        _gpm = d.pop("gpm", UNSET)
        gpm: Gpm | Unset
        if isinstance(_gpm,  Unset):
            gpm = UNSET
        else:
            gpm = Gpm.from_dict(_gpm)




        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        product_clicks = d.pop("product_clicks", UNSET)

        product_impressions = d.pop("product_impressions", UNSET)

        units_sold = d.pop("units_sold", UNSET)

        get_shop_video_product_performance_list_response_data_product = cls(
            ctr=ctr,
            customers=customers,
            daily_avg_buyers=daily_avg_buyers,
            gmv=gmv,
            gpm=gpm,
            id=id,
            name=name,
            product_clicks=product_clicks,
            product_impressions=product_impressions,
            units_sold=units_sold,
        )


        get_shop_video_product_performance_list_response_data_product.additional_properties = d
        return get_shop_video_product_performance_list_response_data_product

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
