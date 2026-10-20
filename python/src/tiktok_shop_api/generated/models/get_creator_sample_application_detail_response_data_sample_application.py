from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_creator_sample_application_detail_response_data_sample_application_creator_fulfillment import (
        GetCreatorSampleApplicationDetailResponseDataSampleApplicationCreatorFulfillment,
    )
    from ..models.sample_product import SampleProduct


T = TypeVar("T", bound="GetCreatorSampleApplicationDetailResponseDataSampleApplication")


@_attrs_define
class GetCreatorSampleApplicationDetailResponseDataSampleApplication:
    """
    Attributes:
        id (str | Unset): Sample application identifier.
        create_time (int | Unset): Sample application create time in seconds.
        sample_product (SampleProduct | Unset):
        main_order_id (str | Unset): The sample order is generated after the sample application is approved by seller.
        activity_id (str | Unset): The sample activity identifier id( only for sample campaign).
        type_ (str | Unset): The type of creator sample application.
            - FREE_SAMPLE : free sample supplied by seller which creator can apply by themselves from pdp page.
            - SAMPLE_COUPON: creator claimed sample coupon (a type of coupon) and used it to purchase orders at a discount
            price.
            - SAMPLE_CAMPAIGN: activity organized by the platform. Creators can participate in this activity to obtain
            sample products provided by the platform for free.
        status (str | Unset): The status of sample applications.
            The possible enumerated values are:
            - PENDING: The sample application is waiting for the seller's review.
            - AWAITING_SHIPMENT: The application is approved, and the seller needs to ship the sample.
            - SHIPPED: The sample has been shipped by the seller and is waiting for the creator to receive the package.
            - CONTENT_PENDING: The creator has received the sample package and is expected to create content.
            - REJECT_CANCELLED: The sample application has been rejected by the seller.
            - OVERDUE_CANCELLED: The sample application has expired due to being overdue.
            - UNFULFILL_CANCELLED: The creator did not fulfill the commitment to create content within the agreed timeframe.
            - SELLER_NOT_SHIP_CANCELLED: The seller did not ship the sample within the required timeframe.
            - WITHDRAW_CANCELLED: The creator withdrew the sample application before the seller approved it.
            - UNFULFILLABLE_CANCELLED: The application was cancelled due to reasons beyond the creator's control, making it
            impossible to create content.
            - OPS_CANCELLED: The application was manually cancelled by operations staff.
            - OPS_FAILED: The application was marked as failed by operations staff.
            - OPS_ COMPLETED: The application was manually marked as completed by operations staff.
            - COMPLETED: The application is complete, and the creator has posted the content.
            This field allows for tracking the status of a sample application throughout its lifecycle, providing visibility
            into each stage of the process for sellers and creators.
        creator_fulfillment (GetCreatorSampleApplicationDetailResponseDataSampleApplicationCreatorFulfillment | Unset):
    """

    id: str | Unset = UNSET
    create_time: int | Unset = UNSET
    sample_product: SampleProduct | Unset = UNSET
    main_order_id: str | Unset = UNSET
    activity_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    status: str | Unset = UNSET
    creator_fulfillment: GetCreatorSampleApplicationDetailResponseDataSampleApplicationCreatorFulfillment | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        create_time = self.create_time

        sample_product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sample_product, Unset):
            sample_product = self.sample_product.to_dict()

        main_order_id = self.main_order_id

        activity_id = self.activity_id

        type_ = self.type_

        status = self.status

        creator_fulfillment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator_fulfillment, Unset):
            creator_fulfillment = self.creator_fulfillment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if sample_product is not UNSET:
            field_dict["sample_product"] = sample_product
        if main_order_id is not UNSET:
            field_dict["main_order_id"] = main_order_id
        if activity_id is not UNSET:
            field_dict["activity_id"] = activity_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if creator_fulfillment is not UNSET:
            field_dict["creator_fulfillment"] = creator_fulfillment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creator_sample_application_detail_response_data_sample_application_creator_fulfillment import (
            GetCreatorSampleApplicationDetailResponseDataSampleApplicationCreatorFulfillment,  # noqa: PLC0415
        )
        from ..models.sample_product import SampleProduct  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        create_time = d.pop("create_time", UNSET)

        _sample_product = d.pop("sample_product", UNSET)
        sample_product: SampleProduct | Unset
        if isinstance(_sample_product, Unset):
            sample_product = UNSET
        else:
            sample_product = SampleProduct.from_dict(_sample_product)

        main_order_id = d.pop("main_order_id", UNSET)

        activity_id = d.pop("activity_id", UNSET)

        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        _creator_fulfillment = d.pop("creator_fulfillment", UNSET)
        creator_fulfillment: GetCreatorSampleApplicationDetailResponseDataSampleApplicationCreatorFulfillment | Unset
        if isinstance(_creator_fulfillment, Unset):
            creator_fulfillment = UNSET
        else:
            creator_fulfillment = (
                GetCreatorSampleApplicationDetailResponseDataSampleApplicationCreatorFulfillment.from_dict(
                    _creator_fulfillment
                )
            )

        get_creator_sample_application_detail_response_data_sample_application = cls(
            id=id,
            create_time=create_time,
            sample_product=sample_product,
            main_order_id=main_order_id,
            activity_id=activity_id,
            type_=type_,
            status=status,
            creator_fulfillment=creator_fulfillment,
        )

        get_creator_sample_application_detail_response_data_sample_application.additional_properties = d
        return get_creator_sample_application_detail_response_data_sample_application

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
