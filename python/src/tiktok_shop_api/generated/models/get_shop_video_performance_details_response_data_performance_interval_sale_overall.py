from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gmv import Gmv
    from ..models.gpm import Gpm


T = TypeVar("T", bound="GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleOverall")


@_attrs_define
class GetShopVideoPerformanceDetailsResponseDataPerformanceIntervalSaleOverall:
    """
    Attributes:
        gmv (Gmv | Unset):
        gpm (Gpm | Unset):
        customers (int | Unset): The total number of customers who placed orders directly from the shoppable video.
        items_sold (int | Unset): The total number of items sold directly from the shoppable video.
        ctr (str | Unset): Ratio of product clicks from the video to impressions of all products in the video, expressed
            as a decimal fraction.
        product_impressions (int | Unset): The number of impressions of all video products
        product_clicks (int | Unset): The number of product clicks from the video
    """

    gmv: Gmv | Unset = UNSET
    gpm: Gpm | Unset = UNSET
    customers: int | Unset = UNSET
    items_sold: int | Unset = UNSET
    ctr: str | Unset = UNSET
    product_impressions: int | Unset = UNSET
    product_clicks: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gmv, Unset):
            gmv = self.gmv.to_dict()

        gpm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gpm, Unset):
            gpm = self.gpm.to_dict()

        customers = self.customers

        items_sold = self.items_sold

        ctr = self.ctr

        product_impressions = self.product_impressions

        product_clicks = self.product_clicks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gmv is not UNSET:
            field_dict["gmv"] = gmv
        if gpm is not UNSET:
            field_dict["gpm"] = gpm
        if customers is not UNSET:
            field_dict["customers"] = customers
        if items_sold is not UNSET:
            field_dict["items_sold"] = items_sold
        if ctr is not UNSET:
            field_dict["ctr"] = ctr
        if product_impressions is not UNSET:
            field_dict["product_impressions"] = product_impressions
        if product_clicks is not UNSET:
            field_dict["product_clicks"] = product_clicks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gmv import Gmv  # noqa: PLC0415
        from ..models.gpm import Gpm  # noqa: PLC0415

        d = dict(src_dict)
        _gmv = d.pop("gmv", UNSET)
        gmv: Gmv | Unset
        if isinstance(_gmv, Unset):
            gmv = UNSET
        else:
            gmv = Gmv.from_dict(_gmv)

        _gpm = d.pop("gpm", UNSET)
        gpm: Gpm | Unset
        if isinstance(_gpm, Unset):
            gpm = UNSET
        else:
            gpm = Gpm.from_dict(_gpm)

        customers = d.pop("customers", UNSET)

        items_sold = d.pop("items_sold", UNSET)

        ctr = d.pop("ctr", UNSET)

        product_impressions = d.pop("product_impressions", UNSET)

        product_clicks = d.pop("product_clicks", UNSET)

        get_shop_video_performance_details_response_data_performance_interval_sale_overall = cls(
            gmv=gmv,
            gpm=gpm,
            customers=customers,
            items_sold=items_sold,
            ctr=ctr,
            product_impressions=product_impressions,
            product_clicks=product_clicks,
        )

        get_shop_video_performance_details_response_data_performance_interval_sale_overall.additional_properties = d
        return get_shop_video_performance_details_response_data_performance_interval_sale_overall

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
