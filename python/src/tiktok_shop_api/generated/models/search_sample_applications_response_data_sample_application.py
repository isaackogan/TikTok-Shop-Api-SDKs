from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_sample_applications_response_data_sample_application_creator import (
        SearchSampleApplicationsResponseDataSampleApplicationCreator,
    )
    from ..models.search_sample_applications_response_data_sample_application_product import (
        SearchSampleApplicationsResponseDataSampleApplicationProduct,
    )


T = TypeVar("T", bound="SearchSampleApplicationsResponseDataSampleApplication")


@_attrs_define
class SearchSampleApplicationsResponseDataSampleApplication:
    """
    Attributes:
        id (str | Unset): The unique id of sample request application ID
        commission_rate (str | Unset): The commission rate set by the merchant for creators for this product,
            represented as a decimal fraction with two decimal places. For example, `0.20` represents 20%. The range is
            [0.01, 0.8].
        status (str | Unset): The status of sample applications.
            The possible enumerated values are:
            - PENDING: The sample application is waiting for the seller's review.
            - AWAITING_SHIPMENT: The application is approved, and the seller needs to ship the sample.
            - SHIPPED: The sample has been shipped by the seller and is waiting for the creator to receive the package.
            - CONTENT_PENDING: The creator has received the sample package and is expected to create content.
            - REJECT_CANCELLED: The sample application has been rejected by the seller.
            - OVERDUE_CANCELLED: The sample application has expired due to being overdue.
            - UNFULFILL_CANCELLED: The creator did not fulfill the commitment to create content within the agreed timeframe.
            - DEL_OPEN_COLLAB: The open collaboration plan has been deleted.
            - SELLER_NOT_SHIP_CANCELLED: The seller did not ship the sample within the required timeframe.
            - WITHDRAW_CANCELLED: The creator withdrew the sample application before the seller approved it.
            - UNFULFILLABLE_CANCELLED: The application was cancelled due to reasons beyond the creator's control, making it
            impossible to create content.
            - OPS_CANCELLED: The application was manually cancelled by operations staff.
            - OPS_FAILED: The application was marked as failed by operations staff.
            - OPS_COMPLETED: The application was manually marked as completed by operations staff.
            - COMPLETED: The application is complete, and the creator has finished creating the content.
        order_id (str | Unset): The sample order is generated after the sample application is approved by seller
        available_quantity (int | Unset): The remaining stock quota of a sample product.
        approve_expiration_time (int | Unset): The seller approval deadline for the sample application, expressed as a
            Unix timestamp in seconds.
        shipment_expiration_time (int | Unset): The deadline for the seller to ship the sample for the application,
            expressed as a Unix timestamp in seconds.
        tracking_number (str | Unset): The logistics tracking number for the sample application order
        fulfillment_status (str | Unset): It indicates the current status of the fulfillment process. The possible
            values are:
            - PENDING: The creator is yet to fulfill the content creation obligation.
            - ONGOING: Fulfillment is in progress; content has been created and is being evaluated against criteria.
            - SUCCEED: Fulfillment has been successfully completed; the content meets the required standards.
            - FAILED: Fulfillment failed; the content did not meet the required standards.
            - OVERDUE: Fulfillment is overdue; the creator did not meet the deadline.
            - SUSPEND: Fulfillment has been suspended.
            - CANCELLED: Fulfillment has been cancelled, either by the creator or due to operational reasons.
            - EXEMPTED: The creator has been exempted from the fulfillment obligation.
        is_approvable (bool | Unset): The sample application can be approved or not.
        disapprovable_reasons (list[str] | Unset): Reasons the sample application cannot be approved. This list may be
            absent or empty even when `is_approvable` is `false`; always check `is_approvable` to determine whether approval
            is allowed.
        partner_name (str | Unset): The name of the partner if the sample application is submitted on behalf of a
            creator by an agency. It is only populated when an agency handles the application process instead of the creator
            directly.
        creator (SearchSampleApplicationsResponseDataSampleApplicationCreator | Unset):
        product (SearchSampleApplicationsResponseDataSampleApplicationProduct | Unset):
    """

    id: str | Unset = UNSET
    commission_rate: str | Unset = UNSET
    status: str | Unset = UNSET
    order_id: str | Unset = UNSET
    available_quantity: int | Unset = UNSET
    approve_expiration_time: int | Unset = UNSET
    shipment_expiration_time: int | Unset = UNSET
    tracking_number: str | Unset = UNSET
    fulfillment_status: str | Unset = UNSET
    is_approvable: bool | Unset = UNSET
    disapprovable_reasons: list[str] | Unset = UNSET
    partner_name: str | Unset = UNSET
    creator: SearchSampleApplicationsResponseDataSampleApplicationCreator | Unset = UNSET
    product: SearchSampleApplicationsResponseDataSampleApplicationProduct | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        commission_rate = self.commission_rate

        status = self.status

        order_id = self.order_id

        available_quantity = self.available_quantity

        approve_expiration_time = self.approve_expiration_time

        shipment_expiration_time = self.shipment_expiration_time

        tracking_number = self.tracking_number

        fulfillment_status = self.fulfillment_status

        is_approvable = self.is_approvable

        disapprovable_reasons: list[str] | Unset = UNSET
        if not isinstance(self.disapprovable_reasons, Unset):
            disapprovable_reasons = self.disapprovable_reasons

        partner_name = self.partner_name

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if commission_rate is not UNSET:
            field_dict["commission_rate"] = commission_rate
        if status is not UNSET:
            field_dict["status"] = status
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if available_quantity is not UNSET:
            field_dict["available_quantity"] = available_quantity
        if approve_expiration_time is not UNSET:
            field_dict["approve_expiration_time"] = approve_expiration_time
        if shipment_expiration_time is not UNSET:
            field_dict["shipment_expiration_time"] = shipment_expiration_time
        if tracking_number is not UNSET:
            field_dict["tracking_number"] = tracking_number
        if fulfillment_status is not UNSET:
            field_dict["fulfillment_status"] = fulfillment_status
        if is_approvable is not UNSET:
            field_dict["is_approvable"] = is_approvable
        if disapprovable_reasons is not UNSET:
            field_dict["disapprovable_reasons"] = disapprovable_reasons
        if partner_name is not UNSET:
            field_dict["partner_name"] = partner_name
        if creator is not UNSET:
            field_dict["creator"] = creator
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_sample_applications_response_data_sample_application_creator import (
            SearchSampleApplicationsResponseDataSampleApplicationCreator,  # noqa: PLC0415
        )
        from ..models.search_sample_applications_response_data_sample_application_product import (
            SearchSampleApplicationsResponseDataSampleApplicationProduct,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        commission_rate = d.pop("commission_rate", UNSET)

        status = d.pop("status", UNSET)

        order_id = d.pop("order_id", UNSET)

        available_quantity = d.pop("available_quantity", UNSET)

        approve_expiration_time = d.pop("approve_expiration_time", UNSET)

        shipment_expiration_time = d.pop("shipment_expiration_time", UNSET)

        tracking_number = d.pop("tracking_number", UNSET)

        fulfillment_status = d.pop("fulfillment_status", UNSET)

        is_approvable = d.pop("is_approvable", UNSET)

        disapprovable_reasons = cast(list[str], d.pop("disapprovable_reasons", UNSET))

        partner_name = d.pop("partner_name", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: SearchSampleApplicationsResponseDataSampleApplicationCreator | Unset
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = SearchSampleApplicationsResponseDataSampleApplicationCreator.from_dict(_creator)

        _product = d.pop("product", UNSET)
        product: SearchSampleApplicationsResponseDataSampleApplicationProduct | Unset
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = SearchSampleApplicationsResponseDataSampleApplicationProduct.from_dict(_product)

        search_sample_applications_response_data_sample_application = cls(
            id=id,
            commission_rate=commission_rate,
            status=status,
            order_id=order_id,
            available_quantity=available_quantity,
            approve_expiration_time=approve_expiration_time,
            shipment_expiration_time=shipment_expiration_time,
            tracking_number=tracking_number,
            fulfillment_status=fulfillment_status,
            is_approvable=is_approvable,
            disapprovable_reasons=disapprovable_reasons,
            partner_name=partner_name,
            creator=creator,
            product=product,
        )

        search_sample_applications_response_data_sample_application.additional_properties = d
        return search_sample_applications_response_data_sample_application

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
