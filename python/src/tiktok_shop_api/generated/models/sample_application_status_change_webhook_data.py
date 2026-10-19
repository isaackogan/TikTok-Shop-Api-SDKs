from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sample_application_status_change_webhook_data_new_status import (
    SampleApplicationStatusChangeWebhookDataNewStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sample_application_status_change_webhook_data_creator import (
        SampleApplicationStatusChangeWebhookDataCreator,
    )
    from ..models.sample_application_status_change_webhook_data_product import (
        SampleApplicationStatusChangeWebhookDataProduct,
    )


T = TypeVar("T", bound="SampleApplicationStatusChangeWebhookData")


@_attrs_define
class SampleApplicationStatusChangeWebhookData:
    """
    Attributes:
        application_id (str | Unset): The id of the sample application
        new_status (SampleApplicationStatusChangeWebhookDataNewStatus | Unset): The status of sample applications.
             The possible enumerated values are:

             * `PENDING`: The sample application is waiting for the seller's review.
             * `AWAITING_SHIPMENT`: The application is approved, and the seller needs to ship the sample.
             * `SHIPPED`: The sample has been shipped by the seller and is waiting for the creator to receive the package.
             * `CONTENT_PENDING`: The creator has received the sample package and is expected to create content.
             * `REJECT_CANCELLED`: The sample application has been rejected by the seller.
             * `OVERDUE_CANCELLED`: The sample application has expired due to being overdue.
             * `UNFULFILL_CANCELLED`: The creator did not fulfill the commitment to create content within the agreed
            timeframe.
             * `DEL_OPEN_COLLAB`: Open collaboration has been deleted.
             * `SELLER_NOT_SHIP_CANCELLED`: The seller did not ship the sample within the required timeframe.
             * `WITHDRAW_CANCELLED`: The creator withdrew the sample application before the seller approved it.
             * `UNFULFILLABLE_CANCELLED`: The application was cancelled due to reasons beyond the creator's control, making
            it impossible to create content.
             * `OPS_CANCELLED`: The application was manually cancelled by operations staff.
             * `OPS_FAILED`: The application was marked as failed by operations staff.
             * `OPS_COMPLETED`: The application was manually marked as completed by operations staff.
             * `COMPLETED`: The application is complete, and the creator has posted the content.

             This field allows for tracking the status of a sample application throughout its lifecycle, providing
            visibility into each stage of the process for sellers and creators.
        creator (list[SampleApplicationStatusChangeWebhookDataCreator] | Unset): Creator detailed information. It
            includes various details such as the creator's TikTok user name and TikTok user id.
        product (list[SampleApplicationStatusChangeWebhookDataProduct] | Unset): Product information.
    """

    application_id: str | Unset = UNSET
    new_status: SampleApplicationStatusChangeWebhookDataNewStatus | Unset = UNSET
    creator: list[SampleApplicationStatusChangeWebhookDataCreator] | Unset = UNSET
    product: list[SampleApplicationStatusChangeWebhookDataProduct] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_id = self.application_id

        new_status: str | Unset = UNSET
        if not isinstance(self.new_status, Unset):
            new_status = self.new_status.value

        creator: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = []
            for creator_item_data in self.creator:
                creator_item = creator_item_data.to_dict()
                creator.append(creator_item)

        product: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = []
            for product_item_data in self.product:
                product_item = product_item_data.to_dict()
                product.append(product_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_id is not UNSET:
            field_dict["application_id"] = application_id
        if new_status is not UNSET:
            field_dict["new_status"] = new_status
        if creator is not UNSET:
            field_dict["creator"] = creator
        if product is not UNSET:
            field_dict["product"] = product

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sample_application_status_change_webhook_data_creator import (
            SampleApplicationStatusChangeWebhookDataCreator,  # noqa: PLC0415
        )
        from ..models.sample_application_status_change_webhook_data_product import (
            SampleApplicationStatusChangeWebhookDataProduct,  # noqa: PLC0415
        )

        d = dict(src_dict)
        application_id = d.pop("application_id", UNSET)

        _new_status = d.pop("new_status", UNSET)
        new_status: SampleApplicationStatusChangeWebhookDataNewStatus | Unset
        if isinstance(_new_status, Unset):
            new_status = UNSET
        else:
            new_status = SampleApplicationStatusChangeWebhookDataNewStatus(_new_status)

        _creator = d.pop("creator", UNSET)
        creator: list[SampleApplicationStatusChangeWebhookDataCreator] | Unset = UNSET
        if _creator is not UNSET:
            creator = []
            for creator_item_data in _creator:
                creator_item = SampleApplicationStatusChangeWebhookDataCreator.from_dict(creator_item_data)

                creator.append(creator_item)

        _product = d.pop("product", UNSET)
        product: list[SampleApplicationStatusChangeWebhookDataProduct] | Unset = UNSET
        if _product is not UNSET:
            product = []
            for product_item_data in _product:
                product_item = SampleApplicationStatusChangeWebhookDataProduct.from_dict(product_item_data)

                product.append(product_item)

        sample_application_status_change_webhook_data = cls(
            application_id=application_id,
            new_status=new_status,
            creator=creator,
            product=product,
        )

        sample_application_status_change_webhook_data.additional_properties = d
        return sample_application_status_change_webhook_data

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
