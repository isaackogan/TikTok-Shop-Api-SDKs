from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info import (
        QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfo,
    )


T = TypeVar("T", bound="QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetail")


@_attrs_define
class QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetail:
    """
    Attributes:
        product_base_info (QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfo
            | Unset):
        product_add_status (bool | Unset): Product added or not
        video_count (int | Unset): Creator post video count in collaboration
        live_count (int | Unset): Creator LIVE count in collaboration
        is_commission_effective (bool | Unset): Whether the target collaboration commission for this creator-product
            pair is currently effective. `false` means an active campaign collaboration takes precedence.
    """

    product_base_info: (
        QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfo | Unset
    ) = UNSET
    product_add_status: bool | Unset = UNSET
    video_count: int | Unset = UNSET
    live_count: int | Unset = UNSET
    is_commission_effective: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_base_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_base_info, Unset):
            product_base_info = self.product_base_info.to_dict()

        product_add_status = self.product_add_status

        video_count = self.video_count

        live_count = self.live_count

        is_commission_effective = self.is_commission_effective

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_base_info is not UNSET:
            field_dict["product_base_info"] = product_base_info
        if product_add_status is not UNSET:
            field_dict["product_add_status"] = product_add_status
        if video_count is not UNSET:
            field_dict["video_count"] = video_count
        if live_count is not UNSET:
            field_dict["live_count"] = live_count
        if is_commission_effective is not UNSET:
            field_dict["is_commission_effective"] = is_commission_effective

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail_product_base_info import (
            QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _product_base_info = d.pop("product_base_info", UNSET)
        product_base_info: (
            QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfo | Unset
        )
        if isinstance(_product_base_info, Unset):
            product_base_info = UNSET
        else:
            product_base_info = (
                QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetailProductBaseInfo.from_dict(
                    _product_base_info
                )
            )

        product_add_status = d.pop("product_add_status", UNSET)

        video_count = d.pop("video_count", UNSET)

        live_count = d.pop("live_count", UNSET)

        is_commission_effective = d.pop("is_commission_effective", UNSET)

        query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail = cls(
            product_base_info=product_base_info,
            product_add_status=product_add_status,
            video_count=video_count,
            live_count=live_count,
            is_commission_effective=is_commission_effective,
        )

        query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail.additional_properties = d
        return query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail

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
