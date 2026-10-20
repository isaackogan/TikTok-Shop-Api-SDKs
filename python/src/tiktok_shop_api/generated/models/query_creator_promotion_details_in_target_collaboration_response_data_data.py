from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail import (
        QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetail,
    )


T = TypeVar("T", bound="QueryCreatorPromotionDetailsInTargetCollaborationResponseDataData")


@_attrs_define
class QueryCreatorPromotionDetailsInTargetCollaborationResponseDataData:
    """
    Attributes:
        product_details (list[QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetail] | Unset):
            Product detail infomation
    """

    product_details: list[QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetail] | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product_details, Unset):
            product_details = []
            for product_details_item_data in self.product_details:
                product_details_item = product_details_item_data.to_dict()
                product_details.append(product_details_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_details is not UNSET:
            field_dict["product_details"] = product_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_creator_promotion_details_in_target_collaboration_response_data_data_product_detail import (
            QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetail,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _product_details = d.pop("product_details", UNSET)
        product_details: (
            list[QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetail] | Unset
        ) = UNSET
        if _product_details is not UNSET:
            product_details = []
            for product_details_item_data in _product_details:
                product_details_item = (
                    QueryCreatorPromotionDetailsInTargetCollaborationResponseDataDataProductDetail.from_dict(
                        product_details_item_data
                    )
                )

                product_details.append(product_details_item)

        query_creator_promotion_details_in_target_collaboration_response_data_data = cls(
            product_details=product_details,
        )

        query_creator_promotion_details_in_target_collaboration_response_data_data.additional_properties = d
        return query_creator_promotion_details_in_target_collaboration_response_data_data

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
