from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.query_creator_promotion_details_in_target_collaboration_request_query_type import (
    QueryCreatorPromotionDetailsInTargetCollaborationRequestQueryType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_creator_promotion_details_in_target_collaboration_request_product_filter import (
        QueryCreatorPromotionDetailsInTargetCollaborationRequestProductFilter,
    )


T = TypeVar("T", bound="QueryCreatorPromotionDetailsInTargetCollaborationRequest")


@_attrs_define
class QueryCreatorPromotionDetailsInTargetCollaborationRequest:
    """
    Attributes:
        creator_user_open_id (str): Creator open id
        invitation_group_id (str): Invitation Group Id
        query (str | Unset): Product ID or product title to match, as selected by `query_type`. Provide both fields to
            filter the returned products.
        query_type (QueryCreatorPromotionDetailsInTargetCollaborationRequestQueryType | Unset): Specifies how `query`
            filters products. Possible values:
            - `PRODUCT_ID`: Match the product ID exactly.
            - `PRODUCT_NAME`: Match product titles by case-sensitive substring.
        invitation_id (str | Unset): Creator Invitation Id
        product_filter (QueryCreatorPromotionDetailsInTargetCollaborationRequestProductFilter | Unset):
    """

    creator_user_open_id: str
    invitation_group_id: str
    query: str | Unset = UNSET
    query_type: QueryCreatorPromotionDetailsInTargetCollaborationRequestQueryType | Unset = UNSET
    invitation_id: str | Unset = UNSET
    product_filter: QueryCreatorPromotionDetailsInTargetCollaborationRequestProductFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator_user_open_id = self.creator_user_open_id

        invitation_group_id = self.invitation_group_id

        query = self.query

        query_type: str | Unset = UNSET
        if not isinstance(self.query_type, Unset):
            query_type = self.query_type.value

        invitation_id = self.invitation_id

        product_filter: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_filter, Unset):
            product_filter = self.product_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creator_user_open_id": creator_user_open_id,
                "invitation_group_id": invitation_group_id,
            }
        )
        if query is not UNSET:
            field_dict["query"] = query
        if query_type is not UNSET:
            field_dict["query_type"] = query_type
        if invitation_id is not UNSET:
            field_dict["invitation_id"] = invitation_id
        if product_filter is not UNSET:
            field_dict["product_filter"] = product_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_creator_promotion_details_in_target_collaboration_request_product_filter import (
            QueryCreatorPromotionDetailsInTargetCollaborationRequestProductFilter,  # noqa: PLC0415
        )

        d = dict(src_dict)
        creator_user_open_id = d.pop("creator_user_open_id")

        invitation_group_id = d.pop("invitation_group_id")

        query = d.pop("query", UNSET)

        _query_type = d.pop("query_type", UNSET)
        query_type: QueryCreatorPromotionDetailsInTargetCollaborationRequestQueryType | Unset
        if isinstance(_query_type, Unset):
            query_type = UNSET
        else:
            query_type = QueryCreatorPromotionDetailsInTargetCollaborationRequestQueryType(_query_type)

        invitation_id = d.pop("invitation_id", UNSET)

        _product_filter = d.pop("product_filter", UNSET)
        product_filter: QueryCreatorPromotionDetailsInTargetCollaborationRequestProductFilter | Unset
        if isinstance(_product_filter, Unset):
            product_filter = UNSET
        else:
            product_filter = QueryCreatorPromotionDetailsInTargetCollaborationRequestProductFilter.from_dict(
                _product_filter
            )

        query_creator_promotion_details_in_target_collaboration_request = cls(
            creator_user_open_id=creator_user_open_id,
            invitation_group_id=invitation_group_id,
            query=query,
            query_type=query_type,
            invitation_id=invitation_id,
            product_filter=product_filter,
        )

        query_creator_promotion_details_in_target_collaboration_request.additional_properties = d
        return query_creator_promotion_details_in_target_collaboration_request

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
