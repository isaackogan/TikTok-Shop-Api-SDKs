from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_gmv import SearchGmv





T = TypeVar("T", bound="GetPostViewSearchVideoResponseDataVideoMetric")



@_attrs_define
class GetPostViewSearchVideoResponseDataVideoMetric:
    """ 
        Attributes:
            search_gmv (SearchGmv):
            search_count (int | Unset): Post-view search page views (PV), not unique search users.
            search_order_count (int | Unset): Post-view search SKU order count, not a deduplicated parent-order count.
            search_product_impression_count (int | Unset): Product impressions from post-view searches.
            video_view_count (int | Unset): Video view count using the same measure as the seller-facing video views metric.
                This is not a separate impression count.
     """

    search_gmv: SearchGmv
    search_count: int | Unset = UNSET
    search_order_count: int | Unset = UNSET
    search_product_impression_count: int | Unset = UNSET
    video_view_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_gmv import SearchGmv # noqa: PLC0415
        search_gmv = self.search_gmv.to_dict()

        search_count = self.search_count

        search_order_count = self.search_order_count

        search_product_impression_count = self.search_product_impression_count

        video_view_count = self.video_view_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "search_gmv": search_gmv,
        })
        if search_count is not UNSET:
            field_dict["search_count"] = search_count
        if search_order_count is not UNSET:
            field_dict["search_order_count"] = search_order_count
        if search_product_impression_count is not UNSET:
            field_dict["search_product_impression_count"] = search_product_impression_count
        if video_view_count is not UNSET:
            field_dict["video_view_count"] = video_view_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_gmv import SearchGmv # noqa: PLC0415
        d = dict(src_dict)
        search_gmv = SearchGmv.from_dict(d.pop("search_gmv"))




        search_count = d.pop("search_count", UNSET)

        search_order_count = d.pop("search_order_count", UNSET)

        search_product_impression_count = d.pop("search_product_impression_count", UNSET)

        video_view_count = d.pop("video_view_count", UNSET)

        get_post_view_search_video_response_data_video_metric = cls(
            search_gmv=search_gmv,
            search_count=search_count,
            search_order_count=search_order_count,
            search_product_impression_count=search_product_impression_count,
            video_view_count=video_view_count,
        )


        get_post_view_search_video_response_data_video_metric.additional_properties = d
        return get_post_view_search_video_response_data_video_metric

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
