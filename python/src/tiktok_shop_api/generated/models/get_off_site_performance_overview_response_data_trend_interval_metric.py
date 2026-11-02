from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.off_site_gmv import OffSiteGmv
  from ..models.tiktok_shop_gmv import TiktokShopGmv





T = TypeVar("T", bound="GetOffSitePerformanceOverviewResponseDataTrendIntervalMetric")



@_attrs_define
class GetOffSitePerformanceOverviewResponseDataTrendIntervalMetric:
    """ 
        Attributes:
            live_off_site_effect_rate (str | Unset): Off-site GMV divided by TikTok Shop GMV for LIVE content in this weekly
                interval, expressed as a decimal ratio.
            off_site_effect_rate (str | Unset): Off-site GMV divided by TikTok Shop GMV for all content in this weekly
                interval, expressed as a decimal ratio.
            off_site_gmv (OffSiteGmv | Unset):
            product_card_off_site_effect_rate (str | Unset): Off-site GMV divided by TikTok Shop GMV for product-card
                content in this weekly interval, expressed as a decimal ratio.
            tiktok_shop_gmv (TiktokShopGmv | Unset):
            video_off_site_effect_rate (str | Unset): Off-site GMV divided by TikTok Shop GMV for video content in this
                weekly interval, expressed as a decimal ratio.
     """

    live_off_site_effect_rate: str | Unset = UNSET
    off_site_effect_rate: str | Unset = UNSET
    off_site_gmv: OffSiteGmv | Unset = UNSET
    product_card_off_site_effect_rate: str | Unset = UNSET
    tiktok_shop_gmv: TiktokShopGmv | Unset = UNSET
    video_off_site_effect_rate: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.off_site_gmv import OffSiteGmv # noqa: PLC0415
        from ..models.tiktok_shop_gmv import TiktokShopGmv # noqa: PLC0415
        live_off_site_effect_rate = self.live_off_site_effect_rate

        off_site_effect_rate = self.off_site_effect_rate

        off_site_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.off_site_gmv, Unset):
            off_site_gmv = self.off_site_gmv.to_dict()

        product_card_off_site_effect_rate = self.product_card_off_site_effect_rate

        tiktok_shop_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tiktok_shop_gmv, Unset):
            tiktok_shop_gmv = self.tiktok_shop_gmv.to_dict()

        video_off_site_effect_rate = self.video_off_site_effect_rate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if live_off_site_effect_rate is not UNSET:
            field_dict["live_off_site_effect_rate"] = live_off_site_effect_rate
        if off_site_effect_rate is not UNSET:
            field_dict["off_site_effect_rate"] = off_site_effect_rate
        if off_site_gmv is not UNSET:
            field_dict["off_site_gmv"] = off_site_gmv
        if product_card_off_site_effect_rate is not UNSET:
            field_dict["product_card_off_site_effect_rate"] = product_card_off_site_effect_rate
        if tiktok_shop_gmv is not UNSET:
            field_dict["tiktok_shop_gmv"] = tiktok_shop_gmv
        if video_off_site_effect_rate is not UNSET:
            field_dict["video_off_site_effect_rate"] = video_off_site_effect_rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.off_site_gmv import OffSiteGmv # noqa: PLC0415
        from ..models.tiktok_shop_gmv import TiktokShopGmv # noqa: PLC0415
        d = dict(src_dict)
        live_off_site_effect_rate = d.pop("live_off_site_effect_rate", UNSET)

        off_site_effect_rate = d.pop("off_site_effect_rate", UNSET)

        _off_site_gmv = d.pop("off_site_gmv", UNSET)
        off_site_gmv: OffSiteGmv | Unset
        if isinstance(_off_site_gmv,  Unset):
            off_site_gmv = UNSET
        else:
            off_site_gmv = OffSiteGmv.from_dict(_off_site_gmv)




        product_card_off_site_effect_rate = d.pop("product_card_off_site_effect_rate", UNSET)

        _tiktok_shop_gmv = d.pop("tiktok_shop_gmv", UNSET)
        tiktok_shop_gmv: TiktokShopGmv | Unset
        if isinstance(_tiktok_shop_gmv,  Unset):
            tiktok_shop_gmv = UNSET
        else:
            tiktok_shop_gmv = TiktokShopGmv.from_dict(_tiktok_shop_gmv)




        video_off_site_effect_rate = d.pop("video_off_site_effect_rate", UNSET)

        get_off_site_performance_overview_response_data_trend_interval_metric = cls(
            live_off_site_effect_rate=live_off_site_effect_rate,
            off_site_effect_rate=off_site_effect_rate,
            off_site_gmv=off_site_gmv,
            product_card_off_site_effect_rate=product_card_off_site_effect_rate,
            tiktok_shop_gmv=tiktok_shop_gmv,
            video_off_site_effect_rate=video_off_site_effect_rate,
        )


        get_off_site_performance_overview_response_data_trend_interval_metric.additional_properties = d
        return get_off_site_performance_overview_response_data_trend_interval_metric

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
