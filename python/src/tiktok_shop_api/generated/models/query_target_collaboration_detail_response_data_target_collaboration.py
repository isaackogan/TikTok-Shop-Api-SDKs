from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_target_collaboration_detail_response_data_target_collaboration_creator import (
        QueryTargetCollaborationDetailResponseDataTargetCollaborationCreator,
    )
    from ..models.query_target_collaboration_detail_response_data_target_collaboration_free_sample_rule import (
        QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule,
    )
    from ..models.query_target_collaboration_detail_response_data_target_collaboration_product import (
        QueryTargetCollaborationDetailResponseDataTargetCollaborationProduct,
    )
    from ..models.seller_contact_info import SellerContactInfo


T = TypeVar("T", bound="QueryTargetCollaborationDetailResponseDataTargetCollaboration")


@_attrs_define
class QueryTargetCollaborationDetailResponseDataTargetCollaboration:
    """
    Attributes:
        id (str | Unset): Target collaboration ID.
        name (str | Unset): Target collaboration name.
        message (str | Unset): Message seller has sent to creators about seller's  introduction and why excited to
            collaborate.
        seller_contact_info (SellerContactInfo | Unset):
        start_time (int | Unset): The start time of the target collaboration, as a Unix timestamp in seconds.
        end_time (int | Unset): The end time of the target collaboration, as a Unix timestamp in seconds.
        update_time (int | Unset): The update time of the target collaboration, as a Unix timestamp in seconds.
        creator_invited_count (int | Unset): The count of creators invited in the target collaboration.
            The count will only include the NORMAL state.
        showcase_creator_count (int | Unset): This field indicates the number of creators who added the product to the
            showcase from target collaboration.
            The count will only include the NORMAL state.
        content_creator_count (int | Unset): The number of creators who posted content featuring products from target
            collaboration.
            The count will only include the NORMAL state.
        product_count (int | Unset): The count of products added in the target collaboration.
            The count will only include the NORMAL state.
        free_sample_rule (QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule | Unset):
        products (list[QueryTargetCollaborationDetailResponseDataTargetCollaborationProduct] | Unset): The information
            of products in the target collaboration.
        creators (list[QueryTargetCollaborationDetailResponseDataTargetCollaborationCreator] | Unset): The information
            of creators in the target collaboration.
        type_ (str | Unset): The type of target collaboration.
            Field values:
            - STANDARD: The target collaboration is created by sellers manually selecting products and creators.
            - TOP_CREATOR_PROGRAM: The target collaboration created by seller joining TikTok Shop Top Creator Program,
            requiring only product submission.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    message: str | Unset = UNSET
    seller_contact_info: SellerContactInfo | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    update_time: int | Unset = UNSET
    creator_invited_count: int | Unset = UNSET
    showcase_creator_count: int | Unset = UNSET
    content_creator_count: int | Unset = UNSET
    product_count: int | Unset = UNSET
    free_sample_rule: QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule | Unset = UNSET
    products: list[QueryTargetCollaborationDetailResponseDataTargetCollaborationProduct] | Unset = UNSET
    creators: list[QueryTargetCollaborationDetailResponseDataTargetCollaborationCreator] | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        message = self.message

        seller_contact_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_contact_info, Unset):
            seller_contact_info = self.seller_contact_info.to_dict()

        start_time = self.start_time

        end_time = self.end_time

        update_time = self.update_time

        creator_invited_count = self.creator_invited_count

        showcase_creator_count = self.showcase_creator_count

        content_creator_count = self.content_creator_count

        product_count = self.product_count

        free_sample_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.free_sample_rule, Unset):
            free_sample_rule = self.free_sample_rule.to_dict()

        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = []
            for creators_item_data in self.creators:
                creators_item = creators_item_data.to_dict()
                creators.append(creators_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if message is not UNSET:
            field_dict["message"] = message
        if seller_contact_info is not UNSET:
            field_dict["seller_contact_info"] = seller_contact_info
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if creator_invited_count is not UNSET:
            field_dict["creator_invited_count"] = creator_invited_count
        if showcase_creator_count is not UNSET:
            field_dict["showcase_creator_count"] = showcase_creator_count
        if content_creator_count is not UNSET:
            field_dict["content_creator_count"] = content_creator_count
        if product_count is not UNSET:
            field_dict["product_count"] = product_count
        if free_sample_rule is not UNSET:
            field_dict["free_sample_rule"] = free_sample_rule
        if products is not UNSET:
            field_dict["products"] = products
        if creators is not UNSET:
            field_dict["creators"] = creators
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_target_collaboration_detail_response_data_target_collaboration_creator import (
            QueryTargetCollaborationDetailResponseDataTargetCollaborationCreator,  # noqa: PLC0415
        )
        from ..models.query_target_collaboration_detail_response_data_target_collaboration_free_sample_rule import (
            QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule,  # noqa: PLC0415
        )
        from ..models.query_target_collaboration_detail_response_data_target_collaboration_product import (
            QueryTargetCollaborationDetailResponseDataTargetCollaborationProduct,  # noqa: PLC0415
        )
        from ..models.seller_contact_info import SellerContactInfo  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        message = d.pop("message", UNSET)

        _seller_contact_info = d.pop("seller_contact_info", UNSET)
        seller_contact_info: SellerContactInfo | Unset
        if isinstance(_seller_contact_info, Unset):
            seller_contact_info = UNSET
        else:
            seller_contact_info = SellerContactInfo.from_dict(_seller_contact_info)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        update_time = d.pop("update_time", UNSET)

        creator_invited_count = d.pop("creator_invited_count", UNSET)

        showcase_creator_count = d.pop("showcase_creator_count", UNSET)

        content_creator_count = d.pop("content_creator_count", UNSET)

        product_count = d.pop("product_count", UNSET)

        _free_sample_rule = d.pop("free_sample_rule", UNSET)
        free_sample_rule: QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule | Unset
        if isinstance(_free_sample_rule, Unset):
            free_sample_rule = UNSET
        else:
            free_sample_rule = QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule.from_dict(
                _free_sample_rule
            )

        _products = d.pop("products", UNSET)
        products: list[QueryTargetCollaborationDetailResponseDataTargetCollaborationProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = QueryTargetCollaborationDetailResponseDataTargetCollaborationProduct.from_dict(
                    products_item_data
                )

                products.append(products_item)

        _creators = d.pop("creators", UNSET)
        creators: list[QueryTargetCollaborationDetailResponseDataTargetCollaborationCreator] | Unset = UNSET
        if _creators is not UNSET:
            creators = []
            for creators_item_data in _creators:
                creators_item = QueryTargetCollaborationDetailResponseDataTargetCollaborationCreator.from_dict(
                    creators_item_data
                )

                creators.append(creators_item)

        type_ = d.pop("type", UNSET)

        query_target_collaboration_detail_response_data_target_collaboration = cls(
            id=id,
            name=name,
            message=message,
            seller_contact_info=seller_contact_info,
            start_time=start_time,
            end_time=end_time,
            update_time=update_time,
            creator_invited_count=creator_invited_count,
            showcase_creator_count=showcase_creator_count,
            content_creator_count=content_creator_count,
            product_count=product_count,
            free_sample_rule=free_sample_rule,
            products=products,
            creators=creators,
            type_=type_,
        )

        query_target_collaboration_detail_response_data_target_collaboration.additional_properties = d
        return query_target_collaboration_detail_response_data_target_collaboration

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
