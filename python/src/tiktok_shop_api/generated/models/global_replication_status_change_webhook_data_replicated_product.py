from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.global_replication_status_change_webhook_data_replicated_product_fail_reason import GlobalReplicationStatusChangeWebhookDataReplicatedProductFailReason





T = TypeVar("T", bound="GlobalReplicationStatusChangeWebhookDataReplicatedProduct")



@_attrs_define
class GlobalReplicationStatusChangeWebhookDataReplicatedProduct:
    """ 
        Attributes:
            product_id (str | Unset): The ID of the product created through replication.
                 Pass this ID to the [GET Product](https://partner.tiktokshop.com/docv2/page/get-product-202309) endpoint for
                more details about the product.
            region (str | Unset): The market where the product has been replicated.
            result (str | Unset): The result of replicating the product.
                 Possible values:

                 * SUCCESS: The product was successfully replicated to the local shop, submitted for listing, and is now under
                review.
                 * DRAFT: The product was successfully replicated to the local shop but saved as a draft local product due to
                validation errors. You need to call [GET Product](https://partner.tiktokshop.com/docv2/page/get-product-202309)
                to obtain the original submitted data, pass that data to [POST Check Product
                Listing](https://partner.tiktokshop.com/docv2/page/check-product-listing-202309) to identify the errors, then
                call [PUT Edit Product](https://partner.tiktokshop.com/docv2/page/edit-product-202309) to rectify the errors and
                send for review.
                 * FAILED: Replication of the product to the local shop was unsuccessful.
            fail_reasons (list[GlobalReplicationStatusChangeWebhookDataReplicatedProductFailReason] | Unset): The list of
                reasons for why the replication failed.
     """

    product_id: str | Unset = UNSET
    region: str | Unset = UNSET
    result: str | Unset = UNSET
    fail_reasons: list[GlobalReplicationStatusChangeWebhookDataReplicatedProductFailReason] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.global_replication_status_change_webhook_data_replicated_product_fail_reason import GlobalReplicationStatusChangeWebhookDataReplicatedProductFailReason # noqa: PLC0415
        product_id = self.product_id

        region = self.region

        result = self.result

        fail_reasons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fail_reasons, Unset):
            fail_reasons = []
            for fail_reasons_item_data in self.fail_reasons:
                fail_reasons_item = fail_reasons_item_data.to_dict()
                fail_reasons.append(fail_reasons_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if region is not UNSET:
            field_dict["region"] = region
        if result is not UNSET:
            field_dict["result"] = result
        if fail_reasons is not UNSET:
            field_dict["fail_reasons"] = fail_reasons

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_replication_status_change_webhook_data_replicated_product_fail_reason import GlobalReplicationStatusChangeWebhookDataReplicatedProductFailReason # noqa: PLC0415
        d = dict(src_dict)
        product_id = d.pop("product_id", UNSET)

        region = d.pop("region", UNSET)

        result = d.pop("result", UNSET)

        _fail_reasons = d.pop("fail_reasons", UNSET)
        fail_reasons: list[GlobalReplicationStatusChangeWebhookDataReplicatedProductFailReason] | Unset = UNSET
        if _fail_reasons is not UNSET:
            fail_reasons = []
            for fail_reasons_item_data in _fail_reasons:
                fail_reasons_item = GlobalReplicationStatusChangeWebhookDataReplicatedProductFailReason.from_dict(fail_reasons_item_data)



                fail_reasons.append(fail_reasons_item)


        global_replication_status_change_webhook_data_replicated_product = cls(
            product_id=product_id,
            region=region,
            result=result,
            fail_reasons=fail_reasons,
        )


        global_replication_status_change_webhook_data_replicated_product.additional_properties = d
        return global_replication_status_change_webhook_data_replicated_product

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
