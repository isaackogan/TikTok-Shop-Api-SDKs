from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.sample_product import SampleProduct
  from ..models.search_creator_sample_applications_response_data_sample_application_creator_fulfillment import SearchCreatorSampleApplicationsResponseDataSampleApplicationCreatorFulfillment





T = TypeVar("T", bound="SearchCreatorSampleApplicationsResponseDataSampleApplication")



@_attrs_define
class SearchCreatorSampleApplicationsResponseDataSampleApplication:
    """ 
        Attributes:
            id (str | Unset): The unique id of sample application.
            sample_product (SampleProduct | Unset):
            main_order_id (str | Unset): The sample order is generated after the sample application is approved by seller.
            activity_id (str | Unset): The sample activity identifier id(only for sample activity).
            status (str | Unset): The status of sample applications.
                The possible enumerated values are:
                - PENDING: The sample application is waiting for the seller's review.
                - AWAITING_SHIPMENT: The application is approved, and the seller needs to ship the sample.
                - SHIPPED: The sample has been shipped by the seller and is waiting for the creator to receive the package.
                - REJECT_CANCELLED: The sample application has been rejected by the seller.
                - OVERDUE_CANCELLED: The sample application has expired due to being overdue.
                - UNFULFILL_CANCELLED: The creator did not fulfill the commitment to create content within the agreed timeframe.
                - FULFILLMENT_SUSPEND: the application fulfillment was paused due to the product status being unpromotable.
                - DEL_OPEN_COLLAB: Open collaboration has been deleted.
                - SELLER_NOT_SHIP_CANCELLED: The seller did not ship the sample within the required timeframe.
                - WITHDRAW_CANCELLED: The creator withdrew the sample application before the seller approved it.
                - UNFULFILLABLE_CANCELLED: The application was cancelled due to reasons beyond the creator's control, making it
                impossible to create content.
                - OPS_CANCELLED: The application was manually cancelled by operations staff.
                - OPS_FAILED: The application was marked as failed by operations staff.
                - OPS_ COMPLETED: The application was manually marked as completed by operations staff.
                - COMPLETED: The application is complete, and the creator has posted the content.
                - TO_BE_POST: the creator has not posted videos/lives for this sample
                - POST_IN_REVIEW: the creator has posted videos/lives which have not satisfied fulfillment rules.
                - POST_FAILED: the creator has posted videos/lives and deleted them before completing sample fulfillment.
                - CANCELED: this application(order) has been canceled.
                This field allows tracking the status of a sample application throughout its lifecycle, providing visibility
                into each stage of the process for sellers and creators.
            creator_fulfillment (SearchCreatorSampleApplicationsResponseDataSampleApplicationCreatorFulfillment | Unset):
     """

    id: str | Unset = UNSET
    sample_product: SampleProduct | Unset = UNSET
    main_order_id: str | Unset = UNSET
    activity_id: str | Unset = UNSET
    status: str | Unset = UNSET
    creator_fulfillment: SearchCreatorSampleApplicationsResponseDataSampleApplicationCreatorFulfillment | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sample_product import SampleProduct # noqa: PLC0415
        from ..models.search_creator_sample_applications_response_data_sample_application_creator_fulfillment import SearchCreatorSampleApplicationsResponseDataSampleApplicationCreatorFulfillment # noqa: PLC0415
        id = self.id

        sample_product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sample_product, Unset):
            sample_product = self.sample_product.to_dict()

        main_order_id = self.main_order_id

        activity_id = self.activity_id

        status = self.status

        creator_fulfillment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator_fulfillment, Unset):
            creator_fulfillment = self.creator_fulfillment.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if sample_product is not UNSET:
            field_dict["sample_product"] = sample_product
        if main_order_id is not UNSET:
            field_dict["main_order_id"] = main_order_id
        if activity_id is not UNSET:
            field_dict["activity_id"] = activity_id
        if status is not UNSET:
            field_dict["status"] = status
        if creator_fulfillment is not UNSET:
            field_dict["creator_fulfillment"] = creator_fulfillment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sample_product import SampleProduct # noqa: PLC0415
        from ..models.search_creator_sample_applications_response_data_sample_application_creator_fulfillment import SearchCreatorSampleApplicationsResponseDataSampleApplicationCreatorFulfillment # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _sample_product = d.pop("sample_product", UNSET)
        sample_product: SampleProduct | Unset
        if isinstance(_sample_product,  Unset):
            sample_product = UNSET
        else:
            sample_product = SampleProduct.from_dict(_sample_product)




        main_order_id = d.pop("main_order_id", UNSET)

        activity_id = d.pop("activity_id", UNSET)

        status = d.pop("status", UNSET)

        _creator_fulfillment = d.pop("creator_fulfillment", UNSET)
        creator_fulfillment: SearchCreatorSampleApplicationsResponseDataSampleApplicationCreatorFulfillment | Unset
        if isinstance(_creator_fulfillment,  Unset):
            creator_fulfillment = UNSET
        else:
            creator_fulfillment = SearchCreatorSampleApplicationsResponseDataSampleApplicationCreatorFulfillment.from_dict(_creator_fulfillment)




        search_creator_sample_applications_response_data_sample_application = cls(
            id=id,
            sample_product=sample_product,
            main_order_id=main_order_id,
            activity_id=activity_id,
            status=status,
            creator_fulfillment=creator_fulfillment,
        )


        search_creator_sample_applications_response_data_sample_application.additional_properties = d
        return search_creator_sample_applications_response_data_sample_application

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
