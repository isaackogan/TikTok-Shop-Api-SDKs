from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_off_site_performance_details_response_data_content_metric_total_gmv import GetOffSitePerformanceDetailsResponseDataContentMetricTotalGmv
  from ..models.off_site_gmv import OffSiteGmv
  from ..models.tiktok_shop_gmv import TiktokShopGmv





T = TypeVar("T", bound="GetOffSitePerformanceDetailsResponseDataContentMetric")



@_attrs_define
class GetOffSitePerformanceDetailsResponseDataContentMetric:
    """ 
        Attributes:
            off_site_effect_rate (str | Unset): Off-site GMV divided by TikTok Shop GMV for this item in the report week,
                expressed as a decimal ratio; 1.0000 means 100%, and the ratio can exceed 1. A null value indicates an
                unavailable ratio and must not be interpreted as zero; the response does not identify the cause of
                unavailability.
            off_site_gmv (OffSiteGmv | Unset):
            tiktok_shop_gmv (TiktokShopGmv | Unset):
            total_gmv (GetOffSitePerformanceDetailsResponseDataContentMetricTotalGmv | Unset):
     """

    off_site_effect_rate: str | Unset = UNSET
    off_site_gmv: OffSiteGmv | Unset = UNSET
    tiktok_shop_gmv: TiktokShopGmv | Unset = UNSET
    total_gmv: GetOffSitePerformanceDetailsResponseDataContentMetricTotalGmv | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_off_site_performance_details_response_data_content_metric_total_gmv import GetOffSitePerformanceDetailsResponseDataContentMetricTotalGmv # noqa: PLC0415
        from ..models.off_site_gmv import OffSiteGmv # noqa: PLC0415
        from ..models.tiktok_shop_gmv import TiktokShopGmv # noqa: PLC0415
        off_site_effect_rate = self.off_site_effect_rate

        off_site_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.off_site_gmv, Unset):
            off_site_gmv = self.off_site_gmv.to_dict()

        tiktok_shop_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tiktok_shop_gmv, Unset):
            tiktok_shop_gmv = self.tiktok_shop_gmv.to_dict()

        total_gmv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total_gmv, Unset):
            total_gmv = self.total_gmv.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if off_site_effect_rate is not UNSET:
            field_dict["off_site_effect_rate"] = off_site_effect_rate
        if off_site_gmv is not UNSET:
            field_dict["off_site_gmv"] = off_site_gmv
        if tiktok_shop_gmv is not UNSET:
            field_dict["tiktok_shop_gmv"] = tiktok_shop_gmv
        if total_gmv is not UNSET:
            field_dict["total_gmv"] = total_gmv

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_off_site_performance_details_response_data_content_metric_total_gmv import GetOffSitePerformanceDetailsResponseDataContentMetricTotalGmv # noqa: PLC0415
        from ..models.off_site_gmv import OffSiteGmv # noqa: PLC0415
        from ..models.tiktok_shop_gmv import TiktokShopGmv # noqa: PLC0415
        d = dict(src_dict)
        off_site_effect_rate = d.pop("off_site_effect_rate", UNSET)

        _off_site_gmv = d.pop("off_site_gmv", UNSET)
        off_site_gmv: OffSiteGmv | Unset
        if isinstance(_off_site_gmv,  Unset):
            off_site_gmv = UNSET
        else:
            off_site_gmv = OffSiteGmv.from_dict(_off_site_gmv)




        _tiktok_shop_gmv = d.pop("tiktok_shop_gmv", UNSET)
        tiktok_shop_gmv: TiktokShopGmv | Unset
        if isinstance(_tiktok_shop_gmv,  Unset):
            tiktok_shop_gmv = UNSET
        else:
            tiktok_shop_gmv = TiktokShopGmv.from_dict(_tiktok_shop_gmv)




        _total_gmv = d.pop("total_gmv", UNSET)
        total_gmv: GetOffSitePerformanceDetailsResponseDataContentMetricTotalGmv | Unset
        if isinstance(_total_gmv,  Unset):
            total_gmv = UNSET
        else:
            total_gmv = GetOffSitePerformanceDetailsResponseDataContentMetricTotalGmv.from_dict(_total_gmv)




        get_off_site_performance_details_response_data_content_metric = cls(
            off_site_effect_rate=off_site_effect_rate,
            off_site_gmv=off_site_gmv,
            tiktok_shop_gmv=tiktok_shop_gmv,
            total_gmv=total_gmv,
        )


        get_off_site_performance_details_response_data_content_metric.additional_properties = d
        return get_off_site_performance_details_response_data_content_metric

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
