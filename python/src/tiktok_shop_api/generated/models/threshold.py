from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Threshold")


@_attrs_define
class Threshold:
    """
    Attributes:
        minimum_follower_count (int | Unset): The creator must have a follower count greater than or equal to this value
            to be eligible to request the sample.
        minimum_gmv (int | Unset): The creator must have the GMV in the past 30 days greater than this value to be
            eligible to request the sample.
        avg_ec_video_views (int | Unset): The creator must have an average number of e-commerce video views in the past
            30 days greater than or equal to this value to be eligible to request the sample.
        category_ids (list[str] | Unset): A list of product first-level category IDs.
            Use this to limit participating creators: for each creator, sort their GMV over the past 30 days by first-level
            product category. If the GMV of one of the categories is among the top three, the creator is eligible to
            participate in the event. No restriction by default.
            For example, if a creator's top three categories are [{Cellphone_ID}, {Furniture_ID}, {Food_ID}], and the value
            of tehis parameter is `[{Food_ID}]`, the creator is qualified for open collaboration.
        predicted_fulfillment_rank (str | Unset): The creators whose predicted rate of posting a shoppable video or LIVE
            after receiving a sample.
            - ALL. All creators regardless of the rate.
            - LOW. The creators whose rate is above or equal to low.
            - MEDIUM. The creators whose rate is above or equal to medium.
            - HIGH. The creators whose rate is high.
    """

    minimum_follower_count: int | Unset = UNSET
    minimum_gmv: int | Unset = UNSET
    avg_ec_video_views: int | Unset = UNSET
    category_ids: list[str] | Unset = UNSET
    predicted_fulfillment_rank: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        minimum_follower_count = self.minimum_follower_count

        minimum_gmv = self.minimum_gmv

        avg_ec_video_views = self.avg_ec_video_views

        category_ids: list[str] | Unset = UNSET
        if not isinstance(self.category_ids, Unset):
            category_ids = self.category_ids

        predicted_fulfillment_rank = self.predicted_fulfillment_rank

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if minimum_follower_count is not UNSET:
            field_dict["minimum_follower_count"] = minimum_follower_count
        if minimum_gmv is not UNSET:
            field_dict["minimum_gmv"] = minimum_gmv
        if avg_ec_video_views is not UNSET:
            field_dict["avg_ec_video_views"] = avg_ec_video_views
        if category_ids is not UNSET:
            field_dict["category_ids"] = category_ids
        if predicted_fulfillment_rank is not UNSET:
            field_dict["predicted_fulfillment_rank"] = predicted_fulfillment_rank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        minimum_follower_count = d.pop("minimum_follower_count", UNSET)

        minimum_gmv = d.pop("minimum_gmv", UNSET)

        avg_ec_video_views = d.pop("avg_ec_video_views", UNSET)

        category_ids = cast(list[str], d.pop("category_ids", UNSET))

        predicted_fulfillment_rank = d.pop("predicted_fulfillment_rank", UNSET)

        threshold = cls(
            minimum_follower_count=minimum_follower_count,
            minimum_gmv=minimum_gmv,
            avg_ec_video_views=avg_ec_video_views,
            category_ids=category_ids,
            predicted_fulfillment_rank=predicted_fulfillment_rank,
        )

        threshold.additional_properties = d
        return threshold

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
