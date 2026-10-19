from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_sample_applications_request_status import SearchSampleApplicationsRequestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchSampleApplicationsRequest")


@_attrs_define
class SearchSampleApplicationsRequest:
    """
    Attributes:
        product_id (str | Unset): The unique identifier of a product. It is used to specify which product's sample
            application details are being queried.
        title (str | Unset): Product name, supports fuzzy search queries. It allows sellers to search for products by
            name when managing sample applications.
        creator_user_oepn_id (str | Unset): The creator's Open ID. Do not use a user ID, creator ID, or seller ID. Send
            this property as `creator_user_oepn_id` exactly as spelled; do not change the wire key to
            `creator_user_open_id`.
        username (str | Unset): TikTok User Name of a creator, supports fuzzy search
        target_collabration_id (str | Unset): The unique ID generated after creating a target collaboration. Send this
            property as `target_collabration_id` exactly as spelled; do not change the wire key to
            `target_collaboration_id`.
        order_id (str | Unset): Main order ID associated with a sample order when the sample application is approved by
            seller.
        status (SearchSampleApplicationsRequestStatus | Unset): The status of sample applications.
            The possible enumerated values are:
            - PENDING: The sample application is waiting for the seller's review.
            - AWAITING_SHIPMENT: The application is approved, and the seller needs to ship the sample.
            - SHIPPED: The sample has been shipped by the seller and is waiting for the creator to receive the package.
            - CONTENT_PENDING: The creator has received the sample package and is expected to create content.
            - REJECT_CANCELLED: The sample application has been rejected by the seller.
            - OVERDUE_CANCELLED: The sample application has expired due to being overdue.
            - UNFULFILL_CANCELLED: The creator did not fulfill the commitment to create content within the agreed timeframe.
            - DEL_OPEN_COLLAB: Open collaboration has been deleted.
            - SELLER_NOT_SHIP_CANCELLED: The seller did not ship the sample within the required timeframe.
            - WITHDRAW_CANCELLED: The creator withdrew the sample application before the seller approved it.
            - UNFULFILLABLE_CANCELLED: The application was cancelled due to reasons beyond the creator's control, making it
            impossible to create content.
            - OPS_CANCELLED: The application was manually cancelled by operations staff.
            - OPS_FAILED: The application was marked as failed by operations staff.
            - OPS_COMPLETED: The application was manually marked as completed by operations staff.
            - COMPLETED: The application is complete, and the creator has posted the content.
            This field allows for tracking the status of a sample application throughout its lifecycle, providing visibility
            into each stage of the process for sellers and creators.
    """

    product_id: str | Unset = UNSET
    title: str | Unset = UNSET
    creator_user_oepn_id: str | Unset = UNSET
    username: str | Unset = UNSET
    target_collabration_id: str | Unset = UNSET
    order_id: str | Unset = UNSET
    status: SearchSampleApplicationsRequestStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        title = self.title

        creator_user_oepn_id = self.creator_user_oepn_id

        username = self.username

        target_collabration_id = self.target_collabration_id

        order_id = self.order_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if title is not UNSET:
            field_dict["title"] = title
        if creator_user_oepn_id is not UNSET:
            field_dict["creator_user_oepn_id"] = creator_user_oepn_id
        if username is not UNSET:
            field_dict["username"] = username
        if target_collabration_id is not UNSET:
            field_dict["target_collabration_id"] = target_collabration_id
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        title = d.pop("title", UNSET)

        creator_user_oepn_id = d.pop("creator_user_oepn_id", UNSET)

        username = d.pop("username", UNSET)

        target_collabration_id = d.pop("target_collabration_id", UNSET)

        order_id = d.pop("order_id", UNSET)

        _status = d.pop("status", UNSET)
        status: SearchSampleApplicationsRequestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SearchSampleApplicationsRequestStatus(_status)

        search_sample_applications_request = cls(
            product_id=product_id,
            title=title,
            creator_user_oepn_id=creator_user_oepn_id,
            username=username,
            target_collabration_id=target_collabration_id,
            order_id=order_id,
            status=status,
        )

        search_sample_applications_request.additional_properties = d
        return search_sample_applications_request

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
