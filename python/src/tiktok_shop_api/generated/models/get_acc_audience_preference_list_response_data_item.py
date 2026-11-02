from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_acc_audience_preference_list_response_data_item_entity_detail import GetACCAudiencePreferenceListResponseDataItemEntityDetail
  from ..models.metric import Metric





T = TypeVar("T", bound="GetACCAudiencePreferenceListResponseDataItem")



@_attrs_define
class GetACCAudiencePreferenceListResponseDataItem:
    """ 
        Attributes:
            entity_cover (str | Unset): Cover image URL for the product, live stream, video or photo post, when available.
                For `PHOTO`, this is the first image URL.
            entity_detail (GetACCAudiencePreferenceListResponseDataItemEntityDetail | Unset):
            entity_id (str | Unset): ID of the ranked entity: product ID for `PRODUCT`, live stream room ID for `LIVE`,
                video ID for `VIDEO`, or photo post ID for `PHOTO`.
            entity_name (str | Unset): Product name for `PRODUCT`, live stream title for `LIVE`, or content title for
                `VIDEO` and `PHOTO`, when available.
            metrics (Metric | Unset):
            rank (int | Unset): One-based position of this entry in the requested ordering, continuing across pages. This is
                a display position for the current pagination sequence, not a stable business ranking.
     """

    entity_cover: str | Unset = UNSET
    entity_detail: GetACCAudiencePreferenceListResponseDataItemEntityDetail | Unset = UNSET
    entity_id: str | Unset = UNSET
    entity_name: str | Unset = UNSET
    metrics: Metric | Unset = UNSET
    rank: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_audience_preference_list_response_data_item_entity_detail import GetACCAudiencePreferenceListResponseDataItemEntityDetail # noqa: PLC0415
        from ..models.metric import Metric # noqa: PLC0415
        entity_cover = self.entity_cover

        entity_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_detail, Unset):
            entity_detail = self.entity_detail.to_dict()

        entity_id = self.entity_id

        entity_name = self.entity_name

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        rank = self.rank


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if entity_cover is not UNSET:
            field_dict["entity_cover"] = entity_cover
        if entity_detail is not UNSET:
            field_dict["entity_detail"] = entity_detail
        if entity_id is not UNSET:
            field_dict["entity_id"] = entity_id
        if entity_name is not UNSET:
            field_dict["entity_name"] = entity_name
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if rank is not UNSET:
            field_dict["rank"] = rank

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_acc_audience_preference_list_response_data_item_entity_detail import GetACCAudiencePreferenceListResponseDataItemEntityDetail # noqa: PLC0415
        from ..models.metric import Metric # noqa: PLC0415
        d = dict(src_dict)
        entity_cover = d.pop("entity_cover", UNSET)

        _entity_detail = d.pop("entity_detail", UNSET)
        entity_detail: GetACCAudiencePreferenceListResponseDataItemEntityDetail | Unset
        if isinstance(_entity_detail,  Unset):
            entity_detail = UNSET
        else:
            entity_detail = GetACCAudiencePreferenceListResponseDataItemEntityDetail.from_dict(_entity_detail)




        entity_id = d.pop("entity_id", UNSET)

        entity_name = d.pop("entity_name", UNSET)

        _metrics = d.pop("metrics", UNSET)
        metrics: Metric | Unset
        if isinstance(_metrics,  Unset):
            metrics = UNSET
        else:
            metrics = Metric.from_dict(_metrics)




        rank = d.pop("rank", UNSET)

        get_acc_audience_preference_list_response_data_item = cls(
            entity_cover=entity_cover,
            entity_detail=entity_detail,
            entity_id=entity_id,
            entity_name=entity_name,
            metrics=metrics,
            rank=rank,
        )


        get_acc_audience_preference_list_response_data_item.additional_properties = d
        return get_acc_audience_preference_list_response_data_item

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
