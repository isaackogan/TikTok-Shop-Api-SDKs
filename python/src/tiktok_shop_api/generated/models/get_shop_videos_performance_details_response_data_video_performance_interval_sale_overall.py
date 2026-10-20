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





T = TypeVar("T", bound="GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSaleOverall")



@_attrs_define
class GetShopVideosPerformanceDetailsResponseDataVideoPerformanceIntervalSaleOverall:
    """ 
        Attributes:
            ctr (str | Unset): Product clicks from the video divided by impressions of all video products.
            customers (int | Unset): The total number of customers who placed orders directly from the shoppable video.
            gmv (Gmv | Unset):
            gpm (Gpm | Unset):
            items_sold (int | Unset): The total number of items sold directly from the shoppable video.
            product_clicks (int | Unset): The number of product clicks from the video.
            product_impressions (int | Unset): The number of impressions of all video products.
     """

    ctr: str | Unset = UNSET
    customers: int | Unset = UNSET
    gmv: Gmv | Unset = UNSET
    gpm: Gpm | Unset = UNSET
    items_sold: int | Unset = UNSET
    product_clicks: int | Unset = UNSET
    product_impressions: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gmv import Gmv # noqa: PLC0415
        from ..models.gpm import Gpm # noqa: PLC0415
        ctr = self.ctr

        customers = self.customers

        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        gpm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpm, Unset):
            gpm = self.gpm.to_dict()

        items_sold = self.items_sold

        product_clicks = self.product_clicks

        product_impressions = self.product_impressions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if ctr is not UNSET:
            field_dict["ctr"] = ctr
        if customers is not UNSET:
            field_dict["customers"] = customers
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if gpm is not UNSET:
            field_dict["gpm"] = gpm
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold
        if product_clicks is not UNSET:
            field_dict["product_clicks"] = product_clicks
        if product_impressions is not UNSET:
            field_dict["product_impressions"] = product_impressions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gmv import Gmv # noqa: PLC0415
        from ..models.gpm import Gpm # noqa: PLC0415
        d = dict(src_dict)
        ctr = d.pop("ctr", UNSET)

        customers = d.pop("customers", UNSET)

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




        items_sold = d.pop("items_sold", UNSET)

        product_clicks = d.pop("product_clicks", UNSET)

        product_impressions = d.pop("product_impressions", UNSET)

        get_shop_videos_performance_details_response_data_video_performance_interval_sale_overall = cls(
            ctr=ctr,
            customers=customers,
            gmv=gmv,
            gpm=gpm,
            items_sold=items_sold,
            product_clicks=product_clicks,
            product_impressions=product_impressions,
        )


        get_shop_videos_performance_details_response_data_video_performance_interval_sale_overall.additional_properties = d
        return get_shop_videos_performance_details_response_data_video_performance_interval_sale_overall

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
